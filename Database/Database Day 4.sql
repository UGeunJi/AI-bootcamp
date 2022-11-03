/* 데이터 집계하기 */
-- > (1) 그룹화하기 (2) 집계함수 사용 (3) 집계쿼리((1)+(2))

-- (3) 집계 쿼리
-- "연도"별 개봉 영화 수의 합 집계하기
use mywork;

select year(release_date), count(*)
  from box_office
  group by year(release_date)
  order by year(release_date);

-- (실습) 2019년 개봉 영화의 "유형"별 매출액의 최댓값, 최솟값, 전체합 집계하기
select movie_type, max(sale_amt), min(sale_amt), sum(sale_amt)
  from box_office
  where year(release_date) = 2019
  group by movie_type
  order by 1;
  
-- (실습) 2019년 개봉 영화 중 매출액이 1억원 이상인 영화의 "분기"별, "배급사"별 개봉 영화수와 매출액(합계) 집계하기

select quarter(release_date) '분기', distributor 배급사, count(*) 영화수, sum(sale_amt) 매출액합
  from box_office
  where year(release_date) = 2019 and sale_amt >= 100000000
  group by quarter(release_date), distributor
  order by 1;
  
-- (실습) world 데이터베이스에서의 city 테이블에서 "국가코드"별로 도시의 수 집계하기
use world;
desc city;
select countrycode, count(*)
  from city
  group by countrycode
  order by 2 desc;
  
-- (실습) world 데이터베이스의 country 테이블에서 "대륙"별 면적(surfacearea)이 가장 큰 순으로 정렬하기

select continent 대륙, sum(surfacearea) 총면적, count(*) 나라수, sum(population) 총인구
  from country
  group by continent
  order by 2 desc;
  
-- (실습) mywork 데이터베이스의 box_office 테이블에서 2019년 개봉 영화 중 1~10위 영화와 나머지 영화를 구분하되,
-- 각 그룹의 매출액 합 집계하기

use mywork;
desc box_office;

select release_date 개봉년도, if(ranks <= 10, '상위10', '나머지') '상위권', sum(sale_amt) 총매출액, count(*) 영화수
 from box_office
 where year(release_date) = 2019
 group by 2
 order by 2 desc;
 
select case when ranks between 1 and 10 then '상위10'
			else '나머지'
		end top_ranks, count(*) 영화수, round(sum(sale_amt)/100000000, 0) '총매출액(unit:억원)'
	from box_office
where year(release_date) = 2019
group by top_ranks
order by 3 asc;

-- 2019년에 개봉한 영화 중 매출액이 1000만원 이상인 영화를 유형별로 매출액 합을 집계(+ 총합 with rollup)
-- with rollup으로 합계(소계, 총계) 구하기
select movie_type, count(*), sum(sale_amt)   -- 1870105386118
  from box_office
  where year(release_date) = 2019 and sale_amt >= 10000000
  group by movie_type with rollup;

-- 아래 쿼리문으로 위의 rollup 총합값이 같음을 확인할 수 있음
select sum(sale_amt)   -- 1870105386118
  from box_office
  where year(release_date) = 2019 and sale_amt >= 10000000;

-- 2019년에 개봉한 영화 중 매출액이 1000만원 이상인 영화를 
-- "월"별, "영화유형"별  매출액 집계하기

select movie_type 영화유형, count(*) 영화수, sum(sale_amt) 총매출액, month(release_date) 월
  from box_office
  where year(release_date) = 2019 and sale_amt >= 10000000
  group by month(release_date), movie_type with rollup
  order by 4;
  
-- grouping 함수 사용하기: grouping의 결과가 1일 때 with rollup의 결과인 총합임을 알 수 있음
-- grouping을 응용하여 총합에 해당하는 null값을 적당한 단어("합계")로 대체
select if(grouping(movie_type) = 0, movie_type, "합계") 유형, count(*) 영화수, sum(sale_amt) 총매출액
  from box_office
  where year(release_date) = 2019
  group by movie_type with rollup;
  
