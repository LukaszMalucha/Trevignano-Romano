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


dataset = pd.read_csv("2017.csv", encoding="utf-8")

dataset["text"] = dataset["text"].str.strip()
dataset["text"] = dataset["text"].str.replace("\n", " ")
dataset["text"] = dataset["text"].str.split("Pubblicato da").str[0]
dataset["text"] = dataset["text"].str.replace("Trevignano romano", "Trevignano Romano")
dataset["text"] = dataset["text"].str.replace("\. ", ".")
dataset["text"] = dataset["text"].str.replace("\.", ". ")
dataset = dataset[dataset["text"].str.contains("Trevignano Romano")]
dataset["text"] = dataset["text"].str.replace("\xa0", "")
dataset["text"] = dataset["text"].str.replace("2017", "2017 ")
dataset["text"] = dataset["text"].str.replace("2017  ", "2017 ")
dataset["text"] = dataset["text"].str.replace("\(rm\)", "")



# Replace Months
dataset["text"] = dataset["text"].str.replace("gennaio 2017", "Gennaio 2017")
dataset["text"] = dataset["text"].str.replace("febbraio 2017", "Febbraio 2017")
dataset["text"] = dataset["text"].str.replace("marzo 2017", "Marzo 2017")
dataset["text"] = dataset["text"].str.replace("aprile 2017", "Aprile 2017")
dataset["text"] = dataset["text"].str.replace("maggio 2017", "Maggio 2017")
dataset["text"] = dataset["text"].str.replace("giugno 2017", "Giugno 2017")
dataset["text"] = dataset["text"].str.replace("luglio 2017", "Luglio 2017")
dataset["text"] = dataset["text"].str.replace("agosto 2017", "Agosto 2017")
dataset["text"] = dataset["text"].str.replace("settembre 2017", "Settembre 2017")
dataset["text"] = dataset["text"].str.replace("ottobre 2017", "Ottobre 2017")
dataset["text"] = dataset["text"].str.replace("novembre 2017", "Novembre 2017")
dataset["text"] = dataset["text"].str.replace("dicembre 2017", "Dicembre 2017")


dataset["text"] = dataset["text"].str.replace("Gennaio 2017", "01 2017")
dataset["text"] = dataset["text"].str.replace("Febbraio 2017", "02 2017")
dataset["text"] = dataset["text"].str.replace("Marzo 2017", "03 2017")
dataset["text"] = dataset["text"].str.replace("Aprile 2017", "04 2017")
dataset["text"] = dataset["text"].str.replace("Maggio 2017", "05 2017")
dataset["text"] = dataset["text"].str.replace("Giugno 2017", "06 2017")
dataset["text"] = dataset["text"].str.replace("Luglio 2017", "07 2017")
dataset["text"] = dataset["text"].str.replace("Agosto 2017", "08 2017")
dataset["text"] = dataset["text"].str.replace("Settembre 2017", "09 2017")
dataset["text"] = dataset["text"].str.replace("Ottobre 2017", "10 2017")
dataset["text"] = dataset["text"].str.replace("Novembre 2017", "11 2017")
dataset["text"] = dataset["text"].str.replace("Dicembre 2017", "12 2017")

dataset["text"] = dataset["text"].str.replace("settembre2017", "09 2017")

dataset["text"] = dataset["text"].str.split("Trevignano Romano")

dataset["text"] = dataset["text"].apply(lambda x: list_cleaner(x))
dataset["text"] = dataset["text"].apply(lambda x: title_remover(x))


text_column = dataset.apply(lambda x: pd.Series(x['text']), axis=1).stack().reset_index(level=1, drop=True)
text_column.name = 'text'
dataset = dataset.drop('text', axis=1).join(text_column)
dataset['text'] = pd.Series(dataset['text'], dtype=object)

