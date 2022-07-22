library(dplyr)
library(tidyverse)
source("func.R")
library(readxl)


pathDB="../database/newRawjson/PST.xlsx"
df=read_excel(pathDB)
cond=read_excel("filesConditions.xlsx")
CD=read_excel("ClinicalData.xlsx")
df<-df %>% mutate(SUBJ=substr(fichier,0,4),TRIAL=substring(fichier,6)) #sep SUBJ to TRIAL
df<-df %>% mutate(VIB=cond %>% pull(VIB), 
                  COND=cond %>% pull(COND))

checkLevels(df,"COND")
checkLevels(df,"VIB")

df.sum<-df %>% group_by(SUBJ,COND,VIB) %>% summarize(
  `left step length`=mean(`left step length`, na.rm=TRUE),
  `right step length`=mean(`right step length`, na.rm=TRUE),
  `left step wide`=mean(`left step wide`, na.rm=TRUE),
  `right step wide`=mean(`right step wide`, na.rm=TRUE),
  `left simple support time`=mean(`left simple support time`, na.rm=TRUE),
  `right simple support time`=mean(`right simple support time`, na.rm=TRUE),
  `left double support time`=mean(`left double support time`, na.rm=TRUE),
  `right double support time`=mean(`right double support time`, na.rm=TRUE)
)
df.sum<-df.sum %>% mutate(HEMILAT=CD$HEMIPLEGIA[SUBJ==CD$SUBJ])


SI<-df.sum %>% select(SUBJ,COND,VIB)
SI["STEP LENGTH"]<-RobinsonIndex(df.sum,
                              l_name = "left step length",
                              r_name = "right step length")
SI["STEP WIDTH"]<-RobinsonIndex(df.sum,
                               l_name = "left step wide",
                               r_name = "right step wide")

SI["SST"]<-RobinsonIndex(df.sum,
                                l_name = "left simple support time",
                                r_name = "right simple support time")
SI["DST"]<-RobinsonIndex(df.sum,
                                 l_name = "left double support time",
                                 r_name = "right double support time")
SI


SA<-df.sum %>% select(SUBJ,COND,VIB)
SA["STEP LENGTH"]<-SymmetryAngle(df.sum,
                                 l_name = "left step length",
                                 r_name = "right step length")
SA["STEP WIDTH"]<-SymmetryAngle(df.sum,
                                l_name = "left step wide",
                                r_name = "right step wide")

SA["SST"]<-SymmetryAngle(df.sum,
                         l_name = "left simple support time",
                         r_name = "right simple support time")
SA["DST"]<-SymmetryAngle(df.sum,
                         l_name = "left double support time",
                         r_name = "right double support time")
SA

