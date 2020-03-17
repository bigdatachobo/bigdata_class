# 1. 5호선 주소 불러오기
# install.packages("readxl")
library(readxl)

subway <- read_xlsx("../data/서울_지하철_전화번호_주소_5호선.xlsx")
head(subway)

colnames(subway) = c("no","line","station","road","earth","post","phone")

# 2. 한글 주소로 lon / lat 얻기
# install.packages("ggmap")
library(ggmap)

googleAPIkey = "AIzaSyBKRq7_4cl5CG-p7rpn4jAAsayRK4qoWYc"

register_google(googleAPIkey)
gg_seoul <- get_googlemap("seoul", zoom = 10, maptype= "terrain")
ggmap(gg_seoul)

library(dplyr)
library(ggplot2)

geo_code <- enc2utf8(subway$road) %>% geocode()

geo_data <- lapply(geo_code,as.numeric)

geoPoint=geom_point(data = geo_code, aes(x=geo_code$lon, y=geo_code$lat))

# 3. subway에 lon / lat 열로 붙여넣기 
subway$lon <- geo_data$lon
subway$lat <- geo_data$lat

# 4. 아파트 실거래가 데이터 전처리
apart <- read_xlsx("../data/apartment.xlsx",skip=16)
head(apart)
# 열이름 바꾸기
colnames(apart) = c("city","bunge","bone","subno","danji","square","conyear","conday","price","floor","madeyear","road")
head(apart)
# 소수점에서 반올림
apart$square <- round(as.numeric(apart$square),0)
head(apart$square)
# 전용면적 85만 추출
aparts <- apart[apart$square== 85,]
head(aparts)
# ","제거 및 수치형으로 변환.
aparts$price <- as.numeric(gsub(",","",aparts$price))
head(aparts$price)

apart$price <- as.numeric(gsub(",","",apart$price))
head(aparts$price)

library(dplyr)
# 단지별 평균 가격 추출
aparts <- aparts %>%
  group_by(danji) %>%
  mutate(mean_value = mean(price))
head(aparts)
# 열끼리 합치기
aparts$combiaddr <- paste(aparts$city, aparts$bunge,sep=" ")
head(aparts$combiaddr)

# 위/경도 데이터 가져오기.
geo_code2 <- enc2utf8(aparts$combiaddr) %>% geocode()

geo_data2 <- lapply(geo_code2,as.numeric)

geoPoint2=geom_point(data = geo_code2, aes(x=geo_code2$lon, y=geo_code2$lat))

aparts$lon <- geo_data2$lon
aparts$lat <- geo_data2$lat

# 5. 구글 지도에 지하쳘역과 아파트 가격 표시하기

# 5-1,2)지하철역 위치 및 아파트 가격 정보 표시하기.
# install.packages("leaflet")
library(leaflet)

content_sub <- paste(sep="<br/>",
                 paste0("<b>호선: </b>",subway$line),
                 paste0("<b>역명: </b>",subway$station),
                 paste0("<b>주소: </b>",subway$road),
                 paste0("<b>전화번호: </b>",subway$phone))

content_apart <- paste(sep="<br/>",
                     paste0("<b>단지명: </b>",aparts$danji),
                     paste0("<b>주소: </b>",aparts$combiaddr),
                     paste0("<b>전용면적(㎡): </b>",aparts$square),
                     paste0("<b>거래금액(만원): </b>",aparts$price),
                     paste0("<b>층: </b>",aparts$floor),
                     paste0("<b>건축년도: </b>",aparts$madeyear))

m<- leaflet() %>%
  addTiles() %>%
  addMarkers(lng = subway$lon,
             lat = subway$lat,
             popup = content_sub,
             label = "지하철",
             clusterOptions = markerClusterOptions()) %>%
  addMarkers(lng = aparts$lon,
             lat = aparts$lat,
             popup = content_apart,
             label = "아파트",
             clusterOptions = markerClusterOptions())

m

