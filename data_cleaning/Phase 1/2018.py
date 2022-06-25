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
dataset["text"] = dataset["text"].str.replace("Cappella del Sacro Cuore" , "")



# JESUS AUTHOR
dataset["author"] = np.where(dataset["date"] == "04_01_2018", "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["date"] == "30_06_2018", "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["date"] == "04_08_2018", "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["date"] == "28_08_2018", "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["date"] == "22_09_2018", "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["date"] == "13_10_2018", "Jesus Christ", dataset["author"])

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
dataset["text_pl"] = dataset["text_pl"].str.replace(" jest w nich otoczonych", " jest w otoczonych nią")
dataset["text_pl"] = dataset["text_pl"].str.replace("Umiłowane dzieci, jak wiele błogosławieństw zstąpi na was dzisiaj, abyście byli tutaj na modlitwie", "Umiłowane dzieci, jak wiele błogosławieństw zstąpi na was dzisiaj, bo jesteście tutaj na modlitwie")
dataset["text_pl"].str.replace("Syna Ojca i Ducha Świętego", "Ojca i Syna i Ducha Świętego")
dataset["text_pl"].str.replace("Umiłowane dzieci, niebawem przybędę, jestem gotowa", "Umiłowane dzieci, niebawem przybędę, jestem gotowy")
dataset["text_pl"].str.replace(" Będziesz uwielbiony moją miłością", " Będziesz uwielbiona moją miłością")
dataset["text_pl"].str.replace(", kochać się, kochać", ", miłujcie się, miłujcie")
dataset["text_pl"].str.replace("nadejdzie ze mną chwalebne", "nadejdzie z moją chwałą")
dataset["text_pl"].str.replace("posyła mnie po zbawienie ludzi", "posyła mnie by zbawić ludzi")
dataset["text_pl"].str.replace("Dzięki za powitanie mnie", "Dziękuje za powitanie mnie")
dataset["text_pl"].str.replace("z powszechną potopem", "podczas powszechnego potopu")
dataset["text_pl"].str.replace("i to właśnie mi robią", "i to właśnie mi czynią")
dataset["text_pl"].str.replace("obejmują i kochają mój krzyż. dzięki za pocieszenie", "przyjmijcie i kochajcie mój Krzyż. dziękuje za pocieszenie")
dataset["text_pl"].str.replace("Amen O", "Amen. O")
dataset["text_pl"].str.replace("nie opuszczajcie siebie. jedni drugich", "nie opuszczajcie siebie nawzajem")
dataset["text_pl"].str.replace("wielu z nich nie będzie już posłusznych temu, co nie pochodzi od Boga, czujni i używają rozeznania od tego, co pochodzi z nieba, a nie", "wielu z nich nie będzie już posłusznych temu, co nie pochodzi od Boga, będzie czuwać i rozeznawać, co pochodzi z nieba, a co nie.")
dataset["text_pl"].str.replace("Pocieszałeś mnie i rozradowałeś moje serce", "Pocieszyliście mnie i rozradowaliście moje serce")
dataset["text_pl"].str.replace("Dzięki, moje klejnoty", "Dziękuje, moje skarby")
dataset["text_pl"].str.replace("Moi maluchy", "Moje maleństwa")
dataset["text_pl"].str.replace("jak faryzeusze .", "jak faryzeusze.")
dataset["text_pl"].str.replace("że jesteście gotowi codziennie krytykować", "że jesteście gotowi na codzienną krytykę")
dataset["text_pl"].str.replace("Mój umiłowany Antychryst", "Moi umiłowani, Antychryst")
dataset["text_pl"].str.replace("Zwróćcie uwagę na moje miłości", "Bądźcie uważni moi kochani")
dataset["text_pl"].str.replace("Życiem ”", "Życiem")
dataset["text_pl"].str.replace("Błogosławię was jeden po drugim", "Błogosławię was wszystkich")
dataset["text_pl"].str.replace("pozostać zawsze blisko", "bądźcie zawsze blisko")
dataset["text_pl"].str.replace("umieć odróżniać dobro od zła", "umiejcie odróżniać dobro od zła")
dataset["text_pl"].str.replace("nie wierzcie w złych ludzi", "nie wierzcie złym ludziom")
dataset["text_pl"].str.replace("Mój Ojcze, on wkrótce wyeliminuje swoich wrogów, wielu wrogów Boga", "Mój Ojciec, on wkrótce wyeliminuje swoich wrogów, wielu wrogów Boga")
dataset["text_pl"].str.replace("aby wołać moją miłość", "aby wyrazić moją miłość")
dataset["text_pl"].str.replace("Jezusa, proszę", "Jezusa. Proszę")
dataset["text_pl"].str.replace(" i odkupienia\. ludzkości", " i odkupienia ludzkości")
dataset["text_pl"].str.replace("On nie przyszedł, aby się zjednoczyć, ale rozdzielić", "On nie przyszedł, aby zjednoczyć, ale aby rozdzielić")
dataset["text_pl"].str.replace("kiedy nastąpi najstraszniejsze", "kiedy nastąpią najstraszniejsze")
dataset["text_pl"].str.replace("Teraz zostawiam cię w spokoju", "Teraz zostawiam cię w pokoju")
dataset["text_pl"].str.replace("wyrządziłeś zbyt wiele szkody", "wyrządziliście zbyt wiele szkód")
dataset["text_pl"].str.replace("ale aby wam pomóc i waszej duszy", "aby pomóc wam i waszym duszom")
dataset["text_pl"].str.replace("Wystarczy udawać, że budzi wątpliwości w głowach braci", "Dość już wzbudzania wątpliwości w głowach waszych braci")
dataset["text_pl"].str.replace("a diabeł igra z waszymi umysłami i sercami", "to diabeł igra z waszymi umysłami i sercami")
dataset["text_pl"].str.replace("Bożą Módlcie się, módlcie się", "Bożą. Módlcie się, módlcie się")
dataset["text_pl"].str.replace("które przede mną nie załamują się", "które przede mną nie otwierają się")
dataset["text_pl"].str.replace("do siebie podnieść", "do siebie zabrać")
dataset["text_pl"].str.replace("w słowie i ewangelii", "w Słowie i Ewangelii")
dataset["text_pl"].str.replace("Ponieważ chcesz mnie opuścić, kochać moje rany, mój krzyż", "Jeśli nie chcesz mnie opuścić, kochaj moje rany, mój Krzyż")
dataset["text_pl"].str.replace("nie bój się moich dzieci", "nie bójcie się moje dzieci")
dataset["text_pl"].str.replace("nie jesteś sam, proszę cię tylko, abyś całkowicie powierzył się nam, pamiętaj", "nie jesteście sami, proszę was tylko, abyściecałkowicie powierzyli się nam, pamiętajcie")
dataset["text_pl"].str.replace("ale ponieważ człowiek", "ponieważ człowiek")
dataset["text_pl"].str.replace("i waszą wiarę, łagodzą", "i wasza wiara łagodzi")
dataset["text_pl"].str.replace("wcześniej, teraz i zawsze", "kiedyś, teraz i zawsze")
dataset["text_pl"].str.replace("nigdy mnie nie opuszczą", "nigdy mnie nie opuszczajcie")
dataset["text_pl"].str.replace("dlatego będą chroniony od wszelkiego zła", "dlatego będziecie chronieni od wszelkiego zła")
dataset["text_pl"].str.replace("miesiącu poświęcić się w moim niepokalanym sercu", "miesiącu poświęcać się mojemu niepokalanem sercu")
dataset["text_pl"].str.replace("On nie przyszedł tylko was sądzić", "On nie przyszedł tylko po to aby was sądzić")
dataset["text_pl"].str.replace("tę ziemię teraz opanowaną przez grzech wojny i przez Ja, który nie jest Bogiem", "ta ziemia jest teraz opanowana przez grzech wojny i przez 'ja', który nie jest Bogiem")
dataset["text_pl"].str.replace(", odmawiać różaniec, broń powstrzymującą zło, tę, która rozprzestrzenia się po świecie", ", odmawiajcie różaniec, to broń która powstrzymuje rozprzestrzeniające się po świecie zło")
dataset["text_pl"].str.replace("terroryzm nie potrwa długo", "terroryzm niebawem przyjdzie")
dataset["text_pl"].str.replace("Moi maluchy", "Moje maleństwa")
dataset["text_pl"].str.replace("będę tam i jeden po drugim błogosławię i będę wstawiać się przez mojego Syna za wszystkie łaski, którymi jestem w tej chwili\. zapytasz", "będę tam, aby wszystkich pobłogosławić i będę wstawiać się przez mojego Syna za wszystkimi łaskami, o które w tej chwili prosicie")
dataset["text_pl"].str.replace("Drogie dzieci, zawsze przygotowujcie się przed przystąpieniem do Eucharystii, dopiero po przebaczeniu wszystkiego w sercu", "Drogie dzieci, zawsze przygotowujcie się przed przystąpieniem do Eucharystii poprzez przebaczenie wszystkiego w sercu")
dataset["text_pl"].str.replace("miłość, tam jest miłość", "miłosierdzie, tam jest miłość")
dataset["text_pl"].str.replace("chce siać, zniszczenie i zamieszanie", "chce posiać zniszczenie i zamieszanie")
dataset["text_pl"].str.replace("w którym jakakolwiek istota ludzka", "w którym każda istota ludzka")
dataset["text_pl"].str.replace("\”,", ",")
dataset["text_pl"].str.replace("Amen\. \"", "Amen.")
dataset["text_pl"].str.replace("częste zbliżanie się do Eucharystii", "częste przystępujcie do Eucharystii")
dataset["text_pl"].str.replace("On przemówi do waszego serca, idąc za wami, dzień po dniu, aby nie możesz się już bez niego obejść, słuchając pokoju, jaki pozostawi w twoich sercach", "On będzie przemawiał do waszych serca idąc za wami, dzień po dniu, aż nie będziecie mogli się już bez niego obejść, słuchając pokoju, jaki pozostawi w waszych sercach")
dataset["text_pl"].str.replace("służą one temu", "służą one")
dataset["text_pl"].str.replace(" zawsze bądź wierny Ewangelii i kochaj się jak bracia", " zawsze bądźcie wierni Ewangelii i kochajcie się jak bracia")
dataset["text_pl"].str.replace("zstąpi na was\. \.", "zstąpi na was.")
dataset["text_pl"].str.replace("Moi maluchy", "Moje maleństwa")
dataset["text_pl"].str.replace("niestety znaki nieba zawsze szukają wyjaśnień naukowych, ale zrozumieją to ci", "niestety zawsze szuka się wyjaśnień naukowych dla znaków Nieba, ale zrozumieją je ci")
dataset["text_pl"].str.replace("bez ich powtarzania", "i nie popełniajcie go ponownie")
dataset["text_pl"].str.replace("żyjcie w wierze i świadczę", "żyjcie w wierze i zaświadczajcie")
dataset["text_pl"].str.replace("nie daj się złapać bólowi", "nie daj się zdominować bólowi")
dataset["text_pl"].str.replace("Jestem tutaj, tutaj", "Jestem tutaj,")
dataset["text_pl"].str.replace("nie zadając mi zbyt wiele, nie zadając pytań", "nie pytając o zbyt wiele")
dataset["text_pl"].str.replace("chciałbym dać !!", "chciałbym dać!!")
dataset["text_pl"].str.replace("krzyczeć prawdę", "krzyczeć o prawdzie ")
dataset["text_pl"].str.replace("jak wiele oddajecie dla Pana", "jak wiele oddajecie Panu")
dataset["text_pl"] = dataset["text_pl"].str.replace("Jestem tutaj, aby zostawić wam pokój, wyjaśnić i pokochać", "Jestem tutaj, aby wam wyjaśniać, kochać was i dawać pokój")
dataset["text_pl"] = dataset["text_pl"].str.replace("porządkują wasze serca", "porządkujcie wasze serca")
dataset["text_pl"] = dataset["text_pl"].str.replace(", dzięki tym", "Dziękuje tym")
dataset["text_pl"] = dataset["text_pl"].str.replace("Refleksja Nasza najsłodsza", "Refleksja: Nasza najsłodsza")
dataset["text_pl"] = dataset["text_pl"].str.replace("gdzie płoną płomienie", "gdzie płonie ogień")
dataset["text_pl"] = dataset["text_pl"].str.replace("„Twój Jezus", " Twój Jezus")
dataset["text_pl"] = dataset["text_pl"].str.replace("niebo się raduje", "Niebo się raduje")
dataset["text_pl"] = dataset["text_pl"].str.replace("Moje klejnoty, czy nie widzisz znaków nieba", "Moje skarby, czy nie widzicie znaków nieba")
dataset["text_pl"] = dataset["text_pl"].str.replace("iw moim", " i w moim")
dataset["text_pl"] = dataset["text_pl"].str.replace("chciałabym was wszystkich zbawionych", "chciałabym, byście wszyscy byli zbawieni")
dataset["text_pl"] = dataset["text_pl"].str.replace(" iz moim", " i z moim")
dataset["text_pl"] = dataset["text_pl"].str.replace("bo silne trzęsienie ziemi je zadrży", "bo silne trzęsienie ziemi nimi wstrząnie")
dataset["text_pl"] = dataset["text_pl"].str.replace("nawet tych, które kładą", "nawet takich, które kładą")
dataset["text_pl"] = dataset["text_pl"].str.replace("do tej pory dokument dotyczący Eucharystii został podpisany", "dokument dotyczący Eucharystii został już podpisany")
dataset["text_pl"] = dataset["text_pl"].str.replace(" Nie będzie już wierzyć w transfigurację", " Nie będzie się już wierzyć w transfigurację")
dataset["text_pl"] = dataset["text_pl"].str.replace("ojca", "Ojca")
dataset["text_pl"] = dataset["text_pl"].str.replace("niestety odsunęła się od Boga", "niestety odsunęły się od Boga")
dataset["text_pl"] = dataset["text_pl"].str.replace("niech Gaudio do mojego serca ujrzy was tutaj, odpowiadających na moje wezwanie w waszych sercach", " Co za radość dla mojego serca, że widzę was tutaj odpowiadających na moje wezwanie w waszych sercach")
dataset["text_pl"] = dataset["text_pl"].str.replace(" poświęconych mężczyzn i kobiet", " poświęconych mężczyzn i kobiety")
dataset["text_pl"] = dataset["text_pl"].str.replace("miał mało czasu do jego dyspozycji", "miał mało czasu do swojej dyspozycji")
dataset["text_pl"] = dataset["text_pl"].str.replace("wszystko się zmienia i wszystko się zmienia", "wszystko się zmienia")
dataset["text_pl"] = dataset["text_pl"].str.replace("który wzywał,", "który wzywany")
dataset["text_pl"] = dataset["text_pl"].str.replace(" iw końcu", " i w końcu")
dataset["text_pl"] = dataset["text_pl"].str.replace("Zostawiam ci spokój", "Zostawiam ci pokój")
dataset["text_pl"] = dataset["text_pl"].str.replace("Na co jeszcze czekasz Czy wszystko", "Na co jeszcze czekasz. Czy wszystko")
dataset["text_pl"] = dataset["text_pl"].str.replace("zastraszy was", "przestraszy was")
dataset["text_pl"] = dataset["text_pl"].str.replace(", a także w sercach ludzkości", ", także w sercach ludzkości")
dataset["text_pl"] = dataset["text_pl"].str.replace("Jezus wciąż przewiduje czas swojego przyjści", "Jezus wciąż oczekuje czasu swojego przyjści")
dataset["text_pl"] = dataset["text_pl"].str.replace("Otóż,", "Teraz")
dataset["text_pl"] = dataset["text_pl"].str.replace("odwróć się plecami bez prawdziwego nawrócenia i bólu", "odwracasz się plecami bez prawdziwego nawrócenia i bólu")
dataset["text_pl"] = dataset["text_pl"].str.replace("ani nie poniżajcie", "ani nie upadajcie na duchu")
dataset["text_pl"] = dataset["text_pl"].str.replace("córko nieba", "córko Nieba")
dataset["text_pl"] = dataset["text_pl"].str.replace("teraz musisz doskonale powiedzieć ", "teraz musisz dokładnie przekazać ")
dataset["text_pl"] = dataset["text_pl"].str.replace("aby przekonwertować", "aby się nawrócić")
dataset["text_pl"] = dataset["text_pl"].str.replace("danych z nieba", "danych z Nieba")
dataset["text_pl"] = dataset["text_pl"].str.replace("kto mówi, że mówią w moim imieniu", "że ci co mówią, mówią w moim imieniu")
dataset["text_pl"] = dataset["text_pl"].str.replace("iz tego powodu", "i z tego powodu")
dataset["text_pl"] = dataset["text_pl"].str.replace("włączonych lampach", "zapalonych lampach")
dataset["text_pl"] = dataset["text_pl"].str.replace("dajcie się namaszczeni ", "dajcie się naznaczyć ")
dataset["text_pl"] = dataset["text_pl"].str.replace("często jedzcie Eucharystię", "często spożywajcie Eucharystię")
dataset["text_pl"] = dataset["text_pl"].str.replace(", słowo Boże jest jedno", "Słowo Boże jest jedno")
dataset["text_pl"] = dataset["text_pl"].str.replace("amen \”", "Amen")
dataset["text_pl"] = dataset["text_pl"].str.replace(" i będziecie szukać i znaleźć Boga", " ,będziecie szukać i znajdziecie Boga")
dataset["text_pl"] = dataset["text_pl"].str.replace("a także dzieci,", "a także jak dzieci,")
dataset["text_pl"] = dataset["text_pl"].str.replace("żeby mnie naśladowała", "żebym była przy was")
dataset["text_pl"] = dataset["text_pl"].str.replace("Jego słowa, otwórz swoje serca", "Jego słowa, otwórz swoje serce")
dataset["text_pl"] = dataset["text_pl"].str.replace("Teraz błogosławię wam, chorzy prezenty i święte przedmioty", "Teraz błogosławię was, obecnych tu chorych i święte przedmioty")
dataset["text_pl"] = dataset["text_pl"].str.replace("wyznajcie", "spowiadajcie się")
dataset["text_pl"] = dataset["text_pl"].str.replace("witajcie łaski", "przyjmijcie łaski")
dataset["text_pl"] = dataset["text_pl"].str.replace("z dumą i dumą", "z dumą i pychą")
dataset["text_pl"] = dataset["text_pl"].str.replace("uczą się z tego, co powiedział Jezus", "uczcie się tego, co powiedział Jezus")
dataset["text_pl"] = dataset["text_pl"].str.replace("iw pośpiechu", "i w pośpiechu")
dataset["text_pl"] = dataset["text_pl"].str.replace("Czekajcie z miłością, pokojem, pokorą, Stwórcą", "Czekajcie z miłością, pokojem, pokorą na Stwórcę")
dataset["text_pl"] = dataset["text_pl"].str.replace("do Ojca \”", "do Ojca")
dataset["text_pl"] = dataset["text_pl"].str.replace("jest napisane wszystko", "jest tam napisane wszystko")
dataset["text_pl"] = dataset["text_pl"].str.replace("wszystko odkładajcie na bok", "odłóż wszystko inne na bok")

ś







dataset["text_en"] = dataset["text_en"].str.replace("perfume", "scent")
dataset["text_en"] = dataset["text_en"].str.replace("just crucify Jesus", "stop crucifying Jesus")
dataset["text_en"] = dataset["text_en"].str.replace("pride and pride", "pride and arrogance")
dataset["text_en"] = dataset["text_en"].str.replace("Wait with love, peace, humility, the Creator", "Wait for the Creator with love, peace, humility ")





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
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("będę obecny", "będę obecna")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("przyszedłam", "przyszłam")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("towarzyszył", "towarzyszyła")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("trzymał", "trzymała")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Ciałam", "Ciałem")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("ciałam", "ciałem")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Jestem szczęśliwy", "Jestem szczęśliwa")



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








