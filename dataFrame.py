# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:57:07 2022

@author: Mathis
"""

import pandas as pd
import numpy as np
import os
import pst

# df=pd.DataFrame(data={
#     'step length': steplength,
#     'step wide' : stepwide,
#     'step angle' : stepangle,
#     'cycle time' : cycletime,
#     'Oscillation time' : oscillationtime,
#     'simple support Time' : simplesupporttime,
#     'double support time' : simplesupporttime
    




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
                
                
            """Step length"""
            leftStepLength , rightStepLength = pst.stepLength(f"database/newRawVF/{folder}/{file}",channels)
                
            # LeftStepLength.append(leftStepLength)
            # RightStepLength.append(rightStepLength)
            
            """Step wide"""
            leftStepWide , rightStepWide = pst.stepWide(f"database/newRawVF/{folder}/{file}",channels)
            # LeftStepWide.append(leftStepWide)
            # RightStepWide.append(rightStepWide)
            
            """Step Angle"""
            leftStepAngle , rightStepAngle = pst.stepAngle(f"database/newRawVF/{folder}/{file}",channels)
            # LeftStepAngle.append(leftStepAngle)
            # RightStepAngle.append(rightStepAngle)
            
            """Cycle Time"""
            leftStrikeCycleTime , rightStrikeCycleTime = pst.cycleTime(f"database/newRawVF/{folder}/{file}")
            # LeftStrikeCycleTime.append(leftStrikeCycleTime)
            # RightStrikeCycleTime.append(rightStrikeCycleTime)
            
            """Oscillation Time"""
            leftOscillationTime , rightOscillationTime = pst.oscillationTime(f"database/newRawVF/{folder}/{file}")
            # LeftStrikeCycleTime.append(leftOscillationTime)
            # RightStrikeCycleTime.append(rightOscillationTime)
            
            """Simple Support Time"""
            leftSSTime , rightSSTime = pst.simpleSupportTime(f"database/newRawVF/{folder}/{file}")
            # LeftSSTime.append(leftSSTime)
            # RightSSTime.append(rightSSTime)
            
            """Double Support Time"""
            leftDSTime , rightDSTime = pst.doubleSupportTime(f"database/newRawVF/{folder}/{file}")
            # LeftDSTime.append(leftDSTime)
            # RightDSTime.append(rightDSTime)
            
         
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
            
            
            df.to_json(f"database/newRawjson/{folder}/json/{file}.json")
            
        
        
        
        
    
        

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