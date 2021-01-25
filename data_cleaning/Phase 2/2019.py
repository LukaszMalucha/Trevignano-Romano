# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np



dataset = pd.read_csv("2019_cleaned.csv", encoding="utf-8")



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
dataset["text_pl"] = dataset["text_pl"].str.replace("ile grzechów każdego dnia gromadzi wszyscy, Kościół, Wierny i nie", "ile grzechów każdego dnia popełniają wszyscy, Kościół, wierzący i niewierzący")
dataset["text_pl"] = dataset["text_pl"].str.replace("Moje dzieci, dlaczego każdego dnia pozwalacie się kusić zło", "Moje dzieci, dlaczego każdego dnia pozwalacie się kusić złu")
dataset["text_pl"] = dataset["text_pl"].str.replace("nie trać jeszcze czasu", "nie trać już czasu")
dataset["text_pl"] = dataset["text_pl"].str.replace("Amen \”\.", "Amen")
dataset["text_pl"] = dataset["text_pl"].str.replace("Moi umiłowani, ci, którzy nadejdą, będą czasami żniw", "Moi umiłowani, czasy, które nadejdą, będą czasami żniw")
dataset["text_pl"] = dataset["text_pl"].str.replace("a którzy jeszcze tego nie zrobili", "a tych którzy jeszcze tego nie zrobili")
dataset["text_pl"] = dataset["text_pl"].str.replace("przysmaki są dla was gotowe", "wspaniałości są dla was przygotowane")
dataset["text_pl"] = dataset["text_pl"].str.replace("weźcie siły w Eucharystię", "czerpcie siły z Eucharystii")
dataset["text_pl"] = dataset["text_pl"].str.replace("i to macierzyńską", "i z matczyną miłością")
dataset["text_pl"] = dataset["text_pl"].str.replace("ile cierpień i udręk będziecie musieli stawić czoła", "ilu cierpieniom i udrękom będziecie musieli stawić czoła")
dataset["text_pl"] = dataset["text_pl"].str.replace("ale z całą miłością, która mnie naciska", "ale z całą miłością, na której mi zależy")
dataset["text_pl"] = dataset["text_pl"].str.replace("iz całą ludzkością", "i z całą ludzkością")
dataset["text_pl"] = dataset["text_pl"].str.replace("ale jak bardzo chciałbym słuchać i pomagać wszystkim", "ale jak bardzo chciałbym wysłuchać i pomóc każdemu")
dataset["text_pl"] = dataset["text_pl"].str.replace("udzielę żądanych łask", "udzielę potrzebnych łask")
dataset["text_pl"] = dataset["text_pl"].str.replace("Jestem tutaj, proszę cię i chcę, żebyś mnie rozpoznał", "Jestem tutaj, proszę cię żebyś mnie rozpoznał")
dataset["text_pl"] = dataset["text_pl"].str.replace("\”\.", ".")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ukochana córko, zostanę z tobą modlić się", "Ukochana córko, zostanę by się z tobą modlić")
dataset["text_pl"] = dataset["text_pl"].str.replace("Zawsze bądź zjednoczony, troszcz się o najsłabszych i największych Twoje nagrody", "Zawsze bądźcie zjednoczeni, troszczcie się o najsłabszych a wielkie będą wasze nagrody")
dataset["text_pl"] = dataset["text_pl"].str.replace("Otóż,", "Teraz")
dataset["text_pl"] = dataset["text_pl"].str.replace("wzniesione do nieba", "wzniesione do Nieba")
dataset["text_pl"] = dataset["text_pl"].str.replace("kocham cię i wzywam mnie, a będę z tobą", "kocham cię, wezwij mnie, a będę z tobą")
dataset["text_pl"] = dataset["text_pl"].str.replace("pozwalając Ja, Współodkupicielce, ostrzec jej dzieci, aby powrócili do Boga Bóg jest dobry i miłosierny", "pozwalając Mi, Współodkupicielce, ostrzec dzieci, aby powróciły do Boga, który jest dobry i miłosierny")
dataset["text_pl"] = dataset["text_pl"].str.replace("dzieci i będziecie", "i będziecie dzieci")
dataset["text_pl"] = dataset["text_pl"].str.replace("wyznawcy Jezusa, na wyznawców szatana", "na wyznawców Jezusa i wyznawców szatana")
dataset["text_pl"] = dataset["text_pl"].str.replace("Wszyscy jesteście Panem", "Wszyscy należycie do Pana")
dataset["text_pl"] = dataset["text_pl"].str.replace("miłość i spokój w tym domu", "miłość i pokój temu domowi")
dataset["text_pl"] = dataset["text_pl"].str.replace("kocham was oburzającą miłością", "kocham was nieporównywalną miłością")
dataset["text_pl"] = dataset["text_pl"].str.replace("Służebnica Pańska", "Służebnico Pańska")
dataset["text_pl"] = dataset["text_pl"].str.replace("upadek wielu moich ulubionych dzieci", "upadek wielu z moich ulubionych dzieci")
dataset["text_pl"] = dataset["text_pl"].str.replace("gdzie zły nie może cię dotknąć", "gdzie zły nie może was dotknąć")
dataset["text_pl"] = dataset["text_pl"].str.replace("grzechowi nie będzie już wierzyć, kiedy w kościele będzie miała miejsce protestantyzacja", "nie będzie się już wierzyć w grzech, gdy w kościele będzie miała miejsce protestantyzacja")
dataset["text_pl"] = dataset["text_pl"].str.replace("kocham was całym sercem \.", "kocham was całym sercem.")
dataset["text_pl"] = dataset["text_pl"].str.replace("aby królestwo niebieskie mogło się otworzyć i cieszyć się tym", "aby Królestwo Niebieskie mogło się otworzyć i bycie cieszyli się tym")
dataset["text_pl"] = dataset["text_pl"].str.replace(" i u mojej mamy", " i do mojej mamy")
dataset["text_pl"] = dataset["text_pl"].str.replace("Wasi bracia i wasz ukochany mąż", "Twoi bracia i ukochany mąż")
dataset["text_pl"] = dataset["text_pl"].str.replace(" jesteście w niebie", " jesteście w Niebie")
dataset["text_pl"] = dataset["text_pl"].str.replace("nadchodzące czasy będą bardzo trudne do stawienia czoła", "będzie trudno stawić czoła nadchdzącym czasom")
dataset["text_pl"] = dataset["text_pl"].str.replace("umyliście swoje sumienie", "oczyciliście swoje sumienie")
dataset["text_pl"] = dataset["text_pl"].str.replace("musisz go intensywnie przeżywać, a nie tylko w nim pomagać", "musisz go intensywnie przeżywać, a nie tylko współuczestniczyć")
dataset["text_pl"] = dataset["text_pl"].str.replace("potrzebujesz też spowiedzi i komunii z innymi", "potrzebujesz też spowiedzi i pojednania ze wszystkimi")
dataset["text_pl"] = dataset["text_pl"].str.replace(" Watykan się potrząśnie", " Watykan zadrży")
dataset["text_pl"] = dataset["text_pl"].str.replace("królestwa niebo", "Królestwa Niebieskiego")
dataset["text_pl"] = dataset["text_pl"].str.replace("od Boga\. ,", "od Boga.")
dataset["text_pl"] = dataset["text_pl"].str.replace("tylko z prawdziwą wiarą może coś zmienić", "tylko prawdziwą wiarą możecie coś zmienić.")
dataset["text_pl"] = dataset["text_pl"].str.replace("nie bądźcie każdym Bogiem z siebie", "nie bądźcie Bogiem sami dla siebie")
dataset["text_pl"] = dataset["text_pl"].str.replace("wzywam mojego Syna", "wzywajcie mojego Syna")
dataset["text_pl"] = dataset["text_pl"].str.replace("aby was chronił", "aby was chronić")
dataset["text_pl"] = dataset["text_pl"].str.replace("pozwól mu się rozpieszczać", "pozwólcie mu się rozpieszczać")
dataset["text_pl"] = dataset["text_pl"].str.replace("umacniać się w wierze, tylko", "umacniajcie się w wierze, tylko")
dataset["text_pl"] = dataset["text_pl"].str.replace("jestem Niepokalane Poczęcie", "jestem Niepokalanyn Poczęciem")
dataset["text_pl"] = dataset["text_pl"].str.replace("zawsze módlcie się Różaniec Święty", "zawsze odmawiajcie Różaniec Święty")
dataset["text_pl"] = dataset["text_pl"].str.replace("wszystkie plany Boże", "wszystkich planów Bożych")
dataset["text_pl"] = dataset["text_pl"].str.replace("niebo i modlitwa", "Niebo i modlitwa")
dataset["text_pl"] = dataset["text_pl"].str.replace("namaszczyc Duchem Świętym", "naznaczyć Duchem Świętym")
dataset["text_pl"] = dataset["text_pl"].str.replace("ale jak wielkie będzie Królestwo Niebieskie, że wy Obiecałam", "ale wielkie będzie Królestwo Niebieskie, obiecuję")
dataset["text_pl"] = dataset["text_pl"].str.replace("uwierzenie i świadectwo o moim zmartwychwstałym Synu", "wierzcie i głoście świadectwo o moim zmartwychwstałym Synu")
dataset["text_pl"] = dataset["text_pl"].str.replace("Kościół odrzuca modlitwy i prawdziwą naukę wiary", "w których Kościół odrzuca modlitwy i prawdziwą naukę wiary")
dataset["text_pl"] = dataset["text_pl"].str.replace("Szatan wierzy, że dotarł jego cel", "Szatan wierzy, że osiągnął swój cel")
dataset["text_pl"] = dataset["text_pl"].str.replace("pokoju, spokój i odwaga", "pokoju, spokóju i odwagi")
dataset["text_pl"] = dataset["text_pl"].str.replace("was dotykał jeden po drugim", "dotykał was wszystkich")
dataset["text_pl"] = dataset["text_pl"].str.replace("Chrzczcie dzieci i unikajcie ich potępienia", "Chrzcijcie dzieci i unikajcie ich potępienia")
dataset["text_pl"] = dataset["text_pl"].str.replace("Gromadźcie w swoich rodzinach wieczerniki modlitewne", "Twórzcie w swoich rodzinach wieczerniki modlitewne")
dataset["text_pl"] = dataset["text_pl"].str.replace(" Usłysz wiatry wojny, które nie są tylko bombami atomowymi, ale wojna na świecie już się rozpoczęła", "Posłuchaj wiatrów wojnu, to jeszcze nie bomby atomowe, ale wojna na świecie już się rozpoczęła")
dataset["text_pl"] = dataset["text_pl"].str.replace("wkrótce niebo się otworzy i ujrzycie królestwo Boże ze wszystkim", "wkrótce Niebo się otworzy i ujrzycie Królestwo Boże ze wszystkim")
dataset["text_pl"] = dataset["text_pl"].str.replace("Jego powtórne przyjście nie potrwa długo", "Jego powtórne przyjście już niedługo długo")
dataset["text_pl"] = dataset["text_pl"].str.replace("wielkie znaki z nieba", "wielkie znaki z Nieba")
dataset["text_pl"] = dataset["text_pl"].str.replace("jest Jedyna", "to jest Jedyna")
dataset["text_pl"] = dataset["text_pl"].str.replace("Nie ma już czasu na marnowanie czasu", "Nie wolno już marnować czasu")
dataset["text_pl"] = dataset["text_pl"].str.replace("aby ktokolwiek przemawiał w wlaniu Ducha Świętego", "aby zawsze przemawiał przez was Duch Święty")
dataset["text_pl"] = dataset["text_pl"].str.replace("by się insynuować", "by się wkraść")
dataset["text_pl"] = dataset["text_pl"].str.replace(" Wołam o wszystko, co się wydarzy, nawrócę się i zawsze będę wierny prawdziwemu Kościołowi", " Płaczę z powodu wszystkiego co się ma zdarzyć, nawróć się i zawsze bądź wierny prawdziwemu Kościołowi")
dataset["text_pl"] = dataset["text_pl"].str.replace("wkrótce nie będziecie już nic więcej", "wkrótce nie będziecie już mieć nic więcej")
dataset["text_pl"] = dataset["text_pl"].str.replace("Diabeł dotknie miejsca i ludzi nie możesz sobie wyobrazić", "Diabeł dotknie miejsc i ludzi, o których by nigdy nie pomyślał")
dataset["text_pl"] = dataset["text_pl"].str.replace("przynieście światło\. w świecie, który jest miłością i pokojem", "przynieście światło światu, którym jest miłość i pokój")
dataset["text_pl"] = dataset["text_pl"].str.replace("Moje kochane, jak wielkie jest Twoje serce", "Moi kochani, jak wielkie są Wasze serca")
dataset["text_pl"] = dataset["text_pl"].str.replace("Jezusem Dzieci", "Jezusem. Dzieci")
dataset["text_pl"] = dataset["text_pl"].str.replace("które Proszę cię", "o które cię proszę")
dataset["text_pl"] = dataset["text_pl"].str.replace("kocham także siebie", "także między wami")
dataset["text_pl"] = dataset["text_pl"].str.replace("wciąż będzie wiele dźwięków, które zadrżą na ziemi", "wciąż będzie wiele głosów, od których zadrży ziemia")
dataset["text_pl"] = dataset["text_pl"].str.replace(" \[i tam Matka Boża pokazała mi serce, które trzymała w dłoniach, które krwawiło\]", " (Matka Boża pokazała mi krwawiące serce, które trzymała w dłoniach)")
dataset["text_pl"] = dataset["text_pl"].str.replace("pochodzą z nieba", "pochodzą z Nieba")
dataset["text_pl"] = dataset["text_pl"].str.replace("waszą jedyną pewność", "wasza jedyna pewność")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ofiaruj mojemu synowi", "Ofiaruj mojemu Synowi")
dataset["text_pl"] = dataset["text_pl"].str.replace("w twoje złe myśli, a on przekształci je w myśli miłości", "ofiaruj swoje złe myśli, a on przekształci je w myśli miłości")
dataset["text_pl"] = dataset["text_pl"].str.replace("którzy zostawiliście Jego Słowo, które jest jeden, dla wszystkich i na zawsze", "który zostawił swoje Słowo, które jest jedno, wieczne i powrzechne")
dataset["text_pl"] = dataset["text_pl"].str.replace("aby mój Syn Jezus przewidział czas swojego przybycia", "aby mój Syn Jezus przyspieszył czas swojego przyjścia")
dataset["text_pl"] = dataset["text_pl"].str.replace("po trzęsieniach ziemi, o wodach, które z mocą zstępują z nieba i które wchodzą do miast jako pani, nadal mimo wszystko nie rozumiesz", "po trzęsieniach ziemi, po wodach, które z mocą zstępują z nieba i które wchodzą do miast jako pani, nadal mimo wszystko nie rozumiesz")
dataset["text_pl"] = dataset["text_pl"].str.replace(" Syna Jezusa Umiłowane dzieci", " Syna Jezusa. Umiłowane dzieci")
dataset["text_pl"] = dataset["text_pl"].str.replace("będę mógł cię nasycić rozkoszami", "będę mógł cię nasycić dobrami")
dataset["text_pl"] = dataset["text_pl"].str.replace("będzie wyglądać\. ", "będzie wyglądać. ")
dataset["text_pl"] = dataset["text_pl"].str.replace(" pewną iz pomocą Moją", " pewną i z pomocą Moją")
dataset["text_pl"] = dataset["text_pl"].str.replace("sercem prosić o przebaczenie", "sercem proście o przebaczenie")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ewangelią \.", "Ewangelią.")
dataset["text_pl"] = dataset["text_pl"].str.replace("nie mam już łez", "brak mi już łez")
dataset["text_pl"] = dataset["text_pl"].str.replace("poście i pokutujcie", "pośćcie i pokutujcie")
dataset["text_pl"] = dataset["text_pl"].str.replace("które przyszły z nieba", "które przyszły z Nieba")
dataset["text_pl"] = dataset["text_pl"].str.replace("nowe przymierze", "Nowe Przymierze")
dataset["text_pl"] = dataset["text_pl"].str.replace("wolności", "liberalności")
dataset["text_pl"] = dataset["text_pl"].str.replace("łez do wylewu", "łez do wylania")
dataset["text_pl"] = dataset["text_pl"].str.replace("Dzieci, sprawiedliwość już się zaczęła ścieżka, nie mogę dłużej trzymać ręki sprawiedliwości", "Dzieci, sprawiedliwość już nadchodzi, nie mogę dłużej wstrzymywać ręki sprawiedliwości")
dataset["text_pl"] = dataset["text_pl"].str.replace("który zamiast tego jest coraz bliżej ziemi", "który jest coraz bliżej ziemi")
dataset["text_pl"] = dataset["text_pl"].str.replace("ponieważ tam przyjdą wszystkie znaki", "ponieważ stamtąd przyjdą wszystkie znaki")
dataset["text_pl"] = dataset["text_pl"].str.replace("diabeł jest uwolniony bardziej niż kiedykolwiek", "diabeł ma więcej swobody niż kiedykolwiek wcześniej")
dataset["text_pl"] = dataset["text_pl"].str.replace("że jego występ dobiega końca", "że jego akt dobiega końca")
dataset["text_pl"] = dataset["text_pl"].str.replace("wtedy Łaski zostaną stokrotnie pomnożone", "dla tych Łaski zostaną stokrotnie pomnożone")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ojcze nasz", "Ojcze Nasz")
dataset["text_pl"] = dataset["text_pl"].str.replace("Wszystko idzie inną stopą", "Wszystko idzie na złą drogę")
dataset["text_pl"] = dataset["text_pl"].str.replace(" i co mama lubi patrzeć na dzieci\. w niebezpieczeństwie\?", " a która mama chce oglądać swoje dzieci w niebezpieczeństwie?")
dataset["text_pl"] = dataset["text_pl"].str.replace("ponieważ moje projekty się spełnią, tak jak wola nieba, miliony będą ludźmi, którzy przyjdą chwalić Pana", "ponieważ moje przedsięwzięcia się udadzą, z woli Nieba, miliony przyjdą chwalić Pana")
dataset["text_pl"] = dataset["text_pl"].str.replace("serca na Grace", "serca na Łaskę")
dataset["text_pl"] = dataset["text_pl"].str.replace("w który stopniowo zostaniesz objęty", " którm stopniowo zostaniesz objęty")
dataset["text_pl"] = dataset["text_pl"].str.replace("rozeznaniu\. \!", "rozeznaniu. !")
dataset["text_pl"] = dataset["text_pl"].str.replace("usunąć i odłożyć na bok", "usuńcie i odłóżcie na bok")
dataset["text_pl"] = dataset["text_pl"].str.replace("usunąć i odłożyć na bok swoje człowieczeństwo i wywyższyć Ducha, być wojownikami i odważnymi", "usuńcie i odłóżcie na bok swoje człowieczeństwo, wywyższcie Ducha, bądźcie odważnymi wojownikami")
dataset["text_pl"] = dataset["text_pl"].str.replace("a Duch Święty wleje się w was", "Duch Święty wleje się w was")
dataset["text_pl"] = dataset["text_pl"].str.replace("i jest jedynym panem Wszechświata", "i on jest jedynym panem Wszechświata")
dataset["text_pl"] = dataset["text_pl"].str.replace("Uwaga dzieci, uwaga", "Uważajcie dzieci, uważajcie")
dataset["text_pl"] = dataset["text_pl"].str.replace(" Z drugiej strony ludzkość", " Jednak ludzkość")
dataset["text_pl"] = dataset["text_pl"].str.replace(" nie dajcie się plagiatować wilkom w owczej skórze", " nie dręczcie się wilkami w owczej skórze")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ja, Ojcze Wszechmogący", "Ja, Ojciec Wszechmogący")
dataset["text_pl"] = dataset["text_pl"].str.replace("dlaczego nie widzicie wojen\! Dlaczego nie rozumiesz\? ", "spójrzcie na wojny! Dlaczego nie rozumiecie?")
dataset["text_pl"] = dataset["text_pl"].str.replace("Posłałem go po wasze zbawienie, a wy odwracajcie się", "Posłałem go po by was zbawił, a wy się odwracacie")
dataset["text_pl"] = dataset["text_pl"].str.replace("O! Moja umiłowana Maryjo, urodzona bez grzechu pierworodnego, pracowała dla Ciebie i dla Ciebie", "O! Moja umiłowana Maryja, urodzona bez grzechu pierworodnego, ileż napracowała się dla Ciebie i dla Ciebie")
dataset["text_pl"] = dataset["text_pl"].str.replace("To, co pozostawiacie swoim dzieciom, bez szacunku, bez świętości, bez wiary", "Wychowujecie swoje dzieci bez szacunku, bez świętości, bez wiary")
dataset["text_pl"] = dataset["text_pl"].str.replace("uczcie miłości i wielka będzie nagroda", ". Uczcie miłości a wielka będzie nagroda")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ja, wasz miłosierny Ojcze", "Ja, wasz miłosierny Ojciec")
dataset["text_pl"] = dataset["text_pl"].str.replace("chciałabym wam poinstruować", "chciałabym wam wskazać")
dataset["text_pl"] = dataset["text_pl"].str.replace("aby był zanurzony w Jego świetle", "abyś mógł być zanurzony w Jego świetle")
dataset["text_pl"] = dataset["text_pl"].str.replace("Pasterze, ewangelizują", "Pasterze ewangelizują")
dataset["text_pl"] = dataset["text_pl"].str.replace("ile łez przelałam !!", "ileż łez przelałam !")
dataset["text_pl"] = dataset["text_pl"].str.replace("zstąpiła z nieba", "zstąpiła z Nieba")
dataset["text_pl"] = dataset["text_pl"].str.replace("zaraza, wszystko się dzieje", "wszystko to się dzieje teraz")
dataset["text_pl"] = dataset["text_pl"].str.replace(" nigdy was nie zostawię w spokoju", " nigdy was nie zostawię samych")
dataset["text_pl"] = dataset["text_pl"].str.replace("rozpacz, rozpacz i smutek", "rozpacz, bezradność i smutek")
dataset["text_pl"] = dataset["text_pl"].str.replace("kiedy nie będziecie się odnaleźć", "w których nie będziecie mogli się odnaleźć")
dataset["text_pl"] = dataset["text_pl"].str.replace("dla tych bram piekła się otworzą", "dla tych bramy piekła się otworzą")
dataset["text_pl"] = dataset["text_pl"].str.replace("który szczególnie w tych czasach włócznia wciąż przeszywa Jego serce", "którego Serce jest przeszywane włócznią szczególnie w tych czasach")
dataset["text_pl"] = dataset["text_pl"].str.replace("Józef i jest ze mną", "Józef ze mną")
dataset["text_pl"] = dataset["text_pl"].str.replace("powierzona przez niebo", "powierzona przez Niebo")
dataset["text_pl"] = dataset["text_pl"].str.replace(" ale nie każdy otwiera swoje serca", " ale nie każdy otwiera swoje serce")
dataset["text_pl"] = dataset["text_pl"].str.replace("co dobre, został stworzony", "co zostało stworzone dobre")
dataset["text_pl"] = dataset["text_pl"].str.replace("błogosławię was jeden po drugim", "błogosławię was wszystkich")
dataset["text_pl"] = dataset["text_pl"].str.replace("Kocham was, dzieci ", "Kocham was dzieci ")
dataset["text_pl"] = dataset["text_pl"].str.replace("Zbyt wiele argumentów oddala was ode mnie i między wami, braćmi", "Zbyt wiele kłótni oddala was ode mnie i od waszych braćmi")
dataset["text_pl"] = dataset["text_pl"].str.replace("ponieważ nie wierzycie w to, co dotykacie swoją ręką", "ponieważ nie wierzycie w to, czego nie dotkniecie swoją ręką")
dataset["text_pl"] = dataset["text_pl"].str.replace("będzie was nienawidzić w moim imieniu", "będą was nienawidzić przez moje Imię")
dataset["text_pl"] = dataset["text_pl"].str.replace("królestwo niebieskie", "Królestwo Niebieskie")
dataset["text_pl"] = dataset["text_pl"].str.replace("dotykam was jeden po drugim", "dotykam was wszystkich")
dataset["text_pl"] = dataset["text_pl"].str.replace("iw Ducha Świętego", "i w Ducha Świętego")
dataset["text_pl"] = dataset["text_pl"].str.replace("bluźnierców, bluźnierców i heretyków", "bluźnierców i heretyków")
dataset["text_pl"] = dataset["text_pl"].str.replace("dumni i dumni", "dumni i pyszni")
dataset["text_pl"] = dataset["text_pl"].str.replace("Królestwa Bożego Dzieci", "Królestwa Bożego. Dzieci")
dataset["text_pl"] = dataset["text_pl"].str.replace("jeśli zgrzeszyliście w tym", "jeśli zgrzeszyliście w czymś")
dataset["text_pl"] = dataset["text_pl"].str.replace("iz moim Jezusem ", "i z moim Jezusem ")
dataset["text_pl"] = dataset["text_pl"].str.replace("ile dla mnie cierpienia i ile będziesz mieć", "ile przeze mnie cierpienia miałaś i będziesz mieć")
dataset["text_pl"] = dataset["text_pl"].str.replace("Część ukochanych dzieci mojego Kościoła, zastępujcie się Bogiem i wygodnie popełniajcie błędy", "Część ukochanych dzieci mojego Kościoła zastępuje sobą Boga i popełnia wygodne błędy")







