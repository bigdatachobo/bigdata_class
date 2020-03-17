install.packages("wordcloud")
install.packages("tm")

library(NLP)
library(RColorBrewer)

data1 <- readLines("../data/tm_test1.txt")
data1
class(data1)

corp1 <- Corpus(VectorSource(data1))
inspect(corp1) # corpus 안의 내용 살펴보기
tdm <- TermDocumentMatrix(corp1)
tdm

m <- as.matrix(tdm)
m # 열이 문장 1개를 의미 
  # 행은 문장 안에 어떤 요소들이 들어있나 표시
  # 1은 단어가 쓰임을 의미 / 0은 쓰이지 않음을 의미.

corp2 <- tm_map(corp1,
                stripWhitespace) # 여러개의 공백을 하나의 공백으로 변환

corp2 <- tm_map(corp2,
                tolower) # 소문자로 변환

corp2 <- tm_map(corp2,
                removeNumbers) # 숫자 제거

corp2 <- tm_map(corp2, 
                removePunctuation)  # 구두점 제거

tdm2 <- TermDocumentMatrix(corp2)

m2 <- as.matrix(tdm2)
m2

class(m2)

colnames(m2) <- c(1:4) # 컬럼 이름을 1,2,3,4 로 바꿈.
m2

freq1 <- sort(rowSums(m2), decreasing = T)
head(freq1, 20)

freq2 <- sort(colSums(m2), decreasing = T)
head(freq2, 20) # 컬럼에서 쓰인 단어들의 합

findFreqTerms(tdm2, 2)

palete <- brewer.pal(7, "Set3")
wordcloud(names(freq1), 
          freq = freq1, 
          scale = c(5,1), 
          min.freq = 1, 
          colors = palete,
          random.order = F,
          random.color = T)

legend(0.3,
       1,
       "tm Package Test #1",
       cex=1,
       fill = NA,
       border = NA,
       bg = "white",
       text.col = "red",
       text.font = 2,
       box.col = "red")

barplot(freq1,
        main = "tm package test #2",
        las=2,
        ylim=c(0,5))

