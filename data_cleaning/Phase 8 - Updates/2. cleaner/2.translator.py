# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np
from google_trans_new import google_translator



dataset = pd.read_csv("march_cleaned.csv", encoding="utf-8")

dataset["text_pl"] = ""
dataset["text_en"] = ""


dataset["text_it"] = dataset["text_it"].str.replace("\"", "")
dataset["text_it"] = dataset["text_it"].str.replace("AmenLa", "Amen. La")
dataset["text_it"] = dataset["text_it"].str.replace("AmenIn", "Amen. In")
dataset["text_it"] = dataset["text_it"].str.replace("Santo \. Amen", "Santo, Amen.")
dataset["text_it"] = dataset["text_it"].str.replace(" : ", ": ")
dataset["text_it"] = dataset["text_it"].str.replace("Spirito santo", "Spirito Santo")
dataset["text_it"] = dataset["text_it"].str.replace("Dio Figli", "Dio. Figli")
dataset["text_it"] = dataset["text_it"].str.replace("Amen Oggi", "Amen. Oggi")
dataset["text_it"] = dataset["text_it"].str.replace("Continua a leggere\. \. \. \»", "")
dataset["text_it"] = dataset["text_it"].str.replace("sinistro\.\.", "sinistro.")
dataset["text_it"] = dataset["text_it"].str.replace("Amen Il ", "Amen. Il ")







dataset["text_en"] = np.where(((dataset["month"] == 3) & (dataset["day"] == 3)), "Dear children, thank you for having responded to my call in your hearts. Beloved children, I, your Mother, ask you: take my hands and listen to what is coming to you from Heaven, for everything is for your salvation. Take advantage of this time of mercy, for soon justice and God's wrath will make themselves felt; by now the time left is very short, as is the time I will remain with you. My beloved ones, do not fear for the times that will come or that have already come, because with prayer and conversion you will be able to save yourselves, but do not play any longer, but open your hearts and let the Holy Spirit enter that will transform you and unite you in one heart with Jesus. My children, if you only knew how much I love you and how much joy I feel seeing you all together in prayer. My beloved ones, pray for the Church and for the consecrated, for they are in darkness, confusion and gloom, that they may be enlightened by God's love. Now I leave you with my motherly blessing,in the name of the Father and the Son and the Holy Spirit, Amen. Today, so many graces will descend upon you, witness them with humility. Your Mother!" , dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 3) & (dataset["day"] == 6)), "Dear children, thank you for responding to my call in your hearts. Beloved children, you ask, why does my Son weep tears of blood? Know that Jesus is sad, grieved for this humanity that is called to salvation, but does not respond to His call. By now, my children, today is the end of the time of Mercy, call on the Lord to have mercy on you, I offer my tears for you. My children, someone will be saved thanks to the suffering offered by this daughter of mine. I ask you: pray, pray very much. My children, technology is about to be attacked by solar eruptions, so be ready. Soon evil will reveal itself before the world, but only those who are faithful to Christ will recognize good from evil, thanks to the infusion of the Holy Spirit. My children, the times that will come will be hard, very hard. As a Mother I ask you to hasten your conversion, do not be lukewarm, only God will be your salvation, entrust your life to Him, everything will be renewed and much will be lost, but I want to save these children of mine. The earth will continue to tremble without ceasing. Now I leave you with My Motherly Blessing in the name of the Father and the Son and the Holy Spirit, Amen." , dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 3) & (dataset["day"] == 9)), "Dear children, your prayers dry my tears. My children, the pain offered must bring joy. My children, not everything will be as you expect, the earth you know will no longer exist, you will be transformed into light and taken to a safe place, do not be afraid because everything will be painless for these moments. I only ask you to pray for your transformation. My children, the new earth will be full of joy and peace and there will be no sickness, everything is ready for your arrival. My children, what you will soon see, you will not be able to bear if you are not in faith and prayer, be careful because the devil will do everything to discourage you, so much so that even those who say they have faith could be caught in his web. My children, bring many souls to Jesus, that they may know Him and be faithful to Him always. My children, many have adhered to the evil, blasphemies and corruptions of the world, but they have not yet understood that their yes must be only for God. My children, please open your eyes and look around, do you not understand where you have arrived? Spiritual warfare is going on, watch over your children, pray for your rulers, so that the light may enter their hearts. Now I leave you with My Motherly Blessing in the name of the Father and the Son and the Holy Spirit, Amen." , dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 3) & (dataset["day"] == 13)), "My children, thank you for having responded to my call in your hearts. Beloved children, in these years of apparitions, not everything has been taken seriously, but now realize that what I am telling you is not slow in coming, and therefore I ask once again for an urgency to convert, be in grace, do not be afraid and be in the joy of the Lord who will soon come. My children, unfortunately many of my children have adapted to the imposition to which they are subjected, I beg you children, do not fear, for I am and will be with you every time you need help and when confusion takes hold of your soul, chase it away with prayer and look at the face of my Son, so that you may have serenity. My children, be disciples, fight for the truth, do not be subject to the devil who with his wiles involves you in lies, the times will be turbulent both for the Church and for politics, make circles of prayer. Now I leave you with my blessing in the name of the Father and the Son and the Holy Spirit, Amen." , dataset["text_en"])






