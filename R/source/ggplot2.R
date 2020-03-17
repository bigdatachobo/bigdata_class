library(ggplot2)
ggplot(data = mpg, aes(x=displ,y=hwy))
# 1. 산점도
# 배기량이 클수룩 연비 낮은분포 "경향"이 관찰됨.
ggplot(data = mpg, aes(x=displ,y=hwy)) + geom_point()#(그래프 유형)

# 축범위 제약
ggplot(data = mpg, aes(x=displ,y=hwy)) + geom_point() + xlim(2,5)

mpg2 <- mpg %>% 
  group_by(drv) %>% 
  summarise(hwy_mean = mean(hwy))

# 2. 막대그래프 (x범주분류값, y연속 크기값)

# 구동 집단의 연비 "크기 차이" 유의
ggplot(data = mpg2, aes(x=drv,y=hwy_mean)) + geom_col()#(그래프 유형)

# 정렬
ggplot(data = mpg2, aes(x=reorder(drv,hwy_mean),y=hwy_mean)) + geom_col()#(그래프 유형)

# 빈도 막대그래프 
# 후륜구동차 연비가 가장 적다.
ggplot(data = mpg, aes(x=drv)) + geom_bar()#(그래프 유형)

# 3.선그래프 ( x-시간값, y-시간에 따라 달라지는 크기값.>>> 추이)
# 추이(progress, development)
economics2 <- ggplot2::economics # 새로운 테이블 불러오기.
ggplot(data = economics2, aes(x=date,y=unemploy)) + geom_line()

# 4. 상자그래프
# 통계적 사분위 분포
# r 이 대부분의 자동차 IQR에 잘 분포
ggplot(data = mpg, aes(x=drv, y=hwy)) + geom_boxplot()









