install.packages('ggplot2')
install.packages("dplyr")
install.packages('readxl')

library(readxl) # 엑셀파일 불러오기
library(dplyr) # 전처리
library(ggplot2) # 시각화

economics <- as.data.frame(ggplot2::economics)
ggplot(data = economics, aes(x=date, y=psavert)) + geom_line()
#############################################################
ggplot(mpg, aes(x=drv, y=hwy)) + geom_boxplot()
#############################################################
# 먼저 세종류로 필터링한 데이터를 만든 후 그 데이터를 기반으로
# 특정 열을 x축으로 둬서 그래프 그린다.

class_mpg <- mpg%>%
  filter(class %in% c("compact","subcompact","suv"))

ggplot(data=class_mpg, aes(x=class,y=cty))+geom_boxplot()
###############################################################
install.packages("foreign") # spss, sas, stata 등 통계분석 S/W 파일 로드 
library(foreign)
################################################################
raw_welfare <- read.spss(file='../data/Koweps_etc/데이터/Koweps_hpc10_2015_beta1.sav', to.data.frame=T)
welfare <- raw_welfare
welfare
head(welfare)
tail(welfare)
View(welfare)
dim(welfare)
str(welfare)
summary(welfare)
###################################################################
welfare <- rename(welfare,
                  sex = h10_g3,           # 성별
                  birth = h10_g4,         # 태어난 연도
                  marriage = h10_g10,     # 혼인 상태
                  religion = h10_g11,     # 종교
                  income = p1002_8aq1,    # 월급
                  code_job = h10_eco9,    # 직종 코드
                  code_region = h10_reg7) # 지역 코드
####################################################################
# 성별에 따른 비교
class(welfare$sex)
#[1] "numeric"
table(welfare$sex)
#   1    2 
#7578 9086

# 이상치 결측 처리
welfare$sex <- ifelse(welfare$sex == 9, NA, welfare$sex)

# 결측치 확인
table(is.na(welfare$sex))

#성별 항목 이름 부여
welfare$sex <- ifelse(welfare$sex == 1, "male", "female")
table(welfare$sex)

qplot(welfare$sex)
###################################################################
# 월급에 따른 비교 
class(welfare$income)
summary(welfare$income)
qplot(welfare$income)

qplot(welfare$income) + xlim(0, 1000)

welfare$income <- ifelse(welfare$income %in% c(0,9999), NA, welfare$income)

# 결측치 확인
table(is.na(welfare$income))
####################################################################
# 1.성별 월급 평균표 만들기
sex_income <- welfare %>%
  filter(!is.na(income)) %>%
  group_by(sex) %>%
  summarise(mean_income = mean(income))

sex_income
ggplot(data=sex_income, aes(x=sex, y=mean_income)) + geom_col()
###################################################################
# 몇 살 때 월급을 가장 많이 받을까?
class(welfare$birth)
summary(welfare$birth)

qplot(welfare$birth)

# 결측치 확인
table(is.na(welfare$birth))

# 이상치 결측 처리
welfare$birth <- ifelse(welfare$birth == 9999, NA, welfare$birth)
table(is.na(welfare$birth))

# 파생변수 만들기 - 나이
welfare$age <- 2015 - welfare$birth + 1
summary(welfare$age)
qplot(welfare$age)

#나이에 따른 월급 평균표 만들기
age_income <- welfare %>%
  filter(!is.na(income)) %>%
  group_by(age) %>%
  summarise(mean_income = mean(income))

ggplot(data = age_income, aes(x=age, y=mean_income)) + geom_line()

welfare <- welfare %>%
  mutate(ageg = ifelse(age < 30, "young",
                       ifelse(age <= 59, "middle", "old")))
table(welfare$ageg)

#1.연령대별 월급 평균표 만들기

ageg_income <- welfare %>%
  filter(!is.na(income)) %>%
  group_by(ageg) %>%
  summarise(mean_income = mean(income))

