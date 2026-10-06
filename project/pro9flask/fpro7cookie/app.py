from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__);
COOKIE_AGE = 60*60*24*7;  # 쿠키 유효 시간 - 7일


@app.get('/')
def index():
    return render_template('index.html');  


@app.get('/login')
def loginFunc():
    name = request.cookies.get('name'); 
    visits = request.cookies.get('visits');

    if name:   # name 쿠키가 존재하면
        visits =int(visits or "0") + 1
        msg = f"안녕하세요 {name}님, {visits}번째 방문입니다"

    else:
        visits = None
        msg = "이름을 입력하면 방문 횟수를 쿠키로 기억합니다"

    resp = make_response(render_template('login.html', msg=msg, name=name, visits=visits));

    # 로그인 상태면 visits 쿠키 갱신
    if name:
        resp.set_cookie('visits', str(visits), max_age=COOKIE_AGE, samesite='Lax');   # name, value 순으로 

    return resp;

@app.post('/login')
def loginFunc2():
    name = (request.form.get('name') or "").strip()  # strip() : 앞 뒤 공백 제거
    resp = make_response(redirect(url_for('loginFunc')));  # get 방식으로 loginFunc 요청
    resp.set_cookie("name", name, max_age=COOKIE_AGE, samesite='Lax');  # 쿠키 생성
    resp.set_cookie("visits", "0", max_age=COOKIE_AGE, samesite='Lax');  # visits 쿠키 초기화

    return resp;


@app.post('/logout')
def logoutFunc():
    # 쿠키 삭제 후 /login(get)으로 이동
    resp = make_response(redirect(url_for('loginFunc')));
    resp.delete_cookie("name")
    resp.delete_cookie("visits")

    return resp;

    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000);