dataset["author"] = np.where(dataset["text"].str.contains("Messaggio di Gesù"), "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["text"].str.contains("Messaggio di Gesu"), "Jesus Christ", dataset["author"])



dataset["day"] = dataset["text"].str.split(" 2017 ").str[0]
dataset["day"] = dataset["day"].str.replace(",", "")
dataset["day"] = dataset["day"].str.strip()
dataset["day"] = dataset["day"].str.split(" ").str[0]
dataset["day"]  = dataset["day"].apply(lambda x: add_zero(x))

dataset["date"] = dataset["date"] + "_" + dataset["day"]


dataset['text'] = dataset["text"].str.split(" 2017 ").str[1]
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
dataset['text'] = dataset['text'].str.replace("Messaggio di Gesù; ", "")
dataset['text'] = dataset['text'].str.replace("Messaggio di Gesu' ", "")
dataset['text'] = dataset['text'].str.replace("Messaggio della Madonna:", "")
dataset['text'] = dataset['text'].str.replace("Messaggio della Madonna durante il S. Rosario recitato sul monte. ", "")
dataset['text'] = dataset['text'].str.replace("Messaggio della Madonna a Gisella sul monte. ", "")


dataset['text'] = dataset['text'].str.strip()

dataset['text'] = dataset['text'].str.replace(",", " , ")
dataset['text'] = dataset['text'].str.replace(" , ", ", ")
dataset['text'] = dataset['text'].str.replace(" , ", ", ")
dataset['text'] = dataset['text'].str.replace(" \.  ", ". ")
dataset['text'] = dataset['text'].str.replace("  ", " ")
dataset['text'] = dataset['text'].str.replace("\(Gisella\) Ore 15:30. ", "")
dataset['text'] = dataset['text'].str.replace("  ", " ")
dataset['text'] = dataset['text'].str.replace("S. Rosario recitato sul monte ", "")
dataset['text'] = dataset['text'].str.replace("\(13 04 ", "")


dataset["date"] = dataset["date"].str.split("_")

dataset["date"] = dataset["date"].str[2] + "_" + dataset["date"].str[1] + "_" + dataset["date"].str[0]
dataset = dataset.drop("day", axis=1)


dataset = dataset[dataset["date"] != "''_03_2017"]
dataset = dataset[dataset["date"] != "MASSAGGI_02_2017"]

dataset["text"] = dataset["text"].str.replace("Poi aggiunge: …Dopo", "Poi aggiunge: Dopo")
dataset["text"] = dataset["text"].str.replace("a casa di amici \. ", "a casa di amici. ")
dataset["text"] = dataset["text"].str.replace(" Caltanissetta \(CT\), 20 08", "")
dataset["text"] = dataset["text"].str.replace(" Caltanissetta, 19 10", "")
dataset["text"] = dataset["text"].str.replace("pregate\. !", "pregate!")
dataset["text"] = dataset["text"].str.replace(" QUESTA FOTO E' STATA SCATTATA IL GIORNO 3 APRILE", "")
dataset["text"] = dataset["text"].str.replace("Lubriano 16 04", "")
dataset["text"] = dataset["text"].str.replace("SEGNO DEL GIORNO", "")
dataset["text"] = dataset["text"].str.replace(" Messaggio del 30 04", "")
dataset["text"] = dataset["text"].str.replace("Lubriano 07 05", "")
dataset["text"] = dataset["text"].str.replace(" ''Popolo Mio''  SEGNI DAL CIELO ''I H S'' ", "")
dataset["text"] = dataset["text"].str.replace("*", "")
dataset["text"] = dataset["text"].str.replace("Thialjina 18 07", "")
dataset["text"] = dataset["text"].str.replace("Caltanissetta 17 10", "")
dataset["text"] = dataset["text"].str.replace("Trevignano Romano 31 10", "")
dataset["text"] = dataset["text"].str.replace("Lucca 14 12", "")
dataset["text"] = dataset["text"].str.replace("''Amore''", "")
dataset["text"] = dataset["text"].str.replace("Bagnoregio 26 08", "")

dataset["author"] = np.where(dataset["date"] == "11_10_2016", "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["date"] == "07_02_2017", "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["date"] == "25_03_2017", "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["date"] == "10_06_2017", "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["date"] == "01_08_2017", "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["date"] == "11_07_2017", "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["date"] == "29_08_2017", "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["date"] == "16_09_2017", "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["date"] == "06_10_2017", "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["date"] == "07_11_2017", "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["date"] == "30_12_2017", "Jesus Christ", dataset["author"])
dataset["text"] = dataset["text"].str.split("Amen Messaggio di Dio Padre:Amati figli").str[0]


dataset["date"] = dataset["date"].str.replace("rm", "12")


dataset_2 = pd.DataFrame([["Holy Father", "03_07_2017", "Amati figli, sono vostro Padre! Siate sempre nella mia misericordia. Sono IO che permetto a Gesù di toccare la terra. Per i consacrati: aprite il vostro cuore ed entrerò con il mio amore dentro di voi con una grande luce che vi permetterà di essere i miei figli e i miei amici. Unitevi all'amore di Maria e di Gesù perché voi, grazie al libero arbitrio, siate miei! Vi benedico nel mio nome, nel nome del Figlio e dello Spirito Santo. Amen "]], columns=["author", "date", "text"])


dataset = dataset.append(dataset_2)

translator = google_translator()  


dataset["text_en"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='en'))
dataset["text_pl"] = dataset["text"].apply(lambda x: translator.translate(x,lang_tgt='pl'))


# SPELLING FIX