ageg_income

ggplot(data = ageg_income, aes(x=ageg, y=mean_income)) + geom_col()

# 범주 순서 지정 : scale_x_discrete(limits = c())
ggplot(data=ageg_income, aes(x=ageg,y=mean_income)) +
  geom_col() + 
  scale_x_discrete(limits = c("young", "middle", "old"))

# 성별 월급 차이는 연령대별로 다를까?
# 연령대 및 성별 월급 평균표 만들기
sex_income <- welfare %>%
  filter(!is.na(income)) %>%
  group_by(ageg, sex) %>%
  summarise(mean_income = mean(income))

sex_income

# stacked graph
ggplot(data = sex_income, aes(x=ageg, y=mean_income, fill = sex)) +
  geom_col() + 
  scale_x_discrete(limits = c("young", "middle", "old"))

# parallel graph
ggplot(data = sex_income, aes(x=ageg, y=mean_income, fill = sex)) +
  geom_col(position="dodge") + 
  scale_x_discrete(limits = c("young", "middle", "old"))

########################################################################
# 나이별 성별 월급차이 분석하기
sex_age <- welfare %>%
  filter(!is.na(income)) %>%
  group_by(age, sex) %>%
  summarise(mean_income = mean(income))

head(sex_age)

ggplot(data = sex_age, aes(x=age, y=mean_income, col=sex)) + geom_line()
#########################################################################
class(welfare$code_job)

table(welfare$code_job)

# 직업분류코드 목록 불러오기
library(readxl)
list_job <- read_excel("../data/Koweps_Codebook.xlsx",col_names=T, sheet=2)
head(list_job)

# welfare에 직업명 결합
welfare <- left_join(welfare,list_job, id="code_job")

welfare %>% 
  filter(!is.na(code_job)) %>%
  select(code_job, job) %>%
  head(10)

# 직업별 월급 평균표
job_income <- welfare %>% 
  filter(!is.na(job) & !is.na(income)) %>%
  group_by(job) %>%
  summarise(mean_income = mean(income))

head(job_income)

# 상위 10개 추출
top10 <- job_income %>%
  arrange(desc(mean_income)) %>%
  head(10)
top10

# 그래프 만들기
ggplot(data = top10, aes(x=reorder(job,mean_income),y=mean_income)) + 
  geom_col()+
  coord_flip() # 90도 회전.

# 4. 하위 10개 추출
bottom <- job_income %>%
  arrange(mean_income) %>%
  head(10)
bottom

ggplot(data = bottom,aes(x=reorder(job,-mean_income), y=mean_income))+
  geom_col()+
  coord_flip()+
  ylim(0,850)

# 성별 직업 빈도

# 남성 직업 빈도 상위 10개 추출
job_male <- welfare %>%
  filter(!is.na(job) & sex == "male") %>%
  group_by(job) %>%
  summarise(n=n()) %>%
  arrange(desc(n)) %>%
  head(10)

job_male

# 여성 직업 빈도 상위 10개 추출
job_female <- welfare %>%
  filter(!is.na(job) & sex == "female") %>%
  group_by(job) %>%
  summarise(n=n()) %>%
  arrange(desc(n)) %>%
  head(10)

job_female

# 남성 직업 빈도 상위 10개 직업
# 'n' >>> 개수 count하라는 변수
ggplot(data = job_male, aes(x=reorder(job,n), y=n)) +
  geom_col()+
  coord_flip()

# 여성 직업 빈도 상위 10개 직업.
ggplot(data = job_female, aes(x=reorder(job,n), y=n)) +
  geom_col()+
  coord_flip()

# 종교 유무에 따른 이혼율
# "종교가 있는 사람들이 이혼을 덜 할까?"

class(welfare$religion)

table(welfare$religion)

welfare$religion <- ifelse(welfare$religion == 1, "yes", "no")
table(welfare$religion)

qplot(welfare$religion)

# 결혼 유무
class(welfare$marriage)

