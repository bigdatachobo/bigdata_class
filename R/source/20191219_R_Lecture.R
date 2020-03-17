getwd()
setwd("D:/Work_R")

exam <- read.csv("data/csv_exam.csv")
head(exam, 10)
tail(exam, 10)
View(exam)
dim(exam)
str(exam)
summary(exam)

##### install ggplot2 ######
install.packages('ggplot2') # 패키지 설치
library(ggplot2) # 라이브러리 등록
ggplot2::mpg  #라이브 러리 속 특정 데이터 불러오기
mpg <- as.data.frame(ggplot2::mpg) # 불러온 데이터 데이터 프레임으로 만들기


##### install dplyr #####
install.packages("dplyr")
library(dplyr)


##### example #####
head(mpg)
tail(mpg)
View(mpg)
dim(mpg)
str(mpg)
summary(mpg)

df_raw <- data.frame(var1 = c(1, 2, 1), var2 = c(2, 3, 2))
df_raw
# 변수 복사
df_new <- df_raw
df_new
# 컬럼명 변경 (rename)
df_new <- rename(df_new, v2 = var2)
df_new


##### 퀴즈 #####
head(mpg)
mpg_new <-rename(mpg, city= cty, highway = hwy )
head(mpg_new)

##### 파생변수 만들기 #####
# sum 추가
df <- data.frame(var1 = c(4,3,8), var2 = c(2,6,1))
df$var_sum <- df$var1 + df$var2
df

# 평균 추가
df$var_mean <- (df$var1 + df$var2) /2 #var_mean 파생변수 생성
df

# 통합연비 변수 생성성
mpg$total <- (mpg$cty + mpg$hwy)/2 
head(mpg)

# 1. 조건문을 활용해 파생변수 만들기
sumary(mpg$total) # 요약 통계량 산출
hist(mpg$total)   # 히스토그램 생성

# 2. 조건문으로 합격 판정 변수 만들기
mpg$test <- ifelse(mpg$total >= 20 , 'pass', 'fail')
head(mpg, 20)

# 3. 빈도표로 합격 판정 자동차 수 살펴보기
table(mpg$test)

# 4. 막대 그래프 빈도 표현하기
qplot(mpg$test)

# 중첩 조건문 활용하기 - 연비 등급 변수 만들기
# A : 30이상 B: 20이상  C: 나머지

mpg$grade <- ifelse(mpg$total >= 30, "A", 
                    ifelse(mpg$total >= 20, "B", "C"))
tail(mpg, 20) #데이터 확인

table(mpg$grade) #ans A:10, B:118, C:106 
qplot(mpg$grade)# 빈도 막대 그래프 

mpg$grade2 <- ifelse(mpg$total >= 30, "A", 
                    ifelse(mpg$total >= 25, "B",
                           ifelse(mpg$total >= 20, "C","D")))
table(mpg$grade2)
qplot(mpg$grade2)


##### 퀴즈 2 #####
midwest <- ggplot2::midwest
midwest <- as.data.frame(ggplot2::midwest)
head(midwest)
summary(midwest)
View(midwest)
midwest <- rename(midwest, total = poptotal, asian = popasian)
midwest$A_P_t <- midwest$asian/ midwest$total * 100
hist(midwest$A_P_t)
head(midwest)
mean(midwest$A_P_t)
midwest$L_or_S <- ifelse(midwest$A_P_t > mean(midwest$A_P_t),"large","small")
midwest
table(midwest$L_or_S)
qplot(midwest$L_or_S)


##### 6장 자유자재로 데이터 가공하기 #####
# 데이터 전처리  - dplyr 패키지를 많이 사용함
# filter, select, arrange, mutate, sumamarise, group_by, left_join, bind_rows
exam 

# filter: 행 추출,  $: 열 추출
exam %>% filter(class ==1) # 파이프라인 연산자 단축키: [control + shift + m]
exam %>% filter(class ==2)
exam %>% filter(class !=3)
exam %>% filter(math > 50)
exam %>% filter(math < 50)
exam %>% filter(english >= 80)
exam %>% filter(english <= 80)
exam %>% filter(class == 1 & math >= 50) # and
exam %>% filter(class == 2 & english >= 80)
exam %>% filter(math >= 90 | english >= 90) # or
exam %>% filter(science < 50 | english < 90)
exam %>% filter(class == 1 | class == 3 | class == 5)
exam %>% filter(class %in% c(1,3,5)) # 포함 된 자료만 

