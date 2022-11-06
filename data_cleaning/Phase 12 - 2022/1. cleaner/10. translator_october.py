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




dataset = pd.read_csv("october_cleaned.csv", encoding="utf-8")




# ITALIAN

dataset["text_it"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 3)), "Cari figli miei, grazie per essere qui nella preghiera e per aver piegato le vostre ginocchia. Figli benedetti, la vostra umile preghiera conforta me e il mio Gesù. Figli miei, non temete per ciò che arriverà perché Io ho già steso il Mio Manto qui, oggi e su tutti coloro che hanno la vera fede. Figli, cibatevi del corpo e del sangue di mio Figlio Gesù, Lui lo ha lasciato per voi, non nel ricordo, ma nella sua presenza vera e viva. Figli, fate in modo che il modernismo della Chiesa non vi contamini, siate fedeli al vero magistero della Fede. Gesù vi guarda e vi manda lo Spirito di discernimento su ciò che è giusto, che è di Dio e su ciò che apre le porte per arrivare nell’abisso di Satana. Figli miei, Io sono con voi e non vi abbandonerò mai. Percorrete la via della santità. Ora vi benedico nel nome del Padre, del Figlio e dello Spirito Santo. Poi la Madonna ha aggiunto che scenderanno tante grazie su coloro che pregheranno la coroncina al preziosissimo sangue di Gesù.", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 7)), "Cari figli Benedetti, grazie per essere qui e per aver piegato le ginocchia nella preghiera. Figli miei, Io sono la Regina del Rosario, del cielo e della terra e vi chiedo di intensificare la recita dei rosari e pregate insieme ai bambini, proteggetevi dal male che attanaglia il mondo. Figli, pregate per la Corea, pregate per i governanti che stanno prendendo decisioni sbagliate, pregate per i santi sacerdoti massacrati dagli attacchi. Figli miei, vi chiedo di Consacrarvi al mio Cuore Immacolato, per la vostra protezione. Ora vi benedico nel nome del Padre, del Figlio e dello Spirito Santo, amen.", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 11)), "Figli miei. grazie per aver risposto alla mia chiamata nel vostro cuore e per aver piegato le ginocchia nella preghiera. Figli miei, quanto soffre il mio cuore per l’umanità che si trova in bilico. Figli, voi che siete i risvegliati, risvegliate le coscienze dei vostri fratelli e pregate per le vostre anime. L’umanità ha cambiato l’amore con l’odio, la preghiera con la bestemmia, il dono che ha lasciato Dio per voi ( l’Eucarestia), ormai è qualcosa senza significato. Figli, questo è il tempo di grazia e tanti saranno i miracoli che accadranno, pregate affinché Dio abbia misericordia. Le grandi potenze si stanno attaccando tra loro a causa della vicinanza di tanti demoni, che li stanno guidando alla grande guerra. L’Italia patirà la fame, ma voi, figli miei, siate uniti sempre nel nome del Signore e fidatevi solo di Lui, perché solo in Lui sarà la vittoria. Fate cenacoli di preghiera anche nelle famiglie, consacratevi al mio Cuore Immacolato ed Io vi proteggerò. Figli, siete attratti da false luci e da grandi invenzioni, ma quando tutto crollerà, la delusione sarà enorme, aprite il cuore e pregate. Ora vi benedico, nel nome del Padre, del Figlio e dello Spirito Santo,amen.", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 16)), "Cari figli, grazie per essere qui nella preghiera e per aver risposto alla mia chiamata nel vostro cuore. Figli miei, grazie per avermi permesso di stare qui con voi, per elargire tante benedizioni.  Pregate in questo luogo Benedetto insieme a questo mio figlio prediletto, innamorato di Gesù come il figlio di un padre (la Madonna si riferiva a Padre Giulio Maria Scozzaro). Figli, le strade saranno tortuose per arrivare a Gesù, ma avrete le benedizioni e la forza necessaria per sostenervi. Vi prego figli, siate fedeli alla Parola e al Vangelo. Ora vi benedico, nel Nome della Santissima Trinità: Padre e Figlio e Spirito Santo. La Madonna ha aggiunto che l’ultimo libro di Padre Giulio (Qual è la vera Chiesa di Cristo?) farà tremare i polsi ai cosiddetti figli di Dio. Ha anche detto: saranno tante le Grazie che scenderanno oggi. Durante la Messa, dopo la Consacrazione, mentre era tenuta elevata l’Eucaristia, Gisella ha visto San Pio da Pietrelcina all’altare, accanto e alla sinistra di Padre Giulio Scozzaro che celebrava la Messa e San Pio ha detto a Gisella: Sto preparando questo mio figlio alla Santità.", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 18)), "Cara figlia, grazie per avermi accolta nel tuo cuore. Devi dire al mondo di prepararsi spiritualmente dagli attacchi del demonio, l’umanità piangerà e striderà i denti. Chiedo di fare riparazione per tutte le offese al mio diletto Figlio. Parlo attraverso quest’anima prediletta, vi mostro i segni della mia presenza eppure molti figli sono sordi alla mia chiamata. L’umanità non capisce ancora che le offese, le blasfemie, i sacrilegi compiuti anche dai miei figli prediletti (Sacerdoti) sarà la loro condanna eterna. Vivono delle cose materiali senza osservare tutte le cose del cielo. Figli, siate umili, piegate sempre le vostre ginocchia nella preghiera, vivete i Comandamenti e cibatevi del Corpo e del Sangue del Redentore. Ora vi benedico nel Nome del Padre e del Figlio e dello Spirito Santo. Amen.", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 23)), "Figli miei, oggi, tante saranno le grazie che scenderanno e tanti raggi luminosi entreranno nelle vostre vite. Io stessa, durante l’Eucarestia, passerò tra voi per benedirvi uno alla volta,nel nome del Padre, del Figlio e dello Spirito Santo, amen.", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 25)), "Cari figli, grazie per essere qui nella preghiera e per aver piegato le vostre ginocchia.  Figli miei, guardate intorno a voi questo mondo malato. Molti pensano che questo tempo sia la fine, ma molto peggio arriverà, non immaginate quanto il demonio possa essere crudele. Molti di voi dicono di conoscere mio Figlio Gesù, con la bocca, ma non con il cuore. Figlia mia, scelta e prediletta da Dio, riceverai presto dal mio Giglio, il manto della gloria e la spada della giustizia, affinché tutto sia per la gloria di Dio. Gesù è con te. Figli, siate sempre pronti per la guerra spirituale che sarà faticosa, ma i miei angeli combatteranno per voi. Figli vi benedico e la pace sia con voi, amen.", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 29)), "Figli miei, grazie per aver risposto alla mia chiamata nel vostro cuore. Figli miei, ormai siete immersi nella più grande guerra spirituale di tutti i tempi, i confusi saranno trascinati via come il vento, avvicinatevi alla vera fede e all’Eucarestia, siate umili e pregate affinché la giustizia di Dio sia mitigata , fate penitenza. Figli , satana ha armato il suo esercito, ma i miei guerrieri di luce vinceranno sempre e saranno protetti, perché hanno scelto di stare sotto il mio Manto Benedetto. Figli prediletti, Dio è con voi , guardate la luce e la croce e siate fedeli a mio Figlio Gesù. Figli vi seguirò e vi istruirò passo passo. Ora vi benedico nel nome del Padre, del Figlio e dello Spirito Santo, amen.  ", dataset["text_it"])

