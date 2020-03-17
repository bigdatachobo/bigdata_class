# 무명함수 -> 유명함수(함수명 two_time)
two_time <- function(){
  print('2배수')
}

two_time()

two_time <- function(x){
  return(x*2)
}

two_time(3)

summary(c(1,2,3))
#Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
#1.0     1.5     2.0     2.0     2.5     3.0 

x=c(1,2,3,4)
# 1사 분위수
x[(3*0.25)+1] + x[(3*0.25)+1]*0.75
# [1] 1.75

# 3사 분위수 
x[(3*0.75)+1] + x[(3*0.75)+1]*0.25
# [1] 3.75

# 1사분위 일반화 함수 정의
first_quard <- function(x){
  y<-sort(x)
  l<-length(y)
  return(y[((l-1)*0.25)+1] + y[((l-1)*0.25)+1]*0.75)
}

# 3사분위 일반화 함수 정의
third_quard <- function(x){
  y<-sort(x)
  l<-length(y)
  return(y[((l-1)*0.75)+1] + y[((l-1)*0.75)+1]*0.25)
}

first_quard(c(7,4,9,2))

third_quard(c(7,4,9,2))

qsummary = function(x){
  x_min = min(x)
  x_mean = mean(x)
  x_sd = sd(x)
  x_max = max(x)
  return(list(x_min = min(x),x_mean = mean(x),x_sd = sd(x),x_max = max(x)))
}

res_list = qsummary(x=c(1,2,3))

sprintf("Min %f Mean %f Sdt %f Max %f",
        res_list$x_min,res_list$x_mean,
        res_list$x_sd,res_list$x_max)
# "$" res_list의 특정 컬럼(x_min)을 불러올때도 쓰임




