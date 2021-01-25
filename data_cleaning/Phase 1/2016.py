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



# DRUGA RUNDA

dataset['text'] = dataset['text'].str.replace("\” ", "")
dataset['text'] = dataset['text'].str.replace("Amen\" ", "Amen")
dataset['text'] = dataset['text'].str.replace("Amen \” ", "Amen. ")
dataset['text'] = dataset['text'].str.replace("\. \" ", ".")
dataset['text'] = dataset['text'].str.replace("Amen\"", "Amen")
dataset['text'] = dataset['text'].str.replace("…\”", "…")
dataset['text'] = dataset['text'].str.replace("\. \. Amen", ". Amen")
dataset['text'] = dataset['text'].str.replace("\. \. Amen", ". Amen")
dataset['text'] = dataset['text'].str.replace("Amen Oggi", "Amen. Oggi")
dataset['text'] = dataset['text'].str.replace("braccio sinistro", "braccio sinistro.")
dataset['text'] = dataset['text'].str.replace("\"", "")

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
dataset["text_pl"] = dataset["text_pl"].str.replace("Moja córka mówi biskupowi", "Moja córko, powiedz biskupowi")
dataset["text_pl"] = dataset["text_pl"].str.replace("zwłaszcza Papieżu, módl się za nich", "zwłaszcza z powodu Papieża. Módl się za nich")
dataset["text_pl"] = dataset["text_pl"].str.replace("Bóg się spieszy", "Bóg nie będzie zwlekać")
dataset["text_pl"] = dataset["text_pl"].str.replace("Twoje imiona są wyryte", "Wasze imiona są wyryte")
dataset["text_pl"] = dataset["text_pl"].str.replace("że jesteście tu coraz liczniejsi", "że jest was tu coraz więcej")
dataset["text_pl"] = dataset["text_pl"].str.replace("Będę cię dotykał jeden po drugim, abyś mógł nieść", "Dotknę was jednego po drugim, abyście mogli nieść")
dataset["text_pl"] = dataset["text_pl"].str.replace(" abym dotknął ziemi", " abym dotknęła ziemi")
dataset["text_pl"] = dataset["text_pl"].str.replace("Uklęknij i bądź pokorny", "Uklęknijcie i bądźcie pokorni")
dataset["text_pl"] = dataset["text_pl"].str.replace("Dzięki, że mnie szukałeś", "Dziękuje, że mnie szukalicie")
dataset["text_pl"] = dataset["text_pl"].str.replace("za znak mojej obecności", "za świadectwo mojej obecności")
dataset["text_pl"] = dataset["text_pl"].str.replace("Sercem twojej matki", "Wraz z sercem twojej matki")
dataset["text_pl"] = dataset["text_pl"].str.replace("Kocham cię i kocham cię", "Kocham cię")
dataset["text_pl"] = dataset["text_pl"].str.replace("Boża dodała:\…", "Boża dodała:")
dataset["text_pl"] = dataset["text_pl"].str.replace("których chciałabym obok mnie w odpowiedzi na moje prośby", "których chciałabym obok mnie podczas moich próśb")
dataset["text_pl"] = dataset["text_pl"].str.replace("Dziękuję wam, moje dzieci, waszej Matce", "Dziękuję wam, moje dzieci. Wasza Matka")
dataset["text_pl"] = dataset["text_pl"].str.replace("Twoje potrzeby, jeden po drugim", "Twoje potrzeby, jedną po drugiej")
dataset["text_pl"] = dataset["text_pl"].str.replace("dlatego wybrałam cię, ze względu na wielką Miłość i wielki Pokój, który masz w swoich sercach", "dlatego wybrałam was, ze względu na wielką Miłość i wielki Pokój, który macie w swoich sercach")
dataset["text_pl"] = dataset["text_pl"].str.replace("Siłą różańca jest zwycięska i potężna broń", "Siła różańca jest zwycięską i potężną bronią")
dataset["text_pl"] = dataset["text_pl"].str.replace("aby otoczyła ją pieszczotą dla wszystkich obecnych", "aby przytuliła wszystkich obecnych")
dataset["text_pl"] = dataset["text_pl"].str.replace("Przyjmijcie Eucharystię", "Przyjmujcie Eucharystię")
dataset["text_pl"] = dataset["text_pl"].str.replace("uczynię łaskę", "udzielę Łaski")
dataset["text_pl"] = dataset["text_pl"].str.replace("aby wszyscy mogli medytować", "aby wszyscy mogli je rozważać")
dataset["text_pl"] = dataset["text_pl"].str.replace(" a nie nic się nie dzieje, a Ziemia może się oczyścić tylko modlitwą i miłością", " żeby nic się nie stało, a Ziemia oczyściła się tylko modlitwą i miłością")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ci, którzy kochają swojego Syna", "Ci, którzy kochają jej Syna")
dataset["text_pl"] = dataset["text_pl"].str.replace("swoim i innym wiernym", "swoim i innych wiernych")
dataset["text_pl"] = dataset["text_pl"].str.replace("Będę przy tobie i będę cię po kolei chwytać za rękę, nadal odmawiać różaniec, ponieważ jest to najsilniejsza i najpotężniejsza broń", "Będę przy was i będę was trzymać za rękę, nadal odmawiajcie różaniec, ponieważ jest to najsilniejsza i najpotężniejsza broń")
dataset["text_pl"] = dataset["text_pl"].str.replace("i przez wielu ludzi, którzy wzywali pomocy dla Pana", "oraz wielu ludzi, którzy wzywali pomocy dla Pana")
dataset["text_pl"] = dataset["text_pl"].str.replace("bo nie będzie zbawiony", "bo nie będą zbawieni")
dataset["text_pl"] = dataset["text_pl"].str.replace("aby zstąpić i wycofać cię, nie zdając", "aby zstąpić i zabrać was. Nie zdając")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ojca w Synu i Ducha", "Ojca i Synu i Ducha")
dataset["text_pl"] = dataset["text_pl"].str.replace("drogi, które wytyczam na waszej drodze", "szlaki, które wytyczam na waszej drodze")
dataset["text_pl"] = dataset["text_pl"].str.replace("Dzisiaj wreszcie mam wśród nas mojego Syna", "Dzisiaj wreszcie mam ze sobą mojego Syna")
dataset["text_pl"] = dataset["text_pl"].str.replace("mojemu Synowi zamieni je w prawdziwą radość", "mojemu Synowi, to zamieni je w prawdziwą radość")
dataset["text_pl"] = dataset["text_pl"].str.replace("Matki Bożej i wznosząc swe oczy ku niebu, która pojawiła się ubrana na biało z świecącą koroną i niebieskim płaszczem z czerwonym sercem w dłoni", "Matki Bożej, wznoszącej swe oczy ku niebu, ubranej na biało, ze świecącą koroną i niebieskim płaszczem trzymającej czerwone serce w dłoni")
dataset["text_pl"] = dataset["text_pl"].str.replace("Nawet dzisiaj Matka Boża jest wśród nas i powiedziała", "Nawet dzisiaj Matka Boża była wśród nas i powiedziała")
dataset["text_pl"] = dataset["text_pl"].str.replace("prosi o przebaczenie, prosi o przebaczenie", "prosi o przebaczenie")
dataset["text_pl"] = dataset["text_pl"].str.replace("obejmijcie swój krzyż, a On zamieni je w radość", "zaakceptujcie swój krzyż, a On zamieni go w radość")
dataset["text_pl"] = dataset["text_pl"].str.replace("a wysłucham was, a także mojego Syna", "a wysłucham was zarówno ja jak i mój Syn")
dataset["text_pl"] = dataset["text_pl"].str.replace(", wstawiam się codziennie u mojego Syna", ". Codziennie wstawiam się za wami u mojego Syna")
dataset["text_pl"] = dataset["text_pl"].str.replace("Proszę, moje dzieci, pozwólcie mu podpisać się pod waszym podpisem", "Proszę, moje dzieci, pozwólWcie mu was opieczętować")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ojca Syna Ducha Świętego", "Ojca, Syna i Ducha Świętego")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ojca Syna i Ducha Świętego", "Ojca, Syna i Ducha Świętego")
dataset["text_pl"] = dataset["text_pl"].str.replace("w moich Synów", "w moich Synach")
dataset["text_pl"] = dataset["text_pl"].str.replace("a dzisiaj zstąpi zbyt wiele łask", "a dzisiaj zstąpi wiele łask")
dataset["text_pl"] = dataset["text_pl"].str.replace("tajemnice fatimskie są na głowach wszystkich", "tajemnice fatimskie znają wszyscy")
dataset["text_pl"] = dataset["text_pl"].str.replace("będzie toczyć się tak, jakby nic się nie działo", "będzie toczyć się tak, jakby nic się nie stało")
dataset["text_pl"] = dataset["text_pl"].str.replace("za wasze tak każdego dnia", "za wasze Tak każdego dnia")
dataset["text_pl"] = dataset["text_pl"].str.replace("waszej misji nie wolno utrudniać", "wasza misja nie może zostać udaremniona")
dataset["text_pl"] = dataset["text_pl"].str.replace("jesteście moimi maluczkimi", "jesteście moimi maleństwami")
dataset["text_pl"] = dataset["text_pl"].str.replace("obejmijcie Jezusa krzyżem w swoich sercach", "przyjmijcie Krzyż Jezusa w swoich sercach")
dataset["text_pl"] = dataset["text_pl"].str.replace("ale nie bójcie się, że zostaniecie napełnieni duchem świętym i ludem Bożym", "ale nie bójcie się, jako Lud Boży zostaniecie napełnieni Duchem Świętym")
dataset["text_pl"] = dataset["text_pl"].str.replace("Japonia i Chile, gdzie ziemia wkrótce się trzęsie", "Wkrótce ziemia się zatrzęsie w Japonii i Chile")
dataset["text_pl"] = dataset["text_pl"].str.replace("ale obejmujesz Serce Jezusa i Jego krzyż", "jeśli obejmiesz Serce Jezusa i Jego krzyż")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ojcze nasz", "Ojcze Nasz")
dataset["text_pl"] = dataset["text_pl"].str.replace(" iw imieniu", " i w imieniu")
dataset["text_pl"] = dataset["text_pl"].str.replace("w swoim sercu", "w swoich sercach")
dataset["text_pl"] = dataset["text_pl"].str.replace("Rozkazuję ci,", "Nakazuję ci,")
dataset["text_pl"] = dataset["text_pl"].str.replace("On i prawdę, miłość i zbawienie", "On jest prawdą, miłością i zbawieniem")
dataset["text_pl"] = dataset["text_pl"].str.replace("Zanieś moje błogosławieństwo swoim rodzinom", "Zanieście moje błogosławieństwo swoim rodzinom")

