data1 <- read.csv("../data/diet_effect.csv")
summary(data1)
data2 <- as.data.frame(sapply(data1,as.numeric))
data2 <- data2[!(data2$after==999),]

boxplot(data2$before, 
        data2$after, 
        col = c("red","blue"), 
        names = c("복용전","복용후"),
        main="다이어트 효과 유/무",
        xlab="복용 비교 확인",
        ylab="몸무게")

t.test(data2$before,data2$after, var.equal = T)

# 완수한 사람들 상관계수
diet_diff <- data2 %>%    
  select(before, after) %>%    
  filter(data2$after != 999) 

summary(diet_diff)

cor.test(diet_diff$before, diet_diff$after)

install.packages("corrplot")
library(corrplot)

diet <- cor(diet_diff)

corrplot(diet) 
corrplot(diet, method = "number") 

################################################################################################

# 2. 범죄율

# 첨부한 파일의
# 구별 ['강간', '강도', '살인', '절도', '폭력', '범죄' 검거율 등 여러 변수의
# 상관 관계를 상관 행렬로 나타내세요.

crime <- read.csv("../data/crime_in_Seoul_include_gu_name.csv",fileEncoding = "UTF-8")

crime <- as.data.frame(sapply(crime, as.numeric))
crime <- crime[,-c(1,2)]

crime_number <- crime[,c(1,3,5,7,9)]
crime_caught <- crime[,c(2,4,6,8,10)]

crime_aggregate <- crime[,c(1:10)]

cor(crime_number)

cor(crime_caught)

library(corrplot)

plot(crime_number)

plot(crime_caught)

corrplot(cor(crime_number))

corrplot(cor(crime_caught))

corrplot(cor(crime_aggregate))
