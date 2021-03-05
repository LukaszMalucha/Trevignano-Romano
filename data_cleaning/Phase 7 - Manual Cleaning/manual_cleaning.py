# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np
from google_trans_new import google_translator  


dataset_old = pd.read_csv("trevignano - Italian Cleaned.csv", encoding="utf-8" )
dataset = pd.read_csv("trevignano.csv", encoding="utf-8" )

dataset1 = pd.read_csv("trevignano.csv", encoding="utf-8", error_bad_lines=False )



#dataset = dataset[['year', 'month', 'day', 'author', 'month_string', 'text_it', 'text_en','text_pl']]
#dataset = dataset.drop_duplicates()


translator = google_translator()  
dataset["text_es"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='es'))
dataset["text_fr"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='fr'))
dataset["text_zh"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='zh'))
dataset.to_csv("trevignano.csv", encoding="utf-8", index=False)

## DO ZROBIENIA

dataset["text_de"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='de'))
dataset["text_pt"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='pt'))





dataset.to_csv("trevignano.csv", encoding="utf-8", index=False)





pl = dataset[["text_pl"]]
pl.to_csv("pl.csv", encoding="utf-8", index=False)





dataset2016 = dataset[dataset["year"] == 2016]
dataset2017 = dataset[dataset["year"] == 2017]
dataset2018 = dataset[dataset["year"] == 2018]
dataset2019 = dataset[dataset["year"] == 2019]
dataset2020 = dataset[dataset["year"] == 2020]
dataset2021 = dataset[dataset["year"] == 2021]




# QUICK FIX


#dataset['text_it'] = np.where((dataset["month"] == 1) & (dataset["day"] == 3), "", dataset["text_it"])




dataset2016.to_json("trevignano2016.js",orient="records")
dataset2017.to_json("trevignano2017.js",orient="records")
dataset2018.to_json("trevignano2018.js",orient="records")
dataset2019.to_json("trevignano2019.js",orient="records")
dataset2020.to_json("trevignano2020.js",orient="records")
dataset2021.to_json("trevignano2021.js",orient="records")



###############################################

dataset.to_csv("trevignano.csv", encoding="utf-8", index=False)










