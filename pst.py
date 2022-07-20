# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 10:50:37 2022

@author: Mathis
"""
from math import *
import pandas as pd
import numpy as np
import os

import pyCGM2
from pyCGM2.Tools import btkTools
import csv
from ezc3d import c3d
import pyomeca
from pyomeca import Markers

# filename="database/newRawVF/06MJ/Take 2014-09-29 02_57_20 PM.4.c3d"

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

# df=getEvents(filename).sort_values(by = ['time'])

# print(df)
# print(df.iloc[1,2])

"""Markers List"""

# channels=['MJ06:RTOE','MJ06:RHEE','MJ06:LTOE','MJ06:LHEE','MJ06:RFWT','MJ06:RBWT','MJ06:LFWT','MJ06:LBWT']            

# m = Markers.from_c3d(filename,channels) 

# print(m)
# Xprogression=m[0]
# Yprogression=m[1]
# Zprogression=m[2]
# A=m.time
# Y=Yprogression[dict(channel=1, time=0)]
# print(Yprogression)
# print(Y.to_numpy())
# print(m[0][4].to_numpy())

"""Test"""


        
# def Test(filename):
#         df=getEvents(filename).sort_values(by = ['time'])
    
#         n=df.shape[0]
#         for k in range(n-1):
#             if df.iloc[k,1]=='Right'and df.iloc[k,0]=='Foot Strike':
#                 print("enter in if")
#                 try:
#                     df.iloc[k+1,1]=='Right'and df.iloc[k+1,0]=='Foot Off'
#                 except: 
#                     print(f'Caught this error: Left Foot Off is not following Right Foot Strike in {filename}' )
#                     pass
#             if df.iloc[k,1]=='Left'and df.iloc[k,0]=='Foot Off':
#                 try:
#                     df.iloc[k+1,1]=='Left'and df.iloc[k+1,0]=='Foot Strike'
#                 except:
#                     print(f'Caught this error: Left Foot Strike is not following Left Foot Off in {filename}' )
#                     pass  
#             if df.iloc[k,1]=='Left'and df.iloc[k,0]=='Foot Strike':
#                 try:
#                     df.iloc[k+1,1]=='Right'and df.iloc[k+1,0]=='Foot Off'
#                 except:
#                     print(f'Caught this error: Right Foot off is not following Left Foot Strike in {filename}' )
#                     pass
               
#             if df.iloc[k,1]=='Right'and df.iloc[k,0]=='Foot Off':
#                 try:
#                     df.iloc[k+1,1]=='Right'and df.iloc[k+1,0]=='Foot Strike'
#                 except Exception as error:
#                     print(f'Caught this error: Right Foot Strike is not following Right Foot Off in {filename}' )
#                     pass  
#         print(f"{filename} done")
    
# df=getEvents(filename).sort_values(by = ['time'])

def Test(df,filename):
        
    
        n=df.shape[0]
        for k in range(n-1):
            if df.iloc[k,1]=='Right'and df.iloc[k,0]=='Foot Strike':
                if df.iloc[k+1,1]!='Left'or df.iloc[k+1,0]!='Foot Off':
                    print(f'Caught this error: Left Foot Off is not following Right Foot Strike in {filename}' )
                    
            if df.iloc[k,1]=='Left'and df.iloc[k,0]=='Foot Off':
                if df.iloc[k+1,1]!='Left'or df.iloc[k+1,0]!='Foot Strike':
                    print(f'Caught this error: Left Foot Strike is not following Left Foot Off in {filename}' )
                     
            if df.iloc[k,1]=='Left'and df.iloc[k,0]=='Foot Strike':
                if df.iloc[k+1,1]!='Right'or df.iloc[k+1,0]!='Foot Off':
                    print(f'Caught this error: Right Foot off is not following Left Foot Strike in {filename}' )
                    
               
            if df.iloc[k,1]=='Right'and df.iloc[k,0]=='Foot Off':
                if df.iloc[k+1,1]!='Right'or df.iloc[k+1,0]!='Foot Strike':
                    print(f'Caught this error: Right Foot Strike is not following Right Foot Off in {filename}' )
                      
        print(f"{filename} done")    


# Folders = os.listdir("database/newRawVF")
# for folder in Folders:                 
#     Files=os.listdir(f"database/newRawVF/{folder}")
#     for filename in Files: 
#         Test(filename, folder)    
    
    
    
    
    
    
            
# df=getEvents(filename).sort_values(by = ['time'])    
# channels=['MJ06:RTOE','MJ06:RHEE','MJ06:LTOE','MJ06:LHEE','MJ06:RFWT','MJ06:RBWT','MJ06:LFWT','MJ06:LBWT']
# markers=Markers.from_c3d(filename,channels)

def stepLength(df,markers):
    Yprogression=markers[1]
    
    Leftstep=[]
    Rightstep=[]
    n=df.shape[0]
    for k in range(1,n):
        if df.iloc[k,1]=='Right':
            if df.iloc[k,0]=='Foot Strike':
                
                t=df.iloc[k,3]
                yRHEE=Yprogression[dict(channel=1, time=t-Yprogression.first_frame)].to_numpy()
                yLHEE=Yprogression[dict(channel=3, time=t-Yprogression.first_frame)].to_numpy()
                steplength=abs(yRHEE-yLHEE)
                Rightstep.append(steplength)
            
        if df.iloc[k,1]=='Left':
            if df.iloc[k,0]=='Foot Strike':
                
                t=df.iloc[k,3]
                yRHEE=Yprogression[dict(channel=1, time=t-Yprogression.first_frame)].to_numpy()
                yLHEE=Yprogression[dict(channel=3, time=t-Yprogression.first_frame)].to_numpy()
                steplength=abs(yLHEE-yRHEE)
                Leftstep.append(steplength)
                
    return np.mean(Leftstep), np.mean(Rightstep)


# df=getEvents(filename).sort_values(by = ['time'])    
# channels=['MJ06:RTOE','MJ06:RHEE','MJ06:LTOE','MJ06:LHEE','MJ06:RFWT','MJ06:RBWT','MJ06:LFWT','MJ06:LBWT']
# markers=Markers.from_c3d(filename,channels)

def cycleTime(df):
    """moyenne de la durée d'un cycle de marche du fichier c3d"""
    
    
    moyCycleLeftStrike = np.mean(df.query("label=='Foot Strike' & Context=='Left'").time.to_numpy()[1:]-df.query("label=='Foot Strike' & Context=='Left'").time.to_numpy()[0:-1])
    moyCycleRightStrike = np.mean(df.query("label=='Foot Strike' & Context=='Right'").time.to_numpy()[1:]-df.query("label=='Foot Strike' & Context=='Right'").time.to_numpy()[0:-1])
    
    return moyCycleLeftStrike , moyCycleRightStrike
        


