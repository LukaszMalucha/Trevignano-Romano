# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np
from google_trans_new import google_translator



dataset = pd.read_csv("april_cleaned.csv", encoding="utf-8")

dataset["text_pl"] = ""
dataset["text_en"] = ""


dataset["text_it"] = dataset["text_it"].str.replace("\"", "")
dataset["text_it"] = dataset["text_it"].str.replace("AmenLa", "Amen. La")
dataset["text_it"] = dataset["text_it"].str.replace("AmenIn", "Amen. In")
dataset["text_it"] = dataset["text_it"].str.replace("Santo \. Amen", "Santo, Amen.")
dataset["text_it"] = dataset["text_it"].str.replace(" : ", ": ")
dataset["text_it"] = dataset["text_it"].str.replace("Spirito santo", "Spirito Santo")
dataset["text_it"] = dataset["text_it"].str.replace("Dio Figli", "Dio. Figli")
dataset["text_it"] = dataset["text_it"].str.replace("Amen Oggi", "Amen. Oggi")
dataset["text_it"] = dataset["text_it"].str.replace("Continua a leggere\. \. \. \»", "")
dataset["text_it"] = dataset["text_it"].str.replace("sinistro\.\.", "sinistro.")
dataset["text_it"] = dataset["text_it"].str.replace("Amen Il ", "Amen. Il ")



# ENGLISH

dataset["text_en"] = np.where(((dataset["month"] == 4) & (dataset["day"] == 3)), "" , dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 4) & (dataset["day"] == 6)), "" , dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 4) & (dataset["day"] == 10)), "" , dataset["text_en"])


# POLISH

dataset["text_pl"] = np.where(((dataset["month"] == 4) & (dataset["day"] == 3)), "" , dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 4) & (dataset["day"] == 6)), "" , dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 4) & (dataset["day"] == 10)), "" , dataset["text_pl"])


translator = google_translator()  

#dataset["text_es"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='es'))
#dataset["text_fr"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='fr'))
#dataset["text_zh"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='zh'))
#dataset["text_de"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='de'))
#dataset["text_pt"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='pt'))







dataset.to_csv("april_2021.csv", encoding="utf-8", index=False)





