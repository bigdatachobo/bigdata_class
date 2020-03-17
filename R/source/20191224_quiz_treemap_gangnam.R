install.packages("readxl")
library(readxl)

coffee <- read_xlsx("../data/gangnam_coffee.xlsx")
coffee

addr <- substr( coffee$소재지전체주소, 11, 14)
head(addr)

addr_num <- gsub("\\d+","",addr) # 숫자제거
addr_trim <- gsub("\\s", "", addr_num) # 공백제거
head(addr_trim)

library(dplyr)

addr_count <- addr_trim %>%
  table()%>%
  data.frame()
head(addr_count)

install.packages("treemap")
library(treemap)

treemap(addr_count, index = ".", vSize="Freq", title="강남구 커피집")
arrange(addr_count, desc(Freq)) %>% head()

