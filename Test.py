# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 14:03:00 2022

@author: Mathis
"""

import pst 
import os


"""Test"""

# filename="database/newRawVF/06MJ/Take 2014-09-29 02_57_20 PM.4.c3d"
# folder="23RN"

                  
# Files=os.listdir(f"database/raw/{folder}")
# for file in Files:
#     pst.Test(f"database/newRawVF/{folder}/{file}")

"""StepLength"""

# filename="database/newRawVF/06MJ/Take 2014-09-29 02_57_20 PM.4.c3d"
# channels=['MJ06:RTOE','MJ06:RHEE','MJ06:LTOE','MJ06:LHEE','MJ06:RFWT','MJ06:RBWT','MJ06:LFWT','MJ06:LBWT']

# Folders = os.listdir("database/raw")
# for folder in Folders:
#     print(folder)
#     markersPrefix=folder[2:4]+folder[0:2]
#     channels=[f'{markersPrefix}:RTOE',f'{markersPrefix}:RHEE',f'{markersPrefix}:LTOE',f'{markersPrefix}:LHEE',f'{markersPrefix}:RFWT',f'{markersPrefix}:RBWT',f'{markersPrefix}:LFWT',f'{markersPrefix}:LBWT']
#     Files=os.listdir(f"database/raw/{folder}")
#     for file in Files:
#         print(file)
#         print(pst.stepLength(f"database/newRawVF/{folder}/{file}",channels))

"""Cycle time"""

# filename="database/newRawVF/06MJ/Take 2014-09-29 02_57_20 PM.4.c3d"

# print(pst.cycleTime(filename))


"""Oscillation time"""

# filename="database/newRawVF/06MJ/Take 2014-09-29 02_57_20 PM.4.c3d"
# folder="06MJ"

# Folders = os.listdir("database/newRawVF")
# for folder in Folders:
#     print(folder)
#     markersPrefix=folder[2:4]+folder[0:2]
#     channels=[f'{markersPrefix}:RTOE',f'{markersPrefix}:RHEE',f'{markersPrefix}:LTOE',f'{markersPrefix}:LHEE',f'{markersPrefix}:RFWT',f'{markersPrefix}:RBWT',f'{markersPrefix}:LFWT',f'{markersPrefix}:LBWT']
#     Files=os.listdir(f"database/newRawVF/{folder}")
#     for file in Files:
#         print(file)
#         print(pst.oscillationTime(f"database/newRawVF/{folder}/{file}"))


"""Simplesupport Time"""
# filename="database/newRawVF/06MJ/Take 2014-09-29 02_57_20 PM.4.c3d"
# print(pst.simplesupportTime(filename))

""""Double Support"""

# filename="database/newRawVF/06MJ/Take 2014-09-29 02_57_20 PM.4.c3d"

# Folders = os.listdir("database/newRawVF")
# for folder in Folders:
#     print(folder)
#     markersPrefix=folder[2:4]+folder[0:2]
#     channels=[f'{markersPrefix}:RTOE',f'{markersPrefix}:RHEE',f'{markersPrefix}:LTOE',f'{markersPrefix}:LHEE',f'{markersPrefix}:RFWT',f'{markersPrefix}:RBWT',f'{markersPrefix}:LFWT',f'{markersPrefix}:LBWT']
#     Files=os.listdir(f"database/newRawVF/{folder}")
#     for file in Files:
#         print(file)
#         print(pst.doubleSupportTime(f"database/newRawVF/{folder}/{file}"))

"""Walk Axis"""

# filename="database/newRawVF/06MJ/Take 2014-09-29 02_57_20 PM.4.c3d"
# channels=['MJ06:RTOE','MJ06:RHEE','MJ06:LTOE','MJ06:LHEE','MJ06:RFWT','MJ06:RBWT','MJ06:LFWT','MJ06:LBWT']

# print(pst.walkAxis(filename,channels))

"""Step Wide"""

# filename="database/newRawVF/06MJ/Take 2014-09-29 02_57_20 PM.4.c3d"
# channels=['MJ06:RTOE','MJ06:RHEE','MJ06:LTOE','MJ06:LHEE','MJ06:RFWT','MJ06:RBWT','MJ06:LFWT','MJ06:LBWT']

# print(pst.stepWide(filename, channels))


"""stepAngle"""

filename="database/newRawVF/06MJ/Take 2014-09-29 02_57_20 PM.4.c3d"
channels=['MJ06:RTOE','MJ06:RHEE','MJ06:LTOE','MJ06:LHEE','MJ06:RFWT','MJ06:RBWT','MJ06:LFWT','MJ06:LBWT']


print(pst.stepAngle(filename,channels))