dataset["text_en"] = dataset["text_en"].str.replace("perfume", "scent")
dataset["text_en"] = dataset["text_en"].str.replace("as I could have", "how could I allow this")
dataset["text_en"] = dataset["text_en"].str.replace("you\. \.", "you.")
dataset["text_en"] = dataset["text_en"].str.replace("demons choose weak souls in the wedding ring", "demons choose souls weak in faith")
dataset["text_en"] = dataset["text_en"].str.replace("Everything takes a different foot", "Everything takes a wong path")
dataset["text_en"] = dataset["text_en"].str.replace("do not allow yourselves to be plagiarized by wolves in sheep's clothing", "don't let yourselves be plagued by wolves in sheep's clothing")



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
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("przyszedłam", "przyszłam")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("was chronił", "was chroniła")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("zwierciadłam", "zwierciadłem")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("Przyszedłam", "Przyszłam")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("rozłemu", "rozłamu")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("rozłemem", "rozłamem")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("ciałam", "ciałem")
dataset_mary["text_pl"] = dataset_mary["text_pl"].str.replace("światłam ", "światłem ")






dataset_jesus = dataset[dataset["author"] != "Holy Mary" ]

dataset= pd.concat([dataset_mary, dataset_jesus])



dataset = dataset.sort_values(by=["year", "month", "day"])

dataset = dataset[["year", "month", "day", "author", "text", "text_en", "text_pl", "month_string"]]

dataset["text_pl"] = dataset["text_pl"].str.replace("Amen \.", "Amen.")
dataset["text_en"] = dataset["text_en"].str.replace("Amen \.", "Amen.")
dataset["text"] = dataset["text"].str.replace("Amen \.", "Amen.")



dataset.to_csv("trevignano_2019.csv", index=False, encoding="utf-8")
dataset.to_json("trevignano_2019.json",orient="records")









