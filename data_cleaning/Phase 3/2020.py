# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np




dataset = pd.read_csv("2020_cleaned.csv", encoding="utf-8")



# SPELLING FIX

dataset["text_pl"] = dataset["text_pl"].str.replace("módlcie się z rękami złożonymi \.", "módlcie się z złożonymi rękami.")





dataset["text_en"] = dataset["text_en"].str.replace("perfume", "scent")


# MARY FORM

dataset_mary = dataset[dataset["author"] == "Holy Mary" ]
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Chciałbym", "Chciałabym")
dataset_jesus = dataset[dataset["author"] != "Holy Mary" ]
dataset= pd.concat([dataset_mary, dataset_jesus])









dataset.to_csv("trevignano_2020.csv", index=False, encoding="utf-8")
dataset.to_json("trevignano_2020.json",orient="records")







