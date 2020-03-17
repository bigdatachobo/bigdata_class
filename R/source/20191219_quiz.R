아래의 문제를 해결해 보세요.

excel_exam.xlsx에서 20명의 학생의 데이터를 불러와서

1. math, english, science  3과목의 합계를 출력하세요.(s_total)

2. math, english, science  3과목의 평균을 출력하세요.(s_mean)

3. 평균이 60점 이상이면 "pass" 그렇지 않으면 "fail"를 부여하는   파생변수test1를 생성하세요.

4. 3의 결과의 빈도수와 그래프로 나타내세요.

5. 평균이 80점 이상이면 "A", 70이상이면 "B", 그외는 "C"를   부여하는 파생변수
test2를 생성하세요.

6. 5의 결과를 상위 10개만 출력하세요.

7. 5의 결과를 하위 7개만 출력하세요.

8. 5의 결과를 빈도수와 그래프로 나타내세요.
##################################################################################################
install.packages('ggplot2')
install.packages("dplyr")
install.packages('readxl')

library(readxl)
library(dplyr)
library(ggplot2)

exam <- read_excel('../data/excel_exam.xlsx')
df <- as.data.frame(exam)
df <- df %>%
    mutate(sub_sum=math+science+english,
           sub_mean=sub_sum/3,
           test1=ifelse(sub_mean >= 60, "pass", "fail"),
           test2=ifelse(sub_mean >= 80, "A", ifelse(sub_mean>=70,"B","C")))

df
qplot(df$test1)
head(df, 10)
head(df, 7)
qplot(df$test2)           
