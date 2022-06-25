# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np


dataset_2016 = pd.read_json("trevignano2016.js" )
dataset_2017 = pd.read_json("trevignano2017.js" )
dataset_2018 = pd.read_json("trevignano2018.js" )
dataset_2019 = pd.read_json("trevignano2019.js" )
dataset_2020 = pd.read_json("trevignano2020.js" )



dataset_2016["text_pl"] = dataset_2016["text_pl"].str.replace("Drogie dzieci, jakie szczęście w moim sercu, widząc was wszystkich zebranych tutaj na modlitwie", "Drogie dzieci, jakie szczęście w moim sercu, widzieć was wszystkich zebranych tutaj na modlitwie")
dataset_2016["text_pl"] = dataset_2016["text_pl"].str.replace("Ale nawet to staje się trudne", "Jednak nawet to staje się trudne")
dataset_2016["text_pl"] = dataset_2016["text_pl"].str.replace("Ducha Świętego\.\.", "Ducha Świętego.")
dataset_2016["text_pl"] = dataset_2016["text_pl"].str.replace("odmawienie", "odmawianie")
dataset_2016["text_pl"] = dataset_2016["text_pl"].str.replace("ja jak i", "ja, jak i")
dataset_2016["text_pl"] = dataset_2016["text_pl"].str.replace("zatakowana", "zaatakowana")
dataset_2016["text_pl"] = dataset_2016["text_pl"].str.replace("pokutujcie z całego serca On wciąż oczekuje Swojego przyjścia,", "pokutujcie z całego serca, On wciąż oczekuje Swojego przyjścia,")
dataset_2016["text_pl"] = dataset_2016["text_pl"].str.replace("10-ciu", "Dziesięciu")
dataset_2016["text_pl"] = dataset_2016["text_pl"].str.replace("zangażowane", "zaangażowane")
dataset_2016["text_pl"] = dataset_2016["text_pl"].str.replace("Ale jestem z wami", "Jednak jestem z wami")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("żeby nieśli móje", "żeby nieśli moje")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("siostrom i braciomi", "siostrom i braciom")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("zatakowana", "zaatakowana")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("zangażowane", "zaangażowane")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("biczowany, tak jak wtedy", "biczowany tak jak wtedy")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("uszczęśliwiacie gdy", "uszczęśliwiacie, gdy")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("Ale jak ograniczona jest twoja miłość do Niego", "Jednak jak ograniczona jest twoja miłość do Niego")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("przyjcia", "przyjścia")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("pokutujcie i przygotujcie się", "pokutujcie i się przygotujcie")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("Co więcej muszę", "Co więcej, muszę")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("znak:'Mój lud'", "znak: 'Mój lud'")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("droga Świętą", "drogą Świętą")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("nadchodzącącymi", "nadchodzącymi")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("nie pochodzącym od Boga smutkiem", "niepochodzącym od Boga smutkiem")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("Po tak wielu instrukcjach do dziś, proszę was o pilne nawrócenie i miłość", "Po tak wielu dotychczasowych wskazaniach, proszę was o pilne nawrócenie i miłość")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("przywiązujcię należną", "przywiązujcie należną")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("Mój Syn, pozwala", "Mój Syn pozwala")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("posyłam aby cię chronili", "posyłam, aby cię chronili")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("trwożcie", "trwóżcie")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("można było tego wszystkiego by uniknąć", "można było tego wszystkiego uniknąć")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("uważajcie dzieci! prześladowania trwają", "uważajcie dzieci! Prześladowania trwają")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("On przyjdzie aby sądzić", "On przyjdzie, aby sądzić")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("nikt nie powie nic oprócz chwalcie Boga za Jego moc i wielkość", "nikt nie powie nic oprócz 'Chwalcie Boga za Jego moc i wielkość'")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("dotyka ziemi prosząc o nawrócenie i miłość", "dotyka ziemi, prosząc o nawrócenie i miłość")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("połączą się tworząc wielki czerwony krzyż,", "połączą się, tworząc wielki czerwony krzyż,")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("Po tak wielu dotychczasowych wskazaniach, proszę", "Po tak wielu dotychczasowych wskazaniach proszę")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("kochajcie mnie tak jak ja was kocham", "kochajcie mnie, tak jak ja was kocham")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("którzy nie widzą zobaczyli", "którzy nie widzą, zobaczyli")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("pokutujcie krocząc drogą świętości.", "pokutujcie, krocząc drogą świętości.")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("Jezus przychodząc na świat, pozostawił swoje przykazania", "Jezus, przychodząc na świat, pozostawił swoje przykazania")
dataset_2017["text_pl"] = dataset_2017["text_pl"].str.replace("Oh!", "Och!")

dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("posyła mnie by zbawić ludzi", "posyła mnie, by zbawić ludzi")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("zniszczona, tak jak", "zniszczona tak jak")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("dziękuje za pocieszenie", "Dziękuje za pocieszenie")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("przyjmijcie tę miłość i radujcie się", "przyjmijcie tę miłość i się radujcie")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("zatakowana", "zaatakowana")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("W tym początku Wielkiego Postu, pamiętaj ", "W tym początku Wielkiego Postu pamiętaj, ")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("W tą Wielkanoc", "W Wielkanoc")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace(" tam gdzie jest Bóg", " tam, gdzie jest Bóg")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("a tam gdzie jest miłość", "a tam, gdzie jest miłość")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("Proszę więc, moje dzieci", "Proszę więc moje dzieci")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("jałowość, tak jak", "jałowość tak jak")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("z taką siłą, jak nigdy", "z taką siłą jak nigdy")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("że będziecie coraz bardziej wyjątkowi", "że będziecie coraz bardziej nadzywczajni")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("To co poczujecie to wielka siła", "To, co poczujecie to wielka siła")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("nie brudzcie swoich rąk", "nie brudźcie swoich rąk")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("Ale jak wielu musi jeszcze", "Jednak jak wielu musi jeszcze")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("poczujesz będzie niewyobrażalne.", "poczujesz, będzie niewyobrażalne.")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("jest napisane musi się wydarzyć przed powrotem Jezusa.", "jest napisane, musi się wydarzyć przed powrotem Jezusa.")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("stójcie ze skrzyżowanymi rękami nic nie robiąc", "siedźcie z założonymi rękami, nic nie robiąc")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("miłòujcie się jak bracia", "miłujcie się jak bracia")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("które się zbliżają są krótkie i", "które się zbliżają, są krótkie i")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("przyjdzie na świat niosąc swój krzyż zbawienia dla ludzkości", "przyjdzie na świat, niosąc swój krzyż zbawienia dla ludzkości")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("będzię", "będzie")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("cierpię widząc, jak wielu modli się", "cierpię, widząc, jak wielu modli się")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("Pragnę żebyście słuchali tylko słów moich prawdziwych posłańców", "Pragnę, żebyście słuchali tylko słów moich prawdziwych posłańców")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("a gdzie jest Miłość tam jestem", "a gdzie jest Miłość, tam ja jestem")
dataset_2018["text_pl"] = dataset_2018["text_pl"].str.replace("Oh!", "Och!")


dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("i prawie rozpadł się", "i prawie się rozpadł")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("ani stary ani młody", "ani stary, ani młody")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("wydaje się być zdominowany", "wydaje się zdominowany")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("o! jak", "oh! Jak")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("Królestwo Niebieskie\.\.", "Królestwo Niebieskie.")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace(" czasy i wzmocnijcie się", " czasy i się wzmocnijcie")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("wszystkiego co materialne", "wszystkiego, co materialne")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("czuję w sercu widząc was tutaj na modlitwie,", "czuję w sercu, widząc was tutaj na modlitwie,")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("czasy, które nadchodzą będą bardzo trudne", "nadchodzące czasy będą bardzo trudne")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("które wiedzą jak mocno dmuchać w umysły niszcząc myśli", "które wiedzą, jak mocno dmuchać w umysły niszcząc myśli")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("wybrali króla piekła będzie cierpieć straszliwie,", "wybrali króla piekła, będzie cierpieć straszliwie,")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("która zginie wybierając rzeczy ziemskie", "która zginie, wybierając rzeczy ziemskie")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("idąc za Ewangelią będą służyć Bogu swoim świadectwem i", "idąc za Ewangelią, będą służyć Bogu swoim świadectwem i")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("będzie znienawidzonych począwszy od hierarchów Kościoła", "będzie znienawidzonych, począwszy od hierarchów Kościoła")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("będziecie mieli więcej niż możecie sobie wyobrazić.", "będziecie mieli więcej, niż możecie sobie wyobrazić.")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("kochajcie mnie tak jak ja was kocham i", "kochajcie mnie tak, jak ja was kocham i")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("kiedy się cieszycie są Moimi darami", "kiedy się cieszycie, są Moimi darami")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("płaczecie są Moimi łzami,", "płaczecie, są Moimi łzami,")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("zostało wam pozostawione nie jest do interpretacji,", "zostało wam pozostawione, nie jest do interpretacji,")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("odczuwam widząc was zgromadzonych na modlitwie w tym błogosławionym miejscu,", "odczuwam, widząc was zgromadzonych na modlitwie w tym błogosławionym miejscu,")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("a gdzie jest Miłość tam jestem", "a gdzie jest Miłość, tam ja jestem")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("nawrócili się dokonując wielkiego oczyszczenia z piękną spowiedzią,", "nawrócili się, dokonując wielkiego oczyszczenia z piękną spowiedzią,")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("spowiedzią,abyście", "spowiedzią, abyście")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("O! drogie dzieci", "Oh! Drogie dzieci")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("dam wam więcej niż możecie unieść.", "dam wam więcej, niż możecie unieść.")
dataset_2019["text_pl"] = dataset_2019["text_pl"].str.replace("Oh!", "Och!")

dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("Znaki, były naszą czystą radością", "Znaki były naszą czystą radością")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("Córko moja, bądź potulna", "Córko moja bądź łagodna")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace(" Ale ty nadal nie rozumiesz", " Jednak ty nadal nie rozumiesz")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace(" jestem tutaj by prosić was byście byli gotowi", " jestem tutaj, by prosić was abyście byli gotowi")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("szansę by wybrać stronę", "szansę, by wybrać stronę")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("O! ileż rozpaczy", "Oh! ileż rozpaczy")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("O! jak wiele niegodziwości", "Oh! Jak wiele niegodziwości")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("byłam bardzo szczęśliwa widząc was zgromadzonych na uroczystej modlitwie i", "byłam bardzo szczęśliwa, widząc was zgromadzonych na uroczystej modlitwie i")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("śpiewająć chwałę Panu", "śpiewając chwałę Panu")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("przyjdzie wcześniej niż myślicie,", "przyjdzie wcześniej, niż myślicie,")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("wiem jak wiele cierpienia spadło na ludzkość,", "wiem, jak wiele cierpienia spadło na ludzkość,")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("świadczcie śpiewając hymny do Pana,", "świadczcie, śpiewając hymny do Pana,")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace(" chcecie zbawienia powierzcie wszystko Bogu.", " chcecie zbawienia, to powierzcie wszystko Bogu.")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("idźcie naprzód broniąc prawdy", "idźcie naprzód, broniąc prawdy.")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("nadejdą wstrząsną wieloma sumieniami,", "nadejdą, wstrząsną wieloma sumieniami,")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("by prosić was abyście byli gotowi", "by prosić was, abyście byli gotowi")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("wejdą do miast niszcząc uprawy,", "wejdą do miast, niszcząc uprawy,")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("Ach! aborcje", "Ach! Aborcje")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("otwierając wasze serca możecie mieć nowego ducha", "otwierając wasze serca, możecie mieć nowego ducha")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("bo czasy, które nadejdą będą bardzo ciężkie", "bo nadchodzące czasy będą bardzo ciężkie")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("wszystko co nadejdzie jest już od dawna przygotowane", "wszystko, co nadejdzie jest już od dawna przygotowane")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("wszystko co przepowiedziałam ma się wydarzyć", "wszystko, co przepowiedziałam, ma się wydarzyć")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("Oh!", "Och!")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("Och! ileż rozpaczy", "Och! Ileż rozpaczy")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("mają wiarę będzie oczekiwać na przyjście Jezusa Chrystusa.", "mają wiarę, poprzedzą przyjście Jezusa Chrystusa.")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("przyłączcie się do nich w śpiewając chwałę Panu", "przyłączcie się do nich, śpiewając chwałę Panu")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("napełniła się pychą i arogancją zapominając o pokorze", "napełniła się pychą i arogancją, zapominając o pokorze")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("po której stronie jesteście", "po czyjej stronie jesteście")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("który choć tak bardzo", "który, choć tak bardzo")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("ratujcie się odmawiając Różaniec Święty,", "ratujcie się, odmawiając Różaniec Święty,")
dataset_2020["text_pl"] = dataset_2020["text_pl"].str.replace("co nadejdzie jest już od dawna przygotowane", "co nadejdzie, jest już od dawna przygotowane")


dataset_2016.to_json("trevignano2016.js",orient="records")
dataset_2017.to_json("trevignano2017.js",orient="records")
dataset_2018.to_json("trevignano2018.js",orient="records")
dataset_2019.to_json("trevignano2019.js",orient="records")
dataset_2020.to_json("trevignano2020.js",orient="records")
















