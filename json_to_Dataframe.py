# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 13:47:58 2022

@author: Mathis
"""

import pandas as pd
import os

df = pd.DataFrame()
Folders = os.listdir("database/newRawjson")

for folder in Folders:
    Files=os.listdir(f"database/newRawjson/{folder}")
    for file in Files:
        df = pd.concat([df, pd.read_json(f"database/newRawjson/{folder}/{file}")])



print(df)