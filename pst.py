# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 10:50:37 2022

@author: Mathis
"""
import pandas as pd
import numpy as np
import os
import btk
import pyCGM2
from pyCGM2.Tools import btkTools
import csv
from ezc3d import c3d
import pyomeca
from pyomeca import Markers

filename="database/newRawVF/06MJ/Take 2014-09-29 02_57_20 PM.4.c3d"

"""Events list"""

# c=c3d(filename)
# c['parameters']['EVENT']
# ListStrikeOff=c['parameters']['EVENT']['LABELS']['value']
# ListLeftRight=c['parameters']['EVENT']['CONTEXTS']['value']
# n=len(ListStrikeOff)
# Labels=[ListLeftRight[i]+' '+ListStrikeOff[i] for i in range(n)]
# Time=c['parameters']['EVENT']['TIMES']['value'][1]
# # print(Time)
# Events=[[Labels[i],Time[i]] for i in range(n)]
# print(Events)

def getEvents(filec3d, part='EVENT'):
    c=c3d(filec3d)
    labels=c['parameters'][part]['LABELS']['value']
    time=c['parameters'][part]['TIMES']['value'][1,:]

    
    try:
        fr_marker=c['parameters']['POINT']['RATE']['value'].astype(int)
    except Exception:
        pass
    
    try:
        fr_analog=c['parameters']['ANALOG']['RATE']['value'].astype(int)
    except Exception:
        pass
    
    try:
        context=c['parameters'][part]['CONTEXTS']['value']
    except Exception:
        pass
    
    events=pd.DataFrame(data={
        'label':labels,
        'time': time
        })
    

    if 'fr_marker' in locals():
        events['frame_marker']= np.array(time*fr_marker, dtype=int)
        
    if 'fr_analog' in locals():
        events['frame_analog']= np.array(time*fr_analog, dtype=int)
        
    if 'context' in locals():
        events.insert(1, 'Context', context)
        
    return(events)

df=getEvents(filename).sort_values(by = ['time'])

print(df)
# print(df.iloc[1,2])

"""Markers List"""

channels=['MJ06:RTOE','MJ06:RHEE','MJ06:LTOE','MJ06:LHEE']            

# m = Markers.from_c3d(filename,channels) 

# # print(m)
# Xprogression=m[0]
# Yprogression=m[1]
# Zprogression=m[2]
# Y=Yprogression[dict(channel=1, time=0)]
# print(Yprogression)
# # print(Y.to_numpy())


"""Test"""


        
# def Test(filename, folder):
#         df=getEvents(f"database/newRawVF/{folder}/{filename}").sort_values(by = ['time'])
    
#         n=df.shape[0]
#         for k in range(n-1):
#             if df.iloc[k,1]=='Right'and df.iloc[k,0]=='Foot Strike':
#                 try:
#                     df.iloc[k,1]=='Left'and df.iloc[k+1,0]=='Foot Off'
#                 except Exception as error:
#                     print(f'Caught this error: Left Foot Off is not following Right Foot Strike in {folder}/{filename}' )
#                     pass
#             if df.iloc[k,1]=='Left'and df.iloc[k,0]=='Foot Off':
#                 try:
#                     df.iloc[k,1]=='Left'and df.iloc[k+1,0]=='Foot Strike'
#                 except Exception as error:
#                     print(f'Caught this error: Left Foot Strike is not following Left Foot Off in {folder}/{filename}' )
#                     pass  
#             if df.iloc[k,1]=='Left'and df.iloc[k,0]=='Foot Strike':
#                 try:
#                     df.iloc[k,1]=='Right'and df.iloc[k+1,0]=='Foot Off'
#                 except Exception as error:
#                     print(f'Caught this error: Right Foot off is not following Left Foot Strike in {folder}/{filename}' )
#                     pass
               
#             if df.iloc[k,1]=='Right'and df.iloc[k,0]=='Foot Off':
#                 try:
#                     df.iloc[k,1]=='Right'and df.iloc[k+1,0]=='Foot Strike'
#                 except Exception as error:
#                     print(f'Caught this error: Right Foot Strike is not following Right Foot Off in {folder}/{filename}' )
#                     pass  
#         return f"{folder}/{filename} OK"
    
    
# Folders = os.listdir("database/newRawVF")
# for folder in Folders:                 
#     Files=os.listdir(f"database/newRawVF/{folder}")
#     for filename in Files: 
#         Test(filename, folder)    
    
    
    
    
    
    
            
    

def stepLenght(filename):
    Yprogression=Markers.from_c3d(filename,channels)[0]
    df=getEvents(filename).sort_values(by = ['time'])
    Leftstep=[]
    Rightstep=[]
    n=df.shape[0]
    for k in range(1,n):
        if df.iloc[k,1]=='Right':
            if df.iloc[k,0]=='Foot Strike':
                
                t=df.iloc[k,2]
                yRHEE=Yprogression[dict(channel=1, time=t-415)].to_numpy()
                yLHEE=Yprogression[dict(channel=3, time=t-415)].to_numpy()
                steplenght=yRHEE-yLHEE
                Rightstep.append(steplenght)
            
        if df.iloc[k,1]=='Left':
            if df.iloc[k,0]=='Foot Strike':
                
                t=df.iloc[k,2]
                yRHEE=Yprogression[dict(channel=1, time=t-415)].to_numpy()
                yLHEE=Yprogression[dict(channel=3, time=t-415)].to_numpy()
                steplenght=yLHEE-yRHEE
                Leftstep.append(steplenght)
                
    return Leftstep, Rightstep




def cycleTime(filename):
    """moyenne de la durée d'un cycle de marche du fichier c3d"""
    df=getEvents(filename).sort_values(by = ['time'])
    
    moyCycleLeftStrike = np.mean(df.query("label=='Foot Strike' & Context=='Left'").time.to_numpy()[1:]-df.query("label=='Foot Strike' & Context=='Left'").time.to_numpy()[0:-1])
    moyCycleRightStrike = np.mean(df.query("label=='Foot Strike' & Context=='Right'").time.to_numpy()[1:]-df.query("label=='Foot Strike' & Context=='Right'").time.to_numpy()[0:-1])
    
    return moyCycleLeftStrike , moyCycleRightStrike
        
   
    
        
    