table(welfare$marriage)

# 코드표 참고
#   0    1    2    3    4    5    6 
#2861 8431 2117  712   84 2433   26

welfare$group_marriage <- ifelse(welfare$marriage == 1, "marriage",
                          ifelse(welfare$marriage == 3, "divorce", NA))

table(welfare$group_marriage)

table(welfare$group)

table(is.na(welfare$group_marriage))

qplot(welfare$group_marriage)

# 종교 유무에 따른 이혼율 분석하기
# 1. 종교 유무에 따른 이혼율 표 만들기

religion_marriage <- welfare %>%
  filter(!is.na(group_marriage)) %>%
  group_by(religion, group_marriage) %>%
  summarise(n=n()) %>%
  mutate(tot_group = sum(n)) %>%
  mutate(pct = round(n/tot_group*100,1))

religion_marriage

# 이혼율 표 만들기
# 이혼 추출
divorce <- religion_marriage %>%
  filter(group_marriage == "divorce") %>%
  select(religion, pct)

divorce
# 그래프 만들기
ggplot(data = divorce, aes(x=religion, y=pct)) + geom_col()

# 연령대 및 종교 유무에 따른 이혼율 분석하기

# 연령대별 이혼율 표 만들기

ageg_marriage <- welfare %>%
  filter(!is.na(group_marriage)) %>%
  group_by(ageg,group_marriage) %>%
  summarise(n=n()) %>%
  mutate(tot_group = sum(n)) %>%
  mutate(pct = round(n/tot_group*100,1))

ageg_marriage

# 연령대별 이혼율 그래프 만들기
# 초년 제외, 이혼 추출
ageg_divorce <- ageg_marriage %>%
  filter(ageg != "young" & group_marriage == "divorce") %>%
  select(ageg, pct)

ageg_divorce

# 그래프 만들기
ggplot(data = ageg_divorce, aes(x=ageg, y=pct)) + geom_col()

# 연령대 , 종교유무 , 결혼상태별 비율표 만들기
ageg_religion_marriage <- welfare %>%   
  filter(!is.na(group_marriage) & ageg != "young") %>%   
  group_by(ageg, religion, group_marriage) %>%   
  summarise(n = n()) %>%   
  mutate(tot_group = sum(n)) %>%   
  mutate(pct = round(n/tot_group*100, 1)) 

ageg_religion_marriage 

# count() 활용 
ageg_religion_marriage <- welfare %>%   
  filter(!is.na(group_marriage) & ageg != "young") %>%   
  count(ageg, religion, group_marriage) %>%   
  group_by(ageg, religion) %>%   
  mutate(pct = round(n/sum(n)*100, 1)) 

ageg_religion_marriage

#연령대 및 종교 유무별 이혼율 표 만들기 
df_divorce <- ageg_religion_marriage %>%   
  filter(group_marriage == "divorce") %>%   
  select(ageg, religion, pct) 

df_divorce

# 4. 연령대 및 종교 유무에 따른 이혼율 그래프 만들기 
ggplot(data = df_divorce, aes(x = ageg, y = pct, fill = religion )) +   
  geom_col(position = "dodge") 

# 지역별 연령대 비율
# 노년층이 많은 지역은 어디일까?

class(welfare$code_region) 
# [1] "numeric"
table(welfare$code_region) 
#    1    2    3    4    5    6    7  <<< 지역을 7군데로 나눔.
# 2486 3711 2785 2036 1467 1257 2922 

# 지역코드 목록 만들기
list_region <- data.frame(code_region = c(1:7),
                          region = c("서울",                                      
                                     "수도권(인천/경기)",                                      
                                     "부산/경남/울산",                                      
                                     "대구/경북",                                      
                                     "대전/충남",                                      
                                     "강원/충북",                                      
                                     "광주/전남/전북/제주도")) 
list_region

