#엑셀파일연동 
install.packages("readxl")
library(readxl)

df=read_excel('Data/excel_exam.xlsx')
df$math
#컬럼명이 없는 경우 col_names = F
df2=read_excel('Data/excel_exam_novar.xlsx'
               ,col_names = F,sheet = 1)
#한글
df3=read.csv('Data/csv_exam.csv',encoding = 'UTF-8')
write.csv(df3,'Data/csv_exam2.csv')
#행인덱스명 제외 저장
write.csv(df3,'Data/csv_exam2.csv',row.names =FALSE)
rm(df3)
#컬럼명이 없는 경우 header =  F
df3<-read.csv('Data/csv_exam2.csv',header = FALSE)

