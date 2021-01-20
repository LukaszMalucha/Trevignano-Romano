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





dataset_1 = pd.read_csv("2020.csv", encoding="utf-8")
dataset_1 = dataset_1[dataset_1["date"] != "2020_05"]
dataset_1["text"] = dataset_1["text"].str.split("Pubblicato da").str[0]


dataset_2 = pd.read_csv("2020_05.csv", encoding="utf-8")
dataset_2["text"] = dataset_2["text"].str.split("Pubblicato da").str[1]

dataset = pd.concat([dataset_1, dataset_2])


dataset["text"] = dataset["text"].str.strip()
dataset["text"] = dataset["text"].str.replace("\n", " ")



dataset["text"] = dataset["text"].str.replace("Trevignano romano", "Trevignano Romano")
dataset["text"] = dataset["text"].str.replace("\. ", ".")
dataset["text"] = dataset["text"].str.replace("\.", ". ")




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
dataset['text'] = dataset['text'].str.replace("Amen \”\.", "Amen.")

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
dataset['text'] = dataset['text'].str.replace("Cenacolo di preghiera a Rimini", "")
dataset['text'] = dataset['text'].str.replace("Chiesa di Santa Maria dell’Assunta", "")
dataset['text'] = dataset['text'].str.split("video dell'i").str[0]

# ITALIAN FIX

dataset["text"] = dataset["text"].str.replace("Poi aggiunge: …Dopo", "Poi aggiunge: Dopo")



# JESUS AUTHOR
dataset["author"] = np.where(dataset["date"] == "04_01_2018", "Jesus Christ", dataset["author"])








translator = google_translator()  


dataset["text_en"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='en'))
dataset["text_pl"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='pl'))

# SPELLING FIX