-- Having 절 사용하기
-- box_office 테이블에서 순위가 1~10위에 있는 영화를 조회하되,
-- "개봉연월별"로 개봉영화 편수 집계하기

select ranks, extract(year_month from release_date) 개봉연월, count(*) 영화수, if(count(*) >= 2, count(*), null) 2편이상
  from box_office
  where ranks <= 10
  group by 2
  order by ranks;
  
select release_date, extract(year_month from release_date) 개봉연월, count(*) 개봉편수
  from box_office
  where ranks between 1 and 10
  group by 개봉연월;


-- 이때 영화가 2편 이상 개봉한 항목만 조회하기
select ranks, extract(year_month from release_date) 개봉연월, count(*) 영화수
  from box_office
  where ranks <= 10 and '영화수' >= 2
  group by 2
  order by ranks;
  
-- 이때 아래와 같이 하면 오류가 뜸
select release_date, extract(year_month from release_date) 개봉연월, count(*) 개봉편수
  from box_office
  where ranks between 1 and 10 and count(*) >= 2
  group by 개봉연월;
  
-- having 절을 사용했을 때 (오류 안뜸)
select extract(year_month from release_date) 개봉연월, count(*) 개봉편수
  from box_office
  where ranks between 1 and 10
  group by 개봉연월
  having count(*) >= 2
  order by 2 desc;
  
-- (실습) "개봉년월"별로 순위가 1~10위에 있는 영화 편수와 매출액 구하기
select ranks, extract(year_month from release_date) 개봉연월, count(*) 영화수, sum(sale_amt)
  from box_office
  where ranks <= 10
  group by 2
  order by ranks;
  
select extract(year_month from release_date)개봉년월, count(*) 영화편수, sum(sale_amt) 매출액함
 from box_office
 where ranks between 1 and 10
 group by 1;

-- 이때 "개봉년월"별 매출액 합이 1500억원 이상인 경우만 조회하기 (having 절 사용)
select ranks, extract(year_month from release_date) 개봉연월, count(*) 영화수, sum(sale_amt)
  from box_office
  where ranks <= 10
  group by 2
  having sum(sale_amt) >= 150000000000
  order by ranks;
  
select extract(year_month from release_date)개봉년월, count(*) 영화편수, round(sum(sale_amt)/100000000,0) '매출액합(unit:억원)'
 from box_office
 where ranks between 1 and 10
 group by 1
 having sum(sale_amt) >= 150000000000;

-- (실습) 2019년 개봉영화 중 매출액이 1000만원 이상인 것을 골라 "영화유형"별로 매출액 합 구하기 (with rollup)
select movie_type, sum(sale_amt)
  from box_office
  where year(release_date) = 2019 and sale_amt >= 10000000
  group by movie_type with rollup;
  
select movie_type 영화유형, count(*) 영화편수, round(sum(sale_amt)/1000000) '총매출액(unit: 백만)'
  from box_office
  where year(release_date) = 2019 and sale_amt >= 10000000
  group by movie_type with rollup;
  
-- 이때 "영화유형"별로 매출액 합계로 나온 결과 행만 조회하기 (having)
select movie_type, sum(sale_amt)
  from box_office
  where year(release_date) = 2019 and sale_amt >= 10000000
  group by movie_type with rollup
  having grouping(movie_type) = 1;
  
select movie_type 영화유형, count(*) 영화편수, round(sum(sale_amt)/1000000) '총매출액(unit: 백만)'
  from box_office
  where year(release_date) = 2019 and sale_amt >= 10000000
  group by movie_type with rollup
  having grouping(movie_type) = 1;
  
-- if절 사용
select if(grouping(movie_type) = 0, movie_type, "합계") 영화유형, count(*) 영화편수, round(sum(sale_amt)/1000000) '총매출액(unit: 백만)'
  from box_office
  where year(release_date) = 2019 and sale_amt >= 10000000
  group by movie_type with rollup;
  
