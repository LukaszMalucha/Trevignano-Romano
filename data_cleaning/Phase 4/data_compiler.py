# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np




dataset2016 = pd.read_csv("trevignano2016.csv", encoding="utf-8")
dataset2017 = pd.read_csv("trevignano2017.csv", encoding="utf-8")
dataset2018 = pd.read_csv("trevignano2018.csv", encoding="utf-8")
dataset2019 = pd.read_csv("trevignano2019.csv", encoding="utf-8")
dataset2020 = pd.read_csv("trevignano2020.csv", encoding="utf-8")
dataset2021 = pd.read_csv("trevignano2021.csv", encoding="utf-8")



dataset = pd.concat([dataset2016, dataset2017, dataset2018, dataset2019, dataset2020, dataset2021])

dataset["text_es"] = " "
dataset["text_fr"] = " "

dataset.isnull().values.any()


dataset.to_csv("trevignano.csv", encoding="utf-8", index=False)

































