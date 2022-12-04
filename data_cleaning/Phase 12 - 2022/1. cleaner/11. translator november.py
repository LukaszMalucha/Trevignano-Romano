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
dataset["text_it"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 5)), "Amati figli, grazie per essere qui nella preghiera e per aver risposto alla mia chiamata nel vostro cuore. Figli amati, le piaghe saranno tante quanto i peccati del mondo, ci saranno terremoti e alluvioni e ancora voi non capite i moniti del cielo. Figli miei, non stancatevi di fare scorte perché vi dico, ancora, che la carestia arriverà all’improvviso. Figli, i tempi della prova saranno pesanti ma voi pregate ed elevate il vostro spirito. Pregate per la Chiesa. Figli amati, siate fiduciosi perché il nuovo tempo non è molto distante, sarà un tempo di amore, di pace dove non ci sarà dolore, ma solo gioia e finalmente opererete solo per il bene. Ora vi lascio con la mia benedizione materna nel nome del Padre, del Figlio e dello Spirito Santo. Amen.", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 8)), "Cara figlia, grazie, per avermi accolta nel tuo cuore. Figlia, devi dire a tutti di amare e perdonare. Non abbiate paura per il domani se siete in Cristo, capisco coloro che amano e che hanno fede e si sentono diversi da questo mondo, che è preso dalle cose frivole, dalle bugie e da una condotta non Cristiana. Le vostre preghiere mitigheranno l’Ira di Dio. Figli, abbiate sempre la pace, l’amore e la speranza nel cuore. Io non vengo per spaventarvi, ma per chiedervi la conversione. Sono una Madre che ama i suoi figli. Figli miei, l’Arcangelo Michele, sarà al vostro fianco, per liberarvi dal male che vi circonda. Gesù è in arrivo e il paradiso vi attende. Ora, vi benedico nel nome del Padre, del Figlio e dello Spirito Santo, amen.", dataset["text_it"])
# dataset["text_it"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 9)), "", dataset["text_it"])
# dataset["text_it"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 1)), "", dataset["text_it"])
# dataset["text_it"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 1)), "", dataset["text_it"])

# ENGLISH
dataset["text_en"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 3)), "My children, thank you for being here and for answering my call in your hearts. My children, my tears flow for those who do not heed my call. I weep for blasphemies and for priests who are not faithful to God. I weep for those who despite the signs of the times, are tied to the false lights of the world. My children, please convert, the times will be hard. Pray that your Father will be merciful. There will be famine in the world and there will be a shortage of food. Children, provide for yourselves and your brothers and sisters. The hearts of men are getting harder and harder and that is how Satan will lead into the abyss. Children, invoke Me in the time of suffering and I will be with you. Call upon my Son Jesus and He will change suffering into peace and sadness into joy. Be firm in faith, many do not know God and do not want to know Him, yet He is Father and does not want to lose you. Children, follow the path of Holiness, read the Gospel and the Word and there you will find everything you need. Love yourselves as God has loved you. Now I leave you with my motherly blessing, in the name of the Father and the Son and the Holy Spirit, Amen.", dataset["text_pl"])
dataset["text_en"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 5)), "Beloved children, thank you for being here in prayer and for answering my call in your hearts. Beloved children, the plagues will be as many as the sins of the world, there will be earthquakes and floods and still you do not understand the warnings of heaven. My children, do not tire of stockpiling because I tell you, again, that famine will come suddenly. My children, the times of trial will be heavy but you pray and elevate your spirits. Pray for the Church. Beloved children, be confident because the new time is not far off, it will be a time of love, of peace where there will be no pain but only joy and finally you will work only for good. Now I leave you with my motherly blessing in the name of the Father and the Son and the Holy Spirit. Amen.", dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 8)), "Dear daughter, thank you, for welcoming me into your heart. Daughter, you must tell everyone to love and forgive. Do not be afraid for tomorrow if you are in Christ, I understand those who love and have faith and feel different from this world, which is caught up in frivolous things, lies and non-Christian conduct. Your prayers will mitigate the Wrath of God. Children, always have peace, love and hope in your hearts. I do not come to frighten you, but to ask you for conversion. I am a Mother who loves her children. My children, Archangel Michael, will be at your side, to deliver you from the evil that surrounds you. Jesus is coming and Heaven awaits you. Now, I bless you in the name of the Father and the Son and the Holy Spirit, Amen.", dataset["text_en"])
# dataset["text_en"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 9)), "", dataset["text_en"])
#dataset["text_en"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 1)), "", dataset["text_en"])
#dataset["text_en"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 1)), "", dataset["text_en"])

