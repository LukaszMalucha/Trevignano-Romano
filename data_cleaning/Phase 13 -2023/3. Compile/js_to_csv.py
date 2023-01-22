# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np
from google_trans_new import google_translator



dataset_2021 = pd.read_json("trevignano2021.js")
dataset_2022 = pd.read_json("trevignano2022.js")

dataset_2021["month_string"] = np.where(dataset_2021["month"] == 9, "September",dataset_2021["month_string"]  )


dataset_2022["text_pt"] = dataset_2022["text_pt"].fillna(" ")

dataset_2021.to_csv("trevignano2021.csv", index=False)
dataset_2022.to_csv("trevignano2022.csv", index=False)




