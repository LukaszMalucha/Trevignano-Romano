# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""


import pandas as pd
import numpy as np
from google_trans_new import google_translator 


dataset_1 = pd.read_csv("2016_cleaned.csv", encoding="utf-8")
dataset_2 = pd.read_csv("2017_cleaned.csv", encoding="utf-8")
dataset_3 = pd.read_csv("2018_cleaned.csv", encoding="utf-8")
dataset_4 = pd.read_csv("2019_cleaned.csv", encoding="utf-8")
dataset_5 = pd.read_csv("2020_cleaned.csv", encoding="utf-8")
dataset_6 = pd.read_csv("2021_cleaned.csv", encoding="utf-8")




dataset = pd.concat([dataset_1,dataset_2,dataset_3,dataset_4,dataset_5,dataset_6])

dataset["month"] = dataset["month"].astype(str)
dataset["month"] = np.where(dataset["month"].str.len() == 1, "0" + dataset["month"], dataset["month"])

dataset["day"] = dataset["day"].astype(str)
dataset["day"] = np.where(dataset["day"].str.len() == 1, "0" + dataset["day"], dataset["day"])

dataset["day"] = dataset["day"].str.replace("Cenacolo", "28")
dataset["day"] = dataset["day"].str.replace("rm", "12")

dataset["date"] = dataset["year"].astype(str) + "-" + dataset["month"].astype(str) + "-" + dataset["day"].astype(str) 
dataset["date"] = dataset["year"].astype(str) + "-" + dataset["month"].astype(str) + "-" + dataset["day"].astype(str) 

ost = pd.date_range("2016-01-01", "2021-12-31")
osta = ost.strftime("%Y-%m-%d")

fr = osta.to_frame(index=False, name="date")


data = fr.merge(dataset, how="left", on=["date"])


data = data[["date", "year"]]



data["apparition"] = np.where(data["year"].isnull(), 0, 1)
data = data[["date", "apparition"]]


data.to_csv("apparitions.csv", encoding="utf-8")





















dataset["year"] = dataset["date"].str.split("_").str[-1]
dataset["month"] = dataset["date"].str.split("_").str[1]
dataset["day"] = dataset["date"].str.split("_").str[0]

dataset["month_string"]  = dataset["month"]

dataset["month_string"] = dataset["month_string"].str.replace("01", "January")
dataset["month_string"] = dataset["month_string"].str.replace("02", "February")
dataset["month_string"] = dataset["month_string"].str.replace("03", "March")
dataset["month_string"] = dataset["month_string"].str.replace("04", "April")
dataset["month_string"] = dataset["month_string"].str.replace("05", "May")
dataset["month_string"] = dataset["month_string"].str.replace("06", "June")
dataset["month_string"] = dataset["month_string"].str.replace("07", "July")
dataset["month_string"] = dataset["month_string"].str.replace("08", "August")
dataset["month_string"] = dataset["month_string"].str.replace("09", "September")
dataset["month_string"] = dataset["month_string"].str.replace("10", "October")
dataset["month_string"] = dataset["month_string"].str.replace("11", "November")
dataset["month_string"] = dataset["month_string"].str.replace("12", "December")



dataset["day"] = dataset["day"].str.replace("Cenacolo", "28")
dataset["day"] = dataset["day"].str.replace("rm", "08")


dataset["text"] = dataset["text"].str.replace("”", "")
dataset["text_en"] = dataset["text_en"].str.replace("”", "")

dataset = dataset.sort_values(by=["year", "month", "day"])



dataset = dataset[["year", "month", "day", "author", "text", "text_en", "text_pl", "month_string"]]

dataset["text_pl"] = dataset["text_pl"].str.replace("Amen \.", "Amen.")
dataset["text_en"] = dataset["text_en"].str.replace("Amen \.", "Amen.")
dataset["text"] = dataset["text"].str.replace("Amen \.", "Amen.")



dataset.to_csv("trevignano.csv", encoding="utf-8")
dataset.to_json("trevignano.json",orient="records")


