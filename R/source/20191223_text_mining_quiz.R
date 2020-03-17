# 2. R - wordcloud 데이터 분석(data/jeju.txt)

# 2-1. 최다 빈도 단어를 막대그래프로 나타내시고

# 2-2. wordcloud로 표현해 보세요.

install.packages("stringr") 
install.packages("rJava") 
install.packages("memoise") 
install.packages("KoNLP") 
install.packages("dplyr")

library(rJava)
library(dplyr) 
library(KoNLP) 
library(vctrs)
library(stringr) 

Sys.setenv(JAVA_HOME="C:/Program Files/Java/jre1.8.0_231/") 

data1<- readLines("../data/jeju.txt")
data1

useNIADic()

data1 <- str_replace_all(data1, "\\W", " ") 
data1 <- str_replace_all(data1, "\\d+", " ")
data1 <- gsub("길"," ",data1)
data1 <- gsub("어디"," ",data1)
data1 <- gsub("지"," ",data1)
data1 <- gsub("날"," ",data1)
data1 <- gsub("일차"," ",data1)
data1 <- gsub("점심"," ",data1)
data1 <- gsub("저녁"," ",data1)
data1 <- gsub("아침"," ",data1)
data1 <- gsub("출발"," ",data1)
data1 <- gsub("제주"," ",data1)
data1 <- gsub("도"," ",data1)
data1 <- gsub("제주도"," ",data1)
data1 <- gsub("날짜"," ",data1)
data1 <- gsub("요일"," ",data1)
data1 <- gsub("첫째"," ",data1)
data1 <- gsub("둘째"," ",data1)
data1 <- gsub("마지막"," ",data1)
data1 <- gsub("처음"," ",data1)
data1 <- gsub("여름"," ",data1)
data1 <- gsub("성수기"," ",data1)
data1 <- gsub("까지"," ",data1)
data1 <- gsub("도착"," ",data1)
data1 <- gsub("오전"," ",data1)
data1 <- gsub("오후"," ",data1)
data1 <- gsub("일"," ",data1)
data1 <- gsub("월"," ",data1)
data1 <- gsub("숙소"," ",data1)
data1 <- gsub("마을"," ",data1)
data1 <- gsub("차"," ",data1)
data1 <- gsub("세째"," ",data1)
data1 <- gsub("여행"," ",data1)

nouns <- extractNoun(data1)

wordcount <- table(unlist(nouns)) 

df_word <- as.data.frame(wordcount, stringsAsFactors = F) 
df_word <- rename(df_word, 
                  word = Var1, 
                  freq = Freq) 

# 두 글자 이상 단어 추출
df_word <- filter(df_word, nchar(word) >= 2) 

top_20 <- df_word %>%   
  arrange(desc(freq)) %>%   
  head(20) 

install.packages("wordcloud") 

library(RColorBrewer) 
library(wordcloud) 

pal <- brewer.pal(8,"Dark2")

set.seed(1234)                   # 난수 고정
wordcloud(words = df_word$word,  # 단어
          freq = df_word$freq,   # 빈도
          min.freq = 2,          # 최소 단어 빈도
          max.words = 200,       # 표현 단어 수
          random.order = F,      # 고빈도 단어 중앙 배치
          rot.per = 0.2,          # 회전 단어 비율
          scale = c(4, 0.2),     # 단어 크기 범위
          colors = pal) 

legend(0.3,
       1,
       "제주도 여행 최빈 단어",
       cex=0.8,
       fill=NA,
       border=NA,
       bg="white",
       text.col="red",
       text.font=2,
       box.col="red")

install.packages("ggplot2")
library(ggplot2)

order <- arrange(top_20, freq)$word 
ggplot(data = top_20, aes(x = word, y = freq)) +   
      ylim(0, 45) +   
      geom_col() +   
      coord_flip() +   
      scale_x_discrete(limit = order) + 
      geom_text(aes(label = freq), hjust = -0.3)