dataset["text_pl"] = dataset["text_pl"].str.replace("zostaniecie katapultowani", "zostaniecie nagle przeniesieni")
dataset["text_pl"] = dataset["text_pl"].str.replace(" zjednoczymy się w modlitwie", " zjednoczmy się w modlitwie")
dataset["text_pl"] = dataset["text_pl"].str.replace("jestem z wami w was i dla was błogosławię", "jestem z wami i błogosławię was")
dataset["text_pl"] = dataset["text_pl"].str.replace("Czytaj dalej\. \. \. \"", "")
dataset["text_pl"] = dataset["text_pl"].str.replace("praktyka, która podkreśla grzech śmiertelny równy tym, którzy zabijają własnego brata", "praktyka, która jest grzechem śmiertelnym równym zabiciu własnego brata")

dataset["text_pl"] = dataset["text_pl"].str.replace("On wciąż oczekuje Jego przyjścia", "On wciąż oczekuje Swojego przyjścia")
dataset["text_pl"] = dataset["text_pl"].str.replace("wojna. ale jesteście wierni mojemu Synowi 10 przykazaniom i gorliwie odmawiajcie różaniec", "wojna, ale wy bądźcie wierni mojemu Synowi, 10-ciu Przykazaniom i gorliwie odmawiajcie Różaniec")
dataset["text_pl"] = dataset["text_pl"].str.replace(", które zostawia moja ukochana Matka", " mojej ukochanej Matki")
dataset["text_pl"] = dataset["text_pl"].str.replace("nieskazitelnego serca", " niepokalanego serca")
dataset["text_pl"] = dataset["text_pl"].str.replace("płaczę za zagubionymi i zgubionymi", "płaczę za zagubionymi i tymi, którzy się zagubią")
dataset["text_pl"] = dataset["text_pl"].str.replace(", wracać i zanurzać się w miłości Boga, zanim będzie za późno", ". Wracajcie i zanurzajcie się w miłości Boga, zanim będzie za późno")
dataset["text_pl"] = dataset["text_pl"].str.replace(" Niektórzy nie zniosą straszliwej wizji, na tyle, by doprowadzić ich do śmierci", " Dla niektórych wizja będzie na tyle nie do zniesienia, że doprowadzi ich do śmierci")
dataset["text_pl"] = dataset["text_pl"].str.replace("zazdrość i zazdrość", " zazdrość i zawiść")
dataset["text_pl"] = dataset["text_pl"].str.replace("gdzie terroryzm już się opanował i nie ustanie", " gdzie terroryzm już zamieszkał i nie ustanie")
dataset["text_pl"] = dataset["text_pl"].str.replace("Módlcie się, aby ta Europa powróciła razem", "Módlcie się, aby ta Europa się zjednoczyła")
dataset["text_pl"] = dataset["text_pl"].str.replace("słyszę wołający mnie głos", "usłyszałam wołający mnie głos")
dataset["text_pl"] = dataset["text_pl"].str.replace("oboje klękamy w nogach łóżka", "oboje klękamy przy nogach łóżka")
dataset["text_pl"] = dataset["text_pl"].str.replace("moją obecność znakiem o mnie", "moją obecność poprzez mój znak")
dataset["text_pl"] = dataset["text_pl"].str.replace("nieba", "Nieba")
dataset["text_pl"] = dataset["text_pl"].str.replace("niebo", "Niebo")
dataset["text_pl"] = dataset["text_pl"].str.replace("Medytuj", "Rozważaj")
dataset["text_pl"] = dataset["text_pl"].str.replace("będziesz miał", "będziesz miała")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ojca, Syna i Ducha Świętego", "Ojca i Syna i Ducha Świętego")
dataset["text_pl"] = dataset["text_pl"].str.replace("Amen Matka Boża", "Amen. Matka Boża")
dataset["text_pl"] = dataset["text_pl"].str.replace("kilkakrotnie się ono włączało", "kilkakrotnie zamigotało")
dataset["text_pl"] = dataset["text_pl"].str.replace("dlatego wybrałam cię", "dlatego wybrałam was")
dataset["text_pl"] = dataset["text_pl"].str.replace("który masz w swoich sercach", "który macie w sercach")
dataset["text_pl"] = dataset["text_pl"].str.replace("aby udzieliła jej pieszczot wszystkim obecnym", "aby przytuliła za nią wszystkich obecnych")
dataset["text_pl"] = dataset["text_pl"].str.replace("Biorę cię za rękę, ale popełniam błędy, nie daj się zaskoczyć pułapkom", "Będę cię trzymać za rękę, nie zrażaj się gdy będziesz popełniać błędy")
dataset["text_pl"] = dataset["text_pl"].str.replace("szlaki, które wytyczam na waszej drodze, nie mogą być zbaczane", "nie możecie zbaczać ze szlaków, które wytyczam na waszej drodze")
dataset["text_pl"] = dataset["text_pl"].str.replace("jakby nas chronił", "jakby miał nas ochronić")
dataset["text_pl"] = dataset["text_pl"].str.replace("ponieważ jest was wielu", "że jest was wielu")
dataset["text_pl"] = dataset["text_pl"].str.replace("Zaufaj mu, zawsze będę cię chronić", "Zaufaj mu, zawsze będzie was chronić")
dataset["text_pl"] = dataset["text_pl"].str.replace("Podczas objawienia Matka Boża po kolei pieściła wszystkich obecnych", "Podczas objawienia Matka Boża po kolei przytulała wszystkich obecnych")
dataset["text_pl"] = dataset["text_pl"].str.replace("kocham cię jak twoją matkę", "kocham cię jak twoja matka")
dataset["text_pl"] = dataset["text_pl"].str.replace("prosi o przebaczenie i wie, jak prosić innych o przebaczenie", "przebaczaj i proś o przebaczenie")
dataset["text_pl"] = dataset["text_pl"].str.replace("Nalegam, by was prosić o modlitwę", "Nieustannie proszę was o modlitwę")
dataset["text_pl"] = dataset["text_pl"].str.replace("który w końcu otworzyła swoje serce", "którzy w końcu otworzyli swoje serca")
dataset["text_pl"] = dataset["text_pl"].str.replace("otworzyli swoje serca Jezusowi", "otworzyli swoje serca na Jezusa")
dataset["text_pl"] = dataset["text_pl"].str.replace("obejmijcie swój krzyż", "przyjmijcie swój krzyż")
dataset["text_pl"] = dataset["text_pl"].str.replace("nie ma dużo czasu, ale wojny", "nie ma dużo czasu. Wojny")
dataset["text_pl"] = dataset["text_pl"].str.replace("będę obok was pocieszać i chronić", "będę obok, by was pocieszać i chronić")
dataset["text_pl"] = dataset["text_pl"].str.replace("asteroida na ziemię", "asteroida do ziemi")
dataset["text_pl"] = dataset["text_pl"].str.replace("swoim rodzinom, a błogosławię was w", "swoim rodzinom. Błogosławię was w")
dataset["text_pl"] = dataset["text_pl"].str.replace("jeśli obejmiesz Serce Jezusa i Jego krzyż", "jeśli przyjmiesz Serce Jezusa i Jego krzyż")
dataset["text_pl"] = dataset["text_pl"].str.replace("Syna Drogie dzieci", "Syna. Drogie dzieci")