# df=getEvents(filename).sort_values(by = ['time'])    
        
def oscillationTime(df):
    
    LFS = df.query("label=='Foot Strike' & Context=='Left'")
    nLFS=LFS.shape[0]
    LFO = df.query("label=='Foot Off' & Context=='Left'")
    nLFO=LFO.shape[0]
    nL=min(nLFS,nLFO)
    
    RFS = df.query("label=='Foot Strike' & Context=='Right'")
    nRFS=RFS.shape[0]
    RFO = df.query("label=='Foot Off' & Context=='Right'")
    nRFO=RFO.shape[0]
    nR=min(nRFS,nRFO)
    
    
    if df.iloc[0,1]=='Left':
        if df.iloc[0,0]=='Foot Strike':
            leftOscillationTime= np.mean(LFS.time.to_numpy()[1:nL]-LFO.time.to_numpy()[0:nL-1])
            rightOscillationTime= np.mean(RFS.time.to_numpy()[0:nR]-RFO.time.to_numpy()[0:nR])
    
        else:
            leftOscillationTime= np.mean(LFS.time.to_numpy()[0:nL]-LFO.time.to_numpy()[0:nL])
            rightOscillationTime= np.mean(RFS.time.to_numpy()[0:nR]-RFO.time.to_numpy()[0:nR])
     
    else:
        if df.iloc[0,0]=='Foot Strike':
            rightOscillationTime= np.mean(RFS.time.to_numpy()[1:nR]-RFO.time.to_numpy()[0:nR-1])
            leftOscillationTime= np.mean(LFS.time.to_numpy()[0:nL]-LFO.time.to_numpy()[0:nL])
     
        else:
            rightOscillationTime= np.mean(RFS.time.to_numpy()[0:nR]-RFO.time.to_numpy()[0:nR])
            leftOscillationTime= np.mean(LFS.time.to_numpy()[0:nL]-LFO.time.to_numpy()[0:nL])
         
     
    
    return leftOscillationTime , rightOscillationTime
    



