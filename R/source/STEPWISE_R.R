install.packages('xlsx')
library(xlsx)
install.packages('readxl')
library(readxl)

setwd('C:/Users/sundooedu/Downloads/BIGDATA BACKUP/R/project/source')

df = read_xls('../data/clima_onion_join.xls')
df = df[,c(98:109,110)]
colnames(df)[13] = 'ten_a_onion'
colnames(df)[2] = 'jan_avg_t'
colnames(df)
lmfit = lm(ten_a_onion~., data=df)
summary(lmfit)
step(lmfit, direction='both')
model = lm(formula = ten_a_onion ~ `평균기온 2월` + `평균기온 3월` + 
     `평균기온 6월` + `평균기온 8월`, data = df)
summary(model)
par(mfrow=c(2,2))
plot(lmfit)


fit <- factanal(df[,c(37:110)], 8, rotation="varimax")
print(fit, digits=2, cutoff=.3, sort=TRUE)
# plot factor 1 by factor 2
load <- fit$loadings[,1:2]
plot(load,type="n") # set up plot
text(load,labels=names(mydata),cex=.7) # add variable names