install.packages('ggplot2') # 패키지 설치
library(ggplot2) # 패키지 로드 (가져오기)
# 패키지의 데이터, 함수 사용 (패키지::함수)
mpg<-ggplot2::mpg # 자동차 연비
ggplot2::qplot(data=mpg, x=drv, y=hwy, geom="boxplot")

# apply()
two_time <- function(x){
  return(x*2)
}

df <- data.frame(x=c(1,2,3,4,5),
                 y=seq(2,10,2))
df
df2 <- apply(df, 1, two_time) # 열방향(1)으로 적용 / df는 x열,y열로 구성됨.
df2 <- apply(df, 1, sum) # 열방향(1)으로 sum 적용
df2 <- apply(df, 2, sum) # 행방향(2)으로 sum 적용 x:15 / y:30
df2

# tapply() >>> 그룹별 처리를 위한 apply 함수
# 인덱스 : 그룹변수 (class) 별로 도심연비(cty)의 평균 산출
tapply(mpg$cty*0.425144, mpg$class, mean) # mpg >>> km/l 로변환하는데 0.425144 곱해준다.

aggregate(mpg$cty*0.425144,list(mpg$class),mean)

str <- c('홍','길','동') 
str2 <- paste(str,collapse = '') # 문자열 붙이기. / 홍길동(''), 홍 길 동('\s')(공백문자 정규표현식)
substr(str2,2,2) # substr(대상문자, 시작,끝)
str3 <- strsplit(str2,split = '') # 문자열 분리

str <- c('홍','길','동')
str4 <- paste(str,collapse = ',')
str5 <- strsplit(str4,split = ',') # 문자열 분리

substr(c("F123","F124","F125","F126"),2,4)
# [1] "123" "124" "125" "126"
# "F123" 네가지 문자열에서 2번째부터 4번째 문자열을 추출하고, 벡터, c()의 요소 전부에 적용 그래서 위와같이 결과가 나왔음.

s = str5[[1]] # 벡터 리턴
s[2] #[1] "길"









