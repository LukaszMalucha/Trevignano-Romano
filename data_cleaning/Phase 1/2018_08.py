# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



from google_trans_new import google_translator  
import pandas as pd
import numpy as np

def list_cleaner(lst):
    clean_lst = []
    for element in lst:
        if "lareginadelrosario" not in element:
            if len(element) > 10:            
                clean_lst.append(element)
    return clean_lst        
            
        

def title_remover(lst):
    clean_lst = [] 
    for element in lst:
        if element[:2] != "ME":
            clean_lst.append(element)
    return clean_lst  

def add_zero(string):
    if len(string) == 1:
        string = "0" + string
    return string    


dataset = pd.read_csv("2018_08.csv", encoding="utf-8")

dataset["text"] = dataset["text"].str.strip()
dataset["text"] = dataset["text"].str.replace("\n", " ")
dataset["text"] = dataset["text"].str.split("Pubblicato da").str[1]
dataset["text"] = dataset["text"].str.replace("Trevignano romano", "Trevignano Romano")
dataset["text"] = dataset["text"].str.replace("\. ", ".")
dataset["text"] = dataset["text"].str.replace("\.", ". ")
dataset = dataset[dataset["text"].str.contains("Trevignano Romano")]
dataset["text"] = dataset["text"].str.replace("\xa0", "")
dataset["text"] = dataset["text"].str.replace("2018", "2018 ")
dataset["text"] = dataset["text"].str.replace("2018  ", "2018 ")
dataset["text"] = dataset["text"].str.replace("\(rm\)", "")
dataset['text'] = dataset['text'].str.replace("- ore 20:20 ", "")
dataset['text'] = dataset['text'].str.replace("1°", "")
dataset['text'] = dataset['text'].str.replace("- 20:20 ", "")
dataset['text'] = dataset['text'].str.replace("16:42 ", "")
dataset['text'] = dataset['text'].str.replace("ore 16:42", "")
dataset['text'] = dataset['text'].str.replace("delle ore 23:05 ", "")
dataset['text'] = dataset['text'].str.replace("​ Amati", "Amati")


# Replace Months
dataset["text"] = dataset["text"].str.replace("gennaio 2018", "Gennaio 2018")
dataset["text"] = dataset["text"].str.replace("febbraio 2018", "Febbraio 2018")
dataset["text"] = dataset["text"].str.replace("marzo 2018", "Marzo 2018")
dataset["text"] = dataset["text"].str.replace("aprile 2018", "Aprile 2018")
dataset["text"] = dataset["text"].str.replace("maggio 2018", "Maggio 2018")
dataset["text"] = dataset["text"].str.replace("giugno 2018", "Giugno 2018")
dataset["text"] = dataset["text"].str.replace("luglio 2018", "Luglio 2018")
dataset["text"] = dataset["text"].str.replace("agosto 2018", "Agosto 2018")
dataset["text"] = dataset["text"].str.replace("settembre 2018", "Settembre 2018")
dataset["text"] = dataset["text"].str.replace("ottobre 2018", "Ottobre 2018")
dataset["text"] = dataset["text"].str.replace("novembre 2018", "Novembre 2018")
dataset["text"] = dataset["text"].str.replace("dicembre 2018", "Dicembre 2018")


dataset["text"] = dataset["text"].str.replace("Gennaio 2018", "01 2018")
dataset["text"] = dataset["text"].str.replace("Febbraio 2018", "02 2018")
dataset["text"] = dataset["text"].str.replace("Marzo 2018", "03 2018")
dataset["text"] = dataset["text"].str.replace("Aprile 2018", "04 2018")
dataset["text"] = dataset["text"].str.replace("Maggio 2018", "05 2018")
dataset["text"] = dataset["text"].str.replace("Giugno 2018", "06 2018")
dataset["text"] = dataset["text"].str.replace("Luglio 2018", "07 2018")
dataset["text"] = dataset["text"].str.replace("Agosto 2018", "08 2018")
dataset["text"] = dataset["text"].str.replace("Settembre 2018", "09 2018")
dataset["text"] = dataset["text"].str.replace("Ottobre 2018", "10 2018")
dataset["text"] = dataset["text"].str.replace("Novembre 2018", "11 2018")
dataset["text"] = dataset["text"].str.replace("Dicembre 2018", "12 2018")