#추출한 행으로 데이터 만들기
class1 <- exam %>% filter(class == 1)
class2 <- exam %>% filter(class == 2)
class2
class1
class2$math
mean(class2$math)

# 나누셈의 몫: %/%     나누셈의 나머지: %%
# Q1
mpg4 <-mpg %>% filter( mpg$displ <= 4)
mpg5 <- mpg %>% filter( mpg$displ >= 5)
mean(mpg4$hwy)
mean(mpg5$hwy)
hhwwyy <- ifelse(mean(mpg4$hwy)> mean(mpg5$hwy), "4가 연비가 좋다.", "5가 연비가 좋다.")
print(hhwwyy)

# Q2
mpg_Audi <-mpg %>% filter( mpg$manufacturer == "audi")
mean(mpg_Audi$cty)
mpg_toyota <-mpg %>% filter( mpg$manufacturer == "toyota")
mean(mpg_toyota$cty)
com <-ifelse(mean(mpg_Audi$cty)> mean(mpg_toyota$cty), "아우디가 연비가 좋다.", "토요타가 연비가 좋다.")
print(com)


# 6-3 필요한 변수(열)만 추출하기
exam %>% select(math)
exam %>% select(english)
exam %>% select(math, english, science) # 여러개를 같이
exam %>% select(-math) #수학만 제외하고 가지고 오겠다.
exam %>% select(-math, -english)

#dplyr 함수 조합하기 + 가독성 높이기
exam %>% 
  filter(class ==1) %>%
  select(class, english)

exam %>% 
  select(id, math) %>% 
  head(10)

# Q1
mpg_filter <-mpg %>% 
  select(class, cty)
head(mpg_filter)

# Q2
mpg_filter %>% 
  filter(mpg_filter$class == 'suv')
mean(mpg_filter$cty)

mpg_filter %>% 
  filter(mpg_filter$class == 'compact')
mean(mpg_filter$cty)


# 6-4 순서대로 정렬하기  Arrange()
exam %>%  arrange(math)       # 오름 차순 정렬 #기본 정렬
exam %>%  arrange(desc(math)) # 내림 차순 정렬
exam %>%  arrange(class, math)# class 정렬 후 math 정렬
exam %>%  arrange(class, desc(math))

# Q
mpg %>%
  filter( mpg$manufacturer == 'audi') %>% 
  arrange(desc(hwy)) %>% 
  head(5)

exam %>% 
  mutate(total = math + english + science) %>% # 총합 변수 추가
  head()                                       # 일부 추출

exam %>% 
  mutate(total = math + english + science) %>%    # 총합 변수 추가
  mutate(mean = (math + english + science)/3) %>% # 총평균 변수
  head()                                          # 일부 추출

exam %>% 
  mutate(test = ifelse(science >=60, 'pass', 'fail')) %>% 
  head

# 추가한 변수를 dplyr 코드에 바로 활용하기
exam %>% 
  mutate(total = math + english + science) %>% 
  arrange(total) %>% 
  head

# Q
mpg_copy <- mpg
mpg_copy %>%
  mutate(total = (cty + hwy),
         mean = total/2) %>% 
  arrange(desc(mean)) %>% 
  head(3)

# 6-6 집단별로 요약하기
exam %>%  summarize(mean_math = mean(math)) #수학 평균 산출
exam %>%  
  group_by(class) %>%               #class 별로 분리
  summarize(mean_math = mean(math)) # math 평균 산출, 열명 지정
exam %>%  
  group_by(class) %>%                    #class 별로 분리
  summarize(mean_math = mean(math),      # math 평균 산출, 열명 지정
            sum_math = sum(math),        # math 합계  
            median_math = median(math),  # math 중앙값
            n = n())                     # math 학생수 -> 몇 행으로 되어 있는지 '빈도'를 구하는 기능
exam

# 집단별로 다시 집단 나누기
mpg %>% 
  group_by(manufacturer, drv) %>%       # 회사별, 구동 방식별 분리
  summarize(mean_cty= mean(cty)) %>%    # cty 평균 산출
  head(10)                              # 일부 출력력

# dplyr 조합하기
# Q
mpg %>%  
  group_by(manufacturer) %>%
  filter(class == 'suv') %>%
  mutate(total = (hwy + cty)) %>%
  summarize(mean = mean(total/2)) %>% 
  arrange(desc(mean)) %>% 
  head(5)

