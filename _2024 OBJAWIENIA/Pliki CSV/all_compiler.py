# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:10:09 2023

@author: lucas
"""

import pandas as pd
import glob
CSV = glob.glob('*.csv')



dataset_all = pd.DataFrame()



for element in CSV:
    dataset = pd.read_csv(element)
    dataset_all = pd.concat([dataset_all, dataset])


dataset_all = dataset_all.drop_duplicates()


dataset_all.to_csv("ALL_apparitions.csv", index=False)

dataset_all["title"] = dataset_all["year"].astype(str) + "-" + dataset_all["month"].astype(str) + "-" + dataset_all["day"].astype(str) + " " + dataset_all["source"] + " - " + dataset_all["author"]
dataset_all["english"] = dataset_all["title"] + "\n" + dataset_all["text_en"] + "\n"

english = dataset_all["english"].to_list()

english = ("\n").join(english)

with open("ENGLISH.txt", "w", encoding='utf-8') as output:
    output.write(english)