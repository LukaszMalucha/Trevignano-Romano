# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np
from google_trans_new import google_translator


dataset_2021 = pd.read_json("trevignano2021.js")



missing_2021 = pd.read_csv("missing_2021.csv")


#Italian
missing_2021["text_it"] = np.where(((missing_2021["month"] == 5) & (missing_2021["day"] == 12)), "Amati figli miei, grazie per essere qui nella preghiera e per aver ascoltato la mia chiamata nel vostro cuore. Figli miei, i tempi in cui andate incontro saranno di dolore, questo è il motivo per cui Io tocco la terra, per poter riunire tutti i miei figli sparsi in tutto il mondo, vi prego figli abbiate pietà del mio Gesù, che più di prima viene bestemmiato e trattato male, questo comportamento continua a flagellarlo senza alcuna pietà. Amati figli, presto arriverà un uomo che sarà osannato dai potenti di tutte le nazioni, ma lui sarà l’anticristo, questo tempo è ormai vicino, la persecuzione avrà inizio in tutte le parti del mondo, ma non temete perché Io sarò sempre con voi per proteggervi. Figli miei, non abbiate paura della verità e della vostra fede, raccomando di seguire sempre il Santo Vangelo. Oggi scenderanno grazie su di voi. Vi lascio con la mia benedizione materna nel nome del Padre, del Figlio e dello Spirito Santo, Amen.", missing_2021["text_it"])
missing_2021["text_it"] = np.where(((missing_2021["month"] == 6) & (missing_2021["day"] == 8)), "Cari figli, grazie per essere qui nella preghiera. Figli amati, vi chiedo spesso di essere fiamme accese per il mondo, ma a volte siete indifferenti. Figli, come disse Gesù ai suoi apostoli: che il vostro parlare sia si si, no no; il di più viene dal maligno. Convertitevi e fatevi trovare pronti per ciò che sta per arrivare. Figli amati,  non ragionate quando siete nella fede,  il ragionamento umano non arriverà  mai a capire ciò che Dio ha preparato per voi, a volte vi guardo mentre cercate date e tempi che solo Dio conosce, ma una cosa voglio svelarla: guardatevi  intorno, anche se a voi sembra un caso,  Io sto provvedendo ad avvicinarvi tutti, ricordate che non è una vostra decisione, ma la Mia. Vorrei che tutti i miei figli prediletti possano stare vicini per aiutarsi l’uno con l’altro per quando arriverà il momento e voglio mettervi insieme per combattere l’ultima battaglia. Figli miei, Dio ha preparato tutto per voi, nuovi cieli e nuova terra, dove ci sarà serenità e gioia, spariranno malattie e lamenti e tutto sarà preghiera e amore per Dio. Ora vi lascio con la mia santa benedizione nel nome del Padre, del Figlio e dello Spirito Santo, amen.", missing_2021["text_it"])



#English
missing_2021["text_en"] = np.where(((missing_2021["month"] == 5) & (missing_2021["day"] == 12)), "My beloved children, thank you for being here in prayer and for listening to My call in your heart. My children, the times you are going through will be times of sorrow, this is why I am touching the earth, so that I can gather all my children scattered all over the world, I beg you children to have mercy on my Jesus, who more than before is blasphemed and treated badly, this behavior continues to scourge him without any mercy. Beloved children, soon a man will come who will be hailed by the powerful of all nations, but he will be the antichrist, this time is near, the persecution will begin in all parts of the world, but do not fear because I will always be with you to protect you. My children, do not be afraid of the truth and of your faith, I recommend that you always follow the Holy Gospel. Today graces will descend upon you. I leave you with my motherly blessing in the name of the Father and the Son and the Holy Spirit, Amen.", missing_2021["text_en"])
missing_2021["text_en"] = np.where(((missing_2021["month"] == 6) & (missing_2021["day"] == 8)), "Dear children, thank you for being here in prayer. Beloved children, I often ask you to be bright flames for the world, but at times you are indifferent. My children, as Jesus said to His apostles: let your speech be yes yes, no no; more comes from the evil one. Convert and be ready for what is coming. Beloved children, do not reason when you are in the faith, human reasoning will never come to understand what God has prepared for you, sometimes I watch you while you look for dates and times that only God knows, but I want to reveal one thing: look around you, even if it seems to you to be a coincidence, I am providing to bring you all closer, remember that it is not your decision, but Mine. I want all My beloved children to be able to stay close to help each other for when the time comes and I want to put you together to fight the last battle. My children, God has prepared everything for you, new heavens and new earth, where there will be serenity and joy, sickness and lamentations will disappear and everything will be prayer and love for God. Now I leave you with my holy blessing in the name of the Father and the Son and the Holy Spirit, Amen.", missing_2021["text_en"])


