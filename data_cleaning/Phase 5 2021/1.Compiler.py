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

dataset_1 = pd.read_csv("2021.csv", encoding="utf-8")
dataset_2 = pd.read_csv("2021_2.csv", encoding="utf-8")

dataset = pd.concat([dataset_1, dataset_2])

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




translator = google_translator()  


dataset["text_en"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='en'))
dataset["text_pl"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='pl'))

# SPELLING FIX

dataset["text_pl"] = dataset["text_pl"].str.replace("bądź mi posłuszny jako Bóg pokoju", "bądź mi posłuszny jako Bógo pokoju")
dataset["text_pl"] = dataset["text_pl"].str.replace("zamiast tego otworzę wasze serca i będę tam", "więc zamiast tego otwórzcie wasze serca i ja tam będę")
dataset["text_pl"] = dataset["text_pl"].str.replace("których cię ", "których was ")
dataset["text_pl"] = dataset["text_pl"].str.replace("siebie razem i zjednoczeni", "siebie razem i będąc zjednoczonymi")
dataset["text_pl"] = dataset["text_pl"].str.replace("krótce mój Jezus cię zabierze i zabierze do nowego świata", "krótce mój Jezus cię zabierze do nowego świata")
dataset["text_pl"] = dataset["text_pl"].str.replace("Jak myślisz, że tylko na tym świecie musisz robić", "Myślisz, że tylko tym  światem trzeba się zajmować")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ale mój świat jest również pełen zobowiązań", "Mój świat także jest pełen zobowiązań")
dataset["text_pl"] = dataset["text_pl"].str.replace("a wy stworzyliście sobie boga", "a wy uczyniliście z siebie boga")
dataset["text_pl"] = dataset["text_pl"].str.replace("Odmawiajcie jego różaniec o swoje zbawienie; czasem potrzebne są też proste słowa, co doceniam", "Odmawiajcie jej różaniec dla swojego zbawienia; czasem potrzebne są też proste słowa, co doceniam")
dataset["text_pl"] = dataset["text_pl"].str.replace("Moje najsłodsze dzieci, zróbcie arkę, tak jak prosiłam Noego, ale prosiłam o to, aby mógł przyprowadzić do mnie wszystkie swoje dzieci, nie tracąc ani jednego.", "Moje najsłodsze dzieci, zróbcie arkę, tak jak prosiłem Noego. Jednak prosiłem go o to, aby mógł przyprowadzić do mnie wszystkie swoje dzieci, nie tracąc ani jednego.")
dataset["text_pl"] = dataset["text_pl"].str.replace("Do was, moje dzieci, nie proszę was,", "Was, moje dzieci, nie proszę ")
dataset["text_pl"] = dataset["text_pl"].str.replace("jak bardzo jesteś umiłowany w moich oczach", "jak bardzo jesteś umiłowana w moich oczach")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ojcze, Synu i Duchu Świętym", "Ojca, Syna i Ducha Świętego")
dataset["text_pl"] = dataset["text_pl"].str.replace("Amen Na koniec", "Amen. Na koniec")
dataset["text_pl"] = dataset["text_pl"].str.replace(" i nim przeżyli", " i w nim żyli")
dataset["text_pl"] = dataset["text_pl"].str.replace("pokoju iw radości", "pokoju i w radości")

# MARY FORM

dataset_mary = dataset[dataset["author"] == "Holy Mary" ]
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("łem", "łam")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Tchnąłam", "Tchnęłam")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("złam", "złem")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Kościołam", "Kościołem")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("jestem obecny", "jestem obecna")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Jestem zasmucony niepowodzeniem", "Jestem zasmucona niepowodzeniem")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("będę was chronił", "będę was chroniła")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Dzieci, bądźcie głupi i głuchy, zwłaszcza gdy macie wyzwanie", "Dzieci, bądźcie głupie i głuche, zwłaszcza gdy was wyzywają")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("posłany przez Mojego Ojca", "posłana przez Mojego Ojca")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Niebo istnieje, ale także do diabła", "Niebo istnieje, ale także diabeł")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("chciałbym", "chciałabym")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("dotknąłem", "dotknęłam")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("oczekiwał", "oczekiwała")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("przepowiedziałem", "przepowiedziałam")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Będziesz uwielbiony", "Będziesz uwielbiona")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("przyszedłem tu nie po", "przyszłam tu nie po")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Zawsze będę cię chronił", "Zawsze będę cię chroniła")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Moja umiłowana apostazja weszła do Kościoła jak nigdy dotąd", "Moja umiłowana, apostazja weszła do Kościoła jak nigdy dotąd")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Cena będzie trochę droga", "Cena będzie bardzo wysoka")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Dzieci, dzisiaj zostanę koronowany przed wami i przed światem, Królowo, po raz kolejny", "Dzieci, dzisiaj zostanę koronowana przed wami i przed światem, zostanę Królową, po raz kolejny")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Pieszczę cię jeden po drugim", "Przytulam was wszystkich")

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

dataset["text_pl"] = dataset["text_pl"].str.replace("Amen \.", "Amen.")
dataset["text_en"] = dataset["text_en"].str.replace("Amen \.", "Amen.")
dataset["text"] = dataset["text"].str.replace("Amen \.", "Amen.")






dataset.to_csv("trevignano_2021.csv", index=False, encoding="utf-8")







