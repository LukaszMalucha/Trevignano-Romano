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


dataset = pd.read_csv("2020_05.csv", encoding="utf-8")

dataset["text"] = dataset["text"].str.strip()
dataset["text"] = dataset["text"].str.replace("\n", " ")
dataset["text"] = dataset["text"].str.split("Pubblicato da").str[1]
dataset["text"] = dataset["text"].str.replace("Trevignano romano", "Trevignano Romano")
dataset["text"] = dataset["text"].str.replace("\. ", ".")
dataset["text"] = dataset["text"].str.replace("\.", ". ")
dataset = dataset[dataset["text"].str.contains("Trevignano Romano")]
dataset["text"] = dataset["text"].str.replace("\xa0", "")
dataset["text"] = dataset["text"].str.replace("2020", "2020 ")
dataset["text"] = dataset["text"].str.replace("2020  ", "2020 ")
dataset["text"] = dataset["text"].str.replace("\(rm\)", "")
dataset['text'] = dataset['text'].str.replace("- ore 20:20 ", "")
dataset['text'] = dataset['text'].str.replace("1°", "")
dataset['text'] = dataset['text'].str.replace("- 20:20 ", "")
dataset['text'] = dataset['text'].str.replace("16:42 ", "")
dataset['text'] = dataset['text'].str.replace("ore 16:42", "")
dataset['text'] = dataset['text'].str.replace("delle ore 23:05 ", "")
dataset['text'] = dataset['text'].str.replace("​ Amati", "Amati")


# Replace Months
dataset["text"] = dataset["text"].str.replace("gennaio 2020", "Gennaio 2020")
dataset["text"] = dataset["text"].str.replace("febbraio 2020", "Febbraio 2020")
dataset["text"] = dataset["text"].str.replace("marzo 2020", "Marzo 2020")
dataset["text"] = dataset["text"].str.replace("aprile 2020", "Aprile 2020")
dataset["text"] = dataset["text"].str.replace("maggio 2020", "Maggio 2020")
dataset["text"] = dataset["text"].str.replace("giugno 2020", "Giugno 2020")
dataset["text"] = dataset["text"].str.replace("luglio 2020", "Luglio 2020")
dataset["text"] = dataset["text"].str.replace("agosto 2020", "Agosto 2020")
dataset["text"] = dataset["text"].str.replace("settembre 2020", "Settembre 2020")
dataset["text"] = dataset["text"].str.replace("ottobre 2020", "Ottobre 2020")
dataset["text"] = dataset["text"].str.replace("novembre 2020", "Novembre 2020")
dataset["text"] = dataset["text"].str.replace("dicembre 2020", "Dicembre 2020")


dataset["text"] = dataset["text"].str.replace("Gennaio 2020", "01 2020")
dataset["text"] = dataset["text"].str.replace("Febbraio 2020", "02 2020")
dataset["text"] = dataset["text"].str.replace("Marzo 2020", "03 2020")
dataset["text"] = dataset["text"].str.replace("Aprile 2020", "04 2020")
dataset["text"] = dataset["text"].str.replace("Maggio 2020", "05 2020")
dataset["text"] = dataset["text"].str.replace("Giugno 2020", "06 2020")
dataset["text"] = dataset["text"].str.replace("Luglio 2020", "07 2020")
dataset["text"] = dataset["text"].str.replace("Agosto 2020", "08 2020")
dataset["text"] = dataset["text"].str.replace("Settembre 2020", "09 2020")
dataset["text"] = dataset["text"].str.replace("Ottobre 2020", "10 2020")
dataset["text"] = dataset["text"].str.replace("Novembre 2020", "11 2020")
dataset["text"] = dataset["text"].str.replace("Dicembre 2020", "12 2020")

dataset["text"] = dataset["text"].str.replace("settembre2020", "09 2020")

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


dataset["day"] = dataset["text"].str.split(" 2020 ").str[0]
dataset["day"] = dataset["day"].str.replace(",", "")
dataset["day"] = dataset["day"].str.strip()
dataset["day"] = dataset["day"].str.split(" ").str[0]
dataset["day"]  = dataset["day"].apply(lambda x: add_zero(x))

dataset["date"] = dataset["date"] + "_" + dataset["day"]


dataset['text'] = dataset["text"].str.split(" 2020 ").str[1]
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
dataset['text'] = dataset['text'].str.replace("Messaggio di Dio Padre ore 19:00 ", "")
dataset['text'] = dataset['text'].str.replace("Messaggio di Dio Padre ore 20:40 ", "")
dataset['text'] = dataset['text'].str.replace("Messaggio di Maria Santissima ore 22:30 ", "")
dataset['text'] = dataset['text'].str.replace("Messaggio di Dio Padre ore 19:00 ", "")
dataset['text'] = dataset['text'].str.replace("messaggio di Gesù ore 21:15", "")
dataset['text'] = dataset['text'].str.replace("messaggio di Gesù ore 21:15", "")
dataset['text'] = dataset['text'].str.replace("ore 18:00 ", "")
dataset['text'] = dataset['text'].str.replace("ore 20:15", "")
dataset['text'] = dataset['text'].str.replace("ore 22:15", "")

