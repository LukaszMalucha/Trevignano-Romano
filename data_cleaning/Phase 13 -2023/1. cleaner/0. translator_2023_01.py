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




dataset = pd.read_csv("january_cleaned.csv", encoding="utf-8")




# ITALIAN

dataset["text_it"] = np.where(((dataset["month"] == 1) & (dataset["day"] == 3)), "Cari Figli, grazie per aver risposto alla mia chiamata nel vostro cuore. Figli, i tempi verso cui andrete incontro saranno duri ed è per questo che vi chiedo di aumentare la vostra preghiera e soprattutto la preghiera del Santo Rosario, arma potente contro il male.  Figli miei, adesso più di prima avrete necessità di protezione, non avete più il parafulmine che prega per voi ma dovete essere pronti e prepararvi per questa trasformazione della vostra anima. Fatevi toccare dalla luce, non siate presi dall’iniquità. Oggi il male festeggia credendo di aver vinto, portando via le anime, illudendole che le luci del modo, il potere e la lussuria, siano più importanti della preghiera e di Dio. Figli, il fuoco cadrà dal cielo perché la terra ha bisogno di essere purificata. Tanti saranno i disastri naturali, terremoti e alluvioni, che si susseguiranno come non mai. Chiedo di pregare per la Chiesa e per gli uomini di essa, corrotti, ormai hanno perso la strada, molti sacerdoti, vescovi e cardinali sono nella confusione. Chiedo ai sacerdoti: ascoltate e credete alle mie parole altrimenti l’inferno vi attenderà. Figli, Io voglio salvarvi e non ho più parole, vi prego aiutatemi figli miei dolcissimi. Il Padre mio vi guarda ed oggi molte saranno le grazie che scenderanno in mezzo a voi. Testimoniate. Vi dico che il Santo Padre è al cospetto di Dio in Paradiso e vi chiede di amarvi l’un l’altro. Un capo di stato verrà attaccato, la guerra invaderà l’Europa. Ora vi benedico nel nome del Padre, del Figlio e dello Spirito Santo. Amen.", dataset["text_it"])


# ENGLISH

dataset["text_en"] = np.where(((dataset["month"] == 1) & (dataset["day"] == 3)), "Dear Children, thank you for responding to my call in your hearts. My children, the times toward which you are going will be hard and that is why I ask you to increase your prayer and especially the prayer of the Holy Rosary, a powerful weapon against evil.  My children, now more than before you will need protection, you no longer have the lightning rod praying for you but you must be ready and prepare for this transformation of your soul. Let the light touch you; do not be caught up in iniquity. Today evil celebrates by believing it has won, taking souls away, deluding them that the lights of the way, power and lust, are more important than prayer and God. Children, fire will fall from heaven because the earth needs to be purified. So many will be the natural disasters, earthquakes and floods, which will come as never before. I ask for prayers for the Church and the men in it, corrupt, now they have lost their way, many priests, bishops and cardinals are in confusion. I ask the priests: listen and believe my words otherwise hell will await you. My children, I want to save you and I have no more words, please help My sweetest children. My Father is watching you and today many will be the graces that will descend among you. Testify. I tell you that the Holy Father stands before God in Heaven and asks you to love one another. A head of state will be attacked, war will invade Europe. Now I bless you in the name of the Father and the Son and the Holy Spirit. Amen.", dataset["text_en"])


# POLISH

dataset["text_pl"] = np.where(((dataset["month"] == 1) & (dataset["day"] == 3)), "Drogie Dzieci, dziękuję Wam, że w swoich sercach odpowiadacie na moje wezwanie. Moje dzieci, czasy, ku którym zmierzacie, będą trudne i dlatego proszę was o wzmożoną modlitwę, a szczególnie o modlitwę Różańca Świętego, potężnej broni przeciwko złu. Moje dzieci, teraz bardziej niż wcześniej potrzebujecie ochrony, nie macie już piorunochronu, który modli się za was, ale musicie być gotowi i przygotować się na tę przemianę waszej duszy. Pozwólcie, by dotknęło was światło, nie dajcie się zawładnąć przez nieprawość. Dziś zło świętuje, wierząc, że zwyciężyło, zabierając dusze, łudząc, że blask świata, władza i żądza, są ważniejsze od modlitwy i Boga. Moje dzieci, ogień spadnie z nieba, ponieważ ziemia musi być oczyszczona. Będzie więcej niż kiedykolwiek wcześniej klęsk żywiołowych, trzęsień ziemi i powodzi. Proszę o modlitwę za Kościół i za ludzi w nim, skorumpowanych, pogubili się, wielu księży, biskupów i kardynałów jest w zamęcie. Proszę księży: słuchajcie i wierzcie w moje słowa, inaczej czeka was piekło. Moje dzieci, chcę was uratować i nie mam już słów, proszę, pomóżcie mi moje najsłodsze dzieci. Mój Ojciec patrzy na was i dziś wiele będzie łask, które zstąpią pośród was. Bądźcie świadectwem. Mówię wam, że Ojciec Święty jest w obecności Boga w Raju i prosi was, abyście się wzajemnie miłowali. Głowa państwa zostanie zaatakowana, wojna wtargnie do Europy. Teraz błogosławię was w imię Ojca i Syna i Ducha Świętego. Amen.", dataset["text_pl"])


dataset = dataset[['year', 'month', 'day', 'author', 'text_it', 'month_string', 'text_pl','text_en']]



from googletrans import Translator
translator = Translator()

dataset["text_es"] = dataset["text_en"].apply(lambda x: translator.translate(x,'es'))
dataset["text_es"] = dataset["text_es"].apply(lambda x: x.text)

dataset["text_fr"] = dataset["text_en"].apply(lambda x: translator.translate(x,'fr'))
dataset["text_fr"] = dataset["text_fr"].apply(lambda x: x.text)

dataset["text_zh"] = dataset["text_en"].apply(lambda x: translator.translate(x,'zh-cn'))
dataset["text_zh"] = dataset["text_zh"].apply(lambda x: x.text)

dataset["text_de"] = dataset["text_en"].apply(lambda x: translator.translate(x,'de'))
dataset["text_de"] = dataset["text_de"].apply(lambda x: x.text)

dataset["text_pt"] = dataset["text_en"].apply(lambda x: translator.translate(x,'pt'))
dataset["text_pt"] = dataset["text_pt"].apply(lambda x: x.text)


dataset["month_string"] = "January"
dataset.to_csv("january_2023.csv", encoding="utf-8", index=False)