mpg %>%  
  group_by(manufacturer) %>%
  filter(class == 'suv') %>%
  mutate(mean = (hwy + cty)/2) %>%
  arrange(desc(mean)) %>% 
  head(5)

#Q1
mpg %>% 
  group_by(class) %>% 
  summarise(mean= mean(cty))
#Q2
mpg

#Q3


##### 오후 수업 #####
# 가로로 합치기
# 중간고사 데이터 생성
test1 <- data.frame(id = c(1,2,3,4,5), midterm = c(60,80,70,90,85))
# 기말고사 데이터 생성
test2 <- data.frame(id = c(1,2,3,4,5), final = c(70,83,65,95,80))

total <- left_join(test1, test2, by = 'id')

# 다른 데이터 활용해 변수 추가하기
# 반별 담임교사 명단 생성
name<- data.frame(class = c(1,2,3,4,5,6), teacher = c('kim', 'lee', 'park', 'choi', 'jung', 'wang'))

exam_new <- left_join(exam, name, by = 'class') # left_join 이기 때문에 name에 있는 class 6의 선생님은 입력되지 않는다.

#세로로 합치기
group_a <- data.frame(id = c(1,2,3,4,5) , test = c(60,80,70,90,85))
group_b <- data.frame(id = c(6,7,8,9,10), test = c(70,83,65,95,80))

group_all <- bind_rows(group_a, group_b)

#Q
fuel <- data.frame(fl = c('c','d','e','p','r'),
                   price_fl = c(2.35, 2.38, 2.11, 2.76, 2.22),
                   stringAsFactors = F)
fuel
mpg<-left_join(mpg, fuel, by = 'fl')
mpg %>% 
  select('model', 'fl', 'price_fl') %>% 
  head(5)



#4. 순서대로 정렬하기
#5. 파생변수 추가하기
#6. 각 집단별로 다시 집단 나누기
#7. 데이터 합치기
아래의 문제를 해결해 보세요.

excel_exam.xlsx에서 20명의 학생의 데이터를 불러와서
1. math, english, science  3과목의 합계를 출력하세요.(s_total)
2. math, english, science  3과목의 평균을 출력하세요.(s_mean)
3. 평균이 60점 이상이면 "pass" 그렇지 않으면 "fail"를 부여하는 파생변수test1를 생성하세요.
4. 3의 결과의 빈도수와 그래프로 나타내세요.
5. 평균이 80점 이상이면 "A", 70이상이면 "B", 그외는 "C"를 부여하는 파생변수 test2를 생성하세요.
6. 5의 결과를 상위 10개만 출력하세요.
7. 5의 결과를 하위 7개만 출력하세요.
8. 5의 결과를 빈도수와 그래프로 나타내세요.

excel_exam <- read_excel('data/excel_exam.xlsx')
exam_xl_df <- as.data.frame(excel_exam)
exam_xl_df <- exam_xl_df %>% 
  mutate(s_total = math + english + science,
         s_mean = s_total/3,
         test1 = ifelse(s_mean>= 60, 'pass', 'fail'),
         test2 = ifelse(s_mean>= 80, 'A', ifelse(s_mean>= 70, 'B', 'C')))
exam_xl_df
qplot(exam_xl_df$test1)
head(exam_xl_df, 10)
head(exam_xl_df, 7)
qplot(exam_xl_df$test2)


# 7장 데이터 정제
# 빠진 데이터, 이상한 데이터 제거 하기
df <- data.frame(sex = c('M','F', NA, 'M', 'F'),
                 score = c(5, 4, 3, 4, NA))
#결측치 확인하기
is.na(df)              #결측치 확인하기
table(is.na(df))       #결측치 빈도수 세기
table(is.na(df$sex))   # 'sex' 컬럼 빈칸 빈도수 세기
table(is.na(df$score)) # 'score' 컬럼 빈칸 빈도수 세기

#결측치값을 포함한 상태로 분석
mean(df$score) #ans NA
sum(df$score) #ans NA

#결측치 제거하기
library(dplyr)               # 파이프라인 등의 기능을 하게 해주는 패키지
df %>% filter(is.na(score))  # score가 NA인 데이터만 출력
df %>% filter(!is.na(score)) # score가 NA가 아닌 데이터만 출력
 
 
#결측치 제외한 데이터로 분석하기
df_nomiss <- df %>% filter(!is.na(score))
mean(df_nomiss$score) #ans 4
sum(df_nomiss$score)  #ans 16

