# RJDBC
install.packages('rJava')
install.packages('DBI')
install.packages('RJDBC')

# 1. R 오라클 연동 패키지 로드
library(rJava)
library(DBI)
library(RJDBC)
library('dplyr')
# 2. r 오라클 driver 로드
drv <- JDBC(driverClass="oracle.jdbc.driver.OracleDriver", 
            classPath="C:/oraclexe/app/oracle/product/11.2.0/server/jdbc/lib/ojdbc6.jar")


# 3. R이 오라클 연결 conn 객체 생성.
conn <- dbConnect(drv, 
                  "jdbc:oracle:thin:@//localhost:1521/xe",  
                  "hr", 
                  "hr")
# 4. 업무(작업)을 처리하기 위한 SQL 쿼리 작성 "DB api" 사용 실행
# SQL 실행결과는 DF(DataFrame)
emp <- dbGetQuery(conn,'select * from emp')
emp2 <- dbGetQuery(conn,'select empno,ename,sal from emp where deptno = 10')
emp2 %>% 
    rename(사원번호 ='EMPNO', 사원명 ='ENAME', 급여='SAL') %>% 
    head(3)
# SQL null -> NA -> 0
# 연봉 = 급여*12 + 커미션을 emp3에 추가
emp3 <- dbGetQuery(conn,'select empno,ename,sal,comm from emp')
emp3 <- emp3 %>%
                mutate(연봉=(SAL*12 +ifelse(is.na(COMM),0,COMM)))
# 부서별 범주별 연봉연속값의 평균요약 관계, 차이 유의
emp4 %>%
  group_by(DEPTNO) %>% # 부서별 범주별
  summarise(연봉평균=mean(연봉)) %>% # 연봉연속값의 평규 요약
  arrange(desc(연봉평균)) %>%
  View()

dyna_sql='select empno, ename, sal, comm, deptno from emp where deptno=:1'
dyna_sql='select empno, ename, sal, comm, deptno from emp where empno=? and ename=?'
data <- dbGetQuery(conn, dyna_sql,data=c(7788),c('SCOTT'))
sql="insert into emp(empno, ename, sal) values(1234,'A',100)"
dbSendUpdate(conn,sql)

