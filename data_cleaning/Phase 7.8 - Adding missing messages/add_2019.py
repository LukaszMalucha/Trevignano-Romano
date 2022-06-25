# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np
from google_trans_new import google_translator


dataset_2019 = pd.read_json("trevignano2019.js")



missing_2019 = pd.read_csv("missing_2019.csv")


#Italian
missing_2019["text_it"] = np.where(((missing_2019["month"] == 4) & (missing_2019["day"] == 13)), "Amati figli, grazie per aver risposto alla mia chiamata nel vostro cuore. Figli miei, quanti dolori ascolto, io sono qui per condurvi verso la luce del Signore. Cari figlioli, io sono arrivata a toccare la terra, ma pochi ascoltano i miei messaggi, sappiate che presto la terra tremerà, ma voi state nella gioia e nell’amore di Dio, non perdetevi, la vostra fonte dovrà essere il Vangelo. Amati figli, in questa settimana di Pasqua, amate la Croce e ringraziate il Signore, non sempre potrete capire tutto ciò che sono i progetti di Dio e spesso è umanamente incomprensibile, solo il cielo e la preghiera potrà rispondere ai vostri quesiti se avrete aperto il vostro cuore. Non cambiate le preghiere e non cambiate nulla dei dogmi della fede perché sarebbe una bestemmia, satana è astuto, prende le anime senza che ve ne accorgiate. Io vi amo, sono vostra Madre, vi proteggo e vi metto tutti sotto il mio Manto. Ora, vi lascio con la mia benedizione materna, nel nome del Padre, del Figlio dello Spirito Santo, Amen.", missing_2019["text_it"])




#English
missing_2019["text_en"] = np.where(((missing_2019["month"] == 4) & (missing_2019["day"] == 13)), "Beloved children, thank you for having responded to my call in your hearts. My children, how many sorrows I hear, I am here to lead you towards the light of the Lord. Dear children, I have come to touch the earth, but few listen to my messages, know that soon the earth will tremble, but you are in the joy and love of God, do not get lost, your source must be the Gospel. Beloved children, in this Easter week, love the Cross and thank the Lord, you will not always be able to understand everything that is God's plan and often it is humanly incomprehensible, only Heaven and prayer will be able to answer your questions if you will have opened your heart. Don't change your prayers and don't change anything about the dogmas of the faith because it would be blasphemy, Satan is cunning, he takes souls without you noticing. I love you, I am your Mother, I protect you and I place you all under my mantle. Now, I leave you with my motherly blessing, in the name of the Father and the Son and the Holy Spirit, Amen.", missing_2019["text_en"])



#Polish
missing_2019["text_pl"] = np.where(((missing_2019["month"] == 4) & (missing_2019["day"] == 13)), "Umiłowane dzieci, dziękuję wam, że odpowiedzieliście na moje wezwanie w waszych sercach. Moje dzieci, jak wiele bólu słyszę, jestem tutaj, aby poprowadzić was ku światłu Pana. Drogie dzieci, przyszłam dotknąć ziemi, ale niewielu słucha moich przesłań, wiedzcie, że wkrótce ziemia zadrży, ale wy jesteście w radości i miłości Boga, nie zgubcie się, waszym źródłem musi być Ewangelia. Umiłowane dzieci, w tym tygodniu wielkanocnym, kochajcie Krzyż i dziękujcie Panu, nie zawsze będziecie mogli zrozumieć wszystko, co jest Bożym planem i często jest to po ludzku niezrozumiałe, tylko niebo i modlitwa będą mogły odpowiedzieć na wasze pytania, jeśli otworzycie swoje serce. Nie zmieniajcie waszych modlitw i nie zmieniajcie nic w dogmatach wiary, bo to byłoby bluźnierstwo, szatan jest przebiegły, zabiera dusze, a wy tego nie zauważacie. Kocham was, jestem waszą Matką, chronię was i chowam was wszystkich pod moim płaszczem. Teraz zostawiam was z moim matczynym błogosławieństwem, w imię Ojca i Syna i Ducha Świętego, Amen.", missing_2019["text_pl"])



translator = google_translator()  
#
#missing_2019["text_es"] = missing_2019["text_en"].apply(lambda x: translator.translate(x,lang_tgt='es'))
#missing_2019["text_fr"] = missing_2019["text_en"].apply(lambda x: translator.translate(x,lang_tgt='fr'))
#missing_2019["text_zh"] = missing_2019["text_en"].apply(lambda x: translator.translate(x,lang_tgt='zh'))
#missing_2019["text_de"] = missing_2019["text_en"].apply(lambda x: translator.translate(x,lang_tgt='de'))
#missing_2019["text_pt"] = missing_2019["text_en"].apply(lambda x: translator.translate(x,lang_tgt='pt'))




import goslate
gs = goslate.Goslate()

missing_2019["text_es"] = missing_2019["text_it"].apply(lambda x: gs.translate(x,'es'))
missing_2019["text_fr"] = missing_2019["text_en"].apply(lambda x: gs.translate(x,'fr'))
missing_2019["text_zh"] = missing_2019["text_en"].apply(lambda x: gs.translate(x,'zh'))
missing_2019["text_de"] = missing_2019["text_en"].apply(lambda x: gs.translate(x,'de'))
missing_2019["text_pt"] = missing_2019["text_en"].apply(lambda x: gs.translate(x,'pt'))




dataset_merged = pd.concat([dataset_2019, missing_2019])


dataset_merged["month_string"] = np.where(dataset_merged["month"] == 4, "April", dataset_merged["month_string"]) 
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 5, "May", dataset_merged["month_string"]) 
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 7, "July", dataset_merged["month_string"]) 
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 9, "August", dataset_merged["month_string"]) 
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 10, "October", dataset_merged["month_string"]) 
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 12, "December", dataset_merged["month_string"]) 



dataset_merged = dataset_merged.sort_values(by=["month", "day"])




dataset_merged.to_json("trevignano2019.js",orient="records")






