#요약통계
#R 기본패키지
#summary(mpg,na.rm = TRUE)
summary(mpg$cty)
#관측값 개수(n), 평균(mean), 표준편차(sd), 중앙값(median), 절삭평균(10% 절삭평균), 중위값절대편차(from 중위값) (MAD, median absolute deviation), 최소값(min), 최대값(max), 범위(range), 왜도(skew), 첨도(kurtosis), 표준오차(SE, standard error)
install.packages("psych")
library(psych)
describe(mpg,na.rm = TRUE)
#-------------------------------------------------------
#basic = TRUE : 관측치 개수, null 개수, NA 개수, 최소값, 최대값, 범위, 합
#desc = TRUE : 중앙값, 평균, 분산, 표준편차, 변이계수
#norm = TRUE : 왜도, 첨도, 정규성 검정통계량, 정규성 검정 P-value

install.packages("pastecs")
library(pastecs)
stat.desc(mpg$cty,norm = T)


install.packages("dplyr")
library(dplyr)
