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


dataset = pd.read_csv("2016.csv", encoding="utf-8")

dataset["text"] = dataset["text"].str.strip()
dataset["text"] = dataset["text"].str.replace("\n", " ")
dataset["text"] = dataset["text"].str.split("Pubblicato da").str[0]
dataset["text"] = dataset["text"].str.replace("Trevignano romano", "Trevignano Romano")
dataset["text"] = dataset["text"].str.replace("\. ", ".")
dataset["text"] = dataset["text"].str.replace("\.", ". ")
dataset = dataset[dataset["text"].str.contains("Trevignano Romano")]
dataset["text"] = dataset["text"].str.replace("\xa0", "")
dataset["text"] = dataset["text"].str.replace("2016", "2016 ")
dataset["text"] = dataset["text"].str.replace("2016  ", "2016 ")


# Replace Months
dataset["text"] = dataset["text"].str.replace("gennaio 2016", "Gennaio 2016")
dataset["text"] = dataset["text"].str.replace("febbraio 2016", "Febbraio 2016")
dataset["text"] = dataset["text"].str.replace("marzo 2016", "Marzo 2016")
dataset["text"] = dataset["text"].str.replace("aprile 2016", "Aprile 2016")
dataset["text"] = dataset["text"].str.replace("maggio 2016", "Maggio 2016")
dataset["text"] = dataset["text"].str.replace("giugno 2016", "Giugno 2016")
dataset["text"] = dataset["text"].str.replace("luglio 2016", "Luglio 2016")
dataset["text"] = dataset["text"].str.replace("agosto 2016", "Agosto 2016")
dataset["text"] = dataset["text"].str.replace("settembre 2016", "Settembre 2016")
dataset["text"] = dataset["text"].str.replace("ottobre 2016", "Ottobre 2016")
dataset["text"] = dataset["text"].str.replace("novembre 2016", "Novembre 2016")
dataset["text"] = dataset["text"].str.replace("dicembre 2016", "Dicembre 2016")


dataset["text"] = dataset["text"].str.replace("Gennaio 2016", "01 2016")
dataset["text"] = dataset["text"].str.replace("Febbraio 2016", "02 2016")
dataset["text"] = dataset["text"].str.replace("Marzo 2016", "03 2016")
dataset["text"] = dataset["text"].str.replace("Aprile 2016", "04 2016")
dataset["text"] = dataset["text"].str.replace("Maggio 2016", "05 2016")
dataset["text"] = dataset["text"].str.replace("Giugno 2016", "06 2016")
dataset["text"] = dataset["text"].str.replace("Luglio 2016", "07 2016")
dataset["text"] = dataset["text"].str.replace("Agosto 2016", "08 2016")
dataset["text"] = dataset["text"].str.replace("Settembre 2016", "09 2016")
dataset["text"] = dataset["text"].str.replace("Ottobre 2016", "10 2016")
dataset["text"] = dataset["text"].str.replace("Novembre 2016", "11 2016")
dataset["text"] = dataset["text"].str.replace("Dicembre 2016", "12 2016")

dataset["text"] = dataset["text"].str.replace("settembre2016", "09 2016")

dataset["text"] = dataset["text"].str.split("Trevignano Romano")

dataset["text"] = dataset["text"].apply(lambda x: list_cleaner(x))
dataset["text"] = dataset["text"].apply(lambda x: title_remover(x))



text_column = dataset.apply(lambda x: pd.Series(x['text']), axis=1).stack().reset_index(level=1, drop=True)
text_column.name = 'text'
dataset = dataset.drop('text', axis=1).join(text_column)
dataset['text'] = pd.Series(dataset['text'], dtype=object)