dataset["text_pl"] = dataset["text_pl"].str.replace("Medytować!", "Medytuj!")
dataset["text_pl"] = dataset["text_pl"].str.replace(" które jest nie tylko duchem, ale także duszy i duszy. fizyczny", " które jest nie tylko duchem, ale także duszą i materią")
dataset["text_en"] = dataset["text_en"].str.replace("spirit, but also of the soul and soul. physical", "spirit, but also of the soul and of the physical")
dataset["text_pl"] = dataset["text_pl"].str.replace("iz matczyną", "i z matczyną")
dataset["text_pl"] = dataset["text_pl"].str.replace(", zadzwoń do mnie, a zawsze będę przy tobie", ", wezwij mnie, a zawsze będę przy tobie")
dataset["text_pl"] = dataset["text_pl"].str.replace("serce Jezusa Moi umiłowani", "serce Jezusa. Moi umiłowani")
dataset["text_pl"] = dataset["text_pl"].str.replace("Niebo istnieje, ale także do diabła", "Niebo istnieje, ale także diabeł")
dataset["text_pl"] = dataset["text_pl"].str.replace("zdradzają mojego Syna, zwłaszcza moich umiłowanych", "zdradzają mojego Syna, zwłaszcza moi umiłowani")
dataset["text_pl"] = dataset["text_pl"].str.replace("Zachowaj spokój, bo mój syn będzie ją chronił do końca, wskrzeszając ją, podobnie jak on, z martwych", "Zachowaj spokój, bo mój syn będzie go chronił do końca, wskrzeszając go, podobnie jak siebie samego, z martwych")
dataset["text_pl"] = dataset["text_pl"].str.replace("cierpi bardziej niż jego ukrzyżowanie", "cierpi bardziej niż podczas ukrzyżowania")
dataset["text_pl"] = dataset["text_pl"].str.replace("co zrobił mój Syn, co było tak złe", "czym zawinił mój Syn")
dataset["text_pl"] = dataset["text_pl"].str.replace("ulotnymi i daleko od Boga, klękajcie", "ulotnymi i oddalili się od Boga, uklęknijcie")
dataset["text_pl"] = dataset["text_pl"].str.replace("która będzie się nieustannie drżeć", "która będzie nieustannie drżeć")
dataset["text_pl"] = dataset["text_pl"].str.replace("otwieram wasze serca, a odkryjecie cuda", "otwórzcie wasze serca, a odkryjecie cuda")
dataset["text_pl"] = dataset["text_pl"].str.replace("żeby nieśli mój uścisk na swoje siostry i ich brac", "żeby nieśli móje orędzie swoim siostrom i braciom")
dataset["text_pl"] = dataset["text_pl"].str.replace(" ponieważ są dla mnie, umiłowane dzieci", " ponieważ są moimi umiłowanymi dziećmi")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ojca, Syna i Ducha Świętego", " Ojca i Syna i Ducha Świętego")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ojca Syna i Ducha Świętego", " Ojca i Syna i Ducha Świętego")
dataset["text_pl"] = dataset["text_pl"].str.replace("którzy doszli do wiary", "którzy odnaleźli wiarę")
dataset["text_pl"] = dataset["text_pl"].str.replace("którzy doszli do wiary", "którzy odnaleźli wiarę")
dataset["text_pl"] = dataset["text_pl"].str.replace("wyjątkowy i wyjątkowy dla Boga", "wyjątkowy dla Boga")
dataset["text_pl"] = dataset["text_pl"].str.replace("święte pisma", "Pismo Święte")
dataset["text_pl"] = dataset["text_pl"].str.replace("będą musieli stawić czoła wielu udrękom", "będzie musiał stawić czoła wielu udrękom")
dataset["text_pl"] = dataset["text_pl"].str.replace("przez tych, którzy się zbliżają", "przez tych, którzy nadchodzą")
dataset["text_pl"] = dataset["text_pl"].str.replace("który jest jedyną tarczą, która ochroni cię przed złem", "który jest jedyną tarczą chroniącą przed złem")
dataset["text_pl"] = dataset["text_pl"].str.replace("Moje maleństwa, płaczę za wami i za wszystko, co zobaczycie, nie płaczcie za zmarłych", "Moje maleństwa, płaczę nad wami i nad wszystkim, co zobaczycie. Nie płaczcie za zmarłymi")
dataset["text_pl"] = dataset["text_pl"].str.replace("Żyjesz w czasach oczyszczenia", "Żyjecie w czasach oczyszczenia")
dataset["text_pl"] = dataset["text_pl"].str.replace("zwłaszcza nowych ludzi, którzy gromadzą się tutaj na modlitwie", "zwłaszcza nowym osobom, którzy gromadzą się tutaj na modlitwie")
dataset["text_pl"] = dataset["text_pl"].str.replace("ponieważ szatan nie da wam rozejmu", "ponieważ szatan nie da wam spokoju")
dataset["text_pl"] = dataset["text_pl"].str.replace("Kocham cię, nie bój się, zawsze będę cię chronić", "Kocham was, nie bójcie się, zawsze będę was chronić")
dataset["text_pl"] = dataset["text_pl"].str.replace("moimi maluchami", "moimi maleństwami")
dataset["text_pl"] = dataset["text_pl"].str.replace(", tylko mój Syn przygotowuje swoje przyjście", ", bo to mój Syn, który przygotowuje swoje przyjście")
dataset["text_pl"] = dataset["text_pl"].str.replace("Amen Matka Boża pobłogosławiła obecnych, jednego po drugim", "Amen. Następnie Matka Boża pobłogosławiła każdego z obecnych.")
dataset["text_pl"] = dataset["text_pl"].str.replace(", tylko mój Syn przygotowuje swoje przyjście", ", bo to mój Syn, który przygotowuje swoje przyjście")
dataset["text_pl"] = dataset["text_pl"].str.replace("aby was z miłością objąć i osądzać jeden po drugim", "aby was wszystkich objąć miłością i osądzić")
dataset["text_pl"] = dataset["text_pl"].str.replace("Umiłowani maluchy", "Umiłowane maleństwa")
dataset["text_pl"] = dataset["text_pl"].str.replace("Módlcie się za Kościół, bo diabeł już się opanował", "Módlcie się za Kościół, w którym diabeł jest już obecny")
dataset["text_pl"] = dataset["text_pl"].str.replace(", ale będę go chronił swoim płaszczem, aby moje ukochane dzieci mogły zostać uratowane", ". Osłonię Kościół swoim płaszczem, aby moje ukochane dzieci mogły zostać uratowane")
dataset["text_pl"] = dataset["text_pl"].str.replace("przede wszystkim zwracać uwagę na światowość, być pokornym i proste i miłosierne", "przede wszystkim światowości, być pokornym, prostym i miłosiernym")
dataset["text_pl"] = dataset["text_pl"].str.replace("Twój Jezus ", "Twój Jezus.")
dataset["text_pl"] = dataset["text_pl"].str.replace("że modląc się do mnie Jezus jest zasłonięty", "że modlitwa do mnie przesłania Jezusa")
dataset["text_pl"] = dataset["text_pl"].str.replace("Trwa wojna z bronią chemiczną", "Nadchodzi wojna z użyciem broni chemicznej")
dataset["text_pl"] = dataset["text_pl"].str.replace("Teraz niech spłynie na was moje święte błogosławieństwo i święte przedmioty", "Teraz niech moje święte błogosławieństwo spłynie na was i święte przedmioty")
dataset["text_pl"] = dataset["text_pl"].str.replace(" ile kłamstwa i obłudy odmawia się Różaniec Święty", "z jakim kłamstwem i obłudą odmawia się Różaniec Święty")
dataset["text_pl"] = dataset["text_pl"].str.replace("ale ostrzeżenie jest ", "choć ostrzeżenie jest ")
dataset["text_pl"] = dataset["text_pl"].str.replace("konwersję", "nawrócenie")
dataset["text_pl"] = dataset["text_pl"].str.replace(" porozmawia z Jezusem, niesie Jego krzyż z miłością", " rozmawiajcie z Jezusem, niecie Jego krzyż z miłością")
dataset["text_pl"] = dataset["text_pl"].str.replace("ale mój ukochany nie będzie musiał się bać", "ale moi ukochani nie będą musieli się bać")
dataset["text_pl"] = dataset["text_pl"].str.replace("Wiedz że cię kocham", "Wiedz, że cię kocham")
dataset["text_pl"] = dataset["text_pl"].str.replace("Wciąż przewiduję moje nadejście, ponieważ ta ziemia jest zbyt zanieczyszczona", "Oczekujcie mojego drugiego przyjcia, ponieważ ta ziemia jest zbyt zanieczyszczona")
dataset["text_pl"] = dataset["text_pl"].str.replace("wielu ucieknie", "wielu będzie uciekać")
dataset["text_pl"] = dataset["text_pl"].str.replace("w Jezusie W tym okresie Wielkiego Postu", "w Jezusie. W tym okresie Wielkiego Postu")
dataset["text_pl"] = dataset["text_pl"].str.replace("i nie módl się z bezwładu", "i nie módl się chaotycznie")
dataset["text_pl"] = dataset["text_pl"].str.replace("Wkrótce na ziemię pojawi się meteoryt", "Wkrótce na ziemię spadnie meteoryt")
dataset["text_pl"] = dataset["text_pl"].str.replace("Niech twoje łzy wyschną z twojej niebiańskiej matki", "Pozwól twojej niebiańskiej matce otrzeć twoje łzy")
dataset["text_pl"] = dataset["text_pl"].str.replace("Amen Matka Boża", "Amen. Matka Boża")
dataset["text_pl"] = dataset["text_pl"].str.replace("powołać was jeden po drugim", "powołać was wszystkich")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ogłoś jego przybycie wszystkim", "Ogłoś Jego przybycie wszystkim")
dataset["text_pl"] = dataset["text_pl"].str.replace("Wyznajcie się i jedzcie tyle", "Spowiadajcie się i jedzcie tyle")
dataset["text_pl"] = dataset["text_pl"].str.replace("chociaż Go pluli i obrażali", "chociaż Go opluwali i obrażali")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ten różaniec, odmawiany na górze w Wielki Czwartek, został wyraźnie wezwany przez Matkę Bożą", "O ten różaniec, odmawiany na górze w Wielki Czwartek, wyraźnie prosiła Matka Boża")
dataset["text_pl"] = dataset["text_pl"].str.replace("Moi maluchy", "Moje maleństwa")
dataset["text_pl"] = dataset["text_pl"].str.replace("Czyńcie wieczerniki modlitwy", "Twórzcie wieczerniki modlitwy")
dataset["text_pl"] = dataset["text_pl"].str.replace("O!!", "O!")
dataset["text_pl"] = dataset["text_pl"].str.replace("jestem i zawsze będę obok was. Tobie. ", "jestem i zawsze będę obok was. ")
dataset["text_pl"] = dataset["text_pl"].str.replace("Moją wielką radością jest widok jednego z moich ulubionych dzieci, do którego zawsze w pokorze wzywam zjednoczonego z wami", "Moją wielką radością jest widok każdego z moich ulubionych dzieci, do którego zawsze w pokorze wzywam zjednoczonego z wami")
dataset["text_pl"] = dataset["text_pl"].str.replace("Jezusa Umiłowane dzieci", "Jezusa. Umiłowane dzieci")
dataset["text_pl"] = dataset["text_pl"].str.replace("tego wszystkiego by uniknąć", "można było tego wszystkiego by uniknąć")
dataset["text_pl"] = dataset["text_pl"].str.replace("prosiłam niektóre narody o poświęcenie mego niepokalanego serca", "prosiłam niektóre narody o poświęcenie mojemu Niepokalanemu Sercu")
dataset["text_pl"] = dataset["text_pl"].str.replace("iz odwagą", "i z odwagą")
dataset["text_pl"] = dataset["text_pl"].str.replace("i zawsze wstawiaj się za tobą", "i zawsze wstawiam się za wami")
dataset["text_pl"] = dataset["text_pl"].str.replace(" \. Amen ", ". Amen")
dataset["text_pl"] = dataset["text_pl"].str.replace("Znam i znam Twoje cierpienia i udręki", "Znam Twoje cierpienia i udręki")
dataset["text_pl"] = dataset["text_pl"].str.replace("Modlę się do was wszystkich o życie w pokorze i ciszy", "Modlę się, byście wszyscy żyli w pokorze i ciszy")
dataset["text_pl"] = dataset["text_pl"].str.replace("Myślisz o każdym", "Myśli o nas wszystkich")
dataset["text_pl"] = dataset["text_pl"].str.replace("Co więcej muszę zrobić, aby mój Syn Jezus kochał? ", "Co więcej musisz zrobić, aby mój Syn Jezus cię kochał? ")
dataset["text_pl"] = dataset["text_pl"].str.replace("Proście o łaski, ale nie módlcie się z otwartym sercem", "Proście o łaski, ale nie modlicie się z otwartym sercem")
dataset["text_pl"] = dataset["text_pl"].str.replace("której przewodnictwo prowadzi do otchłani", "których przewodnictwo prowadzi do otchłani")
dataset["text_pl"] = dataset["text_pl"].str.replace("Umiłowani w niebie", "Umiłowani w Niebie")
dataset["text_pl"] = dataset["text_pl"].str.replace(" Lud Boży, umiłowany przeze mnie i Trójcę Przenajświętszą, aby was zjednoczyć jest tym, czego pragnę dla całej ludzkości", " Ludu Boży, umiłowany przeze mnie i Trójcę Przenajświętszą, czego pragnę dla całej ludzkości, to aby was zjednoczyć.")
dataset["text_pl"] = dataset["text_pl"].str.replace(" Zepsucie ludzi nie ma już czasu", "Nadszedł koniec ludzkiego zepsucia")
dataset["text_pl"] = dataset["text_pl"].str.replace("jak pastorzy", "jak pasterze")
dataset["text_pl"] = dataset["text_pl"].str.replace("Módlcie się za Francję Od chwili", "Módlcie się za Francję. Od chwili")
dataset["text_pl"] = dataset["text_pl"].str.replace("każdego dnia zobaczycie i poczujecie moją obecność", "każdego dnia będziecie widzieć i odczuwać moją obecność, która powzolić wam odczuć moją miłość do was ")
dataset["text_pl"] = dataset["text_pl"].str.replace("Moi umiłowani, wkrótce będziecie się cieszyć rozkoszami", "Moi umiłowani, wkrótce będziecie się radować uciechami")
dataset["text_pl"] = dataset["text_pl"].str.replace("już jest na waszych głowach", "już jest nad waszymi głowami")
dataset["text_pl"] = dataset["text_pl"].str.replace("mojego syna", "mojego Syna")
dataset["text_pl"] = dataset["text_pl"].str.replace("Pomaga zrozumieć, jak wielka jest miłosierna i sprawiedliwa miłość Jezusa", "Pomoże wam zrozumienie, jak wielka jest miłosierna i sprawiedliwa miłość Jezusa")
dataset["text_pl"] = dataset["text_pl"].str.replace("świętych pism przeszłości", "Świętych Pism z przeszłości")
dataset["text_pl"] = dataset["text_pl"].str.replace("czy w ciemność", "czy wybrać ciemność")
dataset["text_pl"] = dataset["text_pl"].str.replace("Moja umiłowana Matko, dotykaj ziemi nie po to", "Moja umiłowana Matka przychodzi na ziemię nie po to")
dataset["text_pl"] = dataset["text_pl"].str.replace("miłości, to jedyne uczucie", "miłości. To jedyne uczucie")
dataset["text_pl"] = dataset["text_pl"].str.replace("kochać się z wami wszystkimi", "miłójcie się wzajemnie")
dataset["text_pl"] = dataset["text_pl"].str.replace("Zawsze podążajcie za moimi orędziami i rozpowszechniajcie je i nigdy nie odchodźcie", "Podążanie za moimi orędziami, rozpowszechnianie ich i nie zawracanie")
dataset["text_pl"] = dataset["text_pl"].str.replace("dając wam to, o co prosi Jezus, pokój, miłość i miłosierdzie", "przynosi to, o co prosi Jezus - pokój, miłość i miłosierdzie")
dataset["text_pl"] = dataset["text_pl"].str.replace("która jest droga Święta", "która jest droga Świętą")
dataset["text_pl"] = dataset["text_pl"].str.replace("ostrzeżenie jest blisko", "Ostrzeżenie jest blisko")
dataset["text_pl"] = dataset["text_pl"].str.replace("przyjście mojego Syna Jezusa Moje umiłowane", "przyjście mojego Syna Jezusa. Moje umiłowane")
dataset["text_pl"] = dataset["text_pl"].str.replace("i rozkoszne dzieci", "i radosne dzieci")
dataset["text_pl"] = dataset["text_pl"].str.replace("Biada tym, którzy szydzą z moich dzieci, zwłaszcza tym, którzy przynoszą światu moje słowo", "Biada tym, którzy wyszydzają moje dzieci, zwłaszcza te, którzy przynoszą światu moje słowo")
dataset["text_pl"] = dataset["text_pl"].str.replace("Błogosławię was jeden po drugim", "Błogosławię was wszystkich")
dataset["text_pl"] = dataset["text_pl"].str.replace("Umiłowane dzieci, płaczę za wami i nadchodzące czasy będą bardzo trudne", "Umiłowane dzieci, płaczę nad wami i nad nadchodzącącymi czasami - będą bardzo trudne")
dataset["text_pl"] = dataset["text_pl"].str.replace("zrujnować, proszę dzieci", "zrujnować. Proszę dzieci")
dataset["text_pl"] = dataset["text_pl"].str.replace("przywiązał je do swoich łańcuchów", "przywiązał ich do swoich łańcuchów")
dataset["text_pl"] = dataset["text_pl"].str.replace("aby wam pomóc i chronić", "aby wam pomóc i was chronić")
dataset["text_pl"] = dataset["text_pl"].str.replace(", błogosławieństwo moje i Ojca", ", Błogosławieństwo moje i Ojca")
dataset["text_pl"] = dataset["text_pl"].str.replace("Pisma święte", "Pisma Święte")
dataset["text_pl"] = dataset["text_pl"].str.replace("Gisella dzisiaj będziesz miała wspaniały znak, ale bądź spokojny", "Gisello, dzisiaj będziesz miała wspaniały znak, ale bądź spokojna")
dataset["text_pl"] = dataset["text_pl"].str.replace("aby wasze trudności nie stały się smutkiem, który nie pochodzi od Boga, ale mój Syn przemieni ich w radość", "aby wasze trudności nie stały się dla was nie pochodzącym od Boga smutkiem, lecz by mój Syn przemienił je w radość")
dataset["text_pl"] = dataset["text_pl"].str.replace(" i będzie miał wiarę, miej wiarę, miej wiarę", ". Miejcie wiarę, miejcie wiarę, miejcie wiarę")
dataset["text_pl"] = dataset["text_pl"].str.replace("wkrótce nastąpi prezentacja antychrysta,", "wkrótce antychryst zostanie przedstawiony,")
dataset["text_pl"] = dataset["text_pl"].str.replace("jedząc Eucharystię", "spożywając Eucharystię")
dataset["text_pl"] = dataset["text_pl"].str.replace("teraz wszystko jest w jednej chwili", "teraz wszystko stanie się nagle")
dataset["text_pl"] = dataset["text_pl"].str.replace("Moja matka", "Moja Matka")
dataset["text_pl"] = dataset["text_pl"].str.replace(", aby nikogo przekonywać o prawdziwości orędzi", "na przekonywanie o prawdziwości orędzi")
dataset["text_pl"] = dataset["text_pl"].str.replace("szansa na zbawienie", "szansa na Zbawienie")
dataset["text_pl"] = dataset["text_pl"].str.replace("kiedy zrozumiecie znaki, że moje przyjście będzie blisko", "gdy zrozumiecie znaki, moje przyjście będzie blisko")
dataset["text_pl"] = dataset["text_pl"].str.replace("stawiając je przeciwko sobie", "stawiając ich przeciwko sobie")
dataset["text_pl"] = dataset["text_pl"].str.replace("Wszystko się rozpada wraz z modlitwą", "Wszystko się rozpada, także modlitwą")
dataset["text_pl"] = dataset["text_pl"].str.replace("tutaj zbliża się sprawiedliwość i kara", "zbliża się sprawiedliwość i kara")
dataset["text_pl"] = dataset["text_pl"].str.replace("pokój, miłość i miłość", "pokój, miłość i miłosierdzie")
dataset["text_pl"] = dataset["text_pl"].str.replace("razem z synem", "razem z Synem")
dataset["text_pl"] = dataset["text_pl"].str.replace(" ziemia nadal będzie się trząść, a morza będą się trząść", " ziemia i morza nadal będą niespokojne")
dataset["text_pl"] = dataset["text_pl"].str.replace("który będziecie mogli nieść,", "który będziecie musieli nieść,")
dataset["text_pl"] = dataset["text_pl"].str.replace("Szatan, Niebo", "Szatan. Niebo")
dataset["text_pl"] = dataset["text_pl"].str.replace("Wyznajcie moje dzieci", "Spowiadajcie się moje dzieci")
dataset["text_pl"] = dataset["text_pl"].str.replace("mój syn", "mój Syn")
dataset["text_pl"] = dataset["text_pl"].str.replace("Jezus był z wami jedną i jedyną rzeczą", "tylko Jezus był w was")
dataset["text_pl"] = dataset["text_pl"].str.replace("cierpienia i wołam o to", "cierpienia i płaczę z powodu tego")
dataset["text_pl"] = dataset["text_pl"].str.replace("szczerego iz", "szczerego i z")
dataset["text_pl"] = dataset["text_pl"].str.replace("chleb życia", "Chleb Życia")
dataset["text_pl"] = dataset["text_pl"].str.replace("która ma zrujnować", "która ma zostać zniszczona")
dataset["text_pl"] = dataset["text_pl"].str.replace("doradzać i pouczać", "doradzać i was pouczać")
dataset["text_pl"] = dataset["text_pl"].str.replace("i przywiązuję wagę do Eucharystii", "i przywiązujcię należną uwagę do Eucharystii")





