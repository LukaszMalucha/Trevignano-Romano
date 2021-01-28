# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np




dataset = pd.read_csv("trevignano_2018.csv", encoding="utf-8")



dataset["author"] = np.where(dataset["text"].str.contains("Il vostro Gesù"), "Jesus Christ", dataset["author"])
dataset["author"] = np.where(dataset["text"].str.contains(" Il Vostro Gesù"), "Jesus Christ", dataset["author"])


dataset["text"] = np.where(dataset["text"] == "x", "", dataset["text"])
dataset["text_en"] = np.where(dataset["text_en"] == "x", "", dataset["text_en"])

# SPELLING FIX
dataset["text_pl"] = dataset["text_pl"].str.replace("aa", "a")
dataset["text_pl"] = dataset["text_pl"].str.replace("Ojca Syna i Ducha Świętego", "Ojca i Syna i Ducha Świętego")
dataset["text_pl"] = dataset["text_pl"].str.replace("niebawem przybędę, jestem gotowa", "niebawem przybędę, jestem gotowy")
dataset["text_pl"] = dataset["text_pl"].str.replace("przygotował dla was mój Ojciec, kochać się, kochać", "przygotował dla was, kocham was, kocham was wszystkich")
dataset["text_pl"] = dataset["text_pl"].str.replace("Kochajcie się bardziej niż własne dzieci", "Kochajcie siebie nawzajem bardziej niż własne dzieci")
dataset["text_pl"] = dataset["text_pl"].str.replace("ale wy z wiarą wygracie całą wieczność na całe życie", "ale wy przez swoją wiarę zdobędziecie życie wieczne")
dataset["text_pl"] = dataset["text_pl"].str.replace("zostawiam ci spokój", "zostawiam ci pokój")
dataset["text_pl"] = dataset["text_pl"].str.replace("twoje zbawienie wkrótce nadejdzie ze mną chwalebne, uśmiechnij się i raduj", "twoje zbawienie wkrótce będzie ze mną w chwale, uśmiechnij się i raduj")
dataset["text_pl"] = dataset["text_pl"].str.replace("Mój Ojciec posyła mnie po zbawienie ludzi, proszę, nie myśl za dużo, nigdy nie zrozumiecie planów mego Ojca", "Mój Ojciec posyła mnie dla zbawienia ludzkości, proszę nie rozumujcie za bardzo, nigdy nie zrozumiecie planów mojego Ojca")
dataset["text_pl"] = dataset["text_pl"].str.replace("Dzięki za powitanie mnie", "Dziękuję, że mnie przyjęliście")
dataset["text_pl"] = dataset["text_pl"].str.replace("I Eucharystii", "i Eucharystii")
dataset["text_pl"] = dataset["text_pl"].str.replace("a co nie\.\.", "a co nie.")
dataset["text_pl"] = dataset["text_pl"].str.replace("teraz w niektórych kościołach mój Syn zniknął", "teraz mój Syn zniknął w niektórych kościołach")
dataset["text_pl"] = dataset["text_pl"].str.replace("znaki z nieba", "znaki z Nieba")
dataset["text_pl"] = dataset["text_pl"].str.replace("ale dlaczego nie powierzysz mi wszystkiego", "ale dlaczego nie ufasz mi we wszystkim")
dataset["text_pl"] = dataset["text_pl"].str.replace("Boga\.Zaczęła", "Boga. Rozpoczęła")
dataset["text_pl"] = dataset["text_pl"].str.replace("Drogie dzieci, dziękujemy, że jesteście tu zgromadzeni", "Drogie dzieci, dziękuję, że tu jesteście")
dataset["text_pl"] = dataset["text_pl"].str.replace("Zapraszam do spojrzenia na znaki, które przyjdą z nieba, dzięki którym zrozumiecie wiele rzeczy", "Zachęcam was, abyście patrzyli na znaki, które przyjdą z nieba, dzięki którym zrozumiecie wiele rzeczy")





dataset.to_csv("trevignano2018.csv", index=False, encoding="utf-8")
dataset.to_json("trevignano2018.json",orient="records")