dataset["author"] = np.where(dataset["text"].str.contains("Messaggio di Gesù"), "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["text"].str.contains("Messaggio di Gesu"), "Jesus Christ", dataset["author"])



dataset["day"] = dataset["text"].str.split(" 2016 ").str[0]
dataset["day"] = dataset["day"].str.replace(",", "")
dataset["day"] = dataset["day"].str.strip()
dataset["day"] = dataset["day"].str.split(" ").str[0]
dataset["day"]  = dataset["day"].apply(lambda x: add_zero(x))

dataset["date"] = dataset["date"] + "_" + dataset["day"]


dataset['text'] = dataset["text"].str.split(" 2016 ").str[1]
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
dataset['text'] = dataset['text'].str.strip()

dataset['text'] = dataset['text'].str.replace(",", " , ")
dataset['text'] = dataset['text'].str.replace(" , ", ", ")
dataset['text'] = dataset['text'].str.replace(" , ", ", ")
dataset['text'] = dataset['text'].str.replace(" \.  ", ". ")
dataset['text'] = dataset['text'].str.replace("  ", " ")
dataset['text'] = dataset['text'].str.replace("\(Gisella\) Ore 15:30. ", "")
dataset['text'] = dataset['text'].str.replace("  ", " ")
dataset['text'] = dataset['text'].str.replace("Recita del Santo Rosario presso la cappella del Sacro Cuore a cura del Parroco Don Gabriele ", " ")
dataset['text'] = dataset['text'].str.replace("Prima recita del Santo Rosario presso la Cappella del Sacro Cuore a cura del Vescovo Romano Rossi ", " ")


dataset["date"] = dataset["date"].str.split("_")

dataset["date"] = dataset["date"].str[2] + "_" + dataset["date"].str[1] + "_" + dataset["date"].str[0]
dataset = dataset.drop("day", axis=1)

dataset['text'] = dataset['text'].str.strip()

dataset['text'] = dataset['text'].str.replace(" \.  ", ". ")


dataset["text"] = dataset["text"].str.replace("Poi aggiunge: …Dopo", "Poi aggiunge: Dopo")
dataset["text"] = dataset["text"].str.replace("a casa di amici \. ", "a casa di amici. ")
dataset["text"] = dataset["text"].str.replace(" Caltanissetta \(CT\), 20 08", "")
dataset["text"] = dataset["text"].str.replace(" Caltanissetta, 19 10", "")




dataset["author"] = np.where(dataset["date"] == "11_10_2016", "Jesus Christ", dataset["author"])


translator = google_translator()  


dataset["text_en"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='en'))
dataset["text_pl"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='pl'))







# SPELLING FIX

dataset["text_pl"] = dataset["text_pl"].str.replace("Medytować!", "Medytuj!")
dataset["text_pl"] = dataset["text_pl"].str.replace("jestem bardzo szczęśliwy", "jestem bardzo szczęśliwa")
dataset["text_pl"] = dataset["text_pl"].str.replace("że kilkakrotnie się włączyło", "że kilkakrotnie zamigotało")
dataset["text_pl"] = dataset["text_pl"].str.replace("Jestem bardzo szczęśliwy", "Jestem bardzo szczęśliwa")
dataset["text_pl"] = dataset["text_pl"].str.replace("Biorę cię za rękę, ale ciągle popełniam błędy, nie daj się zaskoczyć pułapkom. ", "Biorę cię za rękę, ale popełniaj błędy, nie zrażaj się upadkami. ")
dataset["text_pl"] = dataset["text_pl"].str.replace("aby wdmuchnąć w ich serca", "tchnąwszy w ich serca")
dataset["text_pl"] = dataset["text_pl"].str.replace("wzniosłem jej oczy ku niebu", "wznosząc swe oczy ku niebu")
dataset["text_pl"] = dataset["text_pl"].str.replace("kocham cię jak matkę", "kocham cię jak matka")
dataset["text_pl"] = dataset["text_pl"].str.replace("kościół", "Kościół")
dataset["text_pl"] = dataset["text_pl"].str.replace("kościoła", "Kościoła")
dataset["text_pl"] = dataset["text_pl"].str.replace("biorę cię za rękę Pamiętaj", "biorę cię za rękę. Pamiętaj")
dataset["text_pl"] = dataset["text_pl"].str.replace("zazdrość, zazdrość i pycha to uczucia", "zazdrość, zawiść i pycha to uczucia")
dataset["text_pl"] = dataset["text_pl"].str.replace("nie są one od Boga Uwielbiane dzieci", "nie są one od Boga. Uwielbiane dzieci")
dataset["text_pl"] = dataset["text_pl"].str.replace("on zawsze wpada w zasadzkę", "on zawsze czycha")

# MARY FORM

dataset_mary = dataset[dataset["author"] == "Holy Mary" ]
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("łem", "łam")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Tchnąłam", "Tchnęłam")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("złam", "złem")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Kościołam", "Kościołem")


dataset_jesus = dataset[dataset["author"] != "Holy Mary" ]

dataset= pd.concat([dataset_mary, dataset_jesus])







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



dataset = dataset[["year", "month", "day", "author", "text", "text_en", "text_pl", "month_string"]]


dataset.to_csv("2016_cleaned.csv", index=False, encoding="utf-8")


dataset.to_json("trevignano_2016.json",orient="records")





