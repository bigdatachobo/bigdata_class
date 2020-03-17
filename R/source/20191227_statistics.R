data <- read.csv("../data/descriptive.csv", header = T)
head(data)

dim(data) # 행(300개), 열(8개) 정보 - 차원보기

length(data) # 열 (8개)길이

length(data$survey) # survey 컬럼의 관찰치 - 행(300개)

str(data) # 데이터 구조보기 ->  데이터 종류, 행/열, data

# 'dasta.frame':  300 obs. of 8 variables:

str(data$survey) # int [1:300] 1 2 1 4 3 3 NA NA NA 1 ...

# 데이터 특성(최소, 최대, 평균, 분위수, 노이즈 - NA) 제공
summary(data)

# 명목상 의미 없는 수치로 표현된 변수 - 성별(gender)

length(data$gender)
summary(data$gender)
table(data$gender) # 각 성별 빈도수 - outline 확인 -> 0, 5

# 성별 outline 제거
data <- subset(data, data$gender == 1 | data$gender == 2 )
# data 테이블을 대상으로 성별이 1 또는 2인 데이터 대상 subset 만듦.
x<- table(data$gender)
x
barplot(x) # 범주형(명목/ 서열척도) 시각화 -> 막대차트

prop.table(x) # 비율 계산 : 0 < x < 1 사이의 값

y <- prop.table(x)

round(y*100, 2) # 백분율 적용( 소수점 2자리 )

# 1(남)  2(여)  
# 58.25 41.75 

# 3) 척도별 기술통계

# 계급순위를 수치로 표현한 변수 - 학력수준(level)
length(data$level) #학력수준 - 서열
summary(data$level)  # 명목철도와 함게 의미 없음
table(data$level) # 빈도분석 - 의미 있음.

x1<- table(data$level) # 각 학력수준에 빈도수 저장
x1
barplot(x1) # 명목/서열척도 -> 막대차트

#   1   2   3 
# 115  99  70 
# 부모의 학력이 고졸인 경우 115,
# 대졸 99, 대학원 70으로 나타남

# 등간척도 변수의 기술통계량
# 등간 척도 속성의 간격이 일정한 값을 갖는 변수
# 귀하는 교육 시설에 만족하십니까? 1. 매우만족, 2.만족, 3.보통, 4.불만족, 5.매우 불만족 등

# 속성의 간격이 일정한 변수(survey) - 덧셈/뺄셈 연산 가능
survey <- data$survey
survey
summary(survey) # 만족도(5점 척도)인 경우 의미
x1 <- table(survey) # 빈도수
x1
# survey
# 1  2  3  4  5 
# 20 72 61 25  7 
hist(survey)
pie(x1)

# 비율척도 변수의 기술 통계량
# 응답자가 직접 수치로 입력한 변수, 사칙연산이 모두 가능한 변수
# 예. 성적, 키, 나이, 무게, 인구수, 수량, 길이  금액 등

# 수치로 직접 입력한 변수(cost)
length(data$cost)
summary(data$cost) # 요약통계량 - 의미있음(mean) - 8.784, 생활비 통계량
mean(data$cost)
data$cost

# 데이터 정제 - 결측치 제거 및 outline 제거
plot(data$cost) # 0값 위 아래 있는 값들이 결측치임.
data <- subset(data, data$cost >= 2 & data$cost <= 10) # 결측치 제거 / 총점기준 / 좁은범위에선 직선으로 보이지만 결측치 제거후 확대되어 퍼져보이게 된다.
data

x <- data$cost
x
mean(x)
# 평균이 극단치에 영향을 받는 경우 - 중위수(median) 대체
median(x)

min(x)
max(x)
range(x)
sort(x) # 오름차순
sort(x,decreasing = T) 내림차순

sd(x) # 표준편차
var(x) # 분산
# 표준편차 : 표본의 평균에서 얼마나 떨어져 있는가 - 산포도

quantile(x, 1/4) # 1 사분위수 - 25%, 4.6
quantile(x, 3/4) # 3 사분위수 - 75%, 6.2