# POLISH
dataset["text_pl"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 3)), "Moje dzieci, dziękuję wam, że jesteście tutaj i że odpowiadacie na moje wezwanie w waszych sercach. Moje dzieci, moje łzy płyną za tych, którzy nie słuchają mojego wezwania. Płaczę za bluźniercami i za kapłanami, którzy nie są wierni Bogu. Płaczę za tymi, którzy mimo znaków czasu są przywiązani do fałszywych lamp tego świata. Moje dzieci, błagam was o nawrócenie, czasy będą ciężkie. Módlcie się, aby Wasz Ojciec był miłosierny. Na świecie zapanuje głód i zabraknie żywności. Moje dzieci, zapewnijcie byt sobie i swoim braciom. Serca ludzi stają się coraz twardsze i w ten sposób szatan doprowadzi ich do przepaści. Dzieci, przywołajcie Mnie w czasie waszego cierpienia, a Ja będę z wami. Wzywajcie mojego Syna Jezusa, a On przemieni cierpienie w pokój, a smutek w radość. Bądźcie mocni w wierze, wielu nie zna Boga i nie chce Go poznać, a przecież On jest Ojcem i nie chce was stracić. Moje dzieci, idźcie drogą świętości, czytajcie Ewangelię, a tam znajdziecie wszystko, czego potrzebujecie. Kochajcie się tak, jak Bóg was umiłował. A teraz zostawiam was z moim matczynym błogosławieństwem, w imię Ojca i Syna i Ducha Świętego, Amen.", dataset["text_en"])
dataset["text_pl"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 5)), "Umiłowane dzieci, dziękuję wam, że jesteście tu na modlitwie i że odpowiadacie na moje wezwanie w waszych sercach. Umiłowane dzieci, plag będzie tyle, ile grzechów świata, będą trzęsienia ziemi i powodzie, a mimo to nie rozumiecie ostrzeżeń nieba. Dzieci moje, nie męczcie się gromadzeniem zapasów, bo powtarzam wam, że głód przyjdzie nagle. Moje dzieci, czasy próby będą ciężkie, ale wy módlcie się i podnoście na duchu. Módlcie się za Kościół. Ukochane dzieci, bądźcie pewni, bo nowy czas jest już niedaleko, będzie to czas miłości, pokoju, gdzie nie będzie bólu, ale tylko radość i wreszcie będziecie pracować tylko dla dobra. Zostawiam was teraz z moim matczynym błogosławieństwem w imię Ojca i Syna i Ducha Świętego. Amen.", dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 8)), "Droga córko, dziękuję ci, że przyjęłaś mnie do swojego serca. Córko, musisz powiedzieć wszystkim, żeby kochali i przebaczali. Nie lękajcie się o jutro, jeśli jesteście w Chrystusie, rozumiem tych, którzy kochają i mają wiarę i czują się inni niż ten świat, który jest uwikłany w błahe sprawy, kłamstwa i niechrześcijańskie postępowanie. Twoje modlitwy złagodzą Gniew Boży. Moje dzieci, miejcie zawsze w swoich sercach pokój, miłość i nadzieję. Nie przychodzę, by was straszyć, ale by prosić o nawrócenie. Jestem Matką, która kocha swoje dzieci. Moje dzieci, Archanioł Michał będzie u waszego boku, aby uwolnić was od zła, które was otacza. Jezus nadchodzi i Niebo czeka na was. Teraz błogosławię was w imię Ojca i Syna i Ducha Świętego, Amen.", dataset["text_pl"])
# dataset["text_pl"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 9)), "", dataset["text_pl"])
#dataset["text_pl"] = np.where(((dataset["month"] == 11) & (dataset["day"] == 1)), "", dataset["text_pl"])
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
# dataset_translate = dataset
# dataset_translate.to_csv("november_2022.csv", encoding="utf-8", index=False)



