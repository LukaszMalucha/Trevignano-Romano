# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np




dataset = pd.read_csv("trevignano_2016.csv", encoding="utf-8")



# SPELLING FIX

dataset["text_pl"] = dataset["text_pl"].str.replace("miałaa", "miała")
dataset["text_pl"] = dataset["text_pl"].str.replace("ponieważ Szatan nie przestanie brać wszystkich dusz nawet blisko siebie", "bo szatan nie przestanie porywać wszystkich dusz, które się do niego zbliżą")
dataset["text_pl"] = dataset["text_pl"].str.replace(" ale i ty będziesz musiał walczyć o modlitwy", " ale i ty będziesz musiała walczyć o modlitwy")
dataset["text_pl"] = dataset["text_pl"].str.replace("zwłaszcza z powodu Papieża", "zwłaszcza nad Papieżem")
dataset["text_pl"] = dataset["text_pl"].str.replace("Amen\"", "Amen")
dataset["text_pl"] = dataset["text_pl"].str.replace("Dziękuje, że mnie szukalicie", "Dziękuje, że mnie odnaleźliście")
dataset["text_pl"] = dataset["text_pl"].str.replace("Sercem swojej mamy", "Sercem swojej matki")
dataset["text_pl"] = dataset["text_pl"].str.replace("którzy są zgubieni", "którzy są zagubieni")
dataset["text_pl"] = dataset["text_pl"].str.replace("Amen Z tej", "Amen. Z tej")
dataset["text_pl"] = dataset["text_pl"].str.replace("Wasza Matka\. \"", "Wasza Matka.")
dataset["text_pl"] = dataset["text_pl"].str.replace("Pozwala świetlistym promieniom", "Pozwólcie świetlistym promieniom")
dataset["text_pl"] = dataset["text_pl"].str.replace("Amen Przy", "Amen. Przy")
dataset["text_pl"] = dataset["text_pl"].str.replace("mają zatwardziałe serce", "mają zatwardziałe serca")
dataset["text_pl"] = dataset["text_pl"].str.replace("aaa", "a")
dataset["text_pl"] = dataset["text_pl"].str.replace("a nie nic się nie dzieje i że Ziemia może się oczyścić tylko modlitwą i miłością", "aby nie się nie stało i żeby Ziemia mogła się oczyścić tylko modlitwą i miłością")
dataset["text_pl"] = dataset["text_pl"].str.replace("możecie złagodzić ból swoje i innych wiernych w dniach ucisku", "możecie złagodzić ból swój i innych wiernych w dniach ucisku")
dataset["text_pl"] = dataset["text_pl"].str.replace("Będę przy tobie i będę cię po kolei chwytał za rękę", "Będę przy tobie i będę was trzymać za ręce")
dataset["text_pl"] = dataset["text_pl"].str.replace("świat owinięty krwią oraz wielu ludzi, którzy wzywali pomocy dla Pana", "świat splamiony krwią oraz wielu ludzi, którzy wzywali pomocy Pana")
dataset["text_pl"] = dataset["text_pl"].str.replace("obecny i błogosławiła wszystkich w imię Ojca i Syna i Ducha Świętego", "Promienie światła wokół figury Maryi dotykały wszystkich obecnych chorych, a Ona błogosławiła wszystkich w imię Ojca i Syna i Ducha Świętego.")
dataset["text_pl"] = dataset["text_pl"].str.replace("odmówienie różańca", "odmawienie różańca")
dataset["text_pl"] = dataset["text_pl"].str.replace("aa", "a")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ojca i Synu i Ducha Świętego", "Ojca i Syna i Ducha Świętego")
dataset["text_pl"] = dataset["text_pl"].str.replace("rozłożył jego płaszcz", "rozłożyła swój płaszcz")
dataset["text_pl"] = dataset["text_pl"].str.replace("Matka Boża mówi wtedy", "Matka Boża dodaje")
dataset["text_pl"] = dataset["text_pl"].str.replace("szczególnie dla Rzymu", "szczególnie za Rzym")
dataset["text_pl"] = dataset["text_pl"].str.replace("nie czekajcie w ostatniej chwili", "nie czekajcie do ostatniej chwili")
dataset["text_pl"] = dataset["text_pl"].str.replace("Pozwólcie się tchnąć Duchowi Świętemu Mojego Syna", "Pozwólcie Mojemu Synowi tchnąć na was Ducha Świętego")
dataset["text_pl"] = dataset["text_pl"].str.replace("a on daje ci piękną łaskę", "a on daje ci piękną Łaskę")
dataset["text_pl"] = dataset["text_pl"].str.replace("pozwólWcie", "pozwólcie")
dataset["text_pl"] = dataset["text_pl"].str.replace("w moich Synach", "w moich Dzieciach")
dataset["text_pl"] = dataset["text_pl"].str.replace("Córko Moja, nie ufaj i postępuj szczegółowo tylko o to, o co Cię proszę", "Córko Moja, bądź nieufna i zrób dokładnie to, o co Cie proszę")
dataset["text_pl"] = dataset["text_pl"].str.replace(" ponieważ oddalasz się ode Mnie", " oddalasz się ode Mnie")
dataset["text_pl"] = dataset["text_pl"].str.replace("i nie rozpaczajcie w trudnościach", "i nie rozpaczaj w trudnościach")
dataset["text_pl"] = dataset["text_pl"].str.replace("byłbyś w stanie spojrzeć poza siebie i zdalibyście sobie sprawę", "bylibyście w stanie spojrzeć poza siebie i zdać sobie sprawę")
dataset["text_pl"] = dataset["text_pl"].str.replace("miłościąMódl ", "miłością Módl ")
dataset["text_pl"] = dataset["text_pl"].str.replace("Amen Dzisiaj", "Amen. Dzisiaj")
dataset["text_pl"] = dataset["text_pl"].str.replace("aby wlać w was Ducha Świętego", "aby tchnąć w was Ducha Świętego")
dataset["text_pl"] = dataset["text_pl"].str.replace("którzy je zapalają", "którzy je zapalą")
dataset["text_pl"] = dataset["text_pl"].str.replace("mógł wlać w was Pokój", "mógł tchnąć w was Pokój")
dataset["text_pl"] = dataset["text_pl"].str.replace("Nalegam na prośbę o odmawienie różańca", "Bardzo was proszę o odmawienie różańca")
dataset["text_pl"] = dataset["text_pl"].str.replace("zaopatrzenie się w żywność w puszkach i wodę pitną", "zaopatrzcie się w żywność w puszkach i wodę pitną")
dataset["text_pl"] = dataset["text_pl"].str.replace("dni ostrzeżenia", "dni Ostrzeżenia")
dataset["text_pl"] = dataset["text_pl"].str.replace("ducha świętego", "Ducha Świętego")
dataset["text_pl"] = dataset["text_pl"].str.replace("będę was chronił i trzymał mocno", "będę was chroniła i trzymała mocno")
dataset["text_pl"] = dataset["text_pl"].str.replace("będę pojawiał się co 3 dni miesiąca o godzinie 15", "będę pojawiała się co 3 dni miesiąca o godzinie 15")
dataset["text_pl"] = dataset["text_pl"].str.replace("ramię w imieniu tych", "ramię w na tych")
dataset["text_pl"] = dataset["text_pl"].str.replace("praktyka,", "praktykę,")
dataset["text_pl"] = dataset["text_pl"].str.replace(" do Twojego serca", " do Waszego serca")
dataset["text_pl"] = dataset["text_pl"].str.replace(" niepokalanego serca", " Niepokalanego Serca")
dataset["text_pl"] = dataset["text_pl"].str.replace("W końcu znalazłem cię tutaj zebranego w pokoju z Bogiem, z błogością i słodyczą, które masz w swoich sercach", "W końcu znalazłam was tutaj zebranych w pokoju z Bogiem, z błogością i słodyczą, które macie w swoich sercach")


#ś


#dataset["text_en"] = dataset["text_en"].str.replace("perfume", "scent")
#
#
## MARY FORM
#
#dataset_mary = dataset[dataset["author"] == "Holy Mary" ]
#dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Chciałbym", "Chciałabym")
#dataset_jesus = dataset[dataset["author"] != "Holy Mary" ]
#dataset= pd.concat([dataset_mary, dataset_jesus])









dataset.to_csv("trevignano2016.csv", index=False, encoding="utf-8")
dataset.to_json("trevignano2016.json",orient="records")