# 패키지를 이용한 비대칭도 나타내기
install.packages("moments") # 왜도/ 첨도 사용을 위한 패키지 설치
library(moments)
cost <- data$cost
# 왜도 - 평균 중심으로 기울어짐 정도
skewness(cost) # [1] -0.2974908
# 0보다 작으면, 왼쪽방향 비대칭 꼬리, 0보다 크면, 오른쪽 방향 비대칭 꼬리, 
# 0에 근사하면 중심으로 좌우대칭

# 첨도 - 표준정규분포와 비교하여 얼마나 뾰족한가 측정 지표
kurtosis(cost) # [1] 2.683438

# 표준정규분포와 비교하여 첨도가 3이며, 정규분포 곡선을 이루고, 
# 첨도가 3보다 크면 정규분포 보다 뾰족한 형태, 3보다 작으면
# 정규분포 보다 완만한 형태이다.

hist(cost) # 히스토그램으로 왜도/첨도 확인
# 왼쪽방향 비대칭 꼬리, 정규분포 첨도 보다 완만함.

# 2) Hmisc 패키키 이용
install.packages("Hmisc")
library(Hmisc) # 패키지 메모리 로딩

# 전체 변수 대상 기술통계량 제공 - 빈도와 비율 데이터 일괄 수행
describe(data) # Hmisc 패키지에서 제공되는 함수
# 명목, 서열, 등간척도 - n, missing, unique, 빈도수, 비율
# 비율척도 - n, missing, unique, mean, lowest, highest

# 개별 변수 기술통계량
describe(data$gender) # 특정 변수(명목) 기술통계량 - 비율 제공
describe(data$age) # 특정 변수(비율) 기술통계량 - lowest, highest

summary(data$age)

# prettyR 패키지 이용
# Hmisc 패키지 보다 유용

install.packages("prettyR")
library(prettyR)

# 전체 변수 대상

freq(data) # 각 변수별 : 빈도, 결측치, 백분율, 특징 - 소수점 제공

# 개별 변수 대상
freq(data$gender) # 빈도와 비율 제공

# 기술통계량 보고서 데이터 작성

# 거주지역 변수 리코딩
data$resident2[data$resident == 1] <- "특별시"
data$resident2[data$resident >= 2 & data$resident <= 4] <- "광역시"
data$resident2[data$resident == 5] <- "시군구"

x<- table(data$resident2)
prop.table(x) # 비율 계산 : 0 < x < 1
y <- prop.table(x)
round(y*100,2) # 백분율 적용(소수점 2자리)

# 광역시 시군구 특별시 
# 38.03  14.53  47.44 

# 성별 변수 리코딩
data$gender2[data$gender ==1 ] <- "남자"
data$gender2[data$gender ==2 ] <- "여자"

x <- table(data$gender2)
prop.table(x) # 비율 계산 : 0 < x < 1
y <- prop.table(x)
round(y*100,2) # 백분율 적용(소수점 2자리)
#  남자  여자 
# 58.87 41.13 

# 나이변수 리코딩
data$age2[data$age <= 45 ] <- "중년층"
data$age2[data$age >=46 & data$age <= 59] <- "장년층"
data$age2[data$age >=60] <- "노년층"

x<- table(data$age2)
prop.table(x) # 비율 계산 : 0 < x < 1
y<-prop.table(x)
round(y*100,2) # 백분율 적용(소수점 2자리)

# 노년층 장년층 중년층 
# 24.30  68.53   7.17 

# 학력수준
data$level2[data$level == 1] <- "고졸"
data$level2[data$level == 2] <- "대졸"
data$level2[data$level == 3] <- "대학원졸"

x <- table(data$level2)
prop.table(x) # 비율 계산 : 0 < x < 1
y <- prop.table(x)
round(y*100,2) # 백분율 적용(소수점 2자리)
# 고졸     대졸    대학원졸 
# 39.75    36.40    23.85 
