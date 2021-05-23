# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 10:51:04 2020

@author: jmalucl
"""

# ADD DATETIME COLUMN TO FILE

from pathlib import Path
import pandas as pd
import numpy as np


CSV = list(Path.cwd().glob('*.csv'))

CSV_FILES = [str(Path(filename).stem) for filename in CSV]


    

def merge_and_date(CSV_FILES):
    datasets = []
    
    for file in CSV_FILES:
        dataset = pd.read_csv(file + ".csv", encoding='utf-8-sig')
        datasets.append(dataset)
        
    merged_dataset = pd.concat(datasets)
    merged_dataset = merged_dataset.drop_duplicates()
    merged_dataset.to_csv("MERGED.csv",  encoding='utf-8-sig', index=False)       
    return merged_dataset    
    
    
data = merge_and_date(CSV_FILES)    


