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


dataset = pd.read_csv("2019.csv", encoding="utf-8")

dataset["text"] = dataset["text"].str.strip()
dataset["text"] = dataset["text"].str.replace("\n", " ")
dataset["text"] = dataset["text"].str.split("Pubblicato da").str[0]
dataset["text"] = dataset["text"].str.replace("Trevignano romano", "Trevignano Romano")
dataset["text"] = dataset["text"].str.replace("\. ", ".")
dataset["text"] = dataset["text"].str.replace("\.", ". ")
dataset = dataset[dataset["text"].str.contains("Trevignano Romano")]
dataset["text"] = dataset["text"].str.replace("\xa0", "")
dataset["text"] = dataset["text"].str.replace("2019", "2019 ")
dataset["text"] = dataset["text"].str.replace("2019  ", "2019 ")
dataset["text"] = dataset["text"].str.replace("\(rm\)", "")
dataset['text'] = dataset['text'].str.replace("- ore 20:20 ", "")
dataset['text'] = dataset['text'].str.replace("1°", "")
dataset['text'] = dataset['text'].str.replace("- 20:20 ", "")
dataset['text'] = dataset['text'].str.replace("16:42 ", "")
dataset['text'] = dataset['text'].str.replace("ore 16:42", "")
dataset['text'] = dataset['text'].str.replace("delle ore 23:05 ", "")
dataset['text'] = dataset['text'].str.replace("​ Amati", "Amati")


# Replace Months
dataset["text"] = dataset["text"].str.replace("gennaio 2019", "Gennaio 2019")
dataset["text"] = dataset["text"].str.replace("febbraio 2019", "Febbraio 2019")
dataset["text"] = dataset["text"].str.replace("marzo 2019", "Marzo 2019")
dataset["text"] = dataset["text"].str.replace("aprile 2019", "Aprile 2019")
dataset["text"] = dataset["text"].str.replace("maggio 2019", "Maggio 2019")
dataset["text"] = dataset["text"].str.replace("giugno 2019", "Giugno 2019")
dataset["text"] = dataset["text"].str.replace("luglio 2019", "Luglio 2019")
dataset["text"] = dataset["text"].str.replace("agosto 2019", "Agosto 2019")
dataset["text"] = dataset["text"].str.replace("settembre 2019", "Settembre 2019")
dataset["text"] = dataset["text"].str.replace("ottobre 2019", "Ottobre 2019")
dataset["text"] = dataset["text"].str.replace("novembre 2019", "Novembre 2019")
dataset["text"] = dataset["text"].str.replace("dicembre 2019", "Dicembre 2019")


dataset["text"] = dataset["text"].str.replace("Gennaio 2019", "01 2019")
dataset["text"] = dataset["text"].str.replace("Febbraio 2019", "02 2019")
dataset["text"] = dataset["text"].str.replace("Marzo 2019", "03 2019")
dataset["text"] = dataset["text"].str.replace("Aprile 2019", "04 2019")
dataset["text"] = dataset["text"].str.replace("Maggio 2019", "05 2019")
dataset["text"] = dataset["text"].str.replace("Giugno 2019", "06 2019")
dataset["text"] = dataset["text"].str.replace("Luglio 2019", "07 2019")
dataset["text"] = dataset["text"].str.replace("Agosto 2019", "08 2019")
dataset["text"] = dataset["text"].str.replace("Settembre 2019", "09 2019")
dataset["text"] = dataset["text"].str.replace("Ottobre 2019", "10 2019")
dataset["text"] = dataset["text"].str.replace("Novembre 2019", "11 2019")
dataset["text"] = dataset["text"].str.replace("Dicembre 2019", "12 2019")

dataset["text"] = dataset["text"].str.replace("settembre2019", "09 2019")

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


dataset["day"] = dataset["text"].str.split(" 2019 ").str[0]
dataset["day"] = dataset["day"].str.replace(",", "")
dataset["day"] = dataset["day"].str.strip()
dataset["day"] = dataset["day"].str.split(" ").str[0]
dataset["day"]  = dataset["day"].apply(lambda x: add_zero(x))

dataset["date"] = dataset["date"] + "_" + dataset["day"]


dataset['text'] = dataset["text"].str.split(" 2019 ").str[1]
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
dataset['text'] = dataset['text'].str.replace("Cenacolo di preghiera in località Amantea \(CS\) ", "")
dataset['text'] = dataset['text'].str.replace("Cenacolo di preghiera in località Casoli - Contrada Vicenne \(CH\)", "")
dataset['text'] = dataset['text'].str.replace("Cenacolo di preghiera in località Pianello \(PG\)", "")
dataset['text'] = dataset['text'].str.replace("Cenacolo in Montelupo Fiorentino ", "")
dataset['text'] = dataset['text'].str.replace("Fiaccolata", "")
dataset['text'] = dataset['text'].str.replace(" su alla croce blu per la festa  dell' Immacolata", "")
dataset['text'] = dataset['text'].str.replace("\.   Messaggio ricevuto;  ", "")


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





# ITALIAN FIX

dataset["text"] = dataset["text"].str.replace("Poi aggiunge: …Dopo", "Poi aggiunge: Dopo")
dataset["text"] = dataset["text"].str.replace(", amen. Madonna di ", ", Amen.")
dataset["text"] = dataset["text"].str.replace("amen", "Amen")

# JESUS AUTHOR
dataset["author"] = np.where(dataset["date"] == "19_03_2019", "Jesus Christ", dataset["author"])



translator = google_translator()  


dataset["text_en"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='en'))
dataset["text_pl"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='pl'))


# SPELLING FIX

