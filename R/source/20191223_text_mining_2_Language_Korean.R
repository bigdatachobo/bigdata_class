install.packages("rJava") 
install.packages("memoise") 
install.packages("KoNLP") 
install.packages("dplyr")
# 패키지 로드
library(rJava)
library(dplyr) 
library(KoNLP) 

useSejongDic()

mergeUserDic(data.frame("서진수","ncn"))
# buildDictionary(data.frame("서진수","ncn"))

data1 <- readLines("../data/seoul_new.txt")
data1

data2 <- sapply(data1, extractNoun,USE.NAMES = F)
data2

head(unlist(data2), 30)

data3 <- unlist(data2)
data3

# gsub("변경전 글자", "변경후 글자", "원본데이터")

data3 <- gsub("\\d+","",data3)
data3 <- gsub("서울시","",data3)
data3 <- gsub("서울","",data3)
data3 <- gsub("요청","",data3)
data3 <- gsub("제안","",data3)
data3 <- gsub("\\W","",data3)
data3

write(unlist(data3),"../data/seoul_2.txt")

data4 <- read.table("../data/seoul_2.txt")
data4
nrow(data4)
 
wordcount <- table(data4)
wordcount

head(sort(wordcount, decreasing = T),20)

data3 <- gsub("님","",data3)
data3 <- gsub("OO","",data3)
data3 <- gsub("시장","",data3)
data3 <- gsub("한","",data3)
data3 <- gsub("관련","",data3)
data3 <- gsub("개선","",data3)
data3 <- gsub("문제","",data3)
data3 <- gsub("관리","",data3)
data3 <- gsub("민원","",data3)
data3 <- gsub("이용","",data3)
data3 <- gsub("건의","",data3)

data3

write(unlist(data3),"../data/seoul_3.txt")
data4 <- read.table("../data/seoul_3.txt")
wordcount <- table(data4)
head(sort(wordcount, decreasing = T), 20)

library(RColorBrewer)
palete <- brewer.pal(9,"Set3")

wordcloud(names(wordcount),
          freq = wordcount,
          scale = c(5,1),
          rot.per = 0.25,
          min.freq = 1,
          random.order = F,
          random.color = T,
          colors = palete)

legend(0.3,
       1,
       "서울시 응답소 요청사항 분석",
       cex=0.8,
       fill=NA,
       border=NA,
       bg="white",
       text.col="red",
       text.font=2,
       box.col="red")