dataset["text_pl"] = np.where(((dataset["month"] == 3) & (dataset["day"] == 3)), "Drogie dzieci, dziękuję wam, że odpowiedzieliście na moje wezwanie w waszych sercach. Umiłowane dzieci, Ja, wasza Matka, proszę was: trzymajcie mnie za rękę i słuchajcie tego, co przychodzi do was z Nieba, bo wszystko jest dla waszego zbawienia. Wykorzystajcie ten czas miłosierdzia, ponieważ wkrótce sprawiedliwość i gniew Boży dadzą o sobie znać; czas, który pozostał do dyspozycji, jest już bardzo krótki, podobnie jak czas, w którym pozostanę z wami. Umiłowani moi, nie bójcie się czasów, które nadejdą lub już nadeszły, bo modlitwą i nawróceniem będziecie mogli się uratować, ale nie udawajcie już więcej, ale otwórzcie wasze serca i pozwólcie wejść Duchowi Świętemu, a On was przemieni i zjednoczy w jednym sercu z Jezusem. Moje dzieci, gdybyście tylko wiedzieli, jak bardzo was kocham i jak wielką radość odczuwam, gdy widzę was wszystkich razem na modlitwie. Umiłowani moi, módlcie się za Kościół i za osoby konsekrowane, bo są pogrążone w ciemnościach, zamęcie i mroku, aby oświeciła je miłość Boża. Teraz zostawiam was z moim matczynym błogosławieństwem, w imię Ojca i Syna i Ducha Świętego, Amen. Dziś zstąpi na was wiele łask, bądźcie ich świadkami z pokorą. Wasza Matka!" , dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 3) & (dataset["day"] == 6)), "Drogie dzieci, dziękuję wam, że odpowiedzieliście na moje wezwanie w waszych sercach. Umiłowane dzieci, pytacie się, dlaczego mój Syn płacze krwawymi łzami? Wiedzcie, że Jezus jest smutny, zasmucony z powodu tej ludzkości, która jest powołana do zbawienia, ale nie odpowiada na Jego wezwanie. Już teraz, moje dzieci, dziś skończył się czas Miłosierdzia, wzywajcie Pana, aby się nad wami zmiłował, ja ofiaruję za was moje łzy. Moje dzieci, ktoś zostanie uratowany dzięki cierpieniu ofiarowanemu przez tę moją córkę. Proszę was: módlcie się, módlcie się bardzo mocno. Moje dzieci, technologia zostanie wkrótce zaatakowana przez erupcje słoneczne, więc bądźcie gotowi. Wkrótce zło ujawni się przed światem, ale tylko ci, którzy są wierni Chrystusowi, będą odróżniać dobro od zła, dzięki wylaniu Ducha Świętego. Moje dzieci, czasy, które nadejdą, będą ciężkie, bardzo ciężkie. Jako matka proszę was: przyspieszcie swoje nawrócenie, nie bądźcie letni, tylko Bóg będzie waszym zbawieniem, powierzcie Mu swoje życie, wszystko zostanie odnowione i wiele stracicie, ale ja chcę ocalić te moje dzieci. Ziemia będzie nadal drżeć bez ustanku. Teraz zostawiam was z moim matczynym błogosławieństwem w imię Ojca i Syna i Ducha Świętego, Amen." , dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 3) & (dataset["day"] == 9)), "Drogie dzieci, wasze modlitwy osuszają moje łzy. Moje dzieci, ofiarowany ból musi przynieść radość. Moje dzieci, nie wszystko będzie tak, jak się spodziewacie, ziemia, którą znacie, nie będzie już istnieć, zostaniecie przemienieni w światło i zabrani w bezpieczne miejsce, nie bójcie się, ponieważ w tych chwilach wszystko będzie bezbolesne. Proszę was tylko o modlitwę w intencji waszej przemiany. Dzieci moje, nowa ziemia będzie pełna radości i pokoju i nie będzie na niej chorób, wszystko jest gotowe na wasze przyjście. Dzieci moje, tego, co wkrótce zobaczycie, nie będziecie mogli znieść, jeśli nie jesteście w wierze i modlitwie, uważajcie, bo diabeł zrobi wszystko, aby was zniechęcić, tak bardzo, że nawet ci, którzy mówią, że mają wiarę, mogą zostać uwięzieni w jego sieci. Dzieci moje, przyprowadźcie wiele dusz do Jezusa, aby Go poznały i były Mu zawsze wierne. Dzieci moje, wielu przylgnęło do zła, bluźnierstw i zepsucia świata, ale nie zrozumieli jeszcze, że ich 'tak' musi być tylko dla Boga. Dzieci moje, błagam was, otwórzcie oczy i rozejrzyjcie się wokół siebie, czy nie rozumiecie, dokąd doszliście? Walka duchowa toczy się, czuwajcie nad swoimi dziećmi, módlcie się za swoich władców, aby światło mogło wejść do ich serc.  Teraz zostawiam was z moim matczynym błogosławieństwem w imię Ojca i Syna i Ducha Świętego, Amen." , dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 3) & (dataset["day"] == 13)), "Moje dzieci, dziękuję wam, że odpowiedzieliście na moje wezwanie w waszych sercach. Umiłowane dzieci, w tych latach objawień nie wszystko było brane na serio, ale teraz uświadomcie sobie, że to, co wam mówię, nie przychodzi powoli i dlatego jeszcze raz proszę o pilne nawrócenie, bądźcie w łasce, nie bójcie się i bądźcie w radości Pana, który wkrótce przyjdzie. Moje dzieci, niestety wiele moich dzieci dostosowało się do narzuconego reżimu, któremu są poddawane, błagam was dzieci, nie lękajcie się, bo jestem i będę z wami za każdym razem, gdy będziecie potrzebować pomocy, a gdy zamęt ogarnie waszą duszę, odganiajcie go modlitwą i wpatrujcie się w oblicze mojego Syna, abyście mieli spokój. Dzieci moje, bądźcie uczniami, walczcie o prawdę, nie ulegajcie diabłu, który swoimi podstępami wciąga was w kłamstwo, czasy będą burzliwe zarówno dla Kościoła jak i dla polityki, twórzcie koła modlitewne. A teraz zostawiam was z moim błogosławieństwem w imię Ojca i Syna i Ducha Świętego, Amen." , dataset["text_pl"])



translator = google_translator()  

dataset["text_es"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='es'))
dataset["text_fr"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='fr'))
dataset["text_zh"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='zh'))
dataset["text_de"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='de'))
dataset["text_pt"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='pt'))







dataset.to_csv("march_2021.csv", encoding="utf-8", index=False)





