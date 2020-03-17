# 11-1. 미국 주별 강력 범죄율 단계 구분도 만들기 
install.packages(c("ggiraphExtra","maps","mapproj"))   # 한번에 패키지 설치
library(c(ggiraphExtra,tibble,ggplot2,maps,mapproj))   # 한번에 라이브러리 불러오기

install.packages("ggiraphExtra")
library(ggiraphExtra)

str(USArrests)
head(USArrests)
     
library(tibble)

# 행 이름을 state 변수로 바꿔 데이터 프레임 생성
crime <- rownames_to_column(USArrests, var = "state") 

# 지도 데이터와 동일하게 맞추기 위해 state 의 값을 소문자로 수정
crime$state <- tolower(crime$state) 

str(crime)

# 미국 주 지도 데이터 준비하기 
library(ggplot2) 

install.packages("maps")
library(maps)

states_map <- map_data("state") 
str(states_map) 

# 단계 구분도 만들기 
install.packages("mapproj")
library(mapproj)

ggChoropleth(data = crime,         # 지도에 표현할 데이터
             aes(fill = Murder,    # 색깔로 표현할 변수
                 map_id = state),  # 지역 기준 변수
             map = states_map)     # 지도 데이터

# 인터랙티브 단계 구분도 만들기 
ggChoropleth(data = crime,         # 지도에 표현할 데이터
             aes(fill = Murder,    # 색깔로 표현할 변수
                 map_id = state),  # 지역 기준 변수
             map = states_map,     # 지도 데이터
             interactive = T)      # 인터랙티브

# 11-2. 대한민국 시도별 인구, 결핵 환자 수 단계 구분도 만들기 
# 대한민국 시도별 인구 단계 구분도 만들기 
# 패키지 준비하기 
install.packages(c("ggiraphExtra","maps","mapproj","stringi","devtools","dplyr"))   # 한번에 패키지 설치
library(c(ggiraphExtra,tibble,ggplot2,maps,mapproj,stringi,usethis,devtools,kormaps2014,dplyr)) # 한번에 import

install.packages("stringi") 
library(stringi)

install.packages("devtools") 
library(usethis)
library(devtools)
devtools::install_github("cardiomoon/kormaps2014") 
library(kormaps2014) 

library(ggiraphExtra)
library(tibble)
library(ggplot2) 
library(maps)
library(mapproj)

# 대한민국 시도별 인구 데이터 준비하기 
str(changeCode(korpop1))
install.packages("dplyr")
library(dplyr) 
korpop1 <- rename(korpop1,                   
                  pop = 총인구_명,                   
                  name = 행정구역별_읍면동) 

str(changeCode(kormap1)) 

# 단계 구분도 만들기 
ggChoropleth(data = korpop1,       # 지도에 표현할 데이터
             aes(fill = pop,       # 색깔로 표현할 변수
                 map_id = code,    # 지역 기준 변수
                 tooltip = name),  # 지도 위에 표시할 지역명
             map = kormap1,        # 지도 데이터
             interactive = T)        # 인터랙티브

# 대한민국 시도별 결핵 환자 수 단계 구분도 만들기 
str(changeCode(tbc)) 

ggChoropleth(data = tbc,           # 지도에 표현할 데이터
             aes(fill = NewPts,    # 색깔로 표현할 변수
                 map_id = code,    # 지역 기준 변수
                 tooltip = name),  # 지도 위에 표시할 지역명
             map = kormap1,        # 지도 데이터
             interactive = T)      # 인터랙티브


