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
dataset_7 = pd.read_csv("2018_08_cleaned.csv", encoding="utf-8")
dataset_8 = pd.read_csv("2020_05_cleaned.csv", encoding="utf-8")

dataset = pd.concat([dataset_1,dataset_2,dataset_3,dataset_4,dataset_5,dataset_6,dataset_7, dataset_8])




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

translator = google_translator()  


dataset["text_pl"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='pl'))


dataset = dataset[["year", "month", "day", "author", "text", "text_en", "text_pl", "month_string"]]

dataset["text_pl"] = dataset["text_pl"].str.replace("Amen \.", "Amen.")
dataset["text_en"] = dataset["text_en"].str.replace("Amen \.", "Amen.")
dataset["text"] = dataset["text"].str.replace("Amen \.", "Amen.")

dataset.to_json("trevignano.json",orient="records")


