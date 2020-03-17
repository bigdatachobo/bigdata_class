library(plotly)
library(ggplot2) 
 
score <- read.csv("../data/학생별과목별성적_국영수_new.csv", header=T)
score

p <- ggplot(data = score, 
            aes(x = 이름, y = 점수, col = 과목)) + 
  geom_point() 

ggplotly(p)

###########################################################################