# welfare에 지역명 변수 추가.
welfare <- left_join(welfare, list_region, id = "code_region") 
## Joining, by = "code_region" 
welfare %>%   
  select(code_region, region) %>%   
  head # default 6개만 보여줌.

# 1.지역별 연령대 비율 분석하기

region_ageg <- welfare %>%
  group_by(region, ageg) %>%
  summarise(n=n()) %>%
  mutate(tot_group = sum(n)) %>%
  mutate

head(region_ageg)

# count() 활용 
region_ageg <- welfare %>%   
  count(region, ageg) %>%   
  group_by(region) %>%   
  mutate(pct = round(n/sum(n)*100, 2)) 

head(region_ageg)

# 그래프 만들기
ggplot(data = region_ageg, aes(x=region,y=pct, fill=ageg)) + 
  geom_col() + 
  coord_flip()

# 노년층 비율 내림차순 정렬
list_order_old <- region_ageg %>%
  filter(ageg == "old") %>%
  arrange(pct)

list_order_old

# 지역명 순서 변수 만들기
order <- list_order_old$region
order
ggplot(data = region_ageg, aes(x=region, y=pct, fill=ageg)) +
  geom_col()+
  coord_flip()+
  scale_x_discrete(limits = order)

# 4.연령대 순으로 막대 색깔 나열하기
class(region_ageg$ageg)
levels(region_ageg$ageg)

region_ageg$ageg <- factor(region_ageg$ageg,
                           levels = c("old","middle","young"))
class(region_ageg$ageg)

levels(region_ageg$ageg) 

ggplot(data = region_ageg, aes(x=region, y=pct, fill=ageg)) +
  geom_col() +
  coord_flip()+
  scale_x_discrete(limits = order)

# quiz-1
# 한국복지패널데이터를 이용(1~2번)
# 1. 결혼 유.무와 소득의 관계
# 2. 결혼 유.무와 남녀 소득의 관계를 나타내세요.

# marriage and income

# 1. 결혼 유.무와 소득의 관계
table(welfare$marriage)

welfare$group_marriage <- ifelse(welfare$marriage %in% c(1, 4), 'marriage',
                          ifelse(welfare$marriage %in% c(3, 5), 'not_marriage', 'Other'))
table(welfare$group_marriage)

table(is.na(welfare$marriage_blade)) 

marriage_income <- welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(group_marriage) %>% 
  summarise(mean_income = mean(income))

marriage_income

ggplot(data = marriage_income, aes(x = group_marriage, y = mean_income)) +
  geom_col()
 
# 2. 결혼 유.무와 남녀 소득의 관계를 나타내세요.
marriage_income_sex <- welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(group_marriage,sex) %>% 
  summarise(mean_income = mean(income))

marriage_income_sex

ggplot(data = marriage_income_sex, aes(x = group_marriage, y = mean_income, fill=sex)) +
  geom_col(position="dodge")
  

# quiz-2
data1 <- read.csv('../data/2013년_프로야구선수_성적.csv')
data1
#1.
play_count <- data1 %>%
  group_by(팀) %>%
  summarise(play_number = sum(경기))

play_count
#2.
ggplot(data = play_count, aes(x=팀,y=play_number)) + geom_col()

#3. 학생별 국어성적 데이터 불러오기
score <- read.csv('../data/학생별국어성적_new.txt')
score

#4. x축은 이름, y축은 점수로 산점도에 표시되게 그래프를 그려 보세요.
ggplot(data = score, aes(x=이름, y=점수)) +
  geom_point()

#5. 4를 막대그래프로 그려보기
ggplot(data = score, aes(x=이름, y=점수)) +
  geom_col()
#6. 학생과목별 성적 _ 국영수.csv로 아래와 같은 그래프 그리기
t_score <- read.csv('../data/학생별과목별성적_국영수_new.csv')
t_score
ggplot(data = t_score, aes(x=이름, y=점수, fill= 과목)) +
  geom_col()

install.packages("gridExtra")
library(gridExtra)
