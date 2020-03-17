x<--10
y<-5

if ( x-y >=0 ) {
  print ('TRUE ')
  print ('hello ')
  a=10
  cat('a=',a)
  cat('결과=',x-y)
} else if(x-y < 0){
  print ('FALSE ')
  print ('world ')
}

name <-c('A','B')
which(name=='B') # 인덱스 리턴
which(name=='C') # 인덱스 리턴 integer(0)
w=which(name=='C')
length(w) #0
if(length(w)==0){
  print('C 미존재')
}

n<-1:10
for (i in n) {
  print(i)
}

for (i in n) {
  if(i%%2==1){
  print(i)
  }
}

i <- 1
while(i<=10){
  if(i%%2==1){
    print(i)
  }
  i=i+1
}

n<-1:10

for (i in n) {
  if(i%%2==0){
    next() # 제어문으로 이동
  }else{
    print(i)
  }
}

i <- 1
while(i<=10){
  if(i==5) break() # 반복문 종료
  print(i)
  i=i+1
}