dataset["text_en"] = dataset["text_en"].str.replace("I am and will always be next to you. to you", "I am and will always be at yur side")








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
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("namaścił nas pojedynczo", "namaściła nas pojedynczo")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("zostałam posłany przez Boga", "zostałam posłana przez Boga")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Jestem bardzo zasmucony, bo wiem, co cię czeka", "Jestem bardzo zasmucona, bo wiem, co was czeka")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("rozłem", "rozłam")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("nie dajcie się przyłapać na przybyciu Mojego Syna", "nie dajcie się zaskoczyć przybyciem Mojego Syna")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("między dobrem a błędem", "między prawdą a błędem")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("do was z nieba", "do was z Nieba")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("pokoju , Będę", "pokoju. Będę")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("powierzony.", "w zaufaniu.")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("zamknijcie uszy", "zatkajcie uszy")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("święte pisma", "Pismo Święte")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("13.04", "13.04)")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("zgromadzeni, czuję ", "zgromadzeni. Czuję ")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("światłam", "światłem")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("wzywany", "wzywana")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("będę obecny", "będę obecna")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("ile radości dajecie mi, widząc was tutaj na modlitwie", "ile radości dajecie mi, gdy was widzę tutaj na modlitwie")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("aby cię chronili, posyłam ich", "których posyłam aby cię chronili")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Mój Synu", "Mój Syn")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Moi umiłowani, co się dzieje", "Moi umiłowani, dzieje się to")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("dzień wielkiego odstępstwa w kościele, to jest dzisiaj,", "dzień wielkiego odstępstwa w kościele nadszedł,")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Nie czekaj na znaki, które nadejdą, aby cię nawrócić, ale zrób to teraz", "Nie czekaj na nadchodzące znaki aby się nawrócić, ale zrób to teraz")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("rozkoszami", "radościami")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("jest również spowodowane brakiem konsekracji Rosji, o co prosiłam w Fatimie, aby wojny nie rozpoczęły które są teraz nieuchronne", "jest również spowodowane brakiem konsekracji Rosji. Prosiłam o to w Fatimie, aby nie rozpoczęły się wojny, które są już teraz nieuchronne")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Amen Po", "Amen. Po")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Jestem twoją matką i obok ciebie biorę cię za rękę", "Jestem twoją matką, stoję tu i trzymam cię za rękę")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("cierpienia, cierpienia", "troski, cierpienia")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Jezus w tych czasach bardzo dziękuje", "Jezus w tych czasach udziela wielu łask")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("bo mój syn ", "bo mój Syn ")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("wasze serca, bo po cierpieniach otworzy w waszych sercach drzwi miłości i pokój powróci ", "Kochane dzieci, wszystko się wypełni, jendak Jezus będzie przy was. Nie zadręczajcie więc waszych serc, bo po cierpieniu On otworzy drzwi miłości w waszych sercach i powróci pokój")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("iw Moje Imię", "i w Moje Imię")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("teraz wszystko jest szybko zakończone", "niebawem wszystko się skończy")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("kontynuujcie bez przerwy na modlitwie odmawianie Różańca Świętego", "kontynuujcie bez przerw modlitwę Różańca Świętego")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Moi maluchy", "Moje maleństwa")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace(" a wielki wulkan jest gotowy na jego przebudzenie", " a wielki wulkan jest gotowy do przebudzenia")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Ojcowskie imię Syna i Ducha Świętego", "imię Ojca i Syna i Ducha Świętego")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("trzyma razem prawdziwą wiarę", "utrzymuje prawdziwą wiarę")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Wkrótce przybędzie mój Syn, tak jak odszedł", "Wkrótce przybędzie mój Syn, tak samo jak odszedł")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("nadal idziecie za nim 10 przykazań", "nadal przestrzegajcie 10 przykazań")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("uważajcie na dzieci", "uważajcie dzieci")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("powierzając się ", "powierzajcie się ")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("jak bardzo prosi o siebie i", "jak bardzo prosi dla siebie o")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Klejnoty mojego serca Chronię", "Klejnoty mojego serca, chronię")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Przyjdzie na sąd, aby ci, którzy nie widzą, i ci, którzy widzą, stali się ślepymi", "Przyjdzie aby sądzić, by ci, którzy nie widzą zobaczyli, i ci, którzy widzą, stali się ślepcami")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("jaką będziecie mieli z nieba", "jaką będziecie mieli z Nieba")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("radości, miłości i miłości", "radości, miłosierdziu i miłości")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("że będziecie jej potrzebować. z drugiej", "że będziecie się potrzebować nawzajem")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Moje słodkie dzieci, z mojego serca", "Moje słodkie dla mojego serca dzieci,")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("pocieszycie moje serce swoimi", "pocieszacie moje serce swoimi")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("ponieważ nikt nie uwierzył i ci, którzy nas znali, unikali nas, tak jak wtedy ci, którzy są wierni Jezusowi, będą unikani i oczerniani, ponieważ w ich domach i sercach nie ma miłość", "ponieważ nikt nie uwierzył i ci, którzy nas znali, unikali nas, podobnie będą teraz unikać i oczerniać tych, którzy są wierni Jezusowi, bo w ich domach i sercach nie ma miłość")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Moi bracia i ludu", "Moi bracia i mój ludu")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace(" proszę was, ale jak wielka jest wasza miłość do mnie i jak wielka jest wasza wiara, która nie powinna być uwarunkowana otrzymanymi łaskami", " proszę was, by to jak wielka jest wasza miłość do mnie i jak wielka jest wasza wiara, nie było uwarunkowane otrzymanymi łaskami")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace(" Twoja miłość, chcę, żeby była bezwarunkowa i absolutna", " Chcę, by Twoja miłość była bezwarunkowa i absolutna")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace(" i prawdę mówiąc, mówię Ci", " i zaprawdę powiadam Ci")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("a Twoja miłość nie może wzrastać\. lub zmniejsz w zależności od tego, co masz lub czego nie masz", " a Twoja miłość nie może wzrastać lub zmniejszać się w zależności od tego, co masz lub czego nie masz")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("iz pokorą", "i z pokorą")



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


dataset.to_csv("2017_cleaned.csv", index=False, encoding="utf-8")
dataset.to_json("trevignano_2017.json",orient="records")