dataset["text"] = dataset["text"].str.replace("settembre2018", "09 2018")

dataset["text"] = dataset["text"].str.split("Trevignano Romano")

dataset["text"] = dataset["text"].apply(lambda x: list_cleaner(x))
dataset["text"] = dataset["text"].apply(lambda x: title_remover(x))


text_column = dataset.apply(lambda x: pd.Series(x['text']), axis=1).stack().reset_index(level=1, drop=True)
text_column.name = 'text'
dataset = dataset.drop('text', axis=1).join(text_column)
dataset['text'] = pd.Series(dataset['text'], dtype=object)

dataset["author"] = np.where(dataset["text"].str.contains("Messaggio di Gesù"), "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["text"].str.contains("Messaggio di Gesu"), "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["text"].str.contains("Messaggio di Dio Padre"), "Holy Father", dataset["author"])


dataset["day"] = dataset["text"].str.split(" 2018 ").str[0]
dataset["day"] = dataset["day"].str.replace(",", "")
dataset["day"] = dataset["day"].str.strip()
dataset["day"] = dataset["day"].str.split(" ").str[0]
dataset["day"]  = dataset["day"].apply(lambda x: add_zero(x))

dataset["date"] = dataset["date"] + "_" + dataset["day"]


dataset['text'] = dataset["text"].str.split(" 2018 ").str[1]
dataset['text'] = dataset['text'].str.replace("MESSAGGIO:", "")
dataset['text'] = dataset['text'].str.replace("  messaggio  ", "")
dataset['text'] = dataset['text'].str.strip()
dataset['text'] = dataset['text'].str.replace("“", "")





dataset['text'] = dataset['text'].str.replace("messaggio  ", "")
dataset['text'] = dataset['text'].str.replace("MESSAGGIO  ", "")
dataset['text'] = dataset['text'].str.replace("Messaggio  ", "")
dataset['text'] = dataset['text'].str.replace("Messaggio:  ", "")
dataset['text'] = dataset['text'].str.replace("Messaggio di Gesu ", "")
dataset['text'] = dataset['text'].str.replace("Messaggio di Gesù ", "")
dataset['text'] = dataset['text'].str.replace("Messaggio di Gesù: ore 22:55 ", "")
dataset['text'] = dataset['text'].str.replace("Messaggio della Madonna ", "")
dataset['text'] = dataset['text'].str.replace("Messaggio di Gesù: ", "")
dataset['text'] = dataset['text'].str.replace("Messaggio di Gesù;", "")
dataset['text'] = dataset['text'].str.replace("Messaggio di Gesù", "")
dataset['text'] = dataset['text'].str.replace("Messaggio di Gesu", "")
dataset['text'] = dataset['text'].str.replace("Messaggio di Dio Padre, ore 23:25", "")



dataset['text'] = dataset['text'].str.strip()

dataset['text'] = dataset['text'].str.replace(",", " , ")
dataset['text'] = dataset['text'].str.replace(" , ", ", ")
dataset['text'] = dataset['text'].str.replace(" , ", ", ")
dataset['text'] = dataset['text'].str.replace(" \.  ", ". ")
dataset['text'] = dataset['text'].str.replace("  ", " ")
dataset['text'] = dataset['text'].str.replace("\(Gisella\) Ore 15:30. ", "")
dataset['text'] = dataset['text'].str.replace("  ", " ")


dataset['text'] = dataset['text'].str.replace("Messaggio di Dio Padre, ore 23:25", "")

dataset["date"] = dataset["date"].str.split("_")

dataset["date"] = dataset["date"].str[2] + "_" + dataset["date"].str[1] + "_" + dataset["date"].str[0]
dataset = dataset.drop("day", axis=1)





translator = google_translator()  


dataset["text_en"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='en'))


dataset = dataset[dataset["text_en"] != "male"]

dataset = dataset[~dataset["text"].isnull()]
dataset = dataset[dataset["text_en"] != ""]



dataset.to_csv("2018_08_cleaned.csv", index=False, encoding="utf-8")