dataset["text_en"] = dataset["text_en"].str.replace(" I love you and I love you", " I love you")


# MARY FORM

dataset_mary = dataset[dataset["author"] == "Holy Mary" ]
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Następnie wziął udział w odmawianiu z nami Zdrowaś Maryjo i pobłogosławił", "Następnie wzięła udział w odmawianiu z nami Zdrowaś Maryjo i pobłogosławiła")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("łem", "łam")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("otworzył", "otworzyła")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("sam zejdę z aniołami", "sama zejdę z aniołami")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("pobłogosławił", "pobłogosławiła")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("łbym", "łabym")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("łbym", "łabym")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Prosił, żeby nigdy nie przestawał", "Prosiła, aby nigdy nie przestawać")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("złam", "złem")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Kościołam", "Kościołem")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("obecnymi, powiedział", "obecnymi, powiedziała")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("ciałam mojego Syna", "ciałem mojego Syna")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Tchnąłam", "Tchnęłam")

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


dataset["text_pl"] = dataset["text_pl"].str.replace("że gdybyś rozumował umysłam ducha, a nie umysłam głowy", "że gdybyście rozumowali duchem, a nie głową")
dataset["text_pl"] = dataset["text_pl"].str.replace("zdałbyś sobie sprawę", "zdalibyście sobie sprawę")
dataset["text_pl"] = dataset["text_pl"].str.replace("Amerykę Środkową, gdzie nastąpi wielkie trzęsienie ziemi ", "Amerykę Środkową, gdzie nastąpi wielkie trzęsienie ziemi.")
dataset["text_pl"] = dataset["text_pl"].str.replace("Wysyłam ci moją matkę", "Posyłam do ciebie moją Matkę")
dataset["text_pl"] = dataset["text_pl"].str.replace("słuchać jej orędzi", "słuchajcie jej orędzi")
dataset["text_pl"] = dataset["text_pl"].str.replace("was pojedynczo", "każdego z was")
dataset["text_pl"] = dataset["text_pl"].str.replace("nawrócili się, teraz nam się kończy", "nawróćcie się, bo czas się kończy")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ojca Syna i ducha świętego", "Ojca i Syna i Ducha Świętego")
dataset["text_pl"] = dataset["text_pl"].str.replace("wlaniu Ducha Świętego", "zstąpieniu Ducha Świętego")
dataset["text_pl"] = dataset["text_pl"].str.replace("nie bój się Jestem z tobą", "nie bój się, bo Jestem z tobą")
dataset["text_pl"] = dataset["text_pl"].str.replace(", módl się za Australię", "Módl się za Australię")
dataset["text_pl"] = dataset["text_pl"].str.replace("Módlcie się ze mną do Ojcze Nasz", "Odmawiajcie ze mną Ojcze Nasz")
dataset["text_pl"] = dataset["text_pl"].str.replace(" Synem Jezusem na nowej ziemi", " Synem Jezusem do nowej ziemi")
dataset["text_pl"] = dataset["text_pl"].str.replace(", dmuchając w ich serca", ", tchnąwszy w ich serca")
dataset["text_pl"] = dataset["text_pl"].str.replace("Czysta Maryja w lewym ramieniu", "Niepokalana Maryja na lewym ramieniu")

dataset = dataset.sort_values(by=["year", "month", "day"])



dataset = dataset[["year", "month", "day", "author", "text", "text_en", "text_pl", "month_string"]]






















dataset.to_csv("2016_cleaned.csv", index=False, encoding="utf-8")


dataset.to_json("trevignano_2016.json",orient="records")