-- (실습) 2019년 개봉 영화 중 매출액이 1000만원 이상인것을 골라 "월"별, "영화유형"별로 매출액합 집계하기 (with rollup)
select movie_type 영화유형, count(*) 영화편수, round(sum(sale_amt)/1000000) '총매출액(unit: 백만)', month(release_date) 월
  from box_office
  where year(release_date) = 2019 and sale_amt >= 10000000
  group by month(release_date), movie_type with rollup;

-- 이 때 "월"별, "영화유형"별 매출액 합계(유형별소계, 월별총계)로 나온 결과 행만 조회하기 (having 절)
 select count(*) 영화편수, round(sum(sale_amt)/1000000) '총매출액(unit: 백만)', if(grouping(month(release_date)) = 0, month(release_date), "총계") 월, if(grouping(movie_type) = 1, movie_type, "소계") 영화유형
  from box_office
  where year(release_date) = 2019 and sale_amt >= 10000000
  group by month(release_date), movie_type with rollup
  having grouping(movie_type) = 1
  order by month(release_date);
 
-- (실습) box_office 테이블에서 2019년 개봉영화 중 "국가(rep_country)"별 관객수(audience_num)의 합이 50만명 이상인 것을 조회하기 
desc box_office;
select rep_country, sum(audience_num)
  from box_office
  where year(release_date) = 2019
  group by rep_country
  having sum(audience_num) >= 500000;

-- 이때 "국가"별 합계까지 구하는 쿼리 작성하기 (with rollup)
 select rep_country, sum(audience_num)
  from box_office
  where year(release_date) = 2019
  group by rep_country with rollup
  having sum(audience_num) >= 500000;
  
-- (실습) box_office 테이블에서 2015년 이후 개봉한 영화 중
-- 관객수가 100만을 넘긴 영화의 감독과 관객수, 개봉편수를 "연도"별, "감독"별로 집계하기
desc box_office;
select director 감독, year(release_date) 개봉년도, audience_num 관객수, count(*) 개봉편수
  from box_office
  where year(release_date) >= 2015 and audience_num >= 1000000
  group by year(release_date), director;
  
-- 이 때 개봉 편수가 2번 이상되는 건수만 조회하기(having 절)
 select director 감독, year(release_date) 개봉년도, audience_num 관객수, count(*) 개봉편수
  from box_office
  where year(release_date) >= 2015 and audience_num >= 1000000
  group by year(release_date), director
  having count(*) >= 2;
 
/* 테이블간 관계 맺기 */
-- (1) 내부 조인 
use world;
select count(*) from city;     -- 4097
select count(*) from country;  -- 239

-- city 테이블과 country 테이블을 조인해서 country 테이블에 있는 국가명, 대륙명, 인구까지 조회하기
select count(*)   -- 4079건 조회 (1:m의 관계에서 join시 m의 개수로 맞춰짐)
  from city a
  inner join country b
    on a.countrycode = b.code;
    
select a.*, b.name, b.continent, b.population
  from city a
  inner join country b
    on a.countrycode = b.code;

-- join된 결과에 대해 추가적으로 where 문을 통해 필터링
select a.*, b.name, b.continent, b.population
  from city a
  inner join country b
    on a.countrycode = b.code
  where a.countrycode = 'kor';
    
-- 내부 조인에서는 테이블의 위치를 바꿔도 결과는 동일
select a.*, b.name, b.population
  from country a
  inner join city b
    on b.countrycode = a.code
  where b.countrycode = 'kor';

-- (실습) country 테이블과 countrylanguage 테이블 내부조인
-- 조인결과가 어떤 테이블의 개수에 맞춰졌는지 확인
select count(*) from countrylanguage;    -- countrycode, 984, 자식
select count(*) from country;            -- code, 239, 부모

desc country;            
select count(*)             -- 984개로 countrylanguage 테이블의 개수로 맞춰졌다. 1:m의 관계에서 m으로 맞춰짐.
  from country a
  inner join countrylanguage b
	on b.countrycode = a.code;

-- 한국인 경우로 추가 필터링 해보기
select count(*)
  from country a
  inner join countrylanguage b
	on b.countrycode = a.code
  where b.countrycode = 'kor';


-- (2) 외부 조인 
-- (3) 기타 조인 