df=read.csv('C:/Users/sundooedu/Downloads/BIGDATA BACKUP/R/R_day_01/Data/csv_exam.csv')
head(df)
tail(df)
View(df)
dim(df)
str(df) # 속성(attr) = 컬럼 = 열 = 변수
summary(df)

df = data.frame(v1=c(1,2,1),
                v2=c(2,3,2))

df_new <- df # 새 복사본
# 변수명 바꾸기
rename(df_new,math=v1)
rename(df_new,eng=v2)
mpg2 = mpg
mpg2 <- rename(mpg2,city=cty)

# 파생컬럼(변수) 추가
df$v_mean <- (df$v1 + df$v2)/2
df
summary(df$v_sum)
hist(df$v_sum)

mpg = ggplot2::mpg
mpg$total <- (mpg$cty*0.425144 + mpg$hwy*0.425144)/2   # 1mpg(mile per gallon) = 0.425144 kpl(km/liter)
mean(mpg$total)
20*0.425144     


mpg$test <- ifelse(mpg$total>20*0.425144,'pass','fail')
head(mpg)
head(mpg$test,30)
table(mpg$test) # 값에 따른 값분류 빈도(fail pass 111 123)
qplot(mpg$test)

library(dplyr)
# 행추출
df_exam=read.csv('C:/Users/sundooedu/Downloads/BIGDATA BACKUP/R/R_day_01/Data/csv_exam.csv')
# C +S +M : 파이프 연산자
df_exam %>% filter(class==1) # 1클래스(1반)
df_exam %>% filter(class==2) # 2클래스(2반)
df_exam %>% filter(class!=2) # 2클래스(2반)이 아닌 클래스들

df_exam %>% filter(math >= 60)
df_exam %>% filter(english <= 60)

df_exam %>% filter(class==1 & math >= 60)
df_exam %>% filter(english >=80 | math >= 80)
sub_df <- df_exam %>% filter(class %in% c(1,3)) # 목록에 해당(포함되는)하는 행.
class1_df <- df_exam %>% filter(class==1) # 1반학생들 필터링
mean(class1_df$math) # 1반학생이며 수학점수의 평균을 구함.
# Quiz.

# 1. 자동차 배기량에 따라 고속도로 연비가 다른지 알아보자 
# displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중 
# 어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높을까?
cc5_df <- mpg %>% filter(displ >= 5)
cc4_df <- mpg %>% filter(displ <= 4)
mean(cc5_df$hwy) # [1] 18.07895
mean(cc4_df$hwy) # [1] 25.96319

# 2. "chevrolet", "ford", "honda" 자동차의 고속도로 연비 평균을 알아보자 
# 이 회사들의 자동차를 추출한 뒤 hwy 전체 평균을 구해보자.
chev_df <- mpg %>% filter(manufacturer == "chevrolet")
ford_df <- mpg %>% filter(manufacturer == "ford")
honda_df <- mpg %>% filter(manufacturer == "honda")

mean(chev_df$hwy) # [1] 21.89474
mean(ford_df$hwy) # [1] 19.36
mean(honda_df$hwy) # [1] 32.55556

mpg_mf <- mpg %>% filter(manufacturer %in% c("chevrolet","ford","honda"))
mean(mpg_mf$hwy)
#-------------------------------------------------------------------------
# 열추출
# select(변수(열))
df %>% select(math)
df %>% select(english)
df %>% select(class,math,english)

# select(-변수(열)) 
df %>% select(-math) # math는 배제하고 나머지 전부 표시
df %>% select(-english)
df %>% select(-math,-english)

# 1반 학생의 수학
# 1반 학생의 수학의 앞 2개 행
df %>% filter(class==1) %>% select(math) %>% head(2)
df %>% select(math) %>% filter(class==1) # 오류

# math로 행들 오름정렬
df %>% arrange(desc(math))

# mutate(): 파생변수를 추가하여 df 구조를 변경
df %>% mutate(hap = math+english+science)

df %>% mutate(hap = math+english+science,mean=hap/3)
              
df %>% mutate(test=ifelse(math >= 60,'pass','fail & re-test')) %>% head()

df %>% mutate(hap = math+english+science,mean=hap/3,test=ifelse(mean >= 60,'pass','fail & re-test')) %>% head

df %>% mutate(hap = math+english+science,mean=hap/3,test=ifelse(mean >= 60,'pass','fail & re-test')) %>% arrange(desc(mean))

# 반별로 수학평균, 합계, 표준편차, 학생수
df %>% 
  group_by(class) %>%
  summarise(mean_math=mean(math),
            math_sum=sum(math),
            math_sd=sd(math),
            math_n=n())

mpg %>% group_by(manufacturer,drv)








