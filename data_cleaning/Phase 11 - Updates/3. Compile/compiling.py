# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np



dataset_old = pd.read_json("trevignano2021.js")
dataset_jan = dataset_old[dataset_old["month"] == 1]
dataset_feb = dataset_old[dataset_old["month"] == 2]
dataset_mar = pd.read_csv("march_2021.csv", encoding="utf-8")
dataset_apr = pd.read_csv("april_2021.csv", encoding="utf-8")
dataset_may = pd.read_csv("may_2021.csv", encoding="utf-8")
dataset_june = pd.read_csv("june_2021.csv", encoding="utf-8")
dataset_july = pd.read_csv("july_2021.csv", encoding="utf-8")
dataset_august = pd.read_csv("august_2021.csv", encoding="utf-8")
dataset_september = pd.read_csv("september_2021.csv", encoding="utf-8")
dataset_october = pd.read_csv("october_2021.csv", encoding="utf-8")
dataset_november = pd.read_csv("november_2021.csv", encoding="utf-8")
dataset_december = pd.read_csv("december_2021.csv", encoding="utf-8")

dataset2021 = pd.concat([dataset_jan, dataset_feb, dataset_mar, dataset_apr, dataset_may, dataset_june, dataset_july, dataset_august, dataset_september, dataset_october, dataset_november, dataset_december])

dataset2021 = dataset2021.drop_duplicates()
dataset2021 = dataset2021[dataset2021["text_it"].notnull()]
dataset2021 = dataset2021[dataset2021["author"].notnull()]



dataset2021 = dataset2021[['year', 'month', 'day', 'author', 'month_string','text_it', 'text_en', 'text_es', 'text_fr',  'text_pt', 'text_de', 'text_pl','text_zh',]]

dataset2021 = dataset2021.drop_duplicates()

dataset2021.to_json("trevignano2021.js",orient="records")



