#Polish
missing_2021["text_pl"] = np.where(((missing_2021["month"] == 5) & (missing_2021["day"] == 12)), "Moje kochane dzieci, dziękuję wam, że jesteście tutaj na modlitwie i że słuchacie mojego wołania w waszych sercach. Dzieci moje, czasy, które przeżywacie, będą czasami smutku, dlatego dotykam ziemi, aby zgromadzić wszystkie moje dzieci rozproszone po całym świecie, błagam was, dzieci, miejcie litość nad moim Jezusem, który jest bluźniony i traktowany gorzej niż przedtem, to zachowanie nadal go biczuje bez żadnej litości. Umiłowane dzieci, wkrótce przyjdzie człowiek, który będzie okrzyknięty przez potężnych wszystkich narodów, ale on będzie antychrystem, ten czas jest bliski, prześladowania zaczną się we wszystkich częściach świata, ale nie bójcie się, bo ja zawsze będę z wami, aby was chronić. Dzieci moje, nie bójcie się prawdy i waszej wiary; polecam wam, abyście zawsze szli za świętą Ewangelią. Dziś zstąpią na was łaski. Zostawiam was z moim matczynym błogosławieństwem w imię Ojca i Syna i Ducha Świętego, Amen.", missing_2021["text_pl"])
missing_2021["text_pl"] = np.where(((missing_2021["month"] == 6) & (missing_2021["day"] == 8)), "Drogie dzieci, dziękuję wam za waszą obecność na modlitwie. Umiłowane dzieci, często proszę was, abyście byli rozpalonymi płomieniami dla świata, ale czasami jesteście obojętni. Dzieci moje, jak powiedział Jezus do swoich apostołów: niech wasza mowa będzie tak, tak, nie, nie; więcej pochodzi od złego. Przekształćcie się i bądźcie gotowi na to, co nadchodzi. Umiłowane dzieci, nie rozumujcie, gdy jesteście w wierze, ludzkie rozumowanie nigdy nie dojdzie do zrozumienia tego, co Bóg dla was przygotował, czasami obserwuję was, gdy szukacie dat i godzin, które zna tylko Bóg, ale chcę wam objawić jedną rzecz: rozejrzyjcie się wokół siebie, nawet jeśli wydaje się wam to przypadkiem, Ja zapewniam, aby was wszystkich zbliżyć, pamiętajcie, że to nie jest wasza decyzja, ale Moja. Chcę, by wszystkie moje ukochane dzieci mogły pozostać blisko siebie, by pomagać sobie nawzajem, gdy nadejdzie czas, i chcę was zgromadzić, by stoczyć ostatnią bitwę. Moje dzieci, Bóg przygotował dla was wszystko, nowe niebo i nową ziemię, gdzie będzie spokój i radość, znikną choroby i lamenty, a wszystko będzie modlitwą i miłością do Boga. Teraz zostawiam was z moim świętym błogosławieństwem w imię Ojca i Syna i Ducha Świętego, Amen.", missing_2021["text_pl"])



translator = google_translator()  

#missing_2021["text_es"] = missing_2021["text_en"].apply(lambda x: translator.translate(x,lang_tgt='es'))
#missing_2021["text_fr"] = missing_2021["text_en"].apply(lambda x: translator.translate(x,lang_tgt='fr'))
#missing_2021["text_zh"] = missing_2021["text_en"].apply(lambda x: translator.translate(x,lang_tgt='zh'))
#missing_2021["text_de"] = missing_2021["text_en"].apply(lambda x: translator.translate(x,lang_tgt='de'))
#missing_2021["text_pt"] = missing_2021["text_en"].apply(lambda x: translator.translate(x,lang_tgt='pt'))





import goslate
gs = goslate.Goslate()

missing_2021["text_es"] = missing_2021["text_it"].apply(lambda x: gs.translate(x,'es'))
missing_2021["text_fr"] = missing_2021["text_en"].apply(lambda x: gs.translate(x,'fr'))
missing_2021["text_zh"] = missing_2021["text_en"].apply(lambda x: gs.translate(x,'zh'))
missing_2021["text_de"] = missing_2021["text_en"].apply(lambda x: gs.translate(x,'de'))
missing_2021["text_pt"] = missing_2021["text_en"].apply(lambda x: gs.translate(x,'pt'))







dataset_merged = pd.concat([dataset_2021, missing_2021])


dataset_merged["month_string"] = np.where(dataset_merged["month"] == 4, "April", dataset_merged["month_string"]) 
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 5, "May", dataset_merged["month_string"]) 
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 6, "June", dataset_merged["month_string"]) 
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 7, "July", dataset_merged["month_string"]) 
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 9, "August", dataset_merged["month_string"]) 
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 10, "October", dataset_merged["month_string"]) 
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 12, "December", dataset_merged["month_string"]) 



dataset_merged = dataset_merged.sort_values(by=["month", "day"])




dataset_merged.to_json("trevignano2021.js",orient="records")