def simpleSupportTime(df):
    rightSupportTime , leftSupportTime = oscillationTime(df)
    
    return leftSupportTime , rightSupportTime
    
   
# df=getEvents(filename).sort_values(by = ['time'])    

def doubleSupportTime(df):
    
    LFS = df.query("label=='Foot Strike' & Context=='Left'")
    nLFS=LFS.shape[0]
    LFO = df.query("label=='Foot Off' & Context=='Left'")
    nLFO=LFO.shape[0]
    
    
    RFS = df.query("label=='Foot Strike' & Context=='Right'")
    nRFS=RFS.shape[0]
    RFO = df.query("label=='Foot Off' & Context=='Right'")
    nRFO=RFO.shape[0]
    
    nL=min(nLFS,nRFO)
    nR=min(nRFS,nLFO)
    
    if df.iloc[0,0]=='Foot Strike':
        if df.iloc[0,1]=='Left':
            leftDoubleSupportTime = np.mean(RFO.time.to_numpy()[0:nL]-LFS.time.to_numpy()[0:nL])
            rightDoubleSupportTime = np.mean(LFO.time.to_numpy()[0:nR]-RFS.time.to_numpy()[0:nR])
        else:
            leftDoubleSupportTime = np.mean(RFO.time.to_numpy()[0:nL]-LFS.time.to_numpy()[0:nL])
            rightDoubleSupportTime = np.mean(LFO.time.to_numpy()[0:nR]-RFS.time.to_numpy()[0:nR])
       
    else: 
        if df.iloc[0,1]=='Left':
            leftDoubleSupportTime = np.mean(RFO.time.to_numpy()[0:nL]-LFS.time.to_numpy()[0:nL])
            rightDoubleSupportTime = np.mean(LFO.time.to_numpy()[1:nR]-RFS.time.to_numpy()[0:nR-1])
        else:
            leftDoubleSupportTime = np.mean(RFO.time.to_numpy()[1:nL]-LFS.time.to_numpy()[0:nL-1])
            rightDoubleSupportTime = np.mean(LFO.time.to_numpy()[0:nR]-RFS.time.to_numpy()[0:nR])
      



    return leftDoubleSupportTime , rightDoubleSupportTime
    

# df=getEvents(filename).sort_values(by = ['time'])    
# channels=['MJ06:RTOE','MJ06:RHEE','MJ06:LTOE','MJ06:LHEE','MJ06:RFWT','MJ06:RBWT','MJ06:LFWT','MJ06:LBWT']
# markers=Markers.from_c3d(filename,channels)

def walkAxis(markers):
   
    
    
    
    X=(markers[0][4].to_numpy()+markers[0][5].to_numpy()+markers[0][6].to_numpy()+markers[0][7].to_numpy())/4
    Y=(markers[1][4].to_numpy()+markers[1][5].to_numpy()+markers[1][6].to_numpy()+markers[1][7].to_numpy())/4
    n=min(len(X),len(Y))
    startPoint=np.array([X[1],Y[1]])
    endPoint=np.array([X[n-1],Y[n-1]])
    if Y[1]<Y[n-1]:
        walkIndex=1
    else:
        walkIndex=-1
    walkAxis=endPoint-startPoint
    normalized_walkAxis = walkAxis / np.sqrt(np.sum(walkAxis**2))
    return normalized_walkAxis, walkIndex
           
# df=getEvents(filename).sort_values(by = ['time'])    
# channels=['MJ06:RTOE','MJ06:RHEE','MJ06:LTOE','MJ06:LHEE','MJ06:RFWT','MJ06:RBWT','MJ06:LFWT','MJ06:LBWT']
# markers=Markers.from_c3d(filename,channels)       
    
