import base64
import io
from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Flask, render_template
from matplotlib.figure import Figure
import koreanize_matplotlib
import pandas as pd
import pymysql


app = Flask(__name__)

# 실습용 MariaDB 접속 설정
config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123',
    'database': 'test',
    'port': 3306,
    'charset': 'utf8',
}


def get_connection():
    return pymysql.connect(**config)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dbshow')
def dbshow():
    # 필요한 자료를 한 번 조회합니다. 같은 부서는 직원명 순으로 정렬합니다.
    sql = """
        select j.jikwonno as 사번, j.jikwonname as 직원명,
            b.buserno as 부서번호, b.busername as 부서명,
            j.jikwonjik as 직급, j.jikwonpay as 연봉,
            j.jikwonibsail as 입사일, j.jikwongen as 성별
        from jikwon j inner join buser b on j.busernum = b.buserno
        order by b.buserno asc, j.jikwonname asc, j.jikwonno asc
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
            cols = [column[0] for column in cur.description]

    df = pd.DataFrame(rows, columns=cols)
    if df.empty:
        return render_template('dbshow.html', total=0)

    df['연봉'] = pd.to_numeric(df['연봉'])
    df['입사일'] = pd.to_datetime(df['입사일'])

    # 1) 입사 기념일을 기준으로 만 근무년수를 계산합니다.
    today = pd.Timestamp(datetime.now(ZoneInfo('Asia/Seoul')).date())
    before_anniversary = (
        (df['입사일'].dt.month > today.month)
        | ((df['입사일'].dt.month == today.month)
           & (df['입사일'].dt.day > today.day))
    )
    df['근무년수'] = (
        today.year - df['입사일'].dt.year - before_anniversary.astype(int)
    ).astype('Int64')
    employee_df = df[['사번', '직원명', '부서명', '직급', '연봉', '근무년수']]

    # 2) 부서별 통계와 직급별 통계를 각각 구합니다.
    dept_pay = (
        df.groupby('부서명')['연봉']
        .agg(연봉합='sum', 연봉평균='mean').round(2).reset_index()
    )
    position_pay = (
        df.groupby('직급')['연봉']
        .agg(연봉합='sum', 연봉평균='mean').round(2).reset_index()
    )

    # 3) 웹에서는 show() 대신 메모리에 PNG 이미지를 저장합니다.
    fig = Figure(figsize=(12, 4))
    ax1, ax2 = fig.subplots(1, 2)
    ax1.bar(dept_pay['부서명'], dept_pay['연봉합'])
    ax1.set(title='부서별 연봉 합계', xlabel='부서명', ylabel='연봉 합계')
    ax2.bar(dept_pay['부서명'], dept_pay['연봉평균'])
    ax2.set(title='부서별 연봉 평균', xlabel='부서명', ylabel='연봉 평균')
    fig.tight_layout()
    with io.BytesIO() as buffer:
        fig.savefig(buffer, format='png')
        graph = base64.b64encode(buffer.getvalue()).decode('ascii')

    # 4) 성별을 행, 직급을 열로 하는 인원수 교차표입니다.
    frequency_df = pd.crosstab(
        df['성별'], df['직급'], margins=True, margins_name='합계'
    )

    # 5) 동점이면 원본 정렬 순서상 먼저 나오는 한 명을 선택합니다.
    # 연봉이 누락된 직원은 최고 연봉자 선정에서 제외합니다.
    paid_df = df.dropna(subset=['연봉'])
    top_indices = paid_df.groupby('부서명')['연봉'].idxmax()
    top_salary_df = df.loc[
        top_indices, ['부서명', '직원명', '연봉']
    ].reset_index(drop=True)

    # 6) 전체 조회 인원에 대한 부서별 비율입니다.
    total = len(df)
    dept_count = df.groupby('부서명').size()
    dept_ratio = (dept_count / total * 100).round(2)
    ratio_df = pd.DataFrame({
        '인원수': dept_count, '비율(%)': dept_ratio
    }).reset_index()

    return render_template(
        'dbshow.html',
        employee_table=employee_df.to_html(index=False),
        dept_table=dept_pay.to_html(index=False),
        position_table=position_pay.to_html(index=False),
        frequency_table=frequency_df.to_html(),
        top_table=top_salary_df.to_html(index=False),
        ratio_table=ratio_df.to_html(index=False),
        total=total,
        graph=graph,
    )


if __name__ == '__main__':
    app.run(debug=True)
