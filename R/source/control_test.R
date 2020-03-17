x<--10
y<-5
if ( x-y >=0 ) {
  print ('TRUE ') # print()는 자동개행됨.
  print ('hello ')
  a=10 # 지역변수는 "="으로 하는 경우도 있음.
  cat('a=',a,'\n') # cat()은 자동개행이 아니라 끝에 넣어줌.
  cat('결과 =',x-y)
} else if(x-y < 0){
  print ('FALSE ')
  print ('world ')
}

name <- c('A','B')
which(name == 'A') # 인덱스 리턴
which(name == 'C') # 인덱스 리턴 값이 없으면 'integer(0)'리턴
w = which(name == 'C')==integer(0) # logical(0) 리턴함.
length(w) #0
if(length(w)==0){
  print('c 미존재')
}

for ( i in 1:10) {
  cat( i,' ' )
}

n <- seq(1,10,2)
for(i in n){
  print(i)
}

n <- (1:10)
for(i in n){
  if(i%%2==1){ # 홀수만 걸러서 
  print(i)    # 출력
  }
}

i <- 1
while(i <= 10){
  if(i%%2==0){
    print(i)
  }
  i = i+1
}

i <- 1
while(i <= 10){
  if(i%%2==0){
    next()
  }else{
    print(i)
  }
  i=i+1
}

n <- 1:10
for(i in n){
  if(i%%2==0){ # 홀수만 걸러서 
    next #제어문으로 이동  }
  }else{
    print(i)
  }  
}