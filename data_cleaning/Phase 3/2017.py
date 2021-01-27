# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np




dataset = pd.read_csv("trevignano_2017.csv", encoding="utf-8")



dataset["author"] = np.where(dataset["text"].str.contains("Il vostro Gesù"), "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["text"].str.contains(" Il Vostro Gesù"), "Jesus Christ", dataset["author"])


dataset["text"] = np.where(dataset["text"] == "x", "Cari figli, voi consolate il mio cuore e siete in ognuna delle piaghe di mio Figlio,  affidate a Lui le vostre sofferenze. Io sono qui con voi, tutti i giorni, insieme a Gesù. Care figlie, presto i cieli si apriranno e sarete tra le braccia di mio Figlio. I miei angeli vi proteggeranno. Ora vi benedico nel nome del Padre del Figlio e dello Spirito Santo .Amen", dataset["text"])
dataset["text_en"] = np.where(dataset["text_en"] == "x", "Dear children, you console my heart and are in each of my Son's wounds, entrust your sufferings to Him. I am here with you, every day, together with Jesus. Dear daughters, soon the heavens will open and you will be in the arms of my Son. My angels will protect you. Now I bless you in the name of the Father, the Son and the Holy Spirit. Amen.", dataset["text_en"])
dataset["text_pl"] = np.where(dataset["text_pl"] == "x", "Drogie dzieci, pocieszacie moje serce i jesteście w każdej z ran mojego Syna, powierzcie Mu wasze cierpienia. Jestem tu z wami, każdego dnia, razem z Jezusem. Drogie córki, wkrótce otworzą się niebiosa i znajdziecie się w ramionach mojego Syna. Moi aniołowie będą cię chronić. Teraz błogosławię was w imię Ojca, Syna i Ducha Świętego. Amen.", dataset["text_pl"])



# SPELLING FIX
dataset["text_pl"] = dataset["text_pl"].str.replace("aa", "a")
dataset["text_pl"] = dataset["text_pl"].str.replace("którzy idą za ulotnymi", "którzy idą za tym, co ulotne")
dataset["text_pl"] = dataset["text_pl"].str.replace("namaściła nas pojedynczo", "naznaczyła nas pojedynczo")
dataset["text_pl"] = dataset["text_pl"].str.replace("więc nie odwracajcie go", "więc nie odwracajcie się od Niego")
dataset["text_pl"] = dataset["text_pl"].str.replace(" za świat, będzie", " za świat, który będzie")
dataset["text_pl"] = dataset["text_pl"].str.replace("Wkrótce będziesz zmuszony", "Wkrótce będziecie zmuszeni")
dataset["text_pl"] = dataset["text_pl"].str.replace("odmawiajcie w komunii Różaniec Święty", "odmawiajcie wspólnie Różaniec Święty")
dataset["text_pl"] = dataset["text_pl"].str.replace("nowym osobom, którzy", "nowym osobom, które")
dataset["text_pl"] = dataset["text_pl"].str.replace(" jesteśmy u kresu czasu, więc nie traćcie czasu", " jesteśmy u kresu, więc nie traćcie czasu")
dataset["text_pl"] = dataset["text_pl"].str.replace("Otóż ​​błogosławię", "Teraz ​​błogosławię")
dataset["text_pl"] = dataset["text_pl"].str.replace("Więc do zobaczenia, szczególnie dziś wieczorem", "Tak was widzę, szczególnie dzisiaj")
dataset["text_pl"] = dataset["text_pl"].str.replace("grzesznym wyrazem Kościoła", "grzeszną postawą Kościoła")
dataset["text_pl"] = dataset["text_pl"].str.replace("zgromadzicie się tutaj, nie wyobrażajcie sobie, jak bardzo mnie uszczęśliwiacie", "nie wyobrażacie sobie, jak bardzo mnie uszczęśliwiacie gdy gromadzicie się tutaj")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ciałam Mojego Syna", "Ciałem Mojego Syna")
dataset["text_pl"] = dataset["text_pl"].str.replace(" niecie Jego krzyż z miłością", " nieście Jego krzyż z miłością")
dataset["text_pl"] = dataset["text_pl"].str.replace("miłość do niego", "miłość do Niego")
dataset["text_pl"] = dataset["text_pl"].str.replace("Złożę wam wiele podziękowań, przyjmuję ich i z wiarą świadczę o nich", "Uczynię dla was wiele łask, przyjmijcie je i świadczcie o nich z wiarą")
dataset["text_pl"] = dataset["text_pl"].str.replace("w Imieniu Ojca", "w imię Ojca")
dataset["text_pl"] = dataset["text_pl"].str.replace("ziemia wszędzie będzie drżeć coraz silniejsza", "ziemia wszędzie będzie drżeć coraz silniej")
dataset["text_pl"] = dataset["text_pl"].str.replace("ale będziesz miał moją ochronę", "ale będziecie mieć moją ochronę")
dataset["text_pl"] = dataset["text_pl"].str.replace("wstań ponownie, demonstrując zaufanie, jakim pokładasz ufność w Jezusie", "powstań, pokazując swoje zaufanie do Jezusa")
dataset["text_pl"] = dataset["text_pl"].str.replace("Bardzo chciałabym was wszystkich bezpiecznie nieść w ramionach mojego Syn", "Tak bardzo pragnę zanieść was wszystkich bezpiecznie w ramiona mojego Syna")
dataset["text_pl"] = dataset["text_pl"].str.replace(" tak wielu moich ulubionych dzieci", " tak wiele moich ulubionych dzieci")
dataset["text_pl"] = dataset["text_pl"].str.replace("Nigdy nie załamuj się przed swoim krzyżem, tak jak przyjąłam krzyż mojego Syna, który umarł z miłości i pokonał śmierć", "Nigdy nie bądźcie przygnębieni w obliczu waszego krzyża, tak jak ja przyjąłem krzyż mojego Syna, który umarł z miłości i pokonał śmierć")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ogłoś Jego przybycie wszystkim, bądźcie czysty i radosny", "Ogłoś Jego przybycie wszystkim, bądź czysty i radosny")
dataset["text_pl"] = dataset["text_pl"].str.replace("Nie zwlekaj z konwersją", "Nie zwlekaj z nawróceniem")
dataset["text_pl"] = dataset["text_pl"].str.replace(" mojemu sercu, widząc was tutaj zgromadzonych", " mojemu sercu, gdy widzę was tutaj zgromadzonych")
dataset["text_pl"] = dataset["text_pl"].str.replace("w czasie ostrzeżenia", "w czasie Ostrzeżenia")
dataset["text_pl"] = dataset["text_pl"].str.replace("Gdyby człowiek więcej słuchał", "Gdyby człowiek posłuchał")
dataset["text_pl"] = dataset["text_pl"].str.replace("ewangel", "Ewangel")
dataset["text_pl"] = dataset["text_pl"].str.replace("zjednoczyć\.\.", "zjednoczyć.")
dataset["text_pl"] = dataset["text_pl"].str.replace("Wybrałam cię, abyś był dzisiaj przykładem i zawsze, tak jak zebrałam cię dzisiaj, zbiorę cię ponownie, aby zbawić ciebie i wszystkie dusze, które wciąż nie znajdują pokoju, prawdy i drogi", "Wybrałem was, abyście byli przykładem dzisiaj i zawsze, tak jak zgromadziłem was dzisiaj, zgromadzę was ponownie, aby uratować was i wszystkie dusze, które jeszcze nie znalazły pokoju, prawdy i drogi")
dataset["text_pl"] = dataset["text_pl"].str.replace("Drodzy bracia, zbliżam się do was coraz bardziej w tym czasie łaski, każdego dnia będziecie widzieć i odczuwać moją obecność, która powzolić wam odczuć moją miłość do was , aby zasmakować mojej miłości do was", "Drodzy bracia, w tym czasie łaski jestem coraz bliżej was. Każdego dnia będziecie widzieć i odczuwać moją obecność, aby dać wam przedsmak mojej miłości do was")
dataset["text_pl"] = dataset["text_pl"].str.replace("działa w twoich umysłach", "działa w waszych umysłach")
dataset["text_pl"] = dataset["text_pl"].str.replace("miłójcie się wzajemnie", "miłujcie się wzajemnie")
dataset["text_pl"] = dataset["text_pl"].str.replace("Będziecie mieli wiele do walki, zwłaszcza prześladowania moich dzieci będą straszne", "Będziecie mieli o co walczyć, zwłaszcza o prześladowanie moich dzieci. To będzie straszne")
dataset["text_pl"] = dataset["text_pl"].str.replace("Czerp siłę z Jezusa, teraz błogosławię cię", "Nabierzcie siły od Jezusa, teraz błogosławię was")
dataset["text_pl"] = dataset["text_pl"].str.replace("Chcę, aby mury pychy i chwastów zostały zburzone, bądź w pokoju, miłości i prawdzie, przyłączcie się w modlitwie do mojego Syna, aby wszyscy uwierzyli w to, co wam zostawił, swoje ciało żywe w Eucharystii", "Pragnę, aby zostały zburzone mury pychy i niezgody, abyście trwali w pokoju, miłości i prawdzie. Zjednoczcie się w modlitwie z moim Synem, aby wszyscy uwierzyli w to, co wam zostawił, w Jego żywe ciało w Eucharystii")
dataset["text_pl"] = dataset["text_pl"].str.replace("że odpowiedzieliście na moje wezwanie w waszym sercu", "że odpowiedzieliście na moje wezwanie w waszych sercach")
dataset["text_pl"] = dataset["text_pl"].str.replace("Mój syn", "Mój Syn")
dataset["text_pl"] = dataset["text_pl"].str.replace("bądź w mojej łasce", "bądź w mojej Łasce")
dataset["text_pl"] = dataset["text_pl"].str.replace("w moje imię", "w moje Imię")
dataset["text_pl"] = dataset["text_pl"].str.replace("Amen Twój Jezu", "Amen. Twój Jezu")
dataset["text_pl"] = dataset["text_pl"].str.replace("czasuna", "czasu na")
dataset["text_pl"] = dataset["text_pl"].str.replace("Proszę drogie dzieci, wkrótce nadejdzie ostrzeżenie", "Proszę drogie dzieci, wkrótce nadejdzie Ostrzeżenie")
dataset["text_pl"] = dataset["text_pl"].str.replace("Dzieci, bądźcie głupie i głuche, zwłaszcza gdy was wyzywają", "Dzieci, bądźcie nieme i głuche, zwłaszcza gdy was wyzywają")
dataset["text_pl"] = dataset["text_pl"].str.replace("Amen Oto zaszczepiam pokój w waszych sercach", "Amen. Oto zaszczepiam pokój w waszych sercach")
dataset["text_pl"] = dataset["text_pl"].str.replace("iw moim", "i w moim")
dataset["text_pl"] = dataset["text_pl"].str.replace(" dzisiaj odstępstwo jest teraz w moim Kościele", " dzisiaj odstępstwo jest już w moim Kościele")
dataset["text_pl"] = dataset["text_pl"].str.replace("Bądźcie gotowi na czas ostrzeżenia", "Bądźcie gotowi na czas Ostrzeżenia")
dataset["text_pl"] = dataset["text_pl"].str.replace("Wszystko się rozpada, także modlitwą", "Wszystko się rozpada, więc módl się dalej")
dataset["text_pl"] = dataset["text_pl"].str.replace("Amen Bagnoregio 26 08 ", "Amen")
dataset["text_pl"] = dataset["text_pl"].str.replace("jak jasne gwiazdy", "jak jasna gwiazda")
dataset["text_pl"] = dataset["text_pl"].str.replace("i wołam o wszystko, co się dzieje", "i płaczę z powodu wszystkiego, co się dzieje")
dataset["text_pl"] = dataset["text_pl"].str.replace("słuchać w ciszy swojego serca, wywyższać ducha i ratować duszę", "słuchajcie w ciszy swojego serca, wywyższajcie ducha i ratujcie duszę")
dataset["text_pl"] = dataset["text_pl"].str.replace("składali ofiary i post", "składali ofiary i pościli")
dataset["text_pl"] = dataset["text_pl"].str.replace("w moich maluczkich", "w moich maleństwach")
dataset["text_pl"] = dataset["text_pl"].str.replace("zostanę tu na całą modlitwę", "zostanę tu przez całą modlitwę")
dataset["text_pl"] = dataset["text_pl"].str.replace(" Tak bardzo modliłam się do mojego Jezusa, abyś miał wiele łask i tutaj zstąpiłam na ciebie w obfitości", "Tak bardzo modliłam się do mojego Jezusa, abyś miała wiele łask, a oto one zstąpiły na ciebie w obfitości")
dataset["text_pl"] = dataset["text_pl"].str.replace("a na lewej ręce", "a w lewej ręce")
dataset["text_pl"] = dataset["text_pl"].str.replace("wasze serca, bo po cierpieniach otworzy w waszych sercach drzwi miłości i pokój powróci", "Umiłowane dzieci, wszystko się spełni, ale Jezus będzie u waszego boku, aby za wami podążać, dlatego nie trwożcie waszych serc, bo po cierpieniach otworzy drzwi miłości w waszych sercach i powróci pokój")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ponieważ ciągle pytasz mnie, kiedy nadejdzie mój powrót, mówię ci, wkrótce będzie to moje zejście na ziemię, ale poza uściskami będzie też dużo bólu", "Pytacie mnie bowiem nieustannie, kiedy nastąpi mój powrót, a ja wam mówię, że wkrótce nastąpi moje zejście na ziemię, ale oprócz uścisków będzie też wiele bólu")
dataset["text_pl"] = dataset["text_pl"].str.replace("Mnie iw Moje", "Mnie i w Moje")
dataset["text_pl"] = dataset["text_pl"].str.replace("Nawróć się, póki jeszcze masz czas, teraz wszystko jest szybko zakończone", "Przekonaj się, póki jest jeszcze czas. wszystko niebawem się skończy.")
dataset["text_pl"] = dataset["text_pl"].str.replace("Amen, Twój Jezu ", "Amen. Twój Jezu ")
dataset["text_pl"] = dataset["text_pl"].str.replace("Módlcie się, módlcie się, módlcie się, z nieba spadnie deszcz, woda i ogień, a wielki wulkan jest gotowy do przebudzenia", "Módlcie się, módlcie się, módlcie się, z nieba spadnie deszcz wody i ognia, a wielki wulkan jest gotowy na swoje przebudzenie")
dataset["text_pl"] = dataset["text_pl"].str.replace("Amen, Twój Jezu ", "Amen. Twój Jezu ")
dataset["text_pl"] = dataset["text_pl"].str.replace("kocham was i modlicie", "Kocham was. Modlicie")
dataset["text_pl"] = dataset["text_pl"].str.replace("Amen Dzisiejszy znak\:", "Amen")
dataset["text_pl"] = dataset["text_pl"].str.replace("dzieci,,", "dzieci,")
dataset["text_pl"] = dataset["text_pl"].str.replace(" i sercach nie ma miłość", " i sercach nie ma miłości")
dataset["text_pl"] = dataset["text_pl"].str.replace("\`\`", "\"")
dataset["text_pl"] = dataset["text_pl"].str.replace("dziękujemy za ponowne", "dziękuje wam za ponowne")
dataset["text_pl"] = dataset["text_pl"].str.replace("a będziesz miał cuda", "a doświadczysz cudów")
dataset["text_pl"] = dataset["text_pl"].str.replace(" sercu,z", " sercu, z")
dataset["text_pl"] = dataset["text_pl"].str.replace("Umiłowane dzieci, wołam o Syna", "Umiłowane dzieci, płaczę z powodu Syna")
dataset["text_pl"] = dataset["text_pl"].str.replace(" aby mój Syn Jezus kochał",  " aby mój Syn Jezus cię kochał")
dataset["text_pl"] = dataset["text_pl"].str.replace("Proście o łaski, ale",  "Prosicie o łaski, ale")
dataset["text_pl"] = dataset["text_pl"].str.replace("Nadszedł czas\.Nadszedł ",  "Nadszedł czas. Nadszedł ")
dataset["text_pl"] = dataset["text_pl"].str.replace("Miłość, miłość i jedność",  "Miłość, miłosierdzie i jedność")
dataset["text_pl"] = dataset["text_pl"].str.replace("Kocham wszystkich, tak jak ja ciebie",  "Kochaj wszystkich tak, jak ja kocham ciebie")
dataset["text_pl"] = dataset["text_pl"].str.replace(" inni religijni",  " innowiercy")
dataset["text_pl"] = dataset["text_pl"].str.replace("wkrótce niebo się otworzy",  "wkrótce Niebo się otworzy")
dataset["text_pl"] = dataset["text_pl"].str.replace("Jezu, da ci siłę do kontynuowania tej ścieżki",  "Jezus ci siłę do kontynuowania tej ścieżki")
dataset["text_pl"] = dataset["text_pl"].str.replace("Otóż,",  "Teraz")
dataset["text_pl"] = dataset["text_pl"].str.replace("\.Tak ",  ". Tak ")
dataset["text_pl"] = dataset["text_pl"].str.replace(" ale zawsze jesteście na straży",  " ale zawsze bądźcie na straży")
dataset["text_pl"] = dataset["text_pl"].str.replace("skończy\.\.",  "skończy.")
dataset["text_pl"] = dataset["text_pl"].str.replace("Amen Moje dzieci, dziękuję za przyjęcie",  "Amen. Moje dzieci, dziękuję za przyjęcie")
dataset["text_pl"] = dataset["text_pl"].str.replace("że pokuta i wyznanie są pilne",  "że pokuta i spowiedź są pilne")





dataset.to_csv("trevignano2017.csv", index=False, encoding="utf-8")
dataset.to_json("trevignano2017.json",orient="records")