def oscillationTime(filename):
    df = getEvents(filename).sort_values(by = ['time'])
    LFS = df.query("label=='Foot Strike' & Context=='Left'")
    nLFS=LFS.shape[0]
    LFO = df.query("label=='Foot Off' & Context=='Left'")
    nLFO=LFO.shape[0]
    nL=min(nLFS,nLFO)
    
    RFS = df.query("label=='Foot Strike' & Context=='Right'")
    nRFS=RFS.shape[0]
    RFO = df.query("label=='Foot Off' & Context=='Right")
    nRFO=RFO.shape[0]
    nR=min(nRFS,nRFO)
    
    
    if df.iloc[0,1]=='Left':
        if df.iloc[0,0]=='Foot Strike':
            leftOscillationTime= np.mean(LFS.time.to_numpy()[1:nL+1]-LFO.time.to_numpy()[0:nL])
    
        else:
            leftOscillationTime= np.mean(LFS.time.to_numpy()[0:nL+1]-LFO.time.to_numpy()[0:nL+1])
     
    else:
        if df.iloc[0,0]=='Foot Strike':
            rightOscillationTime= np.mean(RFS.time.to_numpy()[1:nR+1]-RFO.time.to_numpy()[0:nR])
     
        else:
            rightOscillationTime= np.mean(RFS.time.to_numpy()[0:nR+1]-RFO.time.to_numpy()[0:nR+1])
         
     
    
    return leftOscillationTime , rightOscillationTime
    



def supportTime(filename):