# ENGLISH
dataset["text_en"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 3)), "My dear children, thank you for being here in prayer and for kneeling down. Blessed children, your humble prayer comforts Me and My Jesus. My children, do not fear for what is to come for I have already spread My Mantle here today and over all who have the true faith. My children, feed yourselves on the body and blood of My Son Jesus, He left it for you, not in remembrance, but in His true and living presence. Children, see to it that the modernism of the Church does not defile you; be faithful to the true Magisterium of the Faith. Jesus is watching you and sending you the Spirit of discernment about what is right, what is of God and what opens the doors to reach into the abyss of Satan. My children, I am with you and will never abandon you. Walk the path of holiness. Now I bless you in the name of the Father and the Son and the Holy Spirit. Then Our Lady added that many graces will descend on those who pray the chaplet to the Most Precious Blood of Jesus.", dataset["text_pl"])
dataset["text_en"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 7)), "Dear blessed children, thank you for being here and for kneeling in prayer. My children, I am the Queen of the Rosary, of heaven and earth and I ask you to intensify the recitation of rosaries and pray together with the children, protect yourselves from the evil that grips the world. My children, pray for Korea, pray for the rulers who are making wrong decisions, pray for the holy priests massacred by attacks. My children, I ask you to Consecrate yourselves to my Immaculate Heart, for your protection. Now I bless you in the name of the Father and the Son and the Holy Spirit, Amen.", dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 11)), "My children. thank you for answering my call in your hearts and for kneeling in prayer. My children, how much my heart aches for humanity that is in the balance. My children, you who are the awakened ones, awaken the consciences of your brothers and pray for your souls. Humanity has changed love to hate, prayer to blasphemy, the gift that God left for you (the Eucharist) is now something without meaning. Children, this is the time of grace and many will be the miracles that will happen, pray for God to have mercy. The great powers are attacking each other because of the proximity of so many demons, who are leading them to the great war. Italy will go hungry, but you, my children, be united always in the name of the Lord and trust only in Him, for only in Him will be the victory. Make cenacles of prayer also in your families, consecrate yourselves to my Immaculate Heart and I will protect you. My children, you are attracted by false lights and great inventions, but when everything collapses, the disappointment will be enormous, open your hearts and pray. Now I bless you in the name of the Father and the Son and the Holy Spirit, Amen.", dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 16)), "Dear children, thank you for being here in prayer and for answering my call in your hearts. My children, thank you for allowing me to be here with you, to bestow so many blessings. Pray in this blessed place together with this beloved son of mine who is in love with Jesus like a father's son (Our Lady was referring to Father Giulio Maria Scozzaro). Children, the roads will be winding to get to Jesus, but you will have the blessings and strength to sustain you. Please children, be faithful to the Word and the Gospel. I bless you now, in the Name of the Most Holy Trinity: Father and Son and Holy Spirit. Our Lady added that Father Giulio' latest book (What is the True Church of Christ?) will make the so-called children of God shake in their boots. She also said, there will be many Graces descending today. During Mass, after the Consecration, while the Eucharist was being held high, Gisella saw St. Pio of Pietrelcina at the altar, next to and to the left of Father Giulio Scozzaro who was celebrating Mass, and St. Pio said to Gisella: I am preparing this son of mine for Holiness.", dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 18)), "Dear daughter, thank you for welcoming me into your heart. You must tell the world to prepare itself spiritually from the devil's attacks; humanity will weep and gnash its teeth. I ask to make reparation for all offenses against my beloved Son. I speak through this beloved soul, I show you the signs of my presence and yet many children are deaf to my call. Humanity still does not understand that the offenses, blasphemies, sacrileges done even by my beloved children (Priests) will be their eternal condemnation. They live on material things without observing all the things of Heaven. My children, be humble, always bend your knees in prayer, live the Commandments and feed on the Body and Blood of the Redeemer. Now I bless you in the Name of the Father and the Son and the Holy Spirit, Amen.", dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 23)), "My children, today, so many graces will descend and so many rays of light will enter your lives. I myself, during the Eucharist, will pass among you to bless you one by one,in the name of the Father and the Son and the Holy Spirit, Amen.", dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 25)), "Dear children, thank you for being here in prayer and for kneeling down.  My children, look around you at this sick world. Many think this time is the end, but much worse will come, you cannot imagine how cruel the devil can be. Many of you say you know my Son Jesus, with your mouth, but not with your heart. My daughter, chosen and beloved of God, you will soon receive from my Lily, the Mantle of Glory and the Sword of Righteousness, so that everything may be for the glory of God. Jesus is with you. Children, always be ready for the spiritual warfare that will be tiring, but my angels will fight for you. Children, I bless you and peace be with you, Amen.", dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 29)), "My children, thank you for responding to my call in your hearts. My children, you are now immersed in the greatest spiritual warfare of all time, the confused will be swept away like the wind, come closer to the true faith and the Eucharist, be humble and pray for God's justice to be mitigated, do penance. Children, Satan has raised his army, but my warriors of light will always win and be protected, for they have chosen to be under my Blessed Mantle. Beloved children, God is with you, behold the light and the cross and be faithful to my Son Jesus. Children I will follow you and instruct you step by step. Now I bless you in the name of the Father and the Son and the Holy Spirit, Amen. ", dataset["text_en"])

# POLISH

dataset["text_pl"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 3)), "Moje drogie dzieci, dziękuję wam, że jesteście tutaj na modlitwie i że uklęknęliście. Błogosławione dzieci, wasza pokorna modlitwa pociesza mnie i mojego Jezusa. Moje dzieci, nie lękajcie się o to, co ma nadejść, ponieważ Ja już rozpostarłam Mój Płaszcz teraz, tutaj i nad wszystkimi, którzy mają prawdziwą wiarę. Moje dzieci, karmcie się Ciałem i Krwią mojego Syna Jezusa, On zostawił je dla was nie na pamiątkę, ale dla swojej prawdziwej i żywej obecności. Moje dzieci, dopilnujcie, aby modernizm Kościoła nie splugawił was, bądźcie wierni prawdziwemu Magisterium Wiary. Jezus obserwuje cię i posyła ci Ducha rozeznania tego, co jest właściwe, co jest z Boga, a tego, co otwiera drzwi do otchłani szatana. Moje dzieci, jestem z wami i nigdy was nie opuszczę. Idźcie drogą świętości. Teraz błogosławię was w imię Ojca i Syna i Ducha Świętego. Następnie Matka Boża dodała, że na tych, którzy odmawiają koronkę do Najdroższej Krwi Pana Jezusa, zstąpi wiele łask.", dataset["text_en"])
dataset["text_pl"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 7)), "Drogie błogosławione dzieci, dziękuję wam, że jesteście tutaj i że uklęknęliście do modlitwy. Moje dzieci, jestem Królową Różańca, nieba i ziemi, i proszę was, abyście zintensyfikowali odmawianie różańców i modląc się razem z dziećmi, chronili się przed złem, które ogarnia świat. Moje dzieci, módlcie się za Koreę, módlcie się za rządzących, którzy podejmują złe decyzje, módlcie się za świętych kapłanów zmasakrowanych atakami. Moje dzieci, proszę was, abyście poświęcili się mojemu Niepokalanemu Sercu, dla waszej ochrony. Teraz błogosławię was w imię Ojca i Syna i Ducha Świętego, Amen.", dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 11)), "Moje dzieci, dziękuję wam, że odpowiadacie na moje wezwanie w waszych sercach i że uklęknęliście do modlitwy. Moje dzieci, jak bardzo moje serce boli z powodu ludzkości, która jest w zawieszeniu. Moje dzieci, wy, którzy jesteście przebudzeni, obudźcie sumienia waszych braci i módlcie się za wasze dusze. Ludzkość zamieniła miłość na nienawiść, modlitwę na bluźnierstwo, dar, który Bóg zostawił dla ciebie (Eucharystia), jest teraz czymś bez znaczenia. Moje dzieci, to jest czas łaski i wiele cudów się wydarzy, módlcie się, aby Bóg się zmiłował. Wielkie mocarstwa atakują się wzajemnie z powodu bliskości tak wielu demonów, które prowadzą je do wielkiej wojny. Włochy będą głodne, ale wy, moje dzieci, bądźcie zawsze zjednoczeni w imię Pana i ufajcie tylko Jemu, bo tylko w Nim będzie zwycięstwo. Twórzcie kręgi modlitewne także w waszych rodzinach, poświęćcie się mojemu Niepokalanemu Sercu, a Ja będę was chronić. Moje dzieci, przyciągają was fałszywe światła i wielkie wynalazki, ale kiedy wszystko się zawali, rozczarowanie będzie ogromne, otwórzcie swoje serca i módlcie się. A teraz błogosławię was w imię Ojca i Syna i Ducha Świętego, Amen.", dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 16)), "Drogie dzieci, dziękuję wam, że jesteście tutaj na modlitwie i że odpowiadacie na moje wezwanie w waszych sercach. Moje dzieci, dziękuję wam, że pozwalacie mi być tutaj z wami, obdarzać was tak wieloma błogosławieństwami. Módl się w tym błogosławionym miejscu razem z moim ukochanym synem, który jest zakochany w Jezusie jak syn ojca (Matka Boża miała na myśli ojca Giulio Maria Scozzaro). Moje dzieci, drogi będą kręte, aby dotrzeć do Jezusa, ale będziecie mieli błogosławieństwa i siłę, która was podtrzyma. Proszę, moje dzieci, bądźcie wierne Słowu i Ewangelii. Teraz błogosławię was, w Imię Trójcy Przenajświętszej: Ojca i Syna i Ducha Świętego. Matka Boża dodała, że najnowsza książka ojca Giulio (Czym jest Prawdziwy Kościół Chrystusa?) sprawi, że tak zwane dzieci Boże będą drżeć. Powiedziała też: będzie dziś wiele Łask zstępujących. Podczas Mszy Świętej, po Konsekracji, gdy Eucharystia była trzymana wysoko, Gisella zobaczyła św. Pio z Pietrelciny przy ołtarzu, obok i na lewo od księdza Giulio Scozzaro, który odprawiał Mszę Świętą, a św. Pio powiedział do Giselli: Przygotowuję tego mojego syna do świętości.", dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 18)), "Drogie dziecko, dziękuję ci za przyjęcie mnie do swojego serca. Musisz powiedzieć światu, aby przygotował się duchowo na ataki diabła; ludzkość będzie płakać i zgrzytać zębami. Proszę o zadośćuczynienie za wszystkie przewinienia wobec mojego ukochanego Syna. Przemawiam przez tę ukochaną duszę, ukazuję wam znaki mojej obecności, a jednak wiele dzieci jest głuchych na moje wezwanie. Ludzkość wciąż nie rozumie, że wykroczenia, bluźnierstwa, świętokradztwa popełniane nawet przez Moje umiłowane dzieci (kapłanów) będą ich wiecznym potępieniem. Żyją sprawami materialnymi, nie dostrzegając spraw niebieskich. Dzieci moje, bądźcie pokorne, zawsze klękajcie do modlitwy, żyjcie przykazaniami i karmcie się Ciałem i Krwią Odkupiciela. Teraz błogosławię was w Imię Ojca i Syna i Ducha Świętego, Amen.", dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 23)), "Moje dzieci, dziś zstąpi wiele łask i wiele promieni światła wejdzie w wasze życie. Ja sama, podczas Eucharystii, przejdę między wami, aby was kolejno pobłogosławić, w imię Ojca i Syna i Ducha Świętego, Amen.", dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 25)), "Drogie dzieci, dziękuję wam, że jesteście tutaj na modlitwie i że klęczycie. Moje dzieci, spójrzcie na ten chory świat wokół siebie. Wielu myśli, że ten czas jest końcem, ale przyjdzie jeszcze wiele zła, nie wyobrażacie sobie, jak okrutny potrafi być diabeł. Wielu z was mówi, że zna mojego Syna Jezusa, ale nie zna Go swoim sercem. Moja córko, wybrana i umiłowana przez Boga, wkrótce otrzymasz od mojej Lilię, Płaszcz Chwały i Miecz Sprawiedliwości, aby wszystko było na chwałę Boga. Jezus jest z tobą. Dzieci, bądźcie zawsze gotowi na walkę duchową, która będzie męcząca, jednak moi aniołowie będą walczyć za was. Dzieci, błogosławię was i pokój niech będzie z wami, Amen.", dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 10) & (dataset["day"] == 29)), "Moje dzieci, dziękuję wam, że odpowiadacie na moje wezwanie w waszych sercach. Moje dzieci, jesteście teraz zanurzeni w największej wojnie duchowej wszech czasów, zdezorientowani zostaną rozwiani jak wiatr, zbliżcie się do prawdziwej wiary i do Eucharystii, bądźcie pokorni i módlcie się, aby sprawiedliwość Boża została złagodzona, czyńcie pokutę. Moje dzieci, szatan uzbroił swoją armię, ale moi wojownicy światła zawsze będą zwyciężać i będą chronieni, ponieważ wybrali bycie pod moim błogosławionym płaszczem. Umiłowane dzieci, Bóg jest z wami, patrzcie na światło i krzyż i bądźcie wierni mojemu Synowi Jezusowi. Moje dzieci, będę za wami szła i pouczała was z każdym krokiem. Teraz błogosławię was w imię Ojca i Syna i Ducha Świętego, Amen.  ", dataset["text_pl"])

dataset = dataset[['year', 'month', 'day', 'author', 'text_it', 'month_string', 'text_pl','text_en']]

dataset_ready = pd.read_csv("october_2022.csv")


dataset = dataset.merge(dataset_ready, how="left", on=['year', 'month', 'day', 'author', 'text_it', 'month_string', 'text_pl','text_en'])

dataset_ok = dataset[~dataset["text_pt"].isnull()]
dataset_translate = dataset[dataset["text_pt"].isnull()]



dataset_translate["text_es"] = dataset_translate["text_it"].apply(lambda x: gs.translate(x,'es'))
dataset_translate["text_fr"] = dataset_translate["text_en"].apply(lambda x: gs.translate(x,'fr'))
dataset_translate["text_zh"] = dataset_translate["text_en"].apply(lambda x: gs.translate(x,'zh'))
dataset_translate["text_de"] = dataset_translate["text_en"].apply(lambda x: gs.translate(x,'de'))
dataset_translate["text_pt"] = dataset_translate["text_en"].apply(lambda x: gs.translate(x,'pt'))


dataset = pd.concat([dataset_ok, dataset_translate])

dataset = dataset.sort_values(by="day")


dataset.to_csv("october_2022.csv", encoding="utf-8", index=False)


# # First Translation
# dataset_translate = dataset
# dataset_translate.to_csv("october_2022.csv", encoding="utf-8", index=False)





