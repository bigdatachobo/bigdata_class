# 엑셀파일 연동
install.packages("readxl")
library(readxl)

# readxl::read_excel()
df = read_excel('C:/Users/sundooedu/Downloads/BIGDATA BACKUP/R/R_day_01/Data/excel_exam.xlsx')
df$math

# 컬럼명이 없는 경우 col_names = F
df2 = read_excel('C:/Users/sundooedu/Downloads/BIGDATA BACKUP/R/R_day_01/Data/excel_exam_novar.xlsx'
                 ,col_names = F)
df$science

# sheet가 있는 경우.
df2 = read_excel('C:/Users/sundooedu/Downloads/BIGDATA BACKUP/R/R_day_01/Data/excel_exam_novar.xlsx'
                 ,col_names = F, sheet=1)
df3=read.csv('C:/Users/sundooedu/Downloads/BIGDATA BACKUP/R/R_day_01/Data/csv_exam.csv')
write.csv(df3,'C:/Users/sundooedu/Downloads/BIGDATA BACKUP/R/R_day_01/Data/csv_exam2.csv')
# 행 인덱스명 제외 저장
write.csv(df3,'C:/Users/sundooedu/Downloads/BIGDATA BACKUP/R/R_day_01/Data/csv_exam2.csv'
          ,row.names = FALSE)
# 컬럼명이 없는 경우 header = F
read.csv('C:/Users/sundooedu/Downloads/BIGDATA BACKUP/R/R_day_01/Data/csv_exam2.csv',header = FALSE)



