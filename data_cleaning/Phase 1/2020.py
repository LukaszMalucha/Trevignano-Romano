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




# DUPLICATE FIX - 05.12.2020







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
dataset["text_pl"] = dataset["text_pl"].str.replace("przygotował\. \.", "przygotował.")
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
dataset["text_pl"] = dataset["text_pl"].str.replace("ile bólu widzieć was tak bezbronnych i zranionych", "ileż to bólu, gdy widzę was tak bezbronnych i zranionych")
dataset["text_pl"] = dataset["text_pl"].str.replace("aby wznieść wasze wołanie do mojego Ojca, który chociaż was tak bardzo kocha, nie jest już w stanie patrzeć na swoje ukochane dzieci przebaczają i nie mają odwagi nieść Najświętszą Eucharystię nawet tym, którzy cierpią, ta próba jest mocna", "aby wznieść wasze wołanie do mojego Ojca, który choć tak bardzo was kocha, nie może już dłużej patrzeć na swoje ukochane dzieci, które są zagubione i nie mają odwagi, aby przynieść Świętą Eucharystię nawet tym, którzy cierpią, ta próba jest silna")
dataset["text_pl"] = dataset["text_pl"].str.replace("radość w Twoje serce", "radość w Waszych sercach")
dataset["text_pl"] = dataset["text_pl"].str.replace("pomyślcie i pomyślcie", "pomyślcie")
dataset["text_pl"] = dataset["text_pl"].str.replace("czas walki dobra ze złem jest w działać", "nadszedł czas walki dobra ze złem")
dataset["text_pl"] = dataset["text_pl"].str.replace(" i wojennych wiatrów", " i wiatrów wojny")
dataset["text_pl"] = dataset["text_pl"].str.replace(" łaska nieba", " łaska Nieba")
dataset["text_pl"] = dataset["text_pl"].str.replace("z wielką ochroną", "pod wielką ochroną")
dataset["text_pl"] = dataset["text_pl"].str.replace("idźcie za moją Matką swoimi śladami", "podążajcie za moją Matką")
dataset["text_pl"] = dataset["text_pl"].str.replace("staliście się podobnymi poddanymi", "staliście się jakby poddanymi")
dataset["text_pl"] = dataset["text_pl"].str.replace(" Moi bracia, przechodzę jeden po drugim, będę was pieścić i błogosławić, jako brata, jako przyjaciela, jako ojc", "Moi bracia, przejdę obok każdego, będę was przytulał i błogosławił, jak brat, jak przyjaciel, jako ojciec")
dataset["text_pl"] = dataset["text_pl"].str.replace("w imię moje", "w Imię moje")
dataset["text_pl"] = dataset["text_pl"].str.replace("trzymaj rękę w mojej", "chwyć mnie za rękę")
dataset["text_pl"] = dataset["text_pl"].str.replace("pójdę za tą misją, bądź spokojny", "będę z tobą podczas tej misji, bądź spokojna")
dataset["text_pl"] = dataset["text_pl"].str.replace("na wezwania z nieba", "na wezwania z Nieba")
dataset["text_pl"] = dataset["text_pl"].str.replace("używają ich do postu i pokuty", "użyjcie go do postu i pokuty")
dataset["text_pl"] = dataset["text_pl"].str.replace("a wasze serca napełni się radością", "a wasze serca napełnią się radością")
dataset["text_pl"] = dataset["text_pl"].str.replace("złóżcie pokój, miłość i radość w swoich sercach", "umieśćcie pokój, miłość i radość w swoich sercach")
dataset["text_pl"] = dataset["text_pl"].str.replace("Daj mi swoje ręce", "Podaj mi rękę")
dataset["text_pl"] = dataset["text_pl"].str.replace("wasze związki modlitewne wznoszą się do nieba", "wasze zjednoczone modlitwy wznoszą się do nieba")
dataset["text_pl"] = dataset["text_pl"].str.replace("była dniem, w którym", "dzień, w którym")
dataset["text_pl"] = dataset["text_pl"].str.replace("nawet wielcy teologowie zabronili kościołom rozpraszać moją trzodę", "nawet wielcy teologowie zamknęli kościoły, rozpraszać moją trzodę")
dataset["text_pl"] = dataset["text_pl"].str.replace("kładąc was pod swoim Błogosławionym płaszczem", "chowając was pod swoim Błogosławionym płaszczem")
dataset["text_pl"] = dataset["text_pl"].str.replace("drogie mojemu sercu jako Matce", "drogie mojemu Matczynemu Sercu")
dataset["text_pl"] = dataset["text_pl"].str.replace("Moi maluchy", "Moje maleństwa")
dataset["text_pl"] = dataset["text_pl"].str.replace("jako Matkę was wszystkich", "jako Matka was wszystkich")
dataset["text_pl"] = dataset["text_pl"].str.replace("was w spokoju Drogie dzieci", "was w spokoju. Drogie dzieci")
dataset["text_pl"] = dataset["text_pl"].str.replace("módlcie się za zmarłych, którzy istnieją i którzy będą", "módlcie się za tych, którzy już umarli i za tych, którzy dopiero umrą")
dataset["text_pl"] = dataset["text_pl"].str.replace("a twoje życie będzie odbiorcą radości i miłości", "a twoje życie otzyma radość i miłość")
dataset["text_pl"] = dataset["text_pl"].str.replace(", a nie bój się", ", więc nie bój się")
dataset["text_pl"] = dataset["text_pl"].str.replace(" Całe twoje życie zostanie przemienione, oto Duch Święty, działaj dalej", " Całe twoje życie zostanie przemienione, bo Duch Święty nadal będzie działał")
dataset["text_pl"] = dataset["text_pl"].str.replace("Nie bój się, dzieci siła i odwaga", "Nie bójcie się dzieci, siły i odwagi")
dataset["text_pl"] = dataset["text_pl"].str.replace("osłodzić moje zbolałe i krwawiące serce", "aby osłodzić moje zbolałe i krwawiące serce")
dataset["text_pl"] = dataset["text_pl"].str.replace("do mnie szczerymi oczami i proszą o pomoc i Łaska", "do mnie ze szczerymi oczami i proszą o pomoc i Łaskę")
dataset["text_pl"] = dataset["text_pl"].str.replace("po prostu dajcie mi swoje ręce", "po prostu podajcie mi swoje ręce")
dataset["text_pl"] = dataset["text_pl"].str.replace(", co chcą was zobowiązać", ", do czego chcą was zobowiązać")
dataset["text_pl"] = dataset["text_pl"].str.replace("nie ma sensu planować ich ucieczki w obliczu tego", "ich planowana ucieczka nie ma sensu w obliczu tego")
dataset["text_pl"] = dataset["text_pl"].str.replace("ponieważ ujrzycie zstępującego Jezusa, gdy odchodził", "ponieważ ujrzycie Jezusa, który tak jak gdy odchodził, teraz zstąpi")
dataset["text_pl"] = dataset["text_pl"].str.replace("ale wołają imię Pana", "ale wołają imienia Pana")
dataset["text_pl"] = dataset["text_pl"].str.replace("Mu wierni Wielu", "Mu wierni. Wielu")
dataset["text_pl"] = dataset["text_pl"].str.replace("od od Fatimy", "od Fatimy")
dataset["text_pl"] = dataset["text_pl"].str.replace("to jest na twoich oczach", "przed twoimi oczami")
dataset["text_pl"] = dataset["text_pl"].str.replace("Bądź jednym chórem podczas odmawiania Różańca Świętego", "Bądźcie jednym chórem podczas odmawiania Różańca Świętego")
dataset["text_pl"] = dataset["text_pl"].str.replace("dajcie mi swoje ręce", "podajcie mi swoje ręce")
dataset["text_pl"] = dataset["text_pl"].str.replace("Chciałbym takich rzeczy w waszym życiu", "Chciałbym tych rzeczy w waszym życiu")
dataset["text_pl"] = dataset["text_pl"].str.replace("Teraz jest nieobecność Boga w dużej części ludzkości", "Teraz Bóg jest nieobecy w dużej części ludzkości")
dataset["text_pl"] = dataset["text_pl"].str.replace("kochaj Pana i Go przemieni wasze serca", "kochaj Pana a On przemieni wasze serca")
dataset["text_pl"] = dataset["text_pl"].str.replace("bo tylko na modlitwie", "bo tylko w modlitwie")
dataset["text_pl"] = dataset["text_pl"].str.replace("gdzie tylko ty będziesz bezpieczny", "gdzie tylko będziesz bezpieczny")
dataset["text_pl"] = dataset["text_pl"].str.replace("Jednak możesz być spokojny, ponieważ nigdy cię nie opuszczę", "Jednak możecie być spokojni, ponieważ nigdy was nie opuszczę")
dataset["text_pl"] = dataset["text_pl"].str.replace("Boga Ta obecna sytuacja dała wielkie próby i tutaj jest to, że kiedy mój Syn powróci, będzie to dzielić, a nie łączyć, ponieważ teraz wybór jest dokonany", "Ta obecna sytuacja dała wielkie dowody i oto, kiedy mój Syn powróci, będzie to dzielenie, a nie jednoczenie, bo teraz wybór jest dokonany")
dataset["text_pl"] = dataset["text_pl"].str.replace("moją małą resztką", "moją małą garstką")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ja Niepokalana i Współodkupicielko", "Ja Niepokalana i Współodkupicielka")
dataset["text_pl"] = dataset["text_pl"].str.replace("nie bój się, że nigdy nie zostawię cię samego", "nie bójcie się, nigdy nie zostawię was samych")
dataset["text_pl"] = dataset["text_pl"].str.replace("Amen Matka Boża", "Amen. Matka Boża")
dataset["text_pl"] = dataset["text_pl"].str.replace("słuchaj jego głosu w swoim sercu", "słuchaj Jego głosu w swoim sercu")
dataset["text_pl"] = dataset["text_pl"].str.replace("Garść gruzów przez diabła", "Garść gruzów z powodu diabła")
dataset["text_pl"] = dataset["text_pl"].str.replace("od teraz\. nastąpi ciąg wydarzeń, nawróć się pilnie, czas się skończył", ". Teraz nastąpi ciąg wydarzeń, nawróć się pilnie, czas się skończył")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ile niestety jest częścią", "Ilu niestety jest częścią")
dataset["text_pl"] = dataset["text_pl"].str.replace("ale będzie ulegać pokusom szatana", "ale będzie uległością wobec pokus szatana")
dataset["text_pl"] = dataset["text_pl"].str.replace("pokutując i prosząc o przebaczenie za to, co robicie dla mojego Kościoła", "pokutujcie i proście o przebaczenie za to, co robicie mojemu Kościołowi")
dataset["text_pl"] = dataset["text_pl"].str.replace("z miłością, miłością", "z miłością, miłosierdziem")
dataset["text_pl"] = dataset["text_pl"].str.replace("stałeś się robotem pozbawionym człowieczeństwa", "stałeś się maszyną pozbawioną człowieczeństwa")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ratujcie się, ponieważ gniew mojego Ojca jest już na was", "Ratujcie się, ponieważ gniew mojego Ojca już na was spadł")
dataset["text_pl"] = dataset["text_pl"].str.replace("Twojego drogiego Jezusa ", "Twój drogi Jezus ")
dataset["text_pl"] = dataset["text_pl"].str.replace("i nie możecie popełniać błędów", "i nie będziecie popełniać błędów")
dataset["text_pl"] = dataset["text_pl"].str.replace("Teraz pieszczę cię jeden po drugim, nadal bądź światłam dla świata", "Teraz przytulam was wszystkich, nadal bądźcie światłem dla świata")
dataset["text_pl"] = dataset["text_pl"].str.replace(", w te szczególne święta Bożego Narodzenia wykorzystują spokój i radość z przyjścia Zbawiciela", ", w te szczególne święta Bożego Narodzenia wykorzystajcie spokój i radość z przyjścia Zbawiciela")
dataset["text_pl"] = dataset["text_pl"].str.replace(" zarządzajcie tym modlitwą", "zawierzcie modlitwie")
dataset["text_pl"] = dataset["text_pl"].str.replace(" i bólu, jaki zadajecie mojemu Synowi Jezusowi", " i z powodu bólu, jaki zadajecie mojemu Synowi Jezusowi")
dataset["text_pl"] = dataset["text_pl"].str.replace(" jaki kiedykolwiek żyła ludzkość", " w jakim kiedykolwiek żyła ludzkość")
dataset["text_pl"] = dataset["text_pl"].str.replace("moje ulubione dzieci są jedne przeciwko drugiemu", "moje ulubione dzieci są przeciw sobie")
dataset["text_pl"] = dataset["text_pl"].str.replace("Opróżnij się i napełnij Bogiem", "Stań się pustym i napełnij się Bogiem")
dataset["text_pl"] = dataset["text_pl"].str.replace(" Bądź w harmonii z niebem, aby spokojnie stawić czoła coraz bliżej Ostrzeżeniu", " Bądź w harmonii z Niebem, aby spokojnie stawić czoła nadchodzącemu Ostrzeżeniu")
dataset["text_pl"] = dataset["text_pl"].str.replace("Będę z wami przez całą modlitwę", "Będę z wami przez całą modlitwę.")
dataset["text_pl"] = dataset["text_pl"].str.replace("a wtedy Ostrzeżenie jest blisko", "a Ostrzeżenie jest blisko")
dataset["text_pl"] = dataset["text_pl"].str.replace("Pieszczę cię jeden po drugim, przypominając ci o mojej miłości do ciebie", "Przytulam was wszystkich, przypominając wam o mojej miłości do was")
dataset["text_pl"] = dataset["text_pl"].str.replace("a nie możesz się doczekać radości mojego świata", "a czeka cię radości mojego świata")
dataset["text_pl"] = dataset["text_pl"].str.replace("kiedy Antychryst ma zamiar wejść", "gdy pojawi się Antychryst")
dataset["text_pl"] = dataset["text_pl"].str.replace(" Uwielbiane dzieci, módlcie się nie tylko o prośbę, ale także o podziękowanie mojemu Synowi Jezusowi za pokój i życie", " Uwielbiane dzieci, nie tylko proście w modlitwie, ale także dziękujcie mojemu Synowi Jezusowi za pokój i życie")
dataset["text_pl"] = dataset["text_pl"].str.replace("zawierzenie Bogu Moje dzieci", "zawierzenie Bogu. Moje dzieci")
dataset["text_pl"] = dataset["text_pl"].str.replace("Idziesz drogą pełną niebezpieczeństw, a mimo to nie wierzysz, nie otwierasz serc", "Idziecie drogą pełną niebezpieczeństw, a mimo to nie wierzycie, nie otwieracie serc")
dataset["text_pl"] = dataset["text_pl"].str.replace(" czego doświadczacie, jest tylko złudzeniem spokoju, ale wszystko nagle upadnie", " czego doświadczacie, będąc tylko złudzeniem spokoju, to wszystko nagle upadnie")
dataset["text_pl"] = dataset["text_pl"].str.replace("która prowadzi do nieba", "która prowadzi do Nieba")
dataset["text_pl"] = dataset["text_pl"].str.replace("wszystko spada, ", "wszystko upada, ")
dataset["text_pl"] = dataset["text_pl"].str.replace("Jeśli nie wpuścisz Jezusa do swoich serc", "Jeśli nie wpuścisz Jezusa do swojego serca")
dataset["text_pl"] = dataset["text_pl"].str.replace("na lewej ręce trzymała trzy różańce", "w lewej ręce trzymała trzy różańce")
dataset["text_pl"] = dataset["text_pl"].str.replace("królestwa niebieskiego", "Królestwa Niebieskiego")
dataset["text_pl"] = dataset["text_pl"].str.replace("dajcie się znaleźć przy zapalonych lampach, tak jak wasze serca i oczami ujrzycie cud nowego życia", "jeżeli znajdzie was przy zapalonych lampach, to wasze serca i oczy ujrzą cud nowego życia")
dataset["text_pl"] = dataset["text_pl"].str.replace("co oferuje wam niebo", "co oferuje wam Niebo")
dataset["text_pl"] = dataset["text_pl"].str.replace("Mój mały odpoczynek będzie prześladowany, wołam za młodych, którzy są daleko od Boga", "Moja mała trzódka będzie prześladowana, płaczę z powodu młodych, którzy są daleko od Boga")
dataset["text_pl"] = dataset["text_pl"].str.replace("wołam za rozbitymi rodzinami, wołam za nieochrzczonymi dziećmi i za tymi, którzy dorastają w szponach zła", "płaczę z powodu rozbitych rodzin, płaczę z powodu nieochrzczonych dzieci i z powodu tych, którzy dorastają w szponach zła")
dataset["text_pl"] = dataset["text_pl"].str.replace("i patrzę na was jeden po drugim, skanuję wasze serca i przynoszę Panu wasze intencje", "i patrzę na was wszystkich, wglądam w wasze serca i przynoszę Panu wasze intencje")
dataset["text_pl"] = dataset["text_pl"].str.replace("ponieważ waszą wiarą kierujecie, przemieniacie serca z kamienia", "ponieważ kierowani swoją wiarą, przemieniacie serca z kamienia")
dataset["text_pl"] = dataset["text_pl"].str.replace(", amen", ", Amen")
dataset["text_pl"] = dataset["text_pl"].str.replace("wielkim refleksją", "wielką refleksją")
dataset["text_pl"] = dataset["text_pl"].str.replace("zachowanie moich kapłanów jest pod obojętnym spojrzeniem tych, którzy mówią, że mają wiarę", "jak zachowują się moi księża pod obojętnym spojrzeniem tych, którzy mówią, że mają wiarę")
dataset["text_pl"] = dataset["text_pl"].str.replace("ale jak traktują mnie, będę ich traktował", "tak jak oni traktują mnie, tak ja będę ich traktował")
dataset["text_pl"] = dataset["text_pl"].str.replace("Bracia, nawracajcie się, teraz czasy się skończyły, inaczej, gdy wrócę, nie rozpoznacie mnie i nie pójdziecie za mną", "Bracia, nawracajcie się, teraz czas się skończył, inaczej, gdy wrócę, nie rozpoznacie mnie i nie pójdziecie za mną")
dataset["text_pl"] = dataset["text_pl"].str.replace("Moi maleńcy", "Moje maleństwa")
dataset["text_pl"] = dataset["text_pl"].str.replace("Córko Moja, rozmawiaj z kapłanami, tak drogimi memu sercu i o nich", "Moja córko, przemów do kapłanów, którzy są tak drodzy mojemu sercu, i powiedz im")
dataset["text_pl"] = dataset["text_pl"].str.replace("jeść Eucharystię", "spożywać Eucharystię")
dataset["text_pl"] = dataset["text_pl"].str.replace("Świętego, amen", "Świętego, Amen")
dataset["text_pl"] = dataset["text_pl"].str.replace("Dzisiaj spłyną na ciebie podziękowania", "Dzisiaj spłyną na ciebie łaski")
dataset["text_pl"] = dataset["text_pl"].str.replace("ale Ja was ochronię i dam wam siłę", "bo Ja was ochronię i dam wam siłę")
dataset["text_pl"] = dataset["text_pl"].str.replace("na modlitwie Drogie dzieci", "na modlitwie. Drogie dzieci")
dataset["text_pl"] = dataset["text_pl"].str.replace(" chce uwodzić przyjemności tego świata, z pieniędzmi i seksem", "chce uwodzić przyjemnościami, pieniędzmi i seksem")
dataset["text_pl"] = dataset["text_pl"].str.replace(" Jesteście przyzwyczajeni do życia mechanicznego, porzucając rzeczy ziemskie i bardziej uważając na sprawy niebieskie", " Jesteście przyzwyczajeni do życia materialnego, porzućcierzeczy ziemskie i bardziej uważajcie na sprawy niebieskie")
dataset["text_pl"] = dataset["text_pl"].str.replace(" nie mówcie Pana, Boga waszego", "nie bójcie się, mówi Pan, Bóg wasz")
dataset["text_pl"] = dataset["text_pl"].str.replace("wasze serca na kamień w otwarte serca", "wasze serca z kamienia w otwarte serca")
dataset["text_pl"] = dataset["text_pl"].str.replace("że możesz być Bogiem siebie", "że możesz być Bogiem dla siebie")
dataset["text_pl"] = dataset["text_pl"].str.replace(" ponieważ w ten sposób nie pójdziesz na właściwą ścieżkę, ale nadal będziesz rozpaczać, beze mnie i bez porzucenia nic nie osiągniesz", " ponieważ w ten sposób nie pójdziesz właściwą ścieżką, ale nadal będziesz rozpaczać, beze mnie i bez porzucenia nic nie osiągniesz")
dataset["text_pl"] = dataset["text_pl"].str.replace("ale jestem tutaj, aby ci dać siebie", "bo jestem tutaj, aby dać ci siebie")
dataset["text_pl"] = dataset["text_pl"].str.replace("wyrażajcie miłość swoim braciom", "przynoście miłość swoim braciom")
dataset["text_pl"] = dataset["text_pl"].str.replace("moimi dziećmi, moimi dziećmi", "moimi dziećmi")
dataset["text_pl"] = dataset["text_pl"].str.replace("ponieważ Pan nie sprawi, że niczego wam braknie", "ponieważ Pan sprawi, że niczego wam braknie")
dataset["text_pl"] = dataset["text_pl"].str.replace("i dzisiaj dla tych, którzy z otwartym sercem proszą o łaski, zostaną wysłuchani i wysłuchani", "i dzisiaj ci, którzy z otwartym sercem proszą o łaski, zostaną wysłuchani")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ostrzeżenie lub oświecenie", "Ostrzeżenie")
dataset["text_pl"] = dataset["text_pl"].str.replace("koronę Różańca Świętego", "koronkę Różańca Świętego")
dataset["text_pl"] = dataset["text_pl"].str.replace("was obrażać,,", "was obrażać,")
dataset["text_pl"] = dataset["text_pl"].str.replace(" jest zawsze w smutku i płaczu", " jest zawsze w nim w smutku i płaczu")
dataset["text_pl"] = dataset["text_pl"].str.replace("na wilki przebrane za baranki", "na wilki w owczej skórze")
dataset["text_pl"] = dataset["text_pl"].str.replace("mój Pan będzie waszym restauratorem i niczego wam nie zabraknie", "mój Pan będzie waszym gospodarzem i niczego wam nie zabraknie")
dataset["text_pl"] = dataset["text_pl"].str.replace("ponieważ zostanie nim wstrząśnięty silnym trzęsieniem ziemi", "ponieważ zostanie wstrząśnięty silnym trzęsieniem ziemi")
dataset["text_pl"] = dataset["text_pl"].str.replace("za świat, który ma wyjść", "dla świata, który ma odejść")
dataset["text_pl"] = dataset["text_pl"].str.replace("Moje dzieci, tutaj jest to, że wiele z moich dzieci nie modli się, ale są zabierane przez rzeczy tego świata", "Moje dzieci, wiele z moich dzieci nie modli się, ale zajmują się rzeczami tego świata")
dataset["text_pl"] = dataset["text_pl"].str.replace(" ciemność i ciemność", " mrok i ciemność")
dataset["text_pl"] = dataset["text_pl"].str.replace("Bogiem, Jeden i Trzech", "Bogiem Trójjedynym")
dataset["text_pl"] = dataset["text_pl"].str.replace("Spójrz, co się dzieje, ale z obojętnością, ale czas już miną", "Patrzycie na wszystko, co się dzieje z obojętnością, a czas już minął")
dataset["text_pl"] = dataset["text_pl"].str.replace("ze Mną możecie mieć zbawienie,", "ze Mną dostąpicie zbawienia,")
dataset["text_pl"] = dataset["text_pl"].str.replace("adorować Boże inny niż Mnie", "adorować bogów innych niż Ja")
dataset["text_pl"] = dataset["text_pl"].str.replace("powrócić jak wcześniej, nic moje dzieci nie wróci jak wcześniej", "być jak kiedyś, nic moje dzieci nie będzie jak kiedyś")
dataset["text_pl"] = dataset["text_pl"].str.replace("cokolwiek innego, Umarłem ", "cokolwiek innego. Umarłem ")
dataset["text_pl"] = dataset["text_pl"].str.replace("Błogosławię was, dzieci, jedno po drugim", "Błogosławię was, dzieci, wszystkie")
dataset["text_pl"] = dataset["text_pl"].str.replace("płaczę za tym", "płaczę z powodu tego")
dataset["text_pl"] = dataset["text_pl"].str.replace("Wierz w miłosiernego Boga, a nie w Jego sprawiedliwość", "Wierzysz w miłosiernego Boga, a nie w Jego sprawiedliwość")
dataset["text_pl"] = dataset["text_pl"].str.replace("niebo już się ściemnia", "niebo już ciemnieje")
dataset["text_pl"] = dataset["text_pl"].str.replace("wszystkim tę łaskę", "wszystkim tę Łaskę")
dataset["text_pl"] = dataset["text_pl"].str.replace("gotowi na nadejście Oświecenia", "gotowi na nadejście Ostrzeżenia")
dataset["text_pl"] = dataset["text_pl"].str.replace("nie męczcie się modlitwą", "niech modlitwa wam się nie nudzi")
dataset["text_pl"] = dataset["text_pl"].str.replace("rozkazywać twoim umysłom", "rozkazywać waszym umysłom")
dataset["text_pl"] = dataset["text_pl"].str.replace("aby wyznać i aby cię pilnie nawrócić", "aby się spowiadać i aby cię pilnie nawrócić")
dataset["text_pl"] = dataset["text_pl"].str.replace("Dzieci, ugnijcie kolana, od wielu lat zalecam wam nieustanną modlitwę, abyście nie byli przywiązani do spraw tego świata, ale nadal żyliście tak, jakby wszystko było wieczne", "Dzieci, zegnijcie kolana, od tylu lat zalecam wam nieustanną modlitwę, abyście nie przywiązywali się do rzeczy tego świata, ale wy nadal żyjecie tak, jakby wszystko było na zawsze")
dataset["text_pl"] = dataset["text_pl"].str.replace("bezużyteczne rzeczy pamiętaj", "bezużyteczne rzeczy. Pamiętaj")
dataset["text_pl"] = dataset["text_pl"].str.replace(" chcą zdominować Twoje życie i umysły", " chcą zdominować Wasze życie i umysły")
dataset["text_pl"] = dataset["text_pl"].str.replace("Moje dzieci, dziękuję wam, że jesteście tu na modlitwie. Moje dzieci, czuję wasze serca i ból, który wam ofiarował, dotknął waszą ręką łaskę Pana", "Dzieci moje, dziękuję wam, że jesteście tutaj na modlitwie. Dzieci moje, czuję wasze serca i z bólem ofiarowanym dotknęliście rękami łaski Pana")
dataset["text_pl"] = dataset["text_pl"].str.replace("bezużyteczne rzeczy pamiętaj", "bezużyteczne rzeczy. Pamiętaj")
dataset["text_pl"] = dataset["text_pl"].str.replace("Moja córko, wielu zastanawia się, co się powtórzy, i nie zdają sobie sprawy, że wszystko upadnie, nie przestrzegają już pierwszego przykazania, nie uwierzyli w moc modlitwy i miłości, są zdezorientowani i zagubieni", "Moja córko, wielu zastanawia się, co będzie dalej i nie zdaje sobie sprawy, że wszystko się rozpadnie; nie przestrzegali pierwszego przykazania, nie wierzyli w moc modlitwy i miłości, są zdezorientowani i zagubieni")
dataset["text_pl"] = dataset["text_pl"].str.replace("Rozpocznie się walka partyzancka, która zamieni się w wojnę, nadejdą czasy, kiedy będą nadal trzymać cię na dystans, zmieniając twój sposób życia, prowadząc cię coraz bardziej w grzech", "Rozpocznie się wojna partyzancka, która przerodzi się w wojnę, nadejdą czasy, w których będą nadal trzymać was odosobnionych, zmieniając sposób, w jaki żyjecie, prowadząc was coraz bardziej do grzechu")
dataset["text_pl"] = dataset["text_pl"].str.replace(" Teraz zostawiam Ci słodką, ukochaną córkę, ofiaruj swój ból, razem z ukochaną małżonką jesteście błogosławieni przez niebo i przez mojego Ojca, nigdy nie będziecie sami", "Teraz zostawiam cię słodka kochana córko, ofiaruj swój smutek, ty wraz ze swoim ukochanym małżonkiem, jesteś błogosławiona przez niebo i mojego Ojca, nigdy nie będziesz sama")
dataset["text_pl"] = dataset["text_pl"].str.replace("Terroryzowali mój lud i masakrują kościoły, to nie koniec Europy, to koniec świata", "Terroryzują mój naród i mordują kościoły, to nie jest koniec Europy, to jest koniec świata")
dataset["text_pl"] = dataset["text_pl"].str.replace("Jak zrobią, co moje dzieci zrobią bez was, będą apostołami, będą światłami, teraz ciemność zapadła w Kościołach", "Jak oni sobie poradzą, co moje dzieci zrobią bez was, bądźcie apostołami, bądźcie światłami, teraz ciemność zstąpiła na Kościoły")
dataset["text_pl"] = dataset["text_pl"].str.replace("Nie powtarzaj tego błędu, ale zeznawaj", "Nie powtarzajcie tego błędu, lecz świadczcie")
dataset["text_pl"] = dataset["text_pl"].str.replace("\”\. Kocham", ". Kocham")
dataset["text_pl"] = dataset["text_pl"].str.replace("Dzieci, jak widzicie, jest to czas wielkiego zamętu, w którym zło kryje się za fałszywymi łupami, będziecie musieli uważać, chodzić razem z Jezusem i karmić się Jego Słowem dla swojego zbawienia", "Dzieci, jak widzicie, jest to czas wielkiego zamieszania, gdzie zło ukrywa się za fałszywymi pozorami, musicie być ostrożni, chodzić razem z Jezusem i karmić się Jego Słowem dla waszego zbawienia")
dataset["text_pl"] = dataset["text_pl"].str.replace("Będę przechodził, aby was błogosławić jeden po drugim", "Przejdę, aby was wszystkich pobłogosławić")
dataset["text_pl"] = dataset["text_pl"].str.replace("tym zamieszanym świecie", "tym świecie pełnym zamieszania")
dataset["text_pl"] = dataset["text_pl"].str.replace("podważając słowa mojej Ewangelii", "poprzez podważenie słów mojej Ewangelii")
dataset["text_pl"] = dataset["text_pl"].str.replace(" Moje dzieci, ufajcie i powierzajcie się sobie, a zawsze będę przy was, pójdę w moje ślady i wezmę mnie za rękę, a będę z wami każdego dnia, aż do końca", "Dzieci moje, ufajcie i polegajcie na Mnie, a Ja będę z wami zawsze, idźcie moimi śladami i bierzcie Mnie za rękę, a Ja będę z wami przez wszystkie dni, aż do końca")
dataset["text_pl"] = dataset["text_pl"].str.replace("Teraz błogosławię was jeden po drugim", "Teraz błogosławię was wszystkich")
dataset["text_pl"] = dataset["text_pl"].str.replace("Świętym, amen", "Świętym, Amen")
dataset["text_pl"] = dataset["text_pl"].str.replace("ale to boli mnie to", "boli mnie to")
dataset["text_pl"] = dataset["text_pl"].str.replace(" iz bronią postu i różańcem na rękach", " i z bronią postu i różańcem w rękach")
dataset["text_pl"] = dataset["text_pl"].str.replace("prorocy tamtych czasów", "prorocy tych czasów")
dataset["text_pl"] = dataset["text_pl"].str.replace("pomyślcie o wszystkim co jest przywiązane do ziemi i nigdy nie patrzysz w niebo, które z miłością chce cię zbawić swoimi znakami i Moimi słowami, aby cię chronić, a jednak jesteś ślepy", "myślicie o wszystkim, co jest związane z ziemią i nigdy nie patrzycie na niebo, które z miłością chce was zbawić swoimi znakami i moimi słowami was chronić, a jednak jesteście ślepi.")
dataset["text_pl"] = dataset["text_pl"].str.replace("jak wielu was gardzi, osądza i prześladuje", "jak wielu wami gardzi, osądza was i prześladuje")
dataset["text_pl"] = dataset["text_pl"].str.replace("będziecie mieli moi Aniołowie obok was", "będziecie mieli moich Aniołów obok was")
dataset["text_pl"] = dataset["text_pl"].str.replace("zwłaszcza gdy będziecie w swoich schronach", "zwłaszcza gdy będziecie w swoich schronieniach")
dataset["text_pl"] = dataset["text_pl"].str.replace("Boga, Jeden i Trzech", "Boga w Trzech Osobach")
dataset["text_pl"] = dataset["text_pl"].str.replace("Nie odchodź aż tak daleko, bo nawet On może cię nie rozpoznać.", "Nie dojdziesz do tego punktu, ponieważ On również może cię nie rozpoznać")
dataset["text_pl"] = dataset["text_pl"].str.replace("wszystkiego, czujność", "wszystkiego, bądźcie czujni")
dataset["text_pl"] = dataset["text_pl"].str.replace("Drogie dzieci, dziękuję wam, że odpowiedzieliście na moje wezwanie w waszych sercach. Jak pięknie jest widzieć moje klęczące dzieci, teraz już rzadko widzę serca ludzi, które przenosi miłość do Mnie i do mojego Syna Jezusa", "Drogie dzieci, dziękuję wam, że odpowiedzieliście na moje wezwanie w waszych sercach. Jak pięknie jest widzieć moje dzieci klęczące, teraz rzadko widzę serca ludzi uniesione miłością do mnie i do mojego Syna Jezusa.")
dataset["text_pl"] = dataset["text_pl"].str.replace("pochwyceni przez ostrzeżenie", "pochwyceni przez Ostrzeżenie")
dataset["text_pl"] = dataset["text_pl"].str.replace("Dzieci, pamiętajcie słowa Jezusa: ze mną albo ze mną. przeciwko mnie ”", "Dzieci, pamiętajcie słowa Jezusa: ze mną albo przeciwko mnie \”")
dataset["text_pl"] = dataset["text_pl"].str.replace("jedynym głosem nieba", "jedynym głosem Nieba")
dataset["text_pl"] = dataset["text_pl"].str.replace("Mu wierni Wielu", "Mu wierni. Wielu")
dataset["text_pl"] = dataset["text_pl"].str.replace("od od Fatimy po Salette", "od Fatimy po Salette")
dataset["text_pl"] = dataset["text_pl"].str.replace("dajcie mi swoje ręce", "podajcie mi wasze ręce")
dataset["text_pl"] = dataset["text_pl"].str.replace("światła , miłość", "światła, miłość")
dataset["text_pl"] = dataset["text_pl"].str.replace("Drogie dzieci, dziękuję wam, że odpowiedzieliście na moje wezwanie w waszych sercach. Moje dzieci, czuję trochę spokoju w waszych sercach, ale pamiętam, że jestem z wami", "Drogie dzieci, dziękuję wam, że odpowiedzieliście na moje wezwanie w waszych sercach. Dzieci moje, odczuwam w waszych sercach niewielką pogodę ducha, ale pamiętajcie, że jestem z wami.")
dataset["text_pl"] = dataset["text_pl"].str.replace("światła , miłość", "światła, miłość")
dataset["text_pl"] = dataset["text_pl"].str.replace(" do Boga Ta obecna sytuacja dała wielkie próby i tutaj jest to, że", " do Boga. Ta obecna sytuacja to czas wielkie próby i ")
dataset["text_pl"] = dataset["text_pl"].str.replace("światła , miłość", "światła, miłość")
dataset["text_pl"] = dataset["text_pl"].str.replace("Amen Matka Boża nosiła dziś niebieską suknię", "Amen. Matka Boża miała dziś niebieską suknię")
dataset["text_pl"] = dataset["text_pl"].str.replace("była owinięta wspaniałym światłam", "była otoczona wspaniałym światłem")




ś


dataset["text_en"] = dataset["text_en"].str.replace("perfume", "scent")
dataset["text_en"] = dataset["text_en"].str.replace("Children, my rest", "Children, my flock")
dataset["text_en"] = dataset["text_en"].str.replace("Children of the Light, because with your Faith you are driving, transforming hearts. stone", "Children of Light, because with your Faith you are driving, transforming hearts of stone")
dataset["text_en"] = dataset["text_en"].str.replace("your prayer unions", "your united prayers")


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
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("będę was prosił ", "będę was prosić ")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("umysłam", "umysłem")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Zostałam wysłany", "Zostałam wysłana")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("zawsze mógł", "zawsze mogła")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("złemanym", "złamanym")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("światłam", "światłem")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("a będę obecny", "a będę obecna")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Chciałbym", "Chciałabym")





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







