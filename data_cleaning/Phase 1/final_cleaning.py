# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 13:54:58 2021

@author: LukaszMalucha
"""

import pandas as pd
import numpy as np


dataset = pd.read_csv("2016_cleaned.csv", encoding="utf-8")


check = dataset[dataset["text"].str.contains("\"")]