dataset["text_pl"] = dataset["text_pl"].str.replace("niedługo przyjadę", "niebawem przybędę")
dataset["text_pl"] = dataset["text_pl"].str.replace(", proszę was świeckich i osób konsekrowanych, aby nadal byli solą dla tej ziemi szkoda, bądź blisko swoich braci, wszystko nadejdzie nagle, więc przygotuj się", "Proszę was, osoby świeckie i konsekrowane, abyście nadal byli solą tej ziemi. Bądźcie blisko swoich braci, wszystko nadejdzie nagle, więc przygotujcie się")
dataset["text_pl"] = dataset["text_pl"].str.replace("Brief Tutaj, moja siostro, to jest moment,", "Już niedługo, moja siostro, nadejdzie moment,")
dataset["text_pl"] = dataset["text_pl"].str.replace("wszyscy potrzebują drugiego", "wszcy potrzebujecie siebie na wzajem")
dataset["text_pl"] = dataset["text_pl"].str.replace(" jak będę miał dla was, nic przegapisz to", " jakie ja mam dla was, za niczym nie będziesz tęsknił")
dataset["text_pl"] = dataset["text_pl"].str.replace("że ​​mój płaszcz jest płaszczem mojej Matki", " że ​​mój płaszcz, przez moją Matkę")
dataset["text_pl"] = dataset["text_pl"].str.replace("dlatego wierzy już wygrałeś", "dlatego wierzy, że już wygrał")
dataset["text_pl"] = dataset["text_pl"].str.replace("przygotował. .", "przygotował\. \.")
dataset["text_pl"] = dataset["text_pl"].str.replace("Cena będzie trochę droga", "Cena będzie bardzo wysoka")
dataset["text_pl"] = dataset["text_pl"].str.replace("dziećmi światła, ponieważ waszą wiarą kierujecie, przemieniacie serca. złóg", "dziećmi światła, ponieważ waszą wiarą kierujecie, przemieniacie serca z kamienia")
dataset["text_pl"] = dataset["text_pl"].str.replace("wkrótce Jezus uwolnią się od tej dyktatury", "wkrótce Jezus uwolni was od tych prześladowań")
dataset["text_pl"] = dataset["text_pl"].str.replace(" Módlcie się o zamieszanie, które istnieje w Kościele i polityce", " Módlcie się o ustanie zamieszania, które istnieje w Kościele i polityce")
dataset["text_pl"] = dataset["text_pl"].str.replace("wkrótce Jezus uwolnią się od tej dyktatury", "wkrótce Jezus uwolni was od tych prześladowań")
dataset["text_pl"] = dataset["text_pl"].str.replace("módlcie miłość w modlitwie", "proście o miłość w modlitwie")
dataset["text_pl"] = dataset["text_pl"].str.replace("ponieważ wojna domowa jest Kolejny", "ponieważ nadchodzi wojna domowa")
dataset["text_pl"] = dataset["text_pl"].str.replace("bo wkrótce ten czas strachu, niesprawiedliwości, pychy już nie będzie", "bo wkrótce ten czas strachu, niesprawiedliwości i pychy przeminie")
dataset["text_pl"] = dataset["text_pl"].str.replace("będziecie chodzić między pięściami i pluć", "będą wam grozić i was obrażać,")
dataset["text_pl"] = dataset["text_pl"].str.replace("Dzieci, mój odpoczynek nie będzie musiał nie bój się niczego", "Dzieci, moje stado nie będzie musiało się niczego bać")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ewangelii\. ,", "Ewangelii, ")
dataset["text_pl"] = dataset["text_pl"].str.replace("bez choroba", "bez chorób")
dataset["text_pl"] = dataset["text_pl"].str.replace("Minąłeś dobro za zło, a zło za dobre", "Zamieniliście dobro za zło, a zło na dobro")
dataset["text_pl"] = dataset["text_pl"].str.replace("aby Jezus mógł przekształcić go w Dzięki", "aby Jezus mógł przekształcić go w Ofiarę")
dataset["text_pl"] = dataset["text_pl"].str.replace("Mów o tych czasach, ale nie medytuj tego, co mówię przez mojego wybranego, kontynuuj tak, jakby wszystko miało się zmienić i powrócić jak wcześniej", "Mówicie o tych czasach, ale nie rozmyślacie o tym co wam przekazuję przez moją wybraną, kontynuujecie tak jakby wszystko miało się odmienić i wrócić do tego co było")
dataset["text_pl"] = dataset["text_pl"].str.replace("nigdy nie jest zasługą waszych zasług", "nigdy nie jest zasługą waszych starań")
dataset["text_pl"] = dataset["text_pl"].str.replace("Fatimy alla Salette", "od Fatimy po Salette")
dataset["text_pl"] = dataset["text_pl"].str.replace("Kochające dzieci", "Kochane dzieci")
dataset["text_pl"] = dataset["text_pl"].str.replace("dajcie mi ręce", "podajcie mi swoje ręce")
dataset["text_pl"] = dataset["text_pl"].str.replace("bądź potulna, ale jasna, każde słowo lub pismo nowej doktryny będzie musiało wzbudzić w ciebie wątpliwości", "bądź cicha, ale jasna, każde słowo lub pismo nowej doktryny będzie musiało wzbudzić w tobie wątpliwości")
dataset["text_pl"] = dataset["text_pl"].str.replace("wołam o ludzkość", "płaczę z powodu ludzkości")
dataset["text_pl"] = dataset["text_pl"].str.replace("dzieci nawracają się", "dzieci nawracajcie się")
dataset["text_pl"] = dataset["text_pl"].str.replace("zbliża się i zbliża do Boga", "przybliża do Boga")
dataset["text_pl"] = dataset["text_pl"].str.replace("pokutować i nawrócić się", "pokutujcie i nawróćcie się")
dataset["text_pl"] = dataset["text_pl"].str.replace("Zbierzcie w imię Pana", "Zbierzcie się w imię Pana")
dataset["text_pl"] = dataset["text_pl"].str.replace("bo wasze pokorne modlitwy za niebo są złotymi iskrami", "bo wasze pokorne modlitwy są dla Nieba złotymi iskrami.")
dataset["text_pl"] = dataset["text_pl"].str.replace("im bliżej zbliża się Czas Triumfu Mojego Niepokalanego Serca i tym bardziej szatan będzie was atakował", "im bardziej zbliża się Czas Triumfu Mojego Niepokalanego Serca, tym bardziej szatan będzie was atakował")
dataset["text_pl"] = dataset["text_pl"].str.replace("myślicieProszę ", "myślicie. Proszę ")
dataset["text_pl"] = dataset["text_pl"].str.replace("pobłogosławieni przez niebo", "pobłogosławieni przez Niebo")
dataset["text_pl"] = dataset["text_pl"].str.replace("wszystkich obecnych jeden po drugim", "wszystkich obecnych")
dataset["text_pl"] = dataset["text_pl"].str.replace("kto otworzy błysk w swoim sercu", "kto otworzy szczelinę w swoim sercu")
dataset["text_pl"] = dataset["text_pl"].str.replace("moimi konsekrowanymi ludźmi", "moimi konsekrowanymi osobami")
dataset["text_pl"] = dataset["text_pl"].str.replace(" wirusy wkroczyły na ich drogę", " pojawiły się wirusy")
dataset["text_pl"] = dataset["text_pl"].str.replace("proszę moje dzieci, aby świecie, do moich umiłowanych, aby się dużo modlić, abym mógł być blisko Ciebie", "proszę moje dzieci na świacie, moje ukochane, aby się dużo modliły, abym mogła być blisko was")
dataset["text_pl"] = dataset["text_pl"].str.replace("nie mieszajcie się w zamieszanie, ale odprawiajcie Msze św", "nie dołączajcie do zamieszania, ale odprawiajcie Msze św")
dataset["text_pl"] = dataset["text_pl"].str.replace("nie boją się dzieci", "nie bójcie się dzieci")
dataset["text_pl"] = dataset["text_pl"].str.replace(" łącznie z żywym Jezusem boskość", " łącznie z Jezusem, żywym w ciele, krwi i boskość")
dataset["text_pl"] = dataset["text_pl"].str.replace("bo ci, którzy", "ci, którzy")
dataset["text_pl"] = dataset["text_pl"].str.replace(", bo ci, którzy nie będą mogli przyjąć Komunii w ustach, zaopatrz się w lnianą chusteczkę i taką samą przynieś ją do ust, nie dotykając jej rękami, zachowaj chusteczkę ostrożnie i zawsze używaj jej ponownie", ", ci, którzy nie będą mogli przyjąć Komunii do ust, niech zaopatrzą się w lnianą chusteczkę i na niej niech podnoszą hostię do ust, nie dotykając hostii rękami, niech pilnują tej chusteczki i zawsze używaj jej ponownie")
dataset["text_pl"] = dataset["text_pl"].str.replace("który przyleci z ziemi", "który pokawi się na ziemi")
dataset["text_pl"] = dataset["text_pl"].str.replace("ale czekać na coś innego", "czeka was jeszcze coś innego")
dataset["text_pl"] = dataset["text_pl"].str.replace("a zło nie da wam już siły, by wrócić do Boga", "a zło odbierze wszystkie siły na powrót do Boga")
dataset["text_pl"] = dataset["text_pl"].str.replace("będę przy wami", "będę przy was")
dataset["text_pl"] = dataset["text_pl"].str.replace("za konsekrowane", "za konsekrowanych")
dataset["text_pl"] = dataset["text_pl"].str.replace(" dusze, korzystając z tej chwili zamieszania", " Dusze, korzystając z tej chwili zamieszania")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ja, Twój Królu", "Ja, Wasz Król")
dataset["text_pl"] = dataset["text_pl"].str.replace("Dlaczego mnie nie kochasz", "Dlaczego nie kochasz mnie")
dataset["text_pl"] = dataset["text_pl"].str.replace(" umysł tego, który doprowadzi cię do zbawienia, nie może zostać oświecony", " umysł, który doprowadzi cię do zbawienia, nie może zostać oświecony")

11.03.2020




ś


dataset["text_en"] = dataset["text_en"].str.replace("perfume", "scent")
dataset["text_en"] = dataset["text_en"].str.replace("Children, my rest", "Children, my flock")
dataset["text_en"] = dataset["text_en"].str.replace("Children of the Light, because with your Faith you are driving, transforming hearts. stone", "Children of Light, because with your Faith you are driving, transforming hearts of stone")



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
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("jego stopy spoczęły", "jej stopy spoczęły")


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








dataset = dataset[dataset["day"] != "LA"]










dataset.to_csv("2020_cleaned.csv", index=False, encoding="utf-8")
dataset.to_json("trevignano_2020.json",orient="records")







