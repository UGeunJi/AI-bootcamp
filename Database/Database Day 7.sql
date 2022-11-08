-- update문으로 데이터 입력하기
-- emp)update1 테이블을 생성 (emp_test로부터 복사)
-- primary key 지정

create table emp_update1
select * from emp_test;

select * from emp_update1;
desc emp_update1;
desc emp_test;

alter table emp_update1
  add constraint primary key (emp_no);    -- 제약사항

/*  
컬럼 추가 (Add)
ALTER TABLE table_name ADD COLUMN ex_column varchar(32) NOT NULL;

컬럼 변경 (Modify)
ALTER TABLE table_name MODIFY COLUMN ex_column varchar(16) NULL;

컬럼 이름까지 변경 (Change)
ALTER TABLE table_name CHANGE COLUMN ex_column ex_column2 varchar(16) NULL;

컬럼 삭제 (Drop)
ALTER TABLE table_name DROP COLUMN ex_column;

테이블 이름 변경 (RENAME)
ALTER TABLE table_name1 RENAME table_name2;

출처: https://extbrain.tistory.com/39
*/

create table emp_update2
select * from emp_test2;

alter table emp_update2
  add constraint primary key (emp_no);

desc emp_update2;
select * from emp_update2;

select * from emp_update1;

-- 단일 테이블 데이터 수정하기
update emp_update1
  set emp_name = concat(emp_name, '2'),
	  salary = salary + 100;
       
select * from emp_update1;

-- (오류 예) primary key 중복 입력
update emp_update1
  set emp_no  = emp_no + 1
  where emp_no >= 1018;
  
-- 뒤부터 입력(꼼수)
-- 그러나 Primary key는 테이블의 근간이 되므로 수정하지 않아야 한다.
update emp_update1
  set emp_no  = emp_no + 1
  where emp_no >= 1018
  order by emp_no desc;
  
-- 다중 테이블 데이터 수정하기
-- 두 테이블 간 관계를 이용해서 업데이트
-- 한 테이블(a)의 컬럼값을 참조해서 다른 테이블(b)의 컬럼값을 변경
update emp_update1 a, emp_update2 b
  set a.salary = b.salary + 1000
  where a.emp_no = b.emp_no;
  
  select * from emp_update1;
  
-- null 값 때문에 연산이 이루어지지 않을 때에는 0으로 바꾼 뒤에 다시 실행을 해주어야 한다.
update emp_update1 a, emp_update2 b
  set a.salary = ifnull(a.salary, 0),
      b.salary = a.salary + 1000
  where a.emp_no = b.emp_no;
  
select * from emp_update1;                                                                                                                                                                                                                                                                        ;
select * from emp_update2;

-- null 값을 없애고 1000을 더해주는 것이 한 번에 되지 않아서 작업을 따로 분리해서 실행시켰다.
update emp_update1 a, emp_update2 b
  set a.salary = ifnull(a.salary, 0)
  where a.emp_no = b.emp_no;
/*
2000
0
0
4000
*/
update emp_update1 a, emp_update2 b
  set b.salary = a.salary + 1000
  where a.emp_no = b.emp_no;
/*
3000
1000
1000
5000
*/

-- 입력과 수정을 동시에 처리하기
-- on diplicate key
-- emp_update2 테이블에 pk가 1003, 1004, 1005인 데이터를 입력
-- 수정 / 입력할 데이터는 emp_name 컬럼
-- 1003, 1004번은 수정, 1005번은 새롭게 입력

/* a 테이블
1003	다빈치2	2021-03-01	0
1004	리차드파인만2	2021-01-10	4000
1005	퀴리부인2	2021-03-01	4100
*/
/* emp_update2 테이블
1001	아인슈타인	2021-01-01	3000
1002	아이작뉴턴	2021-02-01	1000
1003	다빈치	2021-03-01	1000
1004	리차드파인만	2021-01-10	5000
*/

insert into emp_update2
select * from emp_update1 a
  where emp_no between 1003 and 1005
  on duplicate key update emp_name = a.emp_name,
						  salary = a.salary;
                          
