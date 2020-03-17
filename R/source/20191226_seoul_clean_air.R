#통계 분석 기법을 이용한 가설 검정
# 10-1 통계 분석석
# 가설검정, 유의수준결정, 측정도구선정, 데이터 수집, 데이터코딩/프로그래밍, 통계분석 수행, 결과분석
가설검정
귀무가설(영가설,   H0) - 두변수간의 관계까 없다. 또는 차이가 없다. 부정적 형태 진술
ex) 신약 A는 A암 치료에 효과가 없다.
연구가설(대립가설, H1) - 차이가 있다. 또는 효과가 있다. 긍정적 형태 진술 
ex) 신약 A는 A암 치료에 효과가 없다.

#연구 가설을 제시하고 귀무가설을 통해 효과를 인정한다.
분석 결과 생쥐 100마리를 대상으로 했을떄 유의확률 P=0.03이나왔다. 이때 귀무가설은 기각된다.
사회 과학분야에서 임계값 0.05이하이다. 적어도 96마리 이상의 효과가 있어야함. 그러면 H1채택 
의.생명분야에서 임계값 0.01이하이다. 적어도 99마리 이상의 효과가 있어야함. 그러면 H1채택


기술통계 vs 추론통계(모집단 표본)
기 : 지금까지 했던것 
추 : 어떤 값이 발생할 확률
모수(모집단) 통계량(표본)

유의 확률
집단간 차이가 없는데 우연히 차이가 있는 데이터가 추출되 확률

통계 기법
t-검정
: 두집단간의 평균을 비교하여 두 집단간 유의한 차이가 이는지 알아보는것. 

#compat 자동차와 suv 자동차의 연비 검정
데이터 준비
mpg <- as.data.frame(ggplot2::mpg)
library(dplyr)
mpg_diff <- mpg %>% 
  select(class,cty) %>% 
  filter(class %in% c('compact', 'suv'))

table(mpg_diff$class)

t-test()를 이용한 t검정

mpg_diff 데이터를 지정하고, ~ 기호를 이용해 비교할 값인 cty 변수와 비교할 집단인 class 변수를 지정 -> 집단간 분산(퍼진정도)이 같다고 가정하고 var.equal에 T를 지정

t.test(data =mpg_diff, cty~ class, var.equal = T)
# ans p-value < 2.2e-16 : 0.05보다 작으니까 H1(연구가설, 대립가설)을 채택
# h0 두 집단간 차이가 없다. class의 suv와 compact간의 cty가 차이가 없다.
# h1 차이가 있다.
# 결론 h0기각 h1 채택 차이가 있다.



#일반 휘발유(r)과 고급(p) 휘발유의 도시 연비 t 검정
#데이터 준비
mpg_diff2 <- mpg %>% 
  select(fl,cty) %>% 
  filter(fl %in% c("r", "p"))
table(mpg_diff2$fl)

t.test(data= mpg_diff2, cty ~ fl, val.equal = T)
# p-value = 0.2283 (유의수준)이므로 사회과학 임계치0.05보다 크다. 즉, 우연히 나올수있는 확률이다.   
# H0 귀무가설이 유의하지 않다. 그러므로 귀무가설을 채택한다. 두 휘발유간의 차이가 없다로 결론이남.

######################################################################################################
# 퀴즈 (정답아님)
######################################################################################################
#미세먼지 프로젝트 목표
#서울시의 구 중에서 성북구와 중구의 미세먼지 비교 및 지역별 차이 검정

library(readxl)
data <- read_xls('../data/seoul_cleanair.xls',sheet="seoul_cleanair")
data <- read_excel('../data/seoul_cleanair.xls')
data <- read_excel('../data/seoul_cleanair.xls', sheet=1)
data <- read_excel("../data/seoul_cleanair.xls", col_names = T, sheet = 1)
data <- read.csv('../data/seoul_cleanair.csv')


data <- read_xls('seoul_cleanair.xls',sheet="seoul_cleanair")
data <- read_excel('seoul_cleanair.xls')
data <- read_excel('seoul_cleanair.xls', sheet=1)
data <- read_excel("seoul_cleanair.xls", col_names = T, sheet = 1)
data <- read.csv('seoul_cleanair.csv')

## 위에 꺼 다 안됨. 
data <- read.csv('../data/seoul_cleanair.csv', skip = 3)
View(data)
data.type()
data.info()
data <- as.data.frame(data)
View(data)
# 성북구 중구의 미세먼지 비교 및 지역별 차이 검정
head(data)
data <-rename(data,
              구이름= X,
              봄 = '봄.3.4.5월.',
              여름 = '여름.6.7.8월.',
              가을 = '가을.9.10.11월.',
              겨울 = '겨울.12.1.2월.')
gsub(pattern = "(^ +| +$)",
     replacement = "",
     x = data$구이름)
data %>%
  filter(data$구이름 == '성북구')
comparison_city <- data %>% 
  group_by(구이름) %>% 
  filter(구이름  %in% c('종로구 ','중구 ')) %>% 
  summarise()

table(comparison_city)
######################################################################################################



#13-3 상관 분석 - 두변수의 과계성 분석
#상관 분석(Correalation Analysis)

#실업자 수와 개인 소비 지출의 상관관계
데이터 준비
economics <- as.data.frame(ggplot2::economics)
상관분석
cor.test(economics$unemploy, economics$pce)

#p-value < 2.2e-16 상관관계가 유의하다.
#cor: 0.6145176  양수이므로 정비례 관계에 있다.

상관행렬 히트맵 만들기
상관행렬 
여러변수의 관련성을 한번에 알아보고자 할 경우 계수를 행렬로 나타낸 표

데이터 준비
head(mtcars)

car_cor <- cor(mtcars)
round(car_cor,2)

install.packages("corrplot")
library(corrplot)
corrplot(car_cor)
corrplot(car_cor, method = 'number') 
corrplot(car_cor, order = "hclust", addrect = 2) #등등의 다양한 파라미터가 있다.
# order = "hclust": 양과 음으로 묶어서 보기 좋게 해준다.
# addrect = 2 # 보기좋게 라인을 그려 둘로나눠 구분해준다.
col <- colorRampPalette(c('#C3E7FA', '#00BFFF', '#8AE634', '#FFC0CB', '#FFB914'))
col <- colorRampPalette(c(  '#FFC0CB', '#FFB914'))
corrplot(car_cor, col= col(200))


#14-1 신뢰할 수 있는 데이터 분석 보고서 만들기
코드와 결과물이 설명 글과함께 어우러진 보고서
R 마크 다운이란? 보고서 작성하기 위한 형식을 제공함. #like 주피터



