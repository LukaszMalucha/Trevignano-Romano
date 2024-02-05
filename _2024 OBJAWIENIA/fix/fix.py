# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:14:11 2024

@author: lucas
"""
import pandas as pd


dataset = pd.read_json("apparitions_2023_1.js")

dataset = dataset.drop_duplicates()
dataset_2 = pd.read_json("apparitions_2023.js")
dataset_2 = dataset_2.drop_duplicates()