# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np
from google_trans_new import google_translator  




dataset2016 = pd.read_csv("trevignano2016.csv", encoding="utf-8")
dataset2017 = pd.read_csv("trevignano2017.csv", encoding="utf-8")
dataset2018 = pd.read_csv("trevignano2018.csv", encoding="utf-8")
dataset2019 = pd.read_csv("trevignano2019.csv", encoding="utf-8")
dataset2020 = pd.read_csv("trevignano2020.csv", encoding="utf-8")
dataset2021 = pd.read_csv("trevignano2021.csv", encoding="utf-8")



dataset = pd.concat([dataset2016, dataset2017, dataset2018, dataset2019, dataset2020, dataset2021])




dataset["text_es"] = " "
dataset["text_fr"] = " "



translator = google_translator()  


dataset["text_es"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='es'))
dataset["text_fr"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='fr'))
dataset["text_zh"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='zh'))
dataset["text_de"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='de'))
dataset["text_pt"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='pt'))

dataset = dataset.rename(columns={"text" : "text_it"})


dataset.isnull().values.any()


dataset = dataset[['year', 'month', 'day', 'author', 'month_string','text_it', 'text_en', 'text_pl', 'text_es', 'text_fr',  'text_de', 'text_zh',]]


dataset.to_csv("trevignano.csv", encoding="utf-8", index=False)


#dataset = pd.read_csv("trevignano.csv", encoding="utf-8")
#
#translator = google_translator()  
#dataset["text_pt"] = dataset["text_it"].apply(lambda x: translator.translate(x,lang_tgt='pt'))












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


dataset.to_csv("apparition_occurence.csv", encoding="utf-8", index=False)

























