# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""


# pip install googletrans==3.1.0a0
import pandas as pd
import numpy as np
from google_trans_new import google_translator
import goslate
gs = goslate.Goslate()




dataset = pd.read_csv("december_cleaned.csv", encoding="utf-8")




# ITALIAN

dataset["text_it"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 3)), "Cari figli, grazie per essere qui nella preghiera e per aver risposto alla mia chiamata nel vostro cuore. Figli miei, vi chiedo ancora la vera conversione. La preghiera con il cuore sarà portata in Cielo, affinché Dio ascolti le vostre richieste, le vostre lodi, i vostri ringraziamenti. Figli preziosi, molti si sono dati alle lusinghe del maligno, ma voi siate retti, giusti, caritatevoli, umili e accendete una candela benedetta quando pregate per sfuggire alle tenebre che vi attanagliano. Figli amorevoli, Io vi amo con tutto l’amore di una Madre e vi voglio salvi tutti. Cari figli, pregate per la Chiesa, ricordate che Dio è misericordioso ed è buono e nonostante ciò che vedrete accadere non perdete mai la Fede e la Speranza. Dio vuole il vostro bene e vuole riempirvi di grazie. Non rifiutate il Suo immenso amore. Figli infedeli, dico a voi: aprite gi occhi e guardate anche la giustizia di Dio cadere su questa terra. Figli miei fedeli, non abbiate paura, siate vicino a Dio con il cuore.  Figli, pregate per l’America, pagherà a caro prezzo le ingiustizie e le leggi perverse. Ora vi lascio con la mia benedizione Materna, nel nome del Padre, del Figlio e dello Spirito Santo. Amen. La Madonna ricorda ancora di leggere e di meditare il libro dell’Apocalisse di San Giovanni apostolo.", dataset["text_it"])
#dataset["text_it"] = np.where(((dataset["month"] == XXX) & (dataset["day"] == 1)), "", dataset["text_it"])

# ENGLISH

dataset["text_en"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 3)), "Dear children, thank you for being here in prayer and for responding to my call in your hearts. My children, I still ask you for true conversion. Prayer with the heart will be taken to Heaven, so that God may hear your requests, your praises, your thanks. Precious children, many have given themselves over to the enticements of the evil one, but you be upright, righteous, charitable, humble and light a blessed candle when you pray to escape the darkness that grips you. Loving children, I love you with all the love of a Mother and I want you all saved. Dear children, pray for the Church, remember that God is merciful and He is good and despite what you see happening never lose your Faith and Hope. God wants your good and wants to fill you with graces. Do not reject His immense love. Unfaithful children, I say to you: open your eyes and watch God's Justice also fall on this earth. My faithful children, do not be afraid, be close to God with your hearts.  My children, pray for America, she will pay dearly for injustice and perverse laws. Now I leave you with my Motherly blessing, in the name of the Father and the Son and the Holy Spirit, Amen. Our Lady reminds us again to read and meditate on the book of Revelation of St. John the Apostle.", dataset["text_en"])
#dataset["text_en"] = np.where(((dataset["month"] == XXX) & (dataset["day"] == 1)), "", dataset["text_en"])

# POLISH

dataset["text_pl"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 3)), "Drogie dzieci, dziękuję wam, że jesteście tu na modlitwie i że odpowiadacie na moje wezwanie w waszych sercach. Moje dzieci, ponownie proszę was o prawdziwe nawrócenie. Modlitwa sercem będzie zaniesiona do nieba, aby Bóg usłyszał wasze prośby, wasze uwielbienia, wasze podziękowania. Drogie dzieci, wielu oddało się na pastwę Złego, ale wy bądźcie prawi, sprawiedliwi, miłosierni, pokorni i zapalajcie błogosławioną świecę, kiedy modlicie się, aby uciec z ciemności, która was ogarnia. Kochane dzieci, kocham was z całą miłością Matki i pragnę, abyście wszyscy byli zbawieni. Drogie dzieci, módlcie się za Kościół, pamiętajcie, że Bóg jest miłosierny i dobry i mimo tego, co zobaczycie, że się dzieje, nigdy nie traćcie wiary i nadziei. Bóg chce twojego dobra i chce cię napełnić łaskami. Nie odrzucajcie Jego ogromnej miłości. Niewierne dzieci, mówię wam: otwórzcie oczy i zobaczcie też, jak Sprawiedliwość Boża spada na tę ziemię. Moje wierne dzieci, nie bójcie się, swoimi sercami bądźcie blisko Boga. Moje dzieci, módlcie się za Amerykę, ona drogo zapłaci za niesprawiedliwość i przewrotne prawa. Teraz zostawiam was z moim matczynym błogosławieństwem, w imię Ojca i Syna i Ducha Świętego, Amen. Matka Boża ponownie przypomina nam, abyśmy czytali i rozważali księgę Apokalipsy św. Jana Apostoła.", dataset["text_pl"])
#dataset["text_pl"] = np.where(((dataset["month"] == XXX) & (dataset["day"] == 1)), "", dataset["text_pl"])

dataset = dataset[['year', 'month', 'day', 'author', 'text_it', 'month_string', 'text_pl','text_en']]


dataset_translate = dataset

# dataset = dataset.merge(dataset_ready, how="left", on=['year', 'month', 'day', 'author', 'text_it', 'month_string', 'text_pl','text_en'])

# dataset_ok = dataset[~dataset["text_pt"].isnull()]
# dataset_translate = dataset[dataset["text_pt"].isnull()]



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


# dataset = pd.concat([dataset_ok, dataset_translate])

# dataset = dataset.sort_values(by="day")


# dataset.to_csv("XXXX_2022.csv", encoding="utf-8", index=False)


# # First Translation
# dataset_translate = dataset
dataset_translate.to_csv("december_2022.csv", encoding="utf-8", index=False)





