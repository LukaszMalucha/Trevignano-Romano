# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 13:56:41 2021

@author: LukaszMalucha
"""

import pandas as pd
import numpy as np


dataset = pd.read_csv("2016.csv", encoding="utf-8")

dataset = dataset[:51]

dataset["year"] = dataset["year"].str.strip()
dataset["author"] = dataset["year"].str.split(" ").str[:-3].str.join(" ")
dataset["author"] = dataset["author"].str.title()
dataset["month_string"] = dataset["year"].str.split(" ").str[-2].str.title().str.replace(",", "")
dataset["day"] = dataset["year"].str.split(" ").str[-3]
dataset["year"] = dataset["year"].str.split(" ").str[-1].str.replace(",", "")

dataset["month"] = ""

dataset["month"] = np.where(dataset["month_string"] == "January", 1, dataset["month"]) 
dataset["month"] = np.where(dataset["month_string"] == "February", 2, dataset["month"]) 
dataset["month"] = np.where(dataset["month_string"] == "March", 3, dataset["month"]) 
dataset["month"] = np.where(dataset["month_string"] == "April", 4, dataset["month"]) 
dataset["month"] = np.where(dataset["month_string"] == "May", 5, dataset["month"]) 
dataset["month"] = np.where(dataset["month_string"] == "June", 6, dataset["month"]) 
dataset["month"] = np.where(dataset["month_string"] == "July", 7, dataset["month"]) 
dataset["month"] = np.where(dataset["month_string"] == "August", 8, dataset["month"]) 
dataset["month"] = np.where(dataset["month_string"] == "September", 9, dataset["month"])
dataset["month"] = np.where(dataset["month_string"] == "October", 10, dataset["month"]) 
dataset["month"] = np.where(dataset["month_string"] == "November", 11, dataset["month"])
dataset["month"] = np.where(dataset["month_string"] == "December", 12, dataset["month"]) 

dataset["author"] = dataset["author"].str.replace("God The Father", "Holy Father")
dataset["author"] = dataset["author"].str.replace("Blessed Vrigin Mary", "Holy Mary")
dataset["author"] = dataset["author"].str.replace("Blessed Virgn Mary", "Holy Mary")
dataset["author"] = dataset["author"].str.replace("Blessed Virgn Mary", "Holy Mary")

dataset = dataset[['author','day','month', 'month_string', 'year', 'text_pl' ]]

dataset1 = dataset

# DATY W RÓŻNYM FORMACIE !!!!!!!!!!!!!!!!!!!!!!



dataset = pd.read_csv("2021.csv", encoding="utf-8")

#dataset = dataset[51:]

dataset["year"] = dataset["year"].str.strip()
dataset["author"] = dataset["year"].str.split(" ").str[:-3].str.join(" ")
dataset["author"] = dataset["author"].str.title()
dataset["month_string"] = dataset["year"].str.split(" ").str[-3].str.title()
dataset["day"] = dataset["year"].str.split(" ").str[-2].str.replace(",", "")
dataset["year"] = dataset["year"].str.split(" ").str[-1].str.replace(",", "")

dataset["month"] = ""

dataset["month"] = np.where(dataset["month_string"] == "January", 1, dataset["month"]) 
dataset["month"] = np.where(dataset["month_string"] == "February", 2, dataset["month"]) 
dataset["month"] = np.where(dataset["month_string"] == "March", 3, dataset["month"]) 
dataset["month"] = np.where(dataset["month_string"] == "April", 4, dataset["month"]) 
dataset["month"] = np.where(dataset["month_string"] == "May", 5, dataset["month"]) 
dataset["month"] = np.where(dataset["month_string"] == "June", 6, dataset["month"]) 
dataset["month"] = np.where(dataset["month_string"] == "July", 7, dataset["month"]) 
dataset["month"] = np.where(dataset["month_string"] == "August", 8, dataset["month"]) 
dataset["month"] = np.where(dataset["month_string"] == "September", 9, dataset["month"])
dataset["month"] = np.where(dataset["month_string"] == "October", 10, dataset["month"]) 
dataset["month"] = np.where(dataset["month_string"] == "November", 11, dataset["month"])
dataset["month"] = np.where(dataset["month_string"] == "December", 12, dataset["month"]) 

dataset["author"] = dataset["author"].str.replace("God The Father", "Holy Father")
dataset["author"] = dataset["author"].str.replace("Blessed Vrigin Mary", "Holy Mary")
dataset["author"] = dataset["author"].str.replace("Blessed Virgn Mary", "Holy Mary")
dataset["author"] = dataset["author"].str.replace("Blessed Virgn Mary", "Holy Mary")

dataset = dataset[['author','day','month', 'month_string', 'year', 'text_pl' ]]

dataset2 = dataset


dataset = pd.concat([dataset1, dataset2])


dataset.to_json("argentina2021.js",orient="records")










