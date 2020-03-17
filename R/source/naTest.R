df<-data.frame(gender=c('M','F',NA,'M','F'),
           score=c(5,4,3,4,NA))

#결측치 확인
is.na(df)
table(is.na(df))
table(is.na(df$gender))
table(is.na(df$score))

sum(df$score)#결측치

df %>% filter(is.na(score))
#1. filter 기반으로 결측치 제거
df2<-df %>% filter(!is.na(score))
sum(df2$score)#16

df2<-df %>% filter(!is.na(gender) & !is.na(score))
df2
#결측치가 하나라도 포함된 행 제거
df2<-na.omit(df)

#2. 함수인자na.rm = T 기반으로 결측치 제외하여 요약
sum(df$score,na.rm = T)
mean(df$score,na.rm = T)
df %>% summarise(mean(score,na.rm = T))

#3. NA를 별도의 값(기본값,평균,최빈값)으로 변환
mean_na = mean(df$score,na.rm = T)
#df$score의 정제
df$score<-ifelse(is.na(df$score),mean_na,df$score)

#  이상치 3,20
#  통계적 상하위 0.3% 혹은 Q1-1.5*IQR - Q3 +1.5*IQR 
df<-data.frame(gender=c(1,2,3,1,2),
               score=c(5,4,3,4,20))
table(df$gender)
#이상치를 NA로 정의 정제  
df$gender<-ifelse(df$gender==3,NA,df$gender)
df$score<-ifelse(df$score>10,NA,df$score)

df %>% summarise(mean(score,na.rm = T))

boxplot(mpg$hwy)
boxplot(mpg$hwy)$stats
#이상치를 NA로 정의
mpg$hwy<-ifelse(mpg$hwy<12 | mpg$hwy>37,NA,mpg$hwy)
table(is.na(mpg$hwy))
# NA정제 
mpg %>% 
  group_by(drv) %>% 
  summarise(mean(hwy,na.rm = T))

