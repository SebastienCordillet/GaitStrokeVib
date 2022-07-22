# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 09:16:51 2022

@author: cordillet
"""
import os
import pandas as pd

pathPST="database/newRawjson"


listSujets = os.listdir(pathPST)
# print(listSujets)

d=pd.DataFrame()
for subj in listSujets:
    # print(subj)
    subjPath=os.path.join(pathPST, subj, "json")
    listFiles=os.listdir(subjPath)
    # print(listFiles)
    for file in listFiles:
        # print(file)
        filePath=os.path.join(subjPath,file)
        d=d.append(pd.read_json(filePath))
        


print(d)
d.to_excel(os.path.join(pathPST,"PST.xlsx"))
        
        
        