library(tidyverse)
library(kableExtra)
library(plotly)


AsymmetryIndex<- function(left = 0.5, right=0.5, side_hemiparesis='D', method='Robinson'){
  if (side_hemiparesis=='D'){
    unnafected=left
    affected=right
  }else if (side_hemiparesis=='G'){
    unnafected=right
    affected=left
  } else {
    errorCondition("side_hemiparesis argument accept only 'G' (for left) or 'D' for right")
  }
  if (method=='Robinson'){
    SI=((2*(unnafected-affected))/(unnafected+affected))*100
  } else if (method=="Symmetry Angle"){
    TAN=atan(affected/unnafected)*180/pi
    SI=((45-TAN)/90)*100
  }else{
    errorCondition("Method argument accept only 'Robinon' or 'Symmetry Angle'")
  }
  return(SI)
}

RobinsonIndex<-function(df,l_name="longueur pas gauche (cm)",r_name="longueur pas droite (cm)"){
  return(df %>% mutate(l=!!as.name(l_name), r=!!as.name(r_name)) %>% rowwise() %>% 
           mutate(SI=AsymmetryIndex(l,r,HEMILAT)) %>% 
           mutate(SI=round(SI,digits=1)) %>% pull(SI))
}

SymmetryAngle<-function(df,l_name="longueur pas gauche (cm)",r_name="longueur pas droite (cm)"){
  return(df %>% mutate(l=!!as.name(l_name), r=!!as.name(r_name)) %>% rowwise() %>% 
           mutate(SI=AsymmetryIndex(l,r,HEMILAT, method = "Symmetry Angle")) %>% 
           mutate(SI=round(SI,digits=1)) %>% pull(SI))
}


checkConditions<- function(patient="BB20", cdt="avant",sv="BBMV", data=df){
  if (cdt=="avant"){
    n<-df %>% filter(id_patient==patient, condition==cdt) %>% count() %>% pull(n)
  }else{
    n<-df %>% filter(id_patient==patient, condition==cdt, site_vibration==sv) %>% count() %>% pull(n)
  }
  return(n)
}

checkLevels<-function(df, variable, n_desired=NA){
  print(levels(factor(df %>% pull(variable))))
  print(paste(
    "The variable : ",
    variable,
    " have ",
    length(levels(factor(df %>% pull(variable)))),
    " levels.",sep=""
  ))
  if (!is.na(n_desired)){
    if (length(levels(factor(df %>% pull(variable))))!=n_desired){
      warning(paste(
        "Number of levels is ",
        length(levels(factor(df %>% pull(variable)))),
        " but it should be ",
        n_desired,
        ".",sep=""
      ))
    }
  }
}

plotHist<-function(df,variable){
  temp_df<-df %>% select(SUBJ, COND,VIB, variable)
  temp_df<- temp_df %>% mutate(x=ifelse(COND=="avant",1,
                                        ifelse(COND=="pendant" & VIB=="NMV",3,
                                               ifelse(COND=="deuxminutes" & VIB=="NMV",4,
                                                      ifelse(COND=="dixminutes" & VIB=="NMV",5,
                                                             ifelse(COND=="pendant" & VIB=="GMV",7,
                                                                    ifelse(COND=="deuxminutes" & VIB=="GMV",8,
                                                                           ifelse(COND=="dixminutes" & VIB=="GMV",9,
                                                                                  ifelse(COND=="pendant" & VIB=="BBMV",11,
                                                                                         ifelse(COND=="deuxminutes" & VIB=="BBMV",12,
                                                                                                ifelse(COND=="dixminutes" & VIB=="BBMV",13,
                                                                                                       NA))))))))))) %>% 
    mutate(y=!!as.name(variable))
  temp_df<-temp_df %>% arrange(x)
  fig<-plot_ly( x = jitter(temp_df$x), y = temp_df$y, color=temp_df$SUBJ, mode = 'lines+markers')
  fig <- fig %>%
    layout(
      title = variable,
      xaxis = list(
        ticktext = list("Avant", "NMV", "NMV2", "NMV10",
                        "GMV", "GMV2","GMV10",
                        "BBMV","BBMV2","BBMV10"), 
        tickvals = list(1, 3,4, 5, 7,8, 9, 11,12,13),
        tickmode = "array"
      ))
  return(fig)
}