def stepWide(df, markers):
    
    Xprogression=markers[0]
    LeftstepWide=[]
    RightstepWide=[]
    n=df.shape[0]
    for k in range(1,n):
        if df.iloc[k,1]=='Right':
            if df.iloc[k,0]=='Foot Strike':
                
                t=df.iloc[k,3]
                xRHEE=Xprogression[dict(channel=1, time=t-Xprogression.first_frame)].to_numpy()
                xLHEE=Xprogression[dict(channel=3, time=t-Xprogression.first_frame)].to_numpy()
                stepwide=abs(xRHEE-xLHEE)
                RightstepWide.append(stepwide)
            
        if df.iloc[k,1]=='Left':
            if df.iloc[k,0]=='Foot Strike':
                
                t=df.iloc[k,3]
                xRHEE=Xprogression[dict(channel=1, time=t-Xprogression.first_frame)].to_numpy()
                xLHEE=Xprogression[dict(channel=3, time=t-Xprogression.first_frame)].to_numpy()
                stepwide=abs(xLHEE-xRHEE)
                LeftstepWide.append(stepwide)
                
    return np.mean(LeftstepWide), np.mean(RightstepWide)
    
# df=getEvents(filename).sort_values(by = ['time'])    
# channels=['MJ06:RTOE','MJ06:RHEE','MJ06:LTOE','MJ06:LHEE','MJ06:RFWT','MJ06:RBWT','MJ06:LFWT','MJ06:LBWT']
# markers=Markers.from_c3d(filename,channels)

def stepAngle(df,markers):
    
    
    normalized_walkAxis, walkIndex = walkAxis(markers)
    LeftFootAngle=[]
    RightFootAngle=[]
    n=df.shape[0]
    for k in range(n-1):
        if df.iloc[k,0]=='Foot Off':
            if df.iloc[k,1]=='Right':
                tOff=df.iloc[k,3]
               
                xLHEE=markers[0][dict(channel=3, time=tOff-markers[0].first_frame)].to_numpy()
                xLTOE=markers[0][dict(channel=2, time=tOff-markers[0].first_frame)].to_numpy()
                yLHEE=markers[1][dict(channel=3, time=tOff-markers[1].first_frame)].to_numpy()
                yLTOE=markers[1][dict(channel=2, time=tOff-markers[1].first_frame)].to_numpy()

                leftFootVector=np.array([xLTOE-xLHEE, yLTOE-yLHEE])
                
                
                normalized_walkAxis_norm = np.sqrt(sum(normalized_walkAxis**2))     
  
                proj_of_leftFootVector_on_normalized_walkAxis = (np.dot(leftFootVector, normalized_walkAxis)/normalized_walkAxis_norm**2)*normalized_walkAxis
                
                leftFootVector_norm = np.sqrt(sum(leftFootVector**2))
                proj_of_leftFootVector_on_normalized_walkAxis_norm = np.sqrt(sum(proj_of_leftFootVector_on_normalized_walkAxis**2))
  
                angle=acos(proj_of_leftFootVector_on_normalized_walkAxis_norm/leftFootVector_norm)*(360/(2*pi))

               
                LeftFootAngle.append(abs(angle))
        
            if df.iloc[k,1]=='Left':
                tOff=df.iloc[k,3]
                
                xRHEE=markers[0][dict(channel=1, time=tOff-markers[0].first_frame)].to_numpy()
                xRTOE=markers[0][dict(channel=0, time=tOff-markers[0].first_frame)].to_numpy()
                yRHEE=markers[1][dict(channel=1, time=tOff-markers[1].first_frame)].to_numpy()
                yRTOE=markers[1][dict(channel=0, time=tOff-markers[1].first_frame)].to_numpy()
                
                rightFootVector=np.array([xRTOE-xRHEE, yRTOE-yRHEE])

               
               
                normalized_walkAxis_norm = np.sqrt(sum(normalized_walkAxis**2))     
 
                proj_of_rightFootVector_on_normalized_walkAxis = (np.dot(rightFootVector, normalized_walkAxis)/normalized_walkAxis_norm**2)*normalized_walkAxis
               
                rightFootVector_norm = np.sqrt(sum(rightFootVector**2))
                proj_of_rightFootVector_on_normalized_walkAxis_norm = np.sqrt(sum(proj_of_rightFootVector_on_normalized_walkAxis**2))
     
                angle=acos(proj_of_rightFootVector_on_normalized_walkAxis_norm/rightFootVector_norm)*(360/(2*pi))

              
               
                
               
                RightFootAngle.append(abs(angle))
                
                
    
    return np.mean(LeftFootAngle) , np.mean(RightFootAngle)



