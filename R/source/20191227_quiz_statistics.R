# 문제
# descriptive.csv 데이터 셋을 대상으로 다음 조건에 맞게
# 빈도분석 및 기술 통계량 분석 을 수행하시오

# 조건1)
# 명목척도 변수인 학교유형(type), 합격여부(pass) 변수에 대해
# 빈도분석을 수행하고 결과를 막대그래프와 파이차트로 시각화


# 조건2)
# 비율척도 변수인 나이 변수에 대해 요약치(평균, 표준편차)와
# 비대칭도(왜도와 첨도)통계량을 구하고,
# 히스토그램 작성하여 비대칭도 통계량 설명


# 조건3) 나이 변수에 대한 밀도분포곡선과 정규분포 곡선으로 정규분포 검정

desc <- read.csv("../data/descriptive.csv", header = T)
desc

# 조건 1)
type <- desc$type
summary(type)

x1 <- table(type)
x1

hist(type)
pie(x1)

# 조건 2)
install.packages("moments") # 왜도/ 첨도 사용을 위한 패키지 설치
library(moments)
age <- desc$age
age

skewness(age) # 0.3804892
kurtosis(age) # 1.866623
hist(age)
par(new=TRUE)
install.packages("Hmisc")
library(Hmisc)

describe(age)

install.packages("prettyR")
library(prettyR)

freq(data)

# 조건 3)
install.packages("ggplot2")
library(ggplot2)

plot(density(age))
mean(age) # 53.88
sd(age) # 6.813247
sort(age)
dnorms <- dnorm(age,mean(age),sd(age))
par(new=TRUE)
plot(age,dnorms)

