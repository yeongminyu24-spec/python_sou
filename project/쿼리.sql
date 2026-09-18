-- 주석
-- C(insert), R(select), U(update), D(delete) 잠깐 연습 

-- 테이블 생성
CREATE TABLE good(no INT PRIMARY key, name VARCHAR(10) NOT NULL, tel VARCHAR(10),
inwon INT, addr TEXT);

DESC good;

-- 자료 추가
-- 형식 : insert into 테이블명(칼럼명 타입, ...) values(자료,...)
INSERT INTO good(no, name, tel, inwon, addr) VALUES(1, '인사과', '123-1234', 5, '삼성1동');
INSERT INTO good VALUES(2, '영업과', '123-2222', 12, '역삼2동');
INSERT INTO good(no, name, inwon) VALUES('3','자재과','7');
INSERT INTO good(addr, no, name, inwon) VALUES('역삼3동','4','자재2과','7');

SELECT * FROM good;

-- 오류인 경우
INSERT INTO good(no, NAME) VALUES(3, '자재3과');   -- no(PRIMARY key) 중복 에러
INSERT INTO good(no, tel) VALUES(5, '자재3과');    -- name은 not null : 반드시 입력
INSERT INTO good(NAME, no) VALUES(5, '자재3과');   -- 입력자료와 칼럼의 수서가 불일치
INSERT INTO good(no, NAME) VALUES('오', '자재3과'); -- 입력자료 타입 불일치
INSERT INTO good(no, NAME) VALUES(5, '우리회사에서 가장 매출이 좋은 부러운 부서');  -- 입력자료 크기 오류


-- 자료 수정
-- 형식 : update 테이블명 set 칼럼명=수정값, ... where 조건
UPDATE good SET inwon=100 WHERE NO=1;
UPDATE good SET inwon=70, tel='777-7777' WHERE NO=2;
UPDATE good SET inwon=2, tel=null WHERE NO=2;

SELECT * FROM good;

-- 오류인 경우
UPDATE good SET name=null WHERE NO=2;   -- name은 not null : 반드시 입력
UPDATE good SET NO=2 WHERE NO=1;        -- no 중복 오류


-- 자료 삭제
-- 형식 : delete from 테이블명 where 조건  - 부분적으로 행 삭제
DELETE FROM good WHERE NO=2;
SELECT * FROM good;

-- 형식2 : truncate table 테이블명   - where 조건 없음. 행 모두 삭제. 구조만 남음
truncate TABLE good;
SELECT * FROM good;


DROP TABLE good;   -- 테이블 삭제

SHOW TABLES;

----------------------------


-- 기본키(primary key, pk) 제약 조건 - entity integrity
-- 기본키는 빈 값(NULL)이나 중복 값을 가질 수 없다. 자동으로 인덱스가 생성됨.
-- 방법1) 칼럼 레벨
CREATE TABLE aa(bun INT PRIMARY KEY, irum CHAR(10));
DESC aa;

-- 제약 조건 확인
SELECT * FROM information_schema.TABLE_CONDTRAINTS WHERE TABLE_NAME = 'aa';
DROP TABLE aa;

-- 방법 2) 테이블 레벨
CREATE TABLE aa(bun INT, irum CHAR(10), CONSTRAINT aa_bun_pk PRIMARY KEY(bun)); --oracle 용


-- check 제약 조건 - Domain Integrity : 입력 값 조건 부여
CREATE TABLE aa(bun INT, irum CHAR(10), nai INT CHECK(nai>=20));
SELECT * FROM information_schema.TABLE_CONSTRAINTS WHERE TABLE_NAME = 'aa';
INSERT INTO aa VALUES(1,'tom',25);
INSERT INTO aa VALUES(1,'tom',15); --chk err : 조건 불만족

ALTER TABLE aa ADD CONSTRAINT ck_name CHECK(irum IN('tom','join'));  --CHECK 조건 추가
INSERT INTO aa VALUES(3,'john',25);
INSERT INTO aa VALUES(3,'james',25); -- chk err : irum 조건 불만족 
SELECT * FROM aa;

DROP TABLE aa

-- unique 제약 조건- Domain Integrity : 동일값 입력 불허
CREATE TABLE aa(bun INT, irum CHAR(10) UNIQUE);
CREATE TABLE aa(bun INT, irum CHAR(10), CONSTRAINT aa_irum_uk UNIQUE(irum));
INSERT INTO aa VALUES(1, 'john');
INSERT INTO aa VALUES(2,'tom');
INSERT INTO aa VALUES(3,'tom');     --UNIQUE err : 중복 불가 


-- unique 제약 조건 - Domain Integrity : 동일값 입력 불허


-- Referential Integrity(참조키, foreign, 외래키) 제약 조건
-- 다른 테이블의 칼럼값을 참고(fk의 대상은 다른 테이블의 pk 또는 unique 가능)