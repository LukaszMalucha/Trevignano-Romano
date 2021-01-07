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
dataset = pd.read_csv("2018.csv", encoding="utf-8")
dataset["text"] = dataset["text"].str.strip()
dataset["text"] = dataset["text"].str.replace("\n", " ")
 
dataset["text"] = dataset["text"].str.split("Pubblicato da").str[-2]
dataset["text"] = dataset["text"].str.split("Pinterest").str[-1]

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
dataset['text'] = dataset['text'].str.strip()

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


dataset["day"] = dataset["text"].str.split("2018").str[0]
dataset["day"] = dataset["day"].str.replace(",", "")
dataset["day"] = dataset["day"].str.strip()
dataset["day"] = dataset["day"].str.split(" ").str[0]
dataset["day"]  = dataset["day"].apply(lambda x: add_zero(x))

dataset["date"] = dataset["date"] + "_" + dataset["day"]


dataset['text'] = dataset["text"].str.split("2018").str[1]
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

dataset['text'] = dataset['text'].str.split("<!--").str[0]

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



# ITALIAN FIX

dataset["text"] = dataset["text"].str.replace("Poi aggiunge: …Dopo", "Poi aggiunge: Dopo")
dataset["text"] = dataset["text"].str.replace("\……", "...")
dataset["text"] = dataset["text"].str.replace(" Spirito Santo. Amen Alle", " Spirito Santo\. Amen Alle")
dataset["text"] = dataset["text"].str.replace("messaggio di Gesù Fratelli", "messaggio di Gesù: Fratelli")
dataset["text"] = dataset["text"].str.replace("Trevignano Romano 24 02", "")
dataset["text"] = dataset["text"].str.replace("Trevignano Romano 17 03", "")
dataset["text"] = dataset["text"].str.replace(" Continua a leggere\. \. \. \»", "")
dataset["text"] = dataset["text"].str.replace("Marina di Grosseto 10 06", "")
dataset["text"] = dataset["text"].str.replace("Amen\. \" ", "Amen.")
dataset["text"] = dataset["text"].str.replace("Trevignano Romano 4 12" , "")

# JESUS AUTHOR
dataset["author"] = np.where(dataset["date"] == "04_01_2018", "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["date"] == "30_06_2018", "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["date"] == "04_08_2018", "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["date"] == "28_08_2018", "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["date"] == "22_09_2018", "Jesus Christ", dataset["author"])


translator = google_translator()  


dataset["text_en"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='en'))
dataset["text_pl"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='pl'))


# SPELLING FIX

dataset["text_pl"] = dataset["text_pl"].str.replace("niedługo przyjadę", "niebawem przybędę")
dataset["text_pl"] = dataset["text_pl"].str.replace("Dzieci, dajcie sobie pokój między sobą", "Dzieci, zawrzyjcie pokój między sobą")
dataset["text_pl"] = dataset["text_pl"].str.replace("wszyscy mają wiarę", "wszyscy miejcie wiarę")
dataset["text_pl"] = dataset["text_pl"].str.replace("nie opuszczajcie siebie drugi", "nie opuszczajcie siebie nawzajem")
dataset["text_pl"] = dataset["text_pl"].str.replace(" chcę cię tylko kochać, moje wołanie nie ustanie tutaj, pójdę dalej zakochany, kochać się nawzajem tak jak cię kocham", " chcę was tylko kochać,  moje wołanie nie ustanie tutaj, w miłości podążę dalej, miłujcie się nawzajem tak jak umiłowałem was")
dataset["text_pl"] = dataset["text_pl"].str.replace("to wydarzenie będzie oczekiwane ", "to wydarzenie będzie poprzedzone ")
dataset["text_pl"] = dataset["text_pl"].str.replace("ponieważ będziecie smakować Niebo", "ponieważ skosztujecie Nieba")
dataset["text_pl"] = dataset["text_pl"].str.replace("dlatego błagam was o przebaczenie Boga", "dlatego błagam was byście prosili o przebaczenie Boga")
dataset["text_pl"] = dataset["text_pl"].str.replace("zstąpi na was\. \.", "zstąpi na was. .")
dataset["text_pl"] = dataset["text_pl"].str.replace("zazdrość i zazdrość", "zazdrość i zawiść")
dataset["text_pl"] = dataset["text_pl"].str.replace("poczujecie moje perfumy", "poczujecie mój zapach")
dataset["text_pl"] = dataset["text_pl"].str.replace("Pokój i Pokój ", "Pokój i Spokój ")
dataset["text_pl"] = dataset["text_pl"].str.replace("ponieważ wraz z Tabernakulum wszystko spada", "ponieważ wszystko się jednoczy w Tabernakulum")
dataset["text_pl"] = dataset["text_pl"].str.replace("po prostu ukrzyżuj Jezusa", "przestań krzyżować Jezusa")
dataset["text_pl"] = dataset["text_pl"].str.replace("transsubstancjację", "transfigurację")
dataset["text_pl"] = dataset["text_pl"].str.replace("Piotra wkrótce zostanie zniszczona", "Stolica Piotrowa wkrótce zostanie zniszczona")
dataset["text_pl"] = dataset["text_pl"].str.replace("Droga córko moich poświęconych mężczyzn i kobiet", "Droga córko, orzestrzeż moich poświęconych mężczyzn i kobiet")
dataset["text_pl"] = dataset["text_pl"].str.replace("ile wiary znajdzie ?", "ile wiary znajdzie?")
dataset["text_pl"] = dataset["text_pl"].str.replace("pasterze nie pozostają zakotwiczeni w posłuszeństwie, ale walczą z tymi, którzy chcą dodać miłość do szatana, nie angażuj się w masonerię, ale służą duszom wiernych", "pasterze nie pozostają zakotwiczeni w posłuszeństwie, ale walczą z tymi, którzy kochają szatana, nie angażują się w masonerię, ale służą duszom wiernych")
dataset["text_pl"] = dataset["text_pl"].str.replace("\”BĄDŹ ŚWIADKAMI ", "")
dataset["text_pl"] = dataset["text_pl"].str.replace("Mój maluch", "Moje maleństwo")
dataset["text_pl"] = dataset["text_pl"].str.replace("bo wkrótce zainwestuje coś wielkiego ten naród mi drogi", "bo wkrótce coś wielkiego uderzy ten drogi mi naród")
dataset["text_pl"] = dataset["text_pl"].str.replace("ponieważ poznałeś tylko miłość i miłosierdzie Boga, ale masz nadzieję, że nigdy nie widzę jego sprawiedliwości", "ponieważ poznaliście tylko miłość i miłosierdzie Boga, i miejcie nadzieję, że nigdy nie ujrzycie jego sprawiedliwości")
dataset["text_pl"] = dataset["text_pl"].str.replace("Teraz błogosławię wam, chory prezent i święte przedmioty", "Teraz błogosławię was, chorych i święte przedmioty")
dataset["text_pl"] = dataset["text_pl"].str.replace("drodzy moi maluchy", "moje drogie maleństwa")
dataset["text_pl"] = dataset["text_pl"].str.replace("unikajcie pychy i pychy", "unikajcie pychy i wyniosłości")
dataset["text_pl"] = dataset["text_pl"].str.replace("próbują obalić dogmaty należą do mnie", "próbują obalić należące do mnie dogmaty")
dataset["text_pl"] = dataset["text_pl"].str.replace("Wielki grzmot rozciąga się między wami", "Rozlegnie się głos wielkiego gromu")

dataset["text_en"] = dataset["text_en"].str.replace("perfume", "scent")
dataset["text_en"] = dataset["text_en"].str.replace("just crucify Jesus", "stop crucifying Jesus")
dataset["text_en"] = dataset["text_en"].str.replace("pride and pride", "pride and arrogance")

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
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("przyszedłem tu nie po", "przyszłam tu nie po")

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


dataset.to_csv("2018_cleaned.csv", index=False, encoding="utf-8")
dataset.to_json("trevignano_2018.json",orient="records")








