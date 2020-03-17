install.packages("devtools")
devtools::install_github("dkahle/ggmap")
library(devtools)
library(ggmap)


googleAPIkey = "AIzaSyBKRq7_4cl5CG-p7rpn4jAAsayRK4qoWYc"

# 서울의 위치 정보를 가져온 후 gg_seoul 변수에 할당
register_google(googleAPIkey)
gg_seoul <- get_googlemap("seoul", zoom = 6, maptype= "terrain")
ggmap(gg_seoul)
# gg_seoul의 위치 값에 따른 구글 지도 호출 

# 위경도 가져와서 산점도 그리기
# geocode() 함수 활용

# 구글 지도 위에 산점도 그리기
library(dplyr)
library(ggplot2)

# 한글 검색을 위해 utf-8로 변환한 후 위도와 경도 데이터를 geo_code 변수에 할당
geo_code <- enc2utf8("대전역") %>% geocode()

# 리스트를 숫자로 변환하여 geo_data 변수에 할당
geo_data <- as.numeric(geo_code)

# geo_code에 있는 경도(lon)와 위도(lat) 값으로 산점도 그리기  
geoPoint=geom_point(data = geo_code, aes(x=geo_code$lon, y=geo_code$lat))

# 대전역의 위치정보를 가져온 후 구글 지도 호출
get_googlemap(center = geo_data, maptype = "roadmap", zoom=13) %>%
  ggmap() +
  geoPoint

library(stringr)

loc <- read.csv("../data/서울_강동구_공영주차장_위경도.csv", header=T)          
loc

kd <- get_map("Amsa-dong", zoom=13, maptype = "roadmap")
kor.map <- ggmap(kd) + geom_point(data=loc, aes(x=LON, y=LAT),
                                  size=3, alpha=0.7, color="red")
kor.map + geom_text(data = loc, aes(x=LON, y=LAT+0.001, label=주차장명), size=3)
ggsave("../img/kd.png", dpi=500)

###################################################################################
loc2 <- str_sub(loc$주차장명, start=-2, end=-2)
loc2

colors <- c()

for (i in 1:length(loc2)){
  if (loc2[i] == '구'){
    colors <- c(colors,"red")}
  else{
    colors <- c(colors,"blue")}
}

kd <- get_map("Amsa-dong", 
              zoom=13, 
              maptype = "roadmap")

kor.map <- ggmap(kd) + 
           geom_point(data=loc, 
                      aes(x=LON, y=LAT),
                      size=3, 
                      alpha=0.7,
                      color=colors)

kor.map + 
geom_text(data = loc, 
          aes(x = LON, 
              y = LAT+0.001,
              label=주차장명),
          size=3)
# 장애인 도서관 위치 지도에 표시하기
loc <- read.csv("../data/지역별장애인도서관정보.csv",header=T)
loc

kor <- get_map("seoul", zoom=11, maptype="roadmap")
kor.map <- ggmap(kor)+
           geom_point(data = loc, aes(x = LON,
                                      y = LAT),
                      size=4,
                      alpha=0.7)
kor.map +
geom_text(data = loc, aes(x = LON,
                          y = LAT + 0.01,
                          label = 자치구명),
          size = 3)

ggsave("../img/lib.png", dpi = 500)

# 지하철 2호선 역위치를 지도에 표시하기
loc <- read.csv("../data/서울지하철2호선위경도정보.csv", header=T)
loc

kor <- get_map("seoul", zoom=11, maptype="roadmap")
kor.map <- ggmap(kor)+
  geom_point(data = loc, aes(x = LON,
                             y = LAT),
             size= 2,
             alpha=0.7)
kor.map +
  geom_text(data = loc, aes(x = LON,
                            y = LAT + 0.01,
                            label = 역명),
            size = 3)

ggsave("../img/tube.png", dpi = 500)

# 지하철 2,3호선 역위치 지도 위에 표시하기
loc1<-read.csv("../data/서울지하철2호선위경도정보.csv", header=T)
loc1
loc2 <- read.csv("../data/서울지하철3호선역위경도정보.csv", header=T)
loc2



kor <- get_map("seoul", zoom=10, maptype="roadmap")
kor.map <- ggmap(kor)+
  geom_point(data = loc1, 
             aes(x = LON,
                 y = LAT,
                 color='green'),
             size= 2,
             alpha=0.7)+
  geom_point(data = loc2, 
             aes(x = LON,
                 y = LAT,
                 color="coral"),
             size= 2,
             alpha=0.7)
kor.map +
  geom_text(data = loc1, 
            aes(x = LON,
                y = LAT + 0.01,
                label = 역명),
            size = 1)+
  geom_text(data = loc2, 
            aes(x = LON,
                y = LAT + 0.01,
                label = 역명),
            size = 1)

ggsave("../img/tube_combi_2_3.png", dpi = 500)

######################################################################
# leaflet
install.packages("leaflet")
library(leaflet)

m<- leaflet() %>%
  addTiles() %>%
  addMarkers(lng = 174.768,
             lat = -36.852,
             popup = "The birthplace of R")
m
######################################################################
# 강원도 으뜸 음식점 지도위에 표시
loc <- read.csv("../data/강원도으뜸음식점.csv",header=T)
loc

content <- paste(sep="<br/>",
                 paste0("<b>업소명: </b>",loc$업소명),
                 paste0("<b>주소: </b>",loc$소재지도로명주소),
                 paste0("<b>전화번호: </b>",loc$전화번호),
                 paste0("<b>주요메뉴: </b>",loc$주요메뉴))

m<- leaflet() %>%
  addTiles() %>%
  addMarkers(lat = loc$위도,
             lng = loc$경도,
             popup = content,
             clusterOptions = markerClusterOptions())
m


