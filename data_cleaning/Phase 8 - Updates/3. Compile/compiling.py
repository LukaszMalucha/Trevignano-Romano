# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np



dataset_old = pd.read_json("trevignano2021.js")
dataset_mar = pd.read_csv("march_2021.csv", encoding="utf-8")
dataset_apr = pd.read_csv("april_2021.csv", encoding="utf-8")


dataset2021 = pd.concat([dataset_old, dataset_mar, dataset_apr])

dataset2021 = dataset2021[['year', 'month', 'day', 'author', 'month_string','text_it', 'text_en', 'text_es', 'text_fr',  'text_pt', 'text_de', 'text_pl','text_zh',]]

dataset2021.to_json("trevignano2021.js",orient="records")










