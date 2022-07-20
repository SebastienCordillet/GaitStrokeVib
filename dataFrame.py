# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:57:07 2022

@author: Mathis
"""

import pandas as pd
import numpy as np
import os
import pst
from pyomeca import Markers

# df=pd.DataFrame(data={
#     'step length': steplength,
#     'step wide' : stepwide,
#     'step angle' : stepangle,
#     'cycle time' : cycletime,
#     'Oscillation time' : oscillationtime,
#     'simple support Time' : simplesupporttime,
#     'double support time' : simplesupporttime
    

   
channels=['MJ06:RTOE','MJ06:RHEE','MJ06:LTOE','MJ06:LHEE','MJ06:RFWT','MJ06:RBWT','MJ06:LFWT','MJ06:LBWT']



Folders = os.listdir("database/newRawVF")

for folder in Folders:
   
        if folder=='21BJ':
            markersPrefix='BJ'
        else:   
            markersPrefix=folder[2:4]+folder[0:2]
            
        channels=[f'{markersPrefix}:RTOE',f'{markersPrefix}:RHEE',f'{markersPrefix}:LTOE',f'{markersPrefix}:LHEE',f'{markersPrefix}:RFWT',f'{markersPrefix}:RBWT',f'{markersPrefix}:LFWT',f'{markersPrefix}:LBWT']
        
        LeftStepLength=[]
        RightStepLength=[]
        LeftStepWide=[]
        RightStepWide=[]
        LeftStepAngle=[]
        RightStepAngle=[]
        LeftStrikeCycleTime=[]
        RightStrikeCycleTime=[]
        LeftOscillationTime=[]
        RightOscillationTime=[]
        LeftSSTime=[]
        RightSSTime=[]
        LeftDSTime=[]
        RightDSTime=[]
      
        
        Files=os.listdir(f"database/newRawVF/{folder}")
        for file in Files:
            
            df=pst.getEvents(f"database/newRawVF/{folder}/{file}").sort_values(by = ['time'])    
            markers=Markers.from_c3d(f"database/newRawVF/{folder}/{file}",channels)
                
                
            """Step length"""
            leftStepLength , rightStepLength = pst.stepLength(df,markers)
                
            
            
            """Step wide"""
            leftStepWide , rightStepWide = pst.stepWide(df,markers)
           
            
            """Step Angle"""
            leftStepAngle , rightStepAngle = pst.stepAngle(df,markers)
         
            
            """Cycle Time"""
            leftStrikeCycleTime , rightStrikeCycleTime = pst.cycleTime(df)
           
            """Oscillation Time"""
            leftOscillationTime , rightOscillationTime = pst.oscillationTime(df)
         
            
            """Simple Support Time"""
            leftSSTime , rightSSTime = pst.simpleSupportTime(df)
          
            
            """Double Support Time"""
            leftDSTime , rightDSTime = pst.doubleSupportTime(df)
           
            
         
            df= pd.DataFrame({'left step length': leftStepLength,
                                'right step length': rightStepLength,
                                'left step wide' : leftStepWide,
                                'right step wide': rightStepWide,
                                'left step angle' : leftStepAngle,
                                'right step angle': rightStepAngle,
                                'left strike cycle time' : leftStrikeCycleTime,
                                'right strike cycle time' : rightStrikeCycleTime,
                                'left Oscillation time' : leftOscillationTime,
                                'right Oscillation time' : rightOscillationTime,
                                'left simple support time' : leftSSTime,
                                'right simple support time' : rightSSTime,
                                'left double support time' : leftDSTime,
                                'right double support time' : rightDSTime},
                             index=[f"{folder}/{file}"]
                             
                              )
            
            
            df.to_json(f"database/newRawjson/{folder}/{file}.json")
            
        
        
        
        
    
        

# id_patient = Folders
# print(id_patient)

# df = pd.DataFrame({'left step length': LeftStepLength, 'right step length': RightStepLength, 'left step wide' : LeftStepWide, 'right step wide': RightStepWide})


# df = pd.DataFrame({'left step length': LeftStepLength, 'right step length': RightStepLength, 'left step wide' : LeftStepWide, 'right step wide': RightStepWide}, index = id_patient)

# df = pd.DataFrame({'left step length': LeftStepLength,
                  #  'right step length': RightStepLength,
                  #  'left step wide' : LeftStepWide,
                  #  'right step wide': RightStepWide,
                  #  'left step angle' : LeftStepAngle,
                  #  'right step angle': RightStepAngle,
                  #  'left strike cycle time' : LeftStrikeCycleTime,
                  #  'right strike cycle time' : RightStrikeCycleTime,
                  #  'left Oscillation time' : LeftOscillationTime,
                  #  'right Oscillation time' : RightOscillationTime,
                  #  'left simple support time' : LeftSSTime,
                  #  'right simple support time' : RightSSTime,
                  #  'left double support time' : LeftDSTime,
                  #  'right double support time' : RightDSTime},
                  # index = id_patient)

# print(df)