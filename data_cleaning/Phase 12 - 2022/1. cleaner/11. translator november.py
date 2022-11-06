# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np
from google_trans_new import google_translator
import goslate
gs = goslate.Goslate()




dataset = pd.read_csv("november_cleaned.csv", encoding="utf-8")




# ITALIAN

dataset["text_it"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 3)), "Figli miei, grazie per essere qui e per aver risposto alla mia chiamata nel vostro cuore. Figli, le mie lacrime scendono per coloro che non ascoltano la mia chiamata. Piango per le bestemmie e per i sacerdoti che non sono fedeli a Dio. Piango per coloro che nonostante i segni dei tempi, sono legati alle false luci del mondo. Figli, vi prego convertitevi, i tempi saranno duri. Pregate affinché il Padre vostro sia misericordioso. Ci sarà la carestia nel mondo e mancherà il cibo. Figli, provvedete per voi e per i vostri fratelli. Il cuore degli uomini è sempre più duro ed è così che Satana condurrà negli abissi. Figli, invocatemi nel momento della sofferenza e Io sarò con voi. Invocate mio Figlio Gesù e Lui cambierà la sofferenza nella pace e la tristezza nella gioia. Siate saldi nella fede, molti non conoscono Dio e non vogliono conoscerlo, eppure Lui è Padre e non vuole perdervi. Figli, seguite la strada della Santità, leggete il Vangelo e la Parola e lì troverete tutto ciò che vi servirà. Amatevi come Dio vi ha amato. Ora vi lascio con la mia benedizione materna, nel nome del Padre, del Figlio e dello Spirito Santo, amen.", dataset["text_it"])
# dataset["text_it"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 1)), "", dataset["text_it"])

# ENGLISH
dataset["text_en"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 3)), "My children, thank you for being here and for answering my call in your hearts. My children, my tears flow for those who do not heed my call. I weep for blasphemies and for priests who are not faithful to God. I weep for those who despite the signs of the times, are tied to the false lights of the world. My children, please convert, the times will be hard. Pray that your Father will be merciful. There will be famine in the world and there will be a shortage of food. Children, provide for yourselves and your brothers and sisters. The hearts of men are getting harder and harder and that is how Satan will lead into the abyss. Children, invoke Me in the time of suffering and I will be with you. Call upon my Son Jesus and He will change suffering into peace and sadness into joy. Be firm in faith, many do not know God and do not want to know Him, yet He is Father and does not want to lose you. Children, follow the path of Holiness, read the Gospel and the Word and there you will find everything you need. Love yourselves as God has loved you. Now I leave you with my motherly blessing, in the name of the Father and the Son and the Holy Spirit, Amen.", dataset["text_pl"])
#dataset["text_en"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 1)), "", dataset["text_en"])

# POLISH
dataset["text_pl"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 3)), "Moje dzieci, dziękuję wam, że jesteście tutaj i że odpowiadacie na moje wezwanie w waszych sercach. Moje dzieci, moje łzy płyną za tych, którzy nie słuchają mojego wezwania. Płaczę za bluźniercami i za kapłanami, którzy nie są wierni Bogu. Płaczę za tymi, którzy mimo znaków czasu są przywiązani do fałszywych lamp tego świata. Moje dzieci, błagam was o nawrócenie, czasy będą ciężkie. Módlcie się, aby Wasz Ojciec był miłosierny. Na świecie zapanuje głód i zabraknie żywności. Moje dzieci, zapewnijcie byt sobie i swoim braciom. Serca ludzi stają się coraz twardsze i w ten sposób szatan doprowadzi ich do przepaści. Dzieci, przywołajcie Mnie w czasie waszego cierpienia, a Ja będę z wami. Wzywajcie mojego Syna Jezusa, a On przemieni cierpienie w pokój, a smutek w radość. Bądźcie mocni w wierze, wielu nie zna Boga i nie chce Go poznać, a przecież On jest Ojcem i nie chce was stracić. Moje dzieci, idźcie drogą świętości, czytajcie Ewangelię, a tam znajdziecie wszystko, czego potrzebujecie. Kochajcie się tak, jak Bóg was umiłował. A teraz zostawiam was z moim matczynym błogosławieństwem, w imię Ojca i Syna i Ducha Świętego, Amen.", dataset["text_en"])
#dataset["text_pl"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 1)), "", dataset["text_pl"])

dataset = dataset[['year', 'month', 'day', 'author', 'text_it', 'month_string', 'text_pl','text_en']]

dataset_ready = pd.read_csv("november_2022.csv")


dataset = dataset.merge(dataset_ready, how="left", on=['year', 'month', 'day', 'author', 'text_it', 'month_string', 'text_pl','text_en'])

dataset_ok = dataset[~dataset["text_pt"].isnull()]
dataset_translate = dataset[dataset["text_pt"].isnull()]

from googletrans import Translator
translator = Translator()

dataset_translate["text_es"] = dataset_translate["text_en"].apply(lambda x: translator.translate(x,'es'))
dataset_translate["text_es"] = dataset_translate["text_es"].apply(lambda x: x.text)

dataset_translate["text_fr"] = dataset_translate["text_en"].apply(lambda x: translator.translate(x,'fr'))
dataset_translate["text_fr"] = dataset_translate["text_fr"].apply(lambda x: x.text)

dataset_translate["text_zh"] = dataset_translate["text_en"].apply(lambda x: translator.translate(x,'zh-cn'))
dataset_translate["text_zh"] = dataset_translate["text_zh"].apply(lambda x: x.text)

dataset_translate["text_de"] = dataset_translate["text_en"].apply(lambda x: translator.translate(x,'de'))
dataset_translate["text_de"] = dataset_translate["text_de"].apply(lambda x: x.text)

dataset_translate["text_pt"] = dataset_translate["text_en"].apply(lambda x: translator.translate(x,'pt'))
dataset_translate["text_pt"] = dataset_translate["text_pt"].apply(lambda x: x.text)



dataset = pd.concat([dataset_ok, dataset_translate])

dataset = dataset.sort_values(by="day")


dataset.to_csv("november_2022.csv", encoding="utf-8", index=False)


# First Translation
dataset_translate = dataset
dataset_translate.to_csv("november_2022.csv", encoding="utf-8", index=False)



