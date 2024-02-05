# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 12:58:48 2021

@author: LukaszMalucha
"""

import pandas as pd
import numpy as np


dataset = pd.read_csv("ALL_apparitions.csv", encoding="utf-8")



dataset["year"] = dataset["year"].astype(str)
dataset["month"] = dataset["month"].astype(str)
dataset["day"] = dataset["day"].astype(str)

dataset["month"] = np.where(dataset["month"].str.len() == 1, "0" + dataset["month"], dataset["month"] )
dataset["day"] = np.where(dataset["day"].str.len() == 1, "0" + dataset["day"], dataset["day"] )


dataset["date"] = dataset["year"] + "-" + dataset["month"] + "-" + dataset["day"]

dataset = dataset[["date", "author"]]
dataset["apparition"] = 1









begin_date = '2009-01-01'

df = pd.date_range(start='1/1/2009', end='3/3/2023')

data  = pd.DataFrame()

data["date"] = df.strftime("%Y-%m-%d")
data["x"] = 1


dataset_jesus = dataset[dataset["author"] == "Jesus Christ"]
dataset_mary = dataset[dataset["author"] == "Holy Mary"]
dataset_michael = dataset[dataset["author"] == "Archangel Michael"]

dataset = data.merge(dataset, how="left", on=["date"])
dataset = dataset[["date", "apparition"]]
dataset = dataset.fillna(0)
dataset = dataset.groupby(["date"]).sum()
dataset = dataset.reset_index()

dataset_jesus = data.merge(dataset_jesus, how="left", on=["date"])
dataset_jesus = dataset_jesus[["date", "apparition"]]
dataset_jesus = dataset_jesus.fillna(0)
dataset_jesus = dataset_jesus.groupby(["date"]).sum()
dataset_jesus = dataset_jesus.reset_index()

dataset_mary = data.merge(dataset_mary, how="left", on=["date"])
dataset_mary = dataset_mary[["date", "apparition"]]
dataset_mary = dataset_mary.fillna(0)
dataset_mary = dataset_mary.groupby(["date"]).sum()
dataset_mary = dataset_mary.reset_index()

dataset_michael = data.merge(dataset_michael, how="left", on=["date"])
dataset_michael = dataset_michael[["date", "apparition"]]
dataset_michael = dataset_michael.fillna(0)
dataset_michael = dataset_michael.groupby(["date"]).sum()
dataset_michael = dataset_michael.reset_index()



dataset.to_csv("occurence_02_2023.csv", encoding="utf-8", index=False)
dataset_jesus.to_csv("occurence_jesus_02_2023.csv", encoding="utf-8", index=False)
dataset_mary.to_csv("occurence_mary_02_2023.csv", encoding="utf-8", index=False)
dataset_michael.to_csv("occurence_michael_02_2023.csv", encoding="utf-8", index=False)
















