
library(ggplot2)
mpg<-ggplot2::mpg
library(dplyr)
#displ(배기량)이 4 이하인 자동차
mpg4 <- mpg %>% filter(displ<=4)
#hwy(고속도로 연비)
mean(mpg4$hwy) #25
#5 이상인 자동차
mpg5 <- mpg %>% filter(displ>=5)
#hwy(고속도로 연비)
mean(mpg5$hwy)#18

mpg_mf <- mpg %>% 
  filter(manufacturer %in% c("chevrolet", "ford", "honda" ) )
mean(mpg_mf$hwy)

data<- mpg %>% select(class,cty)
head(data)

mpg %>% filter(manufacturer=='audi') %>% 
  arrange(desc(hwy)) %>% 
  head(5)

mpg_copy<-mpg
mpg_copy <- mpg_copy %>% mutate(hap=cty+hwy)
mpg_copy <- mpg_copy %>% mutate(mean=hap/2)
mpg_copy %>%arrange(desc(mean)) %>% 
  head(3)

mpg_copy %>% 
  group_by(manufacturer) %>% 
  filter(class=='suv') %>% 
  arrange(desc(mean))%>% 
  head(5)

str(mpg$cty)

boxplot(mpg$cty).stats

# cty 이상측처리 NA
mpg$cty <- ifelse(mpg$cty<-9 | mpg$cty >26, NA, mpg$cty)
# 상자그림을 만들어 이상치가 사라졌는지 확인
boxplot(mpg$cty)

