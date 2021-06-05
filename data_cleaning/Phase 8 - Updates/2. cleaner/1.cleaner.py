# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""




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


dataset = pd.read_csv("may.csv", encoding="utf-8")

dataset["text"] = dataset["text"].str.strip()
dataset["text"] = dataset["text"].str.replace("\n", " ")
dataset["text"] = dataset["text"].str.split("Pubblicato da").str[0]
dataset["text"] = dataset["text"].str.replace("Trevignano romano", "Trevignano Romano")
dataset["text"] = dataset["text"].str.replace("\. ", ".")
dataset["text"] = dataset["text"].str.replace("\.", ". ")
dataset = dataset[dataset["text"].str.contains("Trevignano Romano")]
dataset["text"] = dataset["text"].str.replace("\xa0", "")
dataset["text"] = dataset["text"].str.replace("2021", "2021 ")
dataset["text"] = dataset["text"].str.replace("2021  ", "2021 ")
dataset["text"] = dataset["text"].str.replace("\(rm\)", "")
dataset['text'] = dataset['text'].str.replace("- ore 20:20 ", "")
dataset['text'] = dataset['text'].str.replace("1°", "")
dataset['text'] = dataset['text'].str.replace("- 20:20 ", "")
dataset['text'] = dataset['text'].str.replace("16:42 ", "")
dataset['text'] = dataset['text'].str.replace("ore 16:42", "")
dataset['text'] = dataset['text'].str.replace("delle ore 23:05 ", "")
dataset['text'] = dataset['text'].str.replace("​ Amati", "Amati")


# Replace Months
dataset["text"] = dataset["text"].str.replace("gennaio 2021", "Gennaio 2021")
dataset["text"] = dataset["text"].str.replace("febbraio 2021", "Febbraio 2021")
dataset["text"] = dataset["text"].str.replace("marzo 2021", "Marzo 2021")
dataset["text"] = dataset["text"].str.replace("aprile 2021", "Aprile 2021")
dataset["text"] = dataset["text"].str.replace("maggio 2021", "Maggio 2021")
dataset["text"] = dataset["text"].str.replace("giugno 2021", "Giugno 2021")
dataset["text"] = dataset["text"].str.replace("luglio 2021", "Luglio 2021")
dataset["text"] = dataset["text"].str.replace("agosto 2021", "Agosto 2021")
dataset["text"] = dataset["text"].str.replace("settembre 2021", "Settembre 2021")
dataset["text"] = dataset["text"].str.replace("ottobre 2021", "Ottobre 2021")
dataset["text"] = dataset["text"].str.replace("novembre 2021", "Novembre 2021")
dataset["text"] = dataset["text"].str.replace("dicembre 2021", "Dicembre 2021")


dataset["text"] = dataset["text"].str.replace("Gennaio 2021", "01 2021")
dataset["text"] = dataset["text"].str.replace("Febbraio 2021", "02 2021")
dataset["text"] = dataset["text"].str.replace("Marzo 2021", "03 2021")
dataset["text"] = dataset["text"].str.replace("Aprile 2021", "04 2021")
dataset["text"] = dataset["text"].str.replace("Maggio 2021", "05 2021")
dataset["text"] = dataset["text"].str.replace("Giugno 2021", "06 2021")
dataset["text"] = dataset["text"].str.replace("Luglio 2021", "07 2021")
dataset["text"] = dataset["text"].str.replace("Agosto 2021", "08 2021")
dataset["text"] = dataset["text"].str.replace("Settembre 2021", "09 2021")
dataset["text"] = dataset["text"].str.replace("Ottobre 2021", "10 2021")
dataset["text"] = dataset["text"].str.replace("Novembre 2021", "11 2021")
dataset["text"] = dataset["text"].str.replace("Dicembre 2021", "12 2021")

dataset["text"] = dataset["text"].str.replace("settembre2021", "09 2021")

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


dataset["day"] = dataset["text"].str.split(" 2021 ").str[0]
dataset["day"] = dataset["day"].str.replace(",", "")
dataset["day"] = dataset["day"].str.strip()
dataset["day"] = dataset["day"].str.split(" ").str[0]
dataset["day"]  = dataset["day"].apply(lambda x: add_zero(x))

dataset["date"] = dataset["date"] + "_" + dataset["day"]


dataset['text'] = dataset["text"].str.split(" 2021 ").str[1]
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
dataset['text'] = dataset['text'].str.replace("Messaggio di Dio Padre \(durante l'estasi\): ore 00:21 ", "")

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




dataset["year"] = dataset["date"].str.split("_").str[-1]
dataset["month"] = dataset["date"].str.split("_").str[1]
dataset["day"] = dataset["date"].str.split("_").str[0]

dataset["month_string"]  = dataset["month"]

dataset["month_string"] = dataset["month_string"].str.replace("01", "January")
dataset["month_string"] = dataset["month_string"].str.replace("02", "February")
dataset["month_string"] = dataset["month_string"].str.replace("03", "March")
dataset["month_string"] = dataset["month_string"].str.replace("04", "April")
dataset["month_string"] = dataset["month_string"].str.replace("05", "May")
dataset["month_string"] = dataset["month_string"].str.replace("06", "June")
dataset["month_string"] = dataset["month_string"].str.replace("07", "July")
dataset["month_string"] = dataset["month_string"].str.replace("08", "August")
dataset["month_string"] = dataset["month_string"].str.replace("09", "September")
dataset["month_string"] = dataset["month_string"].str.replace("10", "October")
dataset["month_string"] = dataset["month_string"].str.replace("11", "November")
dataset["month_string"] = dataset["month_string"].str.replace("12", "December")

dataset = dataset.sort_values(by=["year", "month", "day"])

dataset = dataset[["year", "month", "day", "author", "text", "month_string"]]


dataset["text"] = dataset["text"].str.replace("Amen \.", "Amen.")

dataset = dataset.rename(columns={"text": "text_it"})




dataset.to_csv("may_cleaned.csv", index=False, encoding="utf-8")