#여러 변수 동시에 결측치 없는 데이터 추출하기
df_nomiss <- df %>% filter(!is.na(score) & !is.na(sex))
df_nomiss

#결측치가 하나라도 있으면 제거하기##################################(되도록이면 사용하지 말것)
df_nomiss <- na.omit(df) # 모든 변수에 결측치 없는 데이터 추출
df_nomiss 

# 함수의 결측치 제외 기능 이용하기 - na.rm = T
mean(df$score, na.rm = T) # 결측치 제외하고 평균 산출 #ans 4
sum(df$score, na.rm = T)  # 결측치 제외하고 합계 산출 #ans 16

# summarise()에서 na.rm - T사용하기
# 결측치 생성
exam <- read.csv("csv_exam.csv") # 데이터 불러오기
exam[c(3,8,15), 'math'] <- NA    # 3,8,15행의 math에 na값 할당

# 평균 구하기
exam %>%  summarise(mean_math = mean(math))            #평균 산출  #ans  NA
exam %>%  summarise(mean_math = mean(math, na.rm = T)) #평균 산출  #ans  55.23529

# 다른 함수에 적용하기
exam %>% summarise(mean_math = mean(math , na.rm = T),
                   sum_math = sum(math , na.rm = T),
                   median_math = median(math , na.rm = T))
# ans 
# mean_math   sum_math   median_math
# 55.23529      939          50

# 결측치 대체하기
# 대체법 (imputation)
# 대표값(평균, 최빈값 등) 으로 일괄 대체
# 통계 분석 기법 적용, 예측값 추정해서 대체

# 평균 값으로 결측치 대체하기
# 평균 구하기
mean(exam$math, na.rm = T) #결측치 제외한 math 평균 : 55.23529
exam$math <- ifelse(is.na(exam$math), 55, exam$math) #math가 NA이면 55로 대체 
table(is.na(exam$math)) #ans : FALSE 20 

#Q
#데이터 로드하고 결측치 데이터 만들기
mpg <- as.data.frame(ggplot2::mpg)          # 데이터 불러오기      
mpg[c(65, 124, 131, 153, 212), "hwy"] <- NA # "hwy" 컬럼의 c(65, 124, 131, 153, 212)행에 NA 할당하기 

#결측치 파악하기
table(is.na(mpg$drv)) # NA 0개
table(is.na(mpg$hwy)) # NA 5개

# 결측치 제외하고, 구동 방식별 hwy 평균 알아보기
mpg %>% 
  group_by(drv) %>% 
  summarise(hwy_mean = mean(hwy, na.rm = T))#ans  4:19.2,  f:28.2,  r:21

# 이상치 제거하기 - 1.존재할 수 없는 값
# 논리적으로 존재할 수 없으므로 바로 결측 처리 후 분석 시 제외

# 이상치 포함된데이터 생성 - sex3, score 6
outlier <- data.frame(sex=c(1,2,1,3,2,1),
                      score =c(5,4,3,4,2,6))
outlier 
# 이상치 확인하기
table(outlier$sex)

table(outlier$score)

# 결측 처리하기 - sex
# sex가 3이면 NA 할당
outlier$sex <- ifelse(outlier$sex ==3, NA, outlier$sex)
outlier

# 결측 처리하기 - score
# sex가 1~5 dkslaus NA 할당 >>> 6점이 NA로 바뀌게 됨.
outlier$score <- ifelse(outlier$score > 5, NA, outlier$score)
outlier

#결측치 제외하고 분석
outlier %>% 
  filter(!is.na(sex) & !is.na(score)) %>%
  group_by(sex) %>%
  summarise(mean_score = mean(score))

# 이상치 제거하기 - 2.극단적인 값.

# 상자그림으로 극단치 기준 정해서 제거하기
# 상자그림 생성
mpg <- as.data.frame(ggplot2::mpg)
boxplot(mpg$hwy)

#결측 처리하기
mpg$hwy <- ifelse(mpg$hwy < 12 | mpg$hwy > 37, NA, mpg$hwy)
table(is.na(mpg$hwy))

# 결측치 제외하고 분석하기
mpg %>% 
  group_by(drv) %>% 
  summarise(mean_hwy = mean(hwy, na.rm = T))

# quiz
# 이상치를 일부러 집어넣어 보고 문제 푼다.

mpg <- as.data.frame(ggplot2::mpg)  # mpg 데이터 불러오기
mpg[c(10,14,58,93),"drv"] <- "k"
mpg[c(29,43,129,203),"cty"] <-c(3,4,39,42)
