# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:02:00 2022

@author: Mathis
"""
import btk
import os
import func as fn
import newEventDetector
import matplotlib.pyplot as plt 
import pyomeca
from pyomeca import Markers
import pyCGM2
from pyCGM2.Tools import btkTools
from pyCGM2.Lib import eventDetector
import pyCGM2; LOGGER = pyCGM2.LOGGER

# channels=['MJ06:RTOE','MJ06:RHEE','MJ06:LTOE','MJ06:LHEE']            
# data_path = "database/raw/06MJ/Take 2014-09-29 02_57_20 PM.4.c3d"
# filename="Take 2014-09-29 02_57_20 PM.4.c3d"
# markers=Markers.from_c3d(data_path)
# markers = Markers.from_c3d(data_path,channels) 
# Markers 'xr.DataArray' with 4 channels wich are 2 markers from left foot ans 2 from right


# ZRTOE=markers[2][0]  # "z axis" datas from the 4 channels : xarray.DataArray
# ZRHEE=markers[2][1]
# ZLTOE=markers[2][2]
# ZLHEE=markers[2][3]

# ListZRTOE=ZRTOE.to_numpy().tolist()  # List
# ListZRHEE=ZRHEE.to_numpy().tolist()
# ListZLTOE=ZLTOE.to_numpy().tolist()
# ListZLHEE=ZRHEE.to_numpy().tolist()

# print(markers)  #print datas from the 4 channels

#print(markers[2])  #print "z axis" datas from the 4 channels
#print(ZRTOE.min())
#print(ZRHEE.min())
#print(ZLTOE.min())
#print(ZLHEE.min())


# markers2D=markers[1:3]  # y,z plan 
#print(markers2D)

     

Folders = os.listdir("database/raw")
# print(Folders)
for folder in Folders:                   # folder is a folder in /raw. EXEMPLE: folder=MJ06
    if not os.path.exists(f"database/newRaw/{folder}"):
        
        os.makedirs(f"database/newRaw/{folder}")
        Files=os.listdir(f"database/raw/{folder}")
        # print(Files)
        for filename in Files:             # filename is a file. EXEMPLE:Take 2014-09-29 02_57_20 PM.4.c3d 
        
            # c3d to acq with btk:
            acq=btkTools.smartReader(f"database/raw/{folder}/{filename}")
            
    
            #new acq with events
            acqGait,state = newEventDetector.zeni(acq,folder,footStrikeOffset=0, footOffOffset=0)
    
        #new acq to new c3d
            if not os.path.exists(f"database/newRaw/{folder}/{filename}"):
                event_data_path= f"database/newRaw/{folder}/{filename}"
                btkTools.smartWriter(acqGait, event_data_path)
            else:
                LOGGER.logger.error(f"database/newRaw/{folder}/{filename} already exists")

    else:
        LOGGER.logger.error(f"database/newRaw/{folder} already exists")





folder="21BJ"  
Files=os.listdir("database/raw/21BJ")
for filename in Files:             
    # c3d to acq with btk:
    acq=btkTools.smartReader(f"database/raw/{folder}/{filename}")
    
    #new acq with events
    acqGait,state = newEventDetector.zeni(acq,folder,footStrikeOffset=0, footOffOffset=0)
    
    #new acq to new c3d
    if not os.path.exists(f"database/newRaw/{folder}/{filename}"):
        event_data_path= f"database/newRaw/{folder}/{filename}"
        btkTools.smartWriter(acqGait, event_data_path)
    else:
        LOGGER.logger.error(f"database/newRaw/{folder}/{filename} already exists")

else:
    LOGGER.logger.error(f"database/newRaw/{folder} already exists")











# Folders = os.listdir("database/raw")
# # print(Folders)
# for folder in Folders:                   # folder is a folder in /raw. EXEMPLE: folder=MJ06
#     if not os.path.exists(f"database/newRaw/{folder}"):
        
#         os.makedirs(f"database/newRaw/{folder}")
#         # Files=os.listdir(f"database/raw/{folder}")
#         # print(Files)
#         # for filename in Files:             # filename is a file. EXEMPLE:Take 2014-09-29 02_57_20 PM.4.c3d 
        
#             # c3d to acq with btk:
#         acq=btkTools.smartReader(f"database/raw/{folder}/{filename}")
    
#             #new acq with events
#         newEventDetector.zeni(acq,folder,footStrikeOffset=0, footOffOffset=0)
    
#         #new acq to new c3d
#         if not os.path.exists(f"database/newRaw/{folder}/{filename}"):
#             event_data_path= f"database/newRaw/{folder}/{filename}"
#             btkTools.smartWriter(acq, event_data_path)
#         else:
#             LOGGER.logger.error(f"database/newRaw/{folder}/{filename} already exists")

#     else:
#         LOGGER.logger.error(f"database/newRaw/{folder} already exists")



# folder="06MJ:RBWT"
# print(folder)
# folder=folder[2:4]+folder[0:2]+folder[4:9]
# print(folder)



























