# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np

dataset_jan = pd.read_csv("january_2023.csv", encoding="utf-8")
dataset_jan["month_string"] = "January"


dataset2023 = pd.concat([dataset_jan])

dataset2023 = dataset2023.drop_duplicates()
dataset2023 = dataset2023[dataset2023["text_it"].notnull()]
dataset2023 = dataset2023[dataset2023["author"].notnull()]



dataset2023 = dataset2023[['year', 'month', 'day', 'author', 'month_string','text_it', 'text_en', 'text_es', 'text_fr',  'text_pt', 'text_de', 'text_pl','text_zh',]]

dataset2023 = dataset2023.drop_duplicates()

dataset2023.to_json("trevignano2023.js",orient="records")

dataset2023.to_csv("trevignano2023.csv", index=False)



