select * from emp_update2;
/*
1001	아인슈타인	2021-01-01	3000
1002	아이작뉴턴	2021-02-01	1000
1003	다빈치2	2021-03-01	0
1004	리차드파인만2	2021-01-10	4000
1005	퀴리부인2	2021-03-01	4100
*/

-- (실습) emp_update2 테이블에서 사번이 1001과 1002인 사원명을
-- emp_update1 테이블의 동일 사번을 가진 사원명으로 emp_update2에 변경하는 쿼리 작성하기
update emp_update1 a, emp_update2 b
  set b.emp_name = a.emp_name
  where a.emp_no = b.emp_no
    and b.emp_no between 1001 and 1005;

select * from emp_update1;
select * from emp_update2;

-- Delete문으로 데이터 삭제하기
create table emp_delete
select * from emp_test;

alter table emp_delete
  add constraint primary key (emp_no);

desc emp_delete;  
select * from emp_delete;

create table emp_delete2
select * from emp_test2;

alter table emp_delete2
  add constraint primary key (emp_no);

desc emp_delete2;  
select * from emp_delete2;

-- 단일 테이블 삭제
-- (1) 조건(where)을 넣어서 삭제
select * from emp_delete;

delete from emp_delete
  where salary is null;

-- (2) 모두 삭제
delete from emp_delete;

-- 데이터 복구
insert into emp_delete
select * from emp_test;

-- (3) order by, limit의 조합 추가
-- 두 명의 맥스월 중 한 명(뒷번호 1018)만 삭제하기
select * from emp_delete;

delete from emp_delete
  where emp_name = '맥스웰'
  order by emp_no desc
  limit 1;
  
-- 원하는 것인지 확인
select * from emp_delete
  where emp_name = '맥스웰'
  order by emp_no desc
  limit 1;
  
-- 다중 테이블 삭제
-- (1) 조건으로 삭제
delete a, b
  from emp_delete a, emp_delete2 b
  where a.emp_no = b.emp_no;
  
select * from emp_delete;    -- a table
select * from emp_delete2;   -- b table

-- (2) 모두 삭제
delete a, b
  from emp_delete a, emp_delete b;
  
delete from emp_delete;
delete from emp_delete2;

-- 데이터 복구
select * from emp_test;

insert into emp_delete
select * from emp_test
where emp_no <> 1018;   -- 1018번만 빼고 복사

select * from emp_delete;

insert into emp_delete2
select * from emp_test;

select * from emp_delete2;

insert into emp_delete values
(1019, '막스클랑크', '2021-04-05', 100);

insert into emp_delete2 values
(1018, '맥스웰', '2021-04-05', 100),
(1019, '막스클랑크', '2021-04-05', 100);

-- using 문법으로 테이블 삭제
delete from b
using emp_delete a, emp_delete2 b
  where a.emp_no = b.emp_no;
  
select * from emp_delete;  -- a table
select * from emp_delete2;  -- b table

-- (실습) emp_delete 테이블에서 사원명이 막스클랑크인 데이터를 삭제하는데,
-- 이번에는 사번이 빠른 1건만 삭제하는 쿼리 작성하기
delete from emp_delete
  where emp_name = '막스클랑크'
  order by emp_no asc
  limit 1;
  
select * from emp_delete;

select * from emp_delete
  where emp_name = '막스클랑크'
  order by emp_no asc
  limit 1;

-- (실습) box_office 테이블을 참조해 box_office_copy 테이블을 만들기 (create ~ select ~
-- 이때 box_office 테이블에서 2019년도 개봉 영화 중 관객수가 800만명 이상인 데이터만 들어가야 함
create table box_office_copy
select * from box_office
  where year(release_date) = 2019 and audience_num >= 8000000;
  
select * from box_office_copy;

-- (실습) box_office_copy 테이블 last_year_audi_num 이라는 int 컬럼을 추가한 뒤,
-- box_office 테이블에서 2018년도 개봉영화와 box_office_copy(2019) 테이블의 순위가 같은 건에 대해
-- last_year_audi_num에 2018년도의 관객수를 설정

select years, movie_name, ranks, audience_num, last_year_audi_num from box_office_copy;

ALTER TABLE box_office_copy ADD COLUMN last_year_audi_num int NOT NULL;

update box_office_copy a, box_office b
  set a.audience_num = b.audience_num
  where year(b.release_date) = 2019
    and b.ranks = a.ranks;

select * from box_office_copy;

/*
12274996	16265618
11212710	13934592
9224582	13369064
6584915	12552283
none    none
5661128	9426011
5448134	8021145
*/

-- (실습) 사원의 부서 할당 정보가 들어있는 dept_emp 테이블에서
-- 현재 일하고 있는 않은 사람 삭제하는 쿼리 작성하기
create table dept_emp_test
select * from dept_emp;

select count(*) from dept_emp_test;     -- 33188에서 24135로

delete from dept_emp_test
where sysdate() <= from_date or sysdate() >= to_date;   -- not between도 사용가능

-- 트랜잭션 처리하기
select @@autocommit;

set autocommit = 0;
set autocommit = 1;

-- 트랜잭션용 테이블 생성
create table emp_tran1
select * from emp_test;

alter table emp_tran1
  add constraint primary key (emp_no);
  
create table emp_tran2
select * from emp_test;

alter table emp_tran2
  add constraint primary key (emp_no);

-- DDL(Data Definition Language)
-- 트랜잭션에 영향을 받지 않으므로 commit이나 rollback을 사용할 필요가 없음

-- DML(Data Manipulation Language)
-- 트랜잭션에 영향 받기에 commit이나 rollback 사용 가능

-- 자동커밋 모두 비활성화 상태에서 트랜잭션 처리하기
set autocommit = 0;
select @@autocommit;

-- 데이터 삭제
delete from emp_tran1;
delete from emp_tran2;

-- 데이터 확인(데이터 없음)
select * from emp_tran1;
select * from emp_tran2;

-- 삭제 취소
rollback;

-- 데이터 확인(데이터 있음)
select * from emp_tran1;
select * from emp_tran2;

-- 데이터 삭제
delete from emp_tran1;

-- 삭제 반영
commit;

-- 데이터 확인(emp_tran1 데이터 없음)
select * from emp_tran1;
select * from emp_tran2;

-- 삭제 최소
rollback;

-- 데이터 확인(삭제 취소가 되지는 않음)
select * from emp_tran1;
select * from emp_tran2;

-- > commit이나 rollback문을 만나게 되면 이 지점까지가 한 트랜잭션 (종료)

select @@autocommit;
set autocommit = 1;

-- 데이터 입력
insert into emp_tran1
select * from emp_test;

select * from emp_tran1;

-- 입력 취소
rollback;

-- 데이터 확인(자동커밋이 활성화(@@autocommit = 1)된 상태라 입력(insert)이 실행됨과 동시에 commit이 이루어져 트랜잭션이 완료
select * from emp_tran1;

-- 자동커밋이 활성화된 상태에서 수동으로 트랜잭션을 처리하고 싶을 때
-- start transaction문 사용 (일시적으로 자동커밋이 비활성화됨)
-- commit이나 rollback을 만났을 때 트랜잭션이 종료, 자동커밋이 활성화됨

select @@autocommit;  -- 1로 조회

start transaction;  -- 일시적으로 자동커밋이 비활성화된 상태

-- 데이터 삭제
delete from emp_tran1
  where emp_no >= 1006;
  
-- 데이터 수정
update emp_tran1
  set salary = 0
  where salary is null;
  
select * from emp_tran1;

-- start transaction 이후에 했던 작업들(삭제, 수정) 취소
rollback;

-- 데이터 확인
select * from emp_tran1;

-- savepoint문 사용방법
start transaction;

-- savepoint A 설정
savepoint A;

-- 데이터 삭제
delete from emp_tran1
  where salary is null;
  
-- savepoint B 설정
savepoint B;

-- 데이터 삭제
delete from emp_tran1
  where emp_name = '맥스웰'
  order by emp_no
  limit 1;

-- savepoint B 이후 작업 취소
rollback to savepoint B;

select * from emp_tran1;

-- 최종 반영
commit;

select * from emp_tran1;

-- (실습) 수동으로 트랜잭션 처리하던 중 emp_tran2 테이블에서 salary 컬럼 값이 1000인 건을 삭제하려고 했는데,
-- 실수로 1000이 아닌 100인 건을 삭제
-- 삭제 전으로 되돌리는 과정을 쿼리문으로 작성하기
select @@autocommit;  -- 1로 조회

start transaction;

savepoint C;

delete from emp_tran2
  where salary = 100;
  
rollback to savepoint C;

commit;

/* 데이터 분석에 유용한 분석 쿼리 */
-- 개선된 서브쿼리 CTE 사용하기
-- 부서 관리자 테이블(dept_manager)과 사원 테이블(employees)을 조인해
-- 현재 관리자의 부서번호, 사번, 사원, 이름을 조회하는 쿼리 작성 후
-- 부서 테이블(departments)과 최종 조인해서 부서명까지 조회하는 쿼리
-- (1) 서브쿼리 방식
select a.dept_no, a.dept_name, manager.emp_no, manager.first_name, manager.last_name
  from departments a,
(select b.dept_no, b.emp_no, c.first_name, c.last_name
  from dept_manager b, employees c
  where b.emp_no = c.emp_no
  and sysdate() between b.from_date and b.to_date
) manager
where a.dept_no = manager.dept_no;


-- (2) CTE 방식
with manager as (select b.dept_no, b.emp_no, c.first_name, c.last_name
  from dept_manager b, employees c
  where b.emp_no = c.emp_no
  and sysdate() between b.from_date and b.to_date
)
select a.dept_no, a.dept_name, b.emp_no, b.first_name, b.last_name
  from departments a, manager b
  where a.dept_no = b.dept_no;
  
-- 현재 시점을 기준으로 각 부서에 속한 사원들의 총 급여에 대한 부서별 평균을 구하는 쿼리 작성하기
-- (1) 서브쿼리 방식
select avg(f.dept_salary_sum)  -- 9개 부서에 지출되는 총급여 자체의 평균 193044765.5556
from
(
select a.dept_no, a.dept_name, sum(c.salary) dept_salary_sum, avg(c.salary) dept_salary_avg
  from departments a, dept_emp b, salaries c
  where a.dept_no = b.dept_no
    and b.emp_no = c.emp_no
    and sysdate() between b.from_date and b.to_date
    and sysdate() between c.from_date and c.to_date
  group by a.dept_no
  ) f;


-- (2) CTE
-- 서브쿼리만 만들 수 있으면 굉장히 변환시켜줄 수 있다.
with dept_info as (select a.dept_no, a.dept_name, sum(c.salary) dept_salary_sum, avg(c.salary) dept_salary_avg
  from departments a, dept_emp b, salaries c
  where a.dept_no = b.dept_no
    and b.emp_no = c.emp_no
    and sysdate() between b.from_date and b.to_date
    and sysdate() between c.from_date and c.to_date
  group by a.dept_no
)
select avg(f.dept_salary_sum) -- 9개 부서에 지출되는 총급여 자체의 평균 193044765.5556
from dept_info f;

with dept_info as (select a.dept_no, a.dept_name, sum(c.salary) dept_salary_sum, avg(c.salary) dept_salary_avg
  from departments a, dept_emp b, salaries c
  where a.dept_no = b.dept_no
    and b.emp_no = c.emp_no
    and sysdate() between b.from_date and b.to_date
    and sysdate() between c.from_date and c.to_date
  group by a.dept_no
),
dept_avg as
(
select avg(f.dept_salary_sum) dept_avg_salary -- 9개 부서에 지출되는 총급여 자체의 평균 193044765.5556
from dept_info f
)
select a.dept_no, a.dept_salary_sum, b.dept_avg_salary
  from dept_info a, dept_avg b;
  
-- window function

-- box_office 테이블에서 2018년 이후 개봉된 영화 중에서 랭킹 10위 안에 든 영화들의
-- "연도별" 총 매출액과 평균 매출액을 구하되,
-- 집계되기 전의 개별 영화이름, 랭킹, 매출액도 함께 표시하기
-- (CTE 사용)

select years, sum(sale_amt), avg(sale_amt)
  from box_office
  where year(release_date) >= 2018 and ranks <= 10
  group by year(release_date);
  
select movie_name, ranks, sale_amt
  from box_office
  where year(release_date) >= 2018 and ranks <= 10;
  
-- 서브쿼리
select a.movie_name 이름, a.ranks 순위, a.sale_amt 매출액, f.sale_sum 합계, f.sale_avg 평균
  from box_office a,
  (
  select years, sum(sale_amt) sale_sum, avg(sale_amt) sale_avg
  from box_office
  where year(release_date) >= 2018 and ranks <= 10
  group by year(release_date)
  ) f
  where year(release_date) >= 2018 and ranks <= 10
  group by year(release_date), ranks;

-- CTE
with box_office_sale as (
 select years, sum(sale_amt) sale_sum, avg(sale_amt) sale_avg
  from box_office
  where year(release_date) >= 2018 and ranks <= 10
  group by year(release_date)
)
select a.years 연도, a.movie_name 이름, a.ranks 순위, a.sale_amt 매출액, b.sale_sum 합계, b.sale_avg 평균
  from box_office a, box_office_sale b
  where year(release_date) >= 2018 and ranks <= 10
  group by year(release_date), ranks
  order by a.ranks;

-- 윈도우 함수 사용
select year(release_date), movie_name, ranks, sale_amt,
  sum(sale_amt) over (partition by year(release_date)) 합계,
  avg(sale_amt) over (partition by year(release_date)) 평균
  from box_office
  where year(release_date) >= 2018
    and ranks <= 10;
    
-- 1위인 영화들의 평균 매출액보다 큰 매출액이 큰 영화만 조회
-- (CTE 방식)
with avg_top_movie as (
select avg(sale_amt) avg_sale_amt
  from box_office
  where ranks = 1
  ) 
select a.movie_name, a.years, a.sale_amt, b.avg_sale_amt
  from box_office a, avg_top_movie b
  where a.ranks = 1
  order by years;
  
-- 윈도우 함수
select movie_name, years, sale_amt,
avg(sale_amt) over (partition by ranks) 합계
  from box_office
  where ranks = 1;
  
-- 1위인 영화들의 평균 매출액과 개별 영화이름, 랭킹, 매출액 조회하기
-- (CTE 방식)
with avg_first as
(
select avg(sale_amt) avg_amt
  from box_office
 where ranks = 1
)
select year(a.release_date), a.ranks, a.movie_name, a.sale_amt, b.avg_amt
  from box_office a, avg_first b
 where a.ranks = 1
   -- and a.sale_amt > b.avg_amt
 order by 1;
 
-- (2) 윈도우 함수  
select year(release_date), ranks, movie_name, sale_amt,
  avg(sale_amt) over(partition by ranks) avg_amt
  from box_office
 where ranks = 1;
 
 -- 참고 window 함수에는 평균 매출보다 큰 조건이 안들어가서 아래와같이 cte 사용하여 해결
 with avg_info as
 (
 select year(release_date), ranks, movie_name, sale_amt,
  avg(sale_amt) over(partition by ranks) avg_amt
  from box_office
 where ranks = 1
 )
 select year(a.release_date), a.ranks, a.movie_name, a.sale_amt, b.avg_amt
  from box_office a, avg_info b
   where a.ranks = b.ranks	
     and a.sale_amt = b.sale_amt
     and a.sale_amt > b.avg_amt;