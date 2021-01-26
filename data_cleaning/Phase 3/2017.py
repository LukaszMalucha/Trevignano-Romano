# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np




dataset = pd.read_csv("trevignano_2017.csv", encoding="utf-8")



# SPELLING FIX
dataset["text_pl"] = dataset["text_pl"].str.replace("aa", "a")
dataset["text_pl"] = dataset["text_pl"].str.replace("którzy idą za ulotnymi", "którzy idą za tym, co ulotne")
dataset["text_pl"] = dataset["text_pl"].str.replace("namaściła nas pojedynczo", "naznaczyła nas pojedynczo")
dataset["text_pl"] = dataset["text_pl"].str.replace("więc nie odwracajcie go", "więc nie odwracajcie się od Niego")
dataset["text_pl"] = dataset["text_pl"].str.replace(" za świat, będzie", " za świat, który będzie")
dataset["text_pl"] = dataset["text_pl"].str.replace("Wkrótce będziesz zmuszony", "Wkrótce będziecie zmuszeni")
dataset["text_pl"] = dataset["text_pl"].str.replace("odmawiajcie w komunii Różaniec Święty", "odmawiajcie wspólnie Różaniec Święty")
dataset["text_pl"] = dataset["text_pl"].str.replace("nowym osobom, którzy", "nowym osobom, które")
dataset["text_pl"] = dataset["text_pl"].str.replace(" jesteśmy u kresu czasu, więc nie traćcie czasu", " jesteśmy u kresu, więc nie traćcie czasu")
dataset["text_pl"] = dataset["text_pl"].str.replace("Otóż ​​błogosławię", "Teraz ​​błogosławię")
dataset["text_pl"] = dataset["text_pl"].str.replace("Więc do zobaczenia, szczególnie dziś wieczorem", "Tak was widzę, szczególnie dzisiaj")
dataset["text_pl"] = dataset["text_pl"].str.replace("grzesznym wyrazem Kościoła", "grzeszną postawą Kościoła")






dataset.to_csv("trevignano2017.csv", index=False, encoding="utf-8")
dataset.to_json("trevignano2017.json",orient="records")