dataset['text'] = dataset['text'].str.replace("Cenacolo a Rimini", "")
dataset['text'] = dataset['text'].str.replace("Cenacolo a Verona", "")
dataset['text'] = dataset['text'].str.replace("Cenacolo di preghiera a Belluno bl - Centro di Spiritualità e Cultura, Papa Luciani ", "")
dataset['text'] = dataset['text'].str.replace("Cenacolo di preghiera a Perugia", "")
dataset['text'] = dataset['text'].str.replace("Cenacolo di preghiera a Rimini ", "")
dataset['text'] = dataset['text'].str.replace("Cenacolo di preghiera in località Amantea (CS) ", "")
dataset['text'] = dataset['text'].str.replace("Cenacolo di preghiera in località Casoli - Contrada Vicenne (CH)", "")
dataset['text'] = dataset['text'].str.replace("Cenacolo di preghiera in località Pianello (PG)", "")
dataset['text'] = dataset['text'].str.replace("Cenacolo in Montelupo Fiorentino ", "")
dataset['text'] = dataset['text'].str.replace("Fiaccolata", "")
dataset['text'] = dataset['text'].str.replace(" su alla croce blu per la festa  dell' Immacolata", "")
dataset['text'] = dataset['text'].str.replace("\.   Messaggio ricevuto;  ", "")
dataset['text'] = dataset['text'].str.replace("Cenacolo con il gruppo di Verona. ", "")
dataset['text'] = dataset['text'].str.replace("Cenacolo di preghiera in località Caltanissetta. ", "")
dataset['text'] = dataset['text'].str.replace("Cenacolo di preghiera in località Nettuno, Rm  ", "")
dataset['text'] = dataset['text'].str.replace("Cenacolo in località Roma ", "")
dataset['text'] = dataset['text'].str.replace("Chiesa di Santa Maria dell’Assunta ", "")
dataset['text'] = dataset['text'].str.replace("Messaggio di Maria Madre Santissima Corredentrice per la salvezza dell'umanità:", "")
dataset['text'] = dataset['text'].str.replace("Messaggio in privato di Maria Santissima ore 15:40  ", "")
dataset['text'] = dataset['text'].str.replace("Preghiera con il gruppo di Verona alla croce blu. ", "")
dataset['text'] = dataset['text'].str.replace("a Gisella ricevuto in stato di estasi durante la recita del Santo Rosario. ", "")
dataset['text'] = dataset['text'].str.replace("ore 17:45 ", "")
dataset['text'] = dataset['text'].str.replace("ore 17:50 ", "")
dataset['text'] = dataset['text'].str.replace("ore 18:25 ", "")
dataset['text'] = dataset['text'].str.replace("ore 18:45 ", "")
dataset['text'] = dataset['text'].str.replace("ore 22:00", "")
dataset['text'] = dataset['text'].str.replace("ore 23:20 ", "")
dataset['text'] = dataset['text'].str.replace("\[mercoledì Santo\]", ", mercoledì Santo")


dataset['text'] = dataset['text'].str.strip()

dataset['text'] = dataset['text'].str.replace(",", " , ")
dataset['text'] = dataset['text'].str.replace(" , ", ", ")
dataset['text'] = dataset['text'].str.replace(" , ", ", ")
dataset['text'] = dataset['text'].str.replace(" \.  ", ". ")
dataset['text'] = dataset['text'].str.replace("  ", " ")
dataset['text'] = dataset['text'].str.replace("\(Gisella\) Ore 15:30. ", "")
dataset['text'] = dataset['text'].str.replace("  ", " ")
dataset['text'] = dataset['text'].str.replace(". Cari fratelli, ", "Cari fratelli, ")



dataset["date"] = dataset["date"].str.split("_")

dataset["date"] = dataset["date"].str[2] + "_" + dataset["date"].str[1] + "_" + dataset["date"].str[0]
dataset = dataset.drop("day", axis=1)

dataset["text"] = dataset["text"].str.strip()


dataset['text'] = dataset['text'].str.replace(", Figlia mia amata", "Figlia mia amata")
dataset['text'] = dataset['text'].str.replace(". Cari figli,", "Cari figli,")




translator = google_translator()  


dataset["text_en"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='en'))


dataset = dataset[dataset["text_en"] != "male"]

dataset = dataset[~dataset["text"].isnull()]
dataset = dataset[dataset["text_en"] != ""]



dataset.to_csv("2020_05_cleaned.csv", index=False, encoding="utf-8")








