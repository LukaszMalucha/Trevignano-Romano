# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 12:58:48 2021

@author: LukaszMalucha
"""

import pandas as pd
import numpy as np


dataset_old = pd.read_csv("apparition_occurence.csv", encoding="utf-8")


dataset_mar = pd.read_csv("march_2021.csv", encoding="utf-8")
dataset_apr = pd.read_csv("april_2021.csv", encoding="utf-8")
dataset_may = pd.read_csv("may_2021.csv", encoding="utf-8")
dataset_june = pd.read_csv("june_2021.csv", encoding="utf-8")
dataset_july = pd.read_csv("july_2021.csv", encoding="utf-8")
dataset_august = pd.read_csv("august_2021.csv", encoding="utf-8")
dataset_september = pd.read_csv("september_2021.csv", encoding="utf-8")
dataset_october = pd.read_csv("october_2021.csv", encoding="utf-8")
dataset_november = pd.read_csv("november_2021.csv", encoding="utf-8")

dataset = pd.concat([dataset_mar, dataset_apr, dataset_may, dataset_june, dataset_july, dataset_august, dataset_september, dataset_october,dataset_november])


dataset["year"] = dataset["year"].astype(str)
dataset["month"] = dataset["month"].astype(str)
dataset["day"] = dataset["day"].astype(str)

dataset["month"] = np.where(dataset["month"].str.len() == 1, "0" + dataset["month"], dataset["month"] )
dataset["day"] = np.where(dataset["day"].str.len() == 1, "0" + dataset["day"], dataset["day"] )


dataset["date"] = dataset["year"] + "-" + dataset["month"] + "-" + dataset["day"]

dataset = dataset[["date", "author"]]
dataset["apparition"] = 1









begin_date = '2019-10-16'

df = pd.date_range(start='1/1/2016', end='31/12/2021')

data  = pd.DataFrame()

data["date"] = df.strftime("%Y-%m-%d")
data["x"] = 1


dataset = data.merge(dataset, how="left", on=["date"])

dataset = dataset[["date", "apparition"]]

dataset = dataset.fillna(0)



dataset_all = dataset_old.merge(dataset, on=["date"], how="left")


dataset_all["apparition"] = dataset_all["apparition_x"] + dataset_all["apparition_y"]

dataset_all = dataset_all[["date","apparition"]]




dataset_all.to_csv("apparitions_november.csv", encoding="utf-8", index=False)