dataset["text_pl"] = dataset["text_pl"].str.replace("niedługo przyjadę", "niebawem przybędę")
dataset["text_pl"] = dataset["text_pl"].str.replace("ponieważ aniołów", "ponieważ aniołowie")
dataset["text_pl"] = dataset["text_pl"].str.replace("\. \.", ".")
dataset["text_pl"] = dataset["text_pl"].str.replace("tak jak bym mógł, gdybym nie był dobrym i miłosiernym Ojcem", "jakżebym  mógł na to pozwolić, gdybym nie był dobrym i miłosiernym Ojcem")
dataset["text_pl"] = dataset["text_pl"].str.replace(" jest darem cudowna łaska", " jest darem cudownej łaski")
dataset["text_pl"] = dataset["text_pl"].str.replace("waszego brata Jezu", "wasz brat Jezus")
dataset["text_pl"] = dataset["text_pl"].str.replace("was swoim Tak", "waszym Tak")
dataset["text_pl"] = dataset["text_pl"].str.replace("powrócą nowe choroby", "przyjdą nowe choroby")
dataset["text_pl"] = dataset["text_pl"].str.replace("istnieć\.", "istnieć")
dataset["text_pl"] = dataset["text_pl"].str.replace("ponieważ został zaatakowany przez szatana", "ponieważ został on zaatakowany przez szatana")
dataset["text_pl"] = dataset["text_pl"].str.replace("wybierz wygodniejszą", "wybierasz wygodniejszą")
dataset["text_pl"] = dataset["text_pl"].str.replace("a potem umrzyj na zawsze", "a potem umrzesz na zawsze")
dataset["text_pl"] = dataset["text_pl"].str.replace(" i w Duchu Świętym", " i w Ducha Świętego")
dataset["text_pl"] = dataset["text_pl"].str.replace("razem z tymi, którzy czczą szatana", "po tych, którzy czczą szatana")
dataset["text_pl"] = dataset["text_pl"].str.replace("modlą się na błogosławionych glebach", "modlą się w błogosławionych miejscach")
dataset["text_pl"] = dataset["text_pl"].str.replace("a Duch Święty zleje się na was", "a Duch Święty wleje się w was")
dataset["text_pl"] = dataset["text_pl"].str.replace("demony wybierają słabe dusze w pierścionek zaręczynowy", "demony wybierają dusze o słabej wierze")
dataset["text_pl"] = dataset["text_pl"].str.replace("iz miłością", "i z miłością")
dataset["text_pl"] = dataset["text_pl"].str.replace("Mój Ojcze, posłał moją Najświętszą Matkę", "Mój Ojciec posłał moją Najświętszą Matkę")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ja, Ojcze Wszechmogący, ale nie widzę wojen! Dlaczego nie rozumiesz", "Ja, Ojcze Wszechmogący, dlaczego nie widzicie wojen! Dlaczego nie rozumiesz?")
dataset["text_pl"] = dataset["text_pl"].str.replace("Nie ma potrzeby przeprowadzki i przeprowadzki", "Nie ma potrzeby opuszczenia domu i przeniesienia się")
dataset["text_pl"] = dataset["text_pl"].str.replace(", Moi aniołowie", " Moi aniołowie")
dataset["text_pl"] = dataset["text_pl"].str.replace("Bóg wymiotuje letnich", "Bóg wypluwa letnich")
dataset["text_pl"] = dataset["text_pl"].str.replace("was iz matczyną", "was i z matczyną")
dataset["text_pl"] = dataset["text_pl"].str.replace("nie wpadajcie w pułapkę szatan", "nie wpadajcie w pułapkę szatana")
dataset["text_pl"] = dataset["text_pl"].str.replace("zazdrości i zazdrości", "zazdrości i zawiści")
dataset["text_pl"] = dataset["text_pl"].str.replace("że On jest też dobrze", "że On jest też sprawiedliwy")
dataset["text_pl"] = dataset["text_pl"].str.replace("a moje ukochane dzieci nie odrywają włosów", "a moim ukochanym dzieciom włos z głowy nie spadnie.")
dataset["text_pl"] = dataset["text_pl"].str.replace("Opróżniłem cię ze wszystkiego, ze wszystkiego, co było materialne", "Usunąłem z ciebie wszystko, co było materialne")
dataset["text_pl"] = dataset["text_pl"].str.replace("ile będzie moich prezentów każdego dnia", "ile będzie moich darów każdego dnia")
dataset["text_pl"] = dataset["text_pl"].str.replace("byłem człowiekiem jak Ty, ale też , tak jak ty, stajesz się", "byłem człowiekiem jak Ty, ale także uduchowionym , podobnie jak ty teraz stajesz się")
dataset["text_pl"] = dataset["text_pl"].str.replace("Pokorę polecam mi dzieci", "Pokorę polecam wam dzieci")


dataset["text_en"] = dataset["text_en"].str.replace("perfume", "scent")
dataset["text_en"] = dataset["text_en"].str.replace("as I could have", "how could I allow this")
dataset["text_en"] = dataset["text_en"].str.replace("you\. \.", "you.")
dataset["text_en"] = dataset["text_en"].str.replace("demons choose weak souls in the wedding ring", "demons choose souls weak in faith")

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
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("przepowiedziałem", "przepowiedziałam")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Będziesz uwielbiony", "Będziesz uwielbiona")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("przyszedłem", "przyszłam")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("który przychodzę z łaski", "która przychodzę z łaski")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("które nosicie, dzisiaj dzieci zstąpią wiele łask", "które nosicie. Dzisiaj dzieci zstąpią wiele łask")


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



dataset.to_csv("2019_cleaned.csv", index=False, encoding="utf-8")
dataset.to_json("trevignano_2019.json",orient="records")









