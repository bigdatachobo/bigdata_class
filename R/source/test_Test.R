library(dplyr)
library(ggplot2)
ggplot2::mpg

mpg_comp_suv = mpg %>%
  select(class, cty) %>% 
  filter(class %in% c('compact','suv'))

# t-검증
#(class, cty) 평균 차이 검정.
t.test(data=mpg_comp_suv,cty~class,var.equal=TRUE)

#  기름 종류에 따른 도시 연비 독립 표본 t-검정 
# 도시 연비가 독립 표본 
# 평균 차이가 우연히 발생했을 가능성이 높다.
# 유의하지 않다.
mpg_fl <-mpg %>%
  select(fl,cty) %>%
  filter(fl %in% c('r','p'))
table(mpg_fl$fl)

t.test(data=mpg_fl,cty~fl)

bf <- c(11,14,18,21,26,28,37,45,48,60,64)

af <- c(13,15,17,18,19,23,25,28,29,36,37)

t.test(bf,af,paired=T)

# 실업자수와 개인 지출의 상관관계
# 실업자수의 변화가 지출의 증가 
# 혹은 감소의 추세를 보이는지 즉 차이가 있는지 분석 검정.
# 정비례관계, 상관관계가 유의 

economics <- data.frame(ggplot2::economics)
cor.test(economics$unemploy, economics$pce)
#-------------------------------------------------------------------------
# Quiz 
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
emp <- dbGetQuery(conn,'select * from emp')

emp_job <- emp %>%
  filter(!is.na(JOB)) %>%
  summarise(sal_mean = mean(SAL))
# 막대그래프(X범주분류값, y 연속크기값)
ggplot(data = emp_job, aes(x=JOB,y=sal_mean)) + geom_col()

#t-test
emp_job_sal = emp %>%
  select(JOB, SAL) %>%
  filter(JOB %in% c('MANAGER','SALESMAN'))
# y=x(범주 = 팩터 = Factor= 요인 ) SAL~JOB
t.test(data=emp_job_sal,SAL~JOB,var.equal=TRUE)
#--------------------------------------------------------------

# f-test 분산분석(ANOVA) : Factor의 분류값 3개 이상인 경우
# 집단 분산 차이의 유의가 검정 
emp_job_sal = emp %>%
  select(JOB, SAL) %>%
  filter(JOB %in% c('MANAGER','SALESMAN','CLERK'))
# t.test(data=emp_job_sal,SAL~JOB,var.equal=TRUE) # 오류
# Factor는 JOB
# 일원분산분석( one-way ANOVA)
oneway.test(SAL~JOB, emp_job_sal)


# 내풀이
emp2 <- dbGetQuery(conn,'select job, sal from emp group by job')
emp2 <- emp2 %>%
  mutate(평균봉급=(ifelse(is.na(AVG(SAL)),0,AVG(SAL))))
emp2 %>% 
  rename(사원번호 ='EMPNO', 사원명 ='ENAME', 급여='SAL')

SALESMAN <-c(1250, 1500, 1600)

MANAGER <- c(2450, 2850, 2975)

t.test(MANAGER, SALESMAN, paired=T)
