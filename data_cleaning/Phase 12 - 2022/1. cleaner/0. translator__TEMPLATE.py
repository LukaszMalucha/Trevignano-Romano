# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np
from google_trans_new import google_translator
import goslate
gs = goslate.Goslate()




dataset = pd.read_csv("XXXXXXX_cleaned.csv", encoding="utf-8")




# ITALIAN

#dataset["text_it"] = np.where(((dataset["month"] == XXX) & (dataset["day"] == 1)), "", dataset["text_it"])
#dataset["text_it"] = np.where(((dataset["month"] == XXX) & (dataset["day"] == 1)), "", dataset["text_it"])

# ENGLISH

#dataset["text_en"] = np.where(((dataset["month"] == XXX) & (dataset["day"] == 1)), "", dataset["text_en"])
#dataset["text_en"] = np.where(((dataset["month"] == XXX) & (dataset["day"] == 1)), "", dataset["text_en"])

# POLISH

#dataset["text_pl"] = np.where(((dataset["month"] == XXX) & (dataset["day"] == 1)), "", dataset["text_pl"])
#dataset["text_pl"] = np.where(((dataset["month"] == XXX) & (dataset["day"] == 1)), "", dataset["text_pl"])

dataset = dataset[['year', 'month', 'day', 'author', 'text_it', 'month_string', 'text_pl','text_en']]

dataset_ready = pd.read_csv("XXXX_2022.csv")


dataset = dataset.merge(dataset_ready, how="left", on=['year', 'month', 'day', 'author', 'text_it', 'month_string', 'text_pl','text_en'])

dataset_ok = dataset[~dataset["text_pt"].isnull()]
dataset_translate = dataset[dataset["text_pt"].isnull()]



from googletrans import Translator
translator = Translator()

dataset_translate["text_es"] = dataset_translate["text_en"].apply(lambda x: translator.translate(x,'es'))
dataset_translate["text_es"] = dataset_translate["text_es"].apply(lambda x: x.text)

dataset_translate["text_fr"] = dataset_translate["text_en"].apply(lambda x: translator.translate(x,'fr'))
dataset_translate["text_fr"] = dataset_translate["text_fr"].apply(lambda x: x.text)

dataset_translate["text_zh"] = dataset_translate["text_en"].apply(lambda x: translator.translate(x,'zh-cn'))
dataset_translate["text_zh"] = dataset_translate["text_zh"].apply(lambda x: x.text)

dataset_translate["text_de"] = dataset_translate["text_en"].apply(lambda x: translator.translate(x,'de'))
dataset_translate["text_de"] = dataset_translate["text_de"].apply(lambda x: x.text)

dataset_translate["text_pt"] = dataset_translate["text_en"].apply(lambda x: translator.translate(x,'pt'))
dataset_translate["text_pt"] = dataset_translate["text_pt"].apply(lambda x: x.text)


dataset = pd.concat([dataset_ok, dataset_translate])

dataset = dataset.sort_values(by="day")


dataset.to_csv("XXXX_2022.csv", encoding="utf-8", index=False)


# First Translation
dataset_translate = dataset
dataset_translate.to_csv("september_2022.csv", encoding="utf-8", index=False)





