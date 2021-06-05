# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np
from google_trans_new import google_translator



dataset = pd.read_csv("june_cleaned.csv", encoding="utf-8")

dataset["text_pl"] = ""
dataset["text_en"] = ""
dataset["text_it"] = ""



# ITALIAN
dataset["text_it"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 1)), "Cari figli amati dal cielo, grazie per essere qui nella preghiera e grazie per aver ascoltato la mia chiamata nel vostro cuore. Figli miei, vi chiedo di seguire Dio che è amore, l’unico vero e infinito amore, siate voi uniti nel Suo amore, solo cosi tutto potrà essere slegato dalle trappole infernali. Figli miei, abbiate un cuore puro e potrete entrare nel regno dei cieli, infatti Io fui affidata a Giovanni, un ragazzo dal cuore di bambino, solo lui avrebbe potuto proteggere la grazia. Figli, abbiate fede in Dio e seguite i suoi comandamenti, non lasciatevi distrarre dalle cose del mondo, ma abbiate sempre lo sguardo rivolto al cielo. Ora vi benedico nel nome della Santissima Trinità, Amen.", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 3)), "Figli benedetti, grazie per essere qui nella preghiera e per aver ascoltato la mia chiamata nel vostro cuore. Figli miei se sapeste quanto è grande il mio amore di madre per voi!   Figli, Io sono qui a chiedere ancora la conversione del vostro cuore. Figli cari, siate vicini al mio cuore e a quello di mio Figlio Gesù, solo così avrete la salvezza. Figli miei, ormai la persecuzione è in atto, ma non dovete temere se siete in Cristo, perché nulla vi mancherà. La carestia si sentirà arrivare, eppure chi è con Gesù dovrà stare tranquillo. Figli miei, pregate affinché le chiese non vengano chiuse e affinché il cibo di vita eterna non vi sia tolto. Pregate per i miei figli prediletti (sacerdoti) e per coloro che Io ho chiamato per la salvezza dell’umanità, li riconoscerete dal volto dell’amore. Ora vi lascio con la mia benedizione materna, nel nome del Padre, del Figlio e dello Spirito Santo. Amen. La Madonna  era vestita di bianco e aveva in una mano il cuore di Gesù.", dataset["text_it"])

# ENGLISH
dataset["text_en"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 1)), "Dear beloved children of Heaven, thank you for being here in prayer and thank you for listening to my call in your hearts. My children, I ask you to follow God who is love, the only true and infinite love, be united in His love, only in this way can everything be freed from the traps of hell. My children, have a pure heart and you will be able to enter the Kingdom of Heaven, in fact I was entrusted to John, a boy with a child's heart, only he could have protected grace. My children, have faith in God and follow His commandments, do not let yourselves be distracted by the things of the world, but always have your eyes turned to Heaven. Now I bless you in the name of the Most Holy Trinity, Amen.", dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 3)), "Blessed children, thank you for being here in prayer and for listening to my call in your hearts. My children, if you only knew how great is my motherly love for you! My children, I am here still asking for the conversion of your hearts. Dear children, be close to my heart and to that of my Son Jesus, only in this way will you have salvation. My children, by now the persecution is underway, but you must not fear if you are in Christ, for nothing will be lacking. The famine will be felt coming, yet those who are with Jesus must rest assured. My children, pray that the churches will not be closed and that the food of eternal life will not be taken from you. Pray for my beloved children (priests) and for those whom I have called for the salvation of mankind; you will recognize them by the face of love. Now I leave you with my motherly blessing, in the name of the Father and the Son and the Holy Spirit. Amen. Our Lady was dressed in white and had the heart of Jesus in one hand.", dataset["text_en"])


# POLISH
dataset["text_pl"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 1)), "Drogie ukochane dzieci Nieba, dziękuję wam, że jesteście tutaj na modlitwie i dziękuję wam, że słuchacie mojego wołania w waszych sercach. Dzieci moje, proszę was, naśladujcie Boga, który jest miłością, jedyną prawdziwą i nieskończoną miłością, bądźcie zjednoczeni w Jego miłości, tylko w ten sposób wszystko może być uwolnione z sideł piekła. Dzieci moje, miejcie serce czyste, a będziecie mogli wejść do Królestwa Niebieskiego; w rzeczywistości powierzono mnie Janowi, chłopcu o sercu dziecka, tylko on mógł ochronić łaskę. Dzieci moje, miejcie wiarę w Boga i postępujcie według Jego przykazań; nie dajcie się rozproszyć sprawom tego świata, ale zawsze miejcie wzrok zwrócony ku Niebu. Teraz błogosławię was w imię Trójcy Przenajświętszej, Amen.", dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 3)), "Błogosławione dzieci, dziękuję wam, że jesteście tutaj na modlitwie i że słuchacie mojego wołania w waszych sercach. Dzieci moje, gdybyście tylko wiedziały, jak wielka jest moja matczyna miłość do was! Dzieci moje, jestem tu nadal prosząc o nawrócenie waszych serc. Drogie dzieci, bądźcie blisko mojego serca i serca mojego Syna Jezusa, tylko w ten sposób dostąpicie zbawienia. Moje dzieci, teraz prześladowanie jest w toku, ale nie wolno wam się bać, jeśli jesteście w Chrystusie, bo niczego wam nie zabraknie. Głód będzie odczuwalny w nadchodzącym czasie, jednak ci, którzy są z Jezusem, mogą być spokojni. Dzieci moje, módlcie się, aby kościoły nie zostały zamknięte i aby pokarm życia wiecznego nie został wam odebrany. Módlcie się za moje ukochane dzieci (kapłanów) i za tych, których powołałam dla zbawienia ludzkości; poznacie ich po obliczu miłości. A teraz zostawiam was z moim matczynym błogosławieństwem, w imię Ojca i Syna i Ducha Świętego. Amen. Matka Boża była ubrana na biało, a w ręce trzymała Serce Jezusa.", dataset["text_pl"])       
       
       
       
translator = google_translator()  

dataset["text_es"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='es'))
dataset["text_fr"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='fr'))
dataset["text_zh"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='zh'))
dataset["text_de"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='de'))
dataset["text_pt"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='pt'))





dataset.to_csv("june_2021.csv", encoding="utf-8", index=False)





