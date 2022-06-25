# -*- coding: utf-8 -*-
"""
Created on Fri Jan 1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np
from google_trans_new import google_translator

#dataset["text_it"] = np.where(((dataset["month"] == 9) & (dataset["day"] == 3)), "", dataset["text_it"])



dataset = pd.read_csv("december_cleaned.csv", encoding="utf-8")

dataset["text_pl"] = ""
dataset["text_en"] = ""
dataset["text_it"] = ""
dataset["month_string"] = "December"





# ITALIAN
dataset["text_it"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 3)), "Cari figli, grazie per aver risposto alla mia chiamata nel vostro cuore. Figli, piccoli miei piegate le ginocchia nella preghiera e sentite lo spirito di sacrificio. Figli miei, vedo il vostro cuore e so che non siete pronti per ciò che sta per accadere, ma quanti figli miei messaggeri, vi hanno avvertito, eppure siete ancora sordi al mio materno richiamo, guardate tutti i segni che sono attorno a voi, eppure non volete vedere perché avete paura di decidere, mentre il demonio vi punge con il suo veleno. Siete cambiati nelle vostre abitudini, nella vostra vita, nella vostra famiglia e tutto va verso il baratro, vi prego tornate a Dio, vostra unica salvezza, non avete ancora appreso che non c’è pace, verità e amore senza il mio dolce Gesù? Preparatevi all’incontro con Lui e risorgerete a vita nuova. Ora vi benedico nel nome del Padre, del Figlio e dello Spirito Santo. Abbiate il coraggio di testimoniare la vostra fede. Tante saranno le grazie che oggi scenderanno su di voi.", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 7)), "Figli miei, grazie per aver risposto alla mia chiamata nel vostro cuore. Figli, vi chiedo di non seguire le false luci del mondo, non è così che uscirete dalle tenebre, ma con il massimo affidamento a Dio, Lui vi proteggerà, non abbiate paura. Preparate i vostri rifugi, soprattutto nelle vostre case. Pregate per la chiesa, che verrà distrutta per poi rinascere, Gesù è vicino a voi.  Credete alle parole di una Madre, tutto sarà meraviglioso e questa sarà la rinascita per voi e per il mondo. Pregate molto, continuate ad essere luce, affinché i miei angeli possano riconoscervi. Io passerò accanto a voi per benedirvi uno per uno e per far scendere la pace nei vostri cuori, non siate confusi, ma apritevi all’amore di Dio e nulla vi mancherà. Ora vi benedico nel nome del Padre, del Figlio e dello Spirito Santo. Amen. Messaggio per la Polonia: 'Cari figli, tenetevi per mano l’un l’altro, anche quando tutto vi sarà diventato impossibile, fidatevi di Dio, che non vi abbandonerà. Usate l’astuzia del serpente e la purezza della colomba nulla vi mancherà'.", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 8)), "Figli miei, grazie per aver piegato le vostre ginocchia. Oggi sono qui con voi e mi rivolgo ai convertiti e non, a coloro che credono alle mie apparizioni e non, ai credenti e non credenti, prego affinché durante l’avvertimento possiate rispondere all’ultimo atto di misericordia. Figli miei preparatevi, perché non passerà molto tempo e desidero che voi possiate inginocchiarvi in quel giorno per chiedere perdono e riconoscere il Salvatore del mondo. Ricordate che la sua morte è servita per la vostra salvezza e tornerà ancora per salvarvi e liberarvi dalle catene del maligno. Sarò con voi fino alla fine della preghiera. Vi lascio con la mia benedizione Materna, nel nome del Padre, del Figlio e dello Spirito Santo, Amen.", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 13)), "La statua che rappresenta il Sacro Cuore di Gesù ha iniziato a trasudare olio profumato già nella mattinata del 13 dicembre e ha continuato nelle ore successive. Molte persone sono giunte nella nostra casa per la preghiera del Santo Rosario, poi Gesù ha lasciato il suo messaggio a Gisella. Messaggio di Gesù: 'Figli e fratelli miei, Io vi guardo mentre piegate le vostre ginocchia nella preghiera e  mi riempite di felicità. Pregate per il mio cuore sofferente, aiutatemi!! Figli, questa grazia vi attira me, ma se sapeste quanto è vicino il tempo per riabbracciarvi!! Prendete un po’ di quest’olio benedetto e portatelo nelle vostre case per i momenti bui. Ora fratelli miei, uno per volta avvicinatevi a me e Io vi benedirò, che la pace sia con voi. Chiedo molti cenacoli in questa casa benedetta dove Io sono'.", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 21)), "Cari figli, grazie per essere qui nella preghiera e per aver risposto alla mia chiamata nel vostro cuore. Figli miei, ma quante sono le domande che vi ponete!! Dovete offrire, offrite tutto, Io vi proteggerò dal male peggiore. Voi figli miei, vi compiacete   quando vi chiedo di essere angeli di luce sulla terra, ma tutto ciò che nasce di bello ha necessità della purificazione, non fatevi troppe domande, il mio Gesù ha dato tanta grazia ed era tutta per voi. Io sono con voi, approfittate di questi momenti per riflettere in particolare sull’umiltà, ancora per qualcuno la strada è lunga e faticosa, state vicini tra voi fratelli e aiutatevi. Pregate per la pace nel mondo,  pregate tanto. Ora vi benedico nel nome del Padre del Figlio dello Spirito Santo, Amen", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 28)), "Cari figli, grazie per aver risposto alla mia chiamata nel vostro cuore e per aver piegato le ginocchia nella preghiera. Figli miei, piccoli miei, non tutti siete così pronti alle prove che arrivano nelle vostre vite, perdete la testa e vi fate condurre dal demonio senza riflettere, non capite ancora che sarete forgiati come il ferro, finché non sarete completamente sottomessi a Dio, che può tutto, anche quello che ai vostri occhi sembra impossibile, ma voi figli siete ostinati e spesso presuntuosi. Questo Natale, chi ha davvero pregato con il cuore per la nascita di Gesù? Eravate troppo presi dalle cose del mondo, non dalla preghiera, riflettete e vegliate perché il tempo è qui, crescete spiritualmente.  Io voglio salvarvi perché siete i miei figli, la vera fede si vede durante la tempesta, la strada per Dio è piena di inciampi, ma voi continuate a cercare le scorciatoie e le cose facili, e questa non è la strada giusta. Pregate con il cuore aperto e non con la paura e l’angoscia, offrite tutto a Gesù e fidatevi di Lui. Ora vi lascio con la mia benedizione materna nel nome del Padre, del Figlio e dello Spirito Santo, Amen.", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 29)), "Figli miei, grazie per aver risposto alla mia chiamata nel vostro cuore. Cari figli, questo è tempo della giustizia. Figli, quanto sarà bello il mondo rinnovato!!.. Quando tutto sarà finito, vedrete che i cieli e la terra avranno una luce meravigliosa, dove vigerà solo la pace e l’amore. Figli miei, questi sono i tempi dove il male si paleserà, vedrete con i vostri occhi, chi ha vissuto fingendo e chi ora ha scelto di farsi rapire dalle tenebre, vedrete la separazione tra il bene e il male, non abbiate paura, questo è il tempo di raccolta. Siate forti, perché le prove non sono finite e voi dovrete essere pronti a fronteggiare tutto questo e quando pensate che tutto sembrerà perduto, Io e il mio Gesù interverremo insieme con i miei angeli. Venite figli miei, abbeveratevi nella fonte dell’amore, Io sarò sempre con voi.  Ora vi benedico nel nome del Padre, del Figlio dello Spirito Santo, Amen.", dataset["text_it"])


# ENGLISH
dataset["text_en"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 3)), "Dear children, thank you for responding to my call in your hearts. My little children, bend your knees in prayer and feel the spirit of sacrifice. My children, I see your heart and I know that you are not ready for what is about to happen, but how many of my messenger children have warned you, yet you are still deaf to my motherly call, you look at all the signs that are around you, yet you do not want to see because you are afraid to decide, while the devil stings you with his poison. You have changed in your habits, in your life, in your family and everything is going towards the abyss, I beg you to return to God, your only salvation, have you not yet learned that there is no peace, truth and love without my sweet Jesus? Prepare yourselves for the encounter with Him and you will rise to new life. Now I bless you in the name of the Father and the Son and the Holy Spirit. Have the courage to witness your faith. Many will be the graces that will descend upon you today.", dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 7)), "My children, thank you for having responded to my call in your hearts. My children, I ask you not to follow the false lights of the world, this is not how you will come out of the darkness, but with the greatest trust in God, He will protect you, do not be afraid. Prepare your shelters, especially in your homes. Pray for the church, which will be destroyed and then be reborn, Jesus is near you.  Believe the words of a Mother, everything will be wonderful and this will be rebirth for you and for the world. Pray a lot, continue to be light, so that my angels may recognize you. I will pass by you to bless you one by one and to let peace descend in your hearts, do not be confused, but open yourselves to God's love and nothing will be lacking. Now I bless you in the name of the Father and the Son and the Holy Spirit, Amen. Message for Poland: 'Dear children, hold each other's hands, even when everything has become impossible for you, trust God, who will not abandon you. Use the cunning of the serpent and the purity of the dove and nothing will fail you'.", dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 8)), "My children, thank you for bending your knees. Today I am here with you and I am addressing converts and non-converts, those who believe in my apparitions and non-believers, I pray that during the warning you may respond to the last act of mercy. My children, prepare yourselves, for not much time will pass and I desire that you be able to kneel on that day to ask for forgiveness and recognize the Savior of the world. Remember that His death served for your salvation and He will come again to save you and free you from the chains of the evil one. I will be with you until the end of prayer. I leave you with my Motherly blessing, in the name of the Father and the Son and the Holy Spirit, Amen.", dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 13)), "The statue representing the Sacred Heart of Jesus began to exude fragrant oil as early as the morning of December 13 and continued in the following hours. Many people came to our house for the prayer of the Holy Rosary, then Jesus left his message to Gisella. Message from Jesus: 'My children and brothers, I am watching you as you bend your knees in prayer and fill me with happiness. Pray for my Suffering Heart, help me! My children, this grace draws you to me, but if you knew how close the time is to embrace you again! Take some of this blessed oil and bring it into your homes for the dark times. Now, My brothers, one by one, draw near to Me and I will bless you, may peace be with you. I ask for many cenacles in this blessed house where I am'.", dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 21)), "Dear children, thank you for being here in prayer and for responding to my call in your hearts. My children, how many questions are you asking yourselves! You must offer, offer everything, I will protect you from the worst evil. My children, you rejoice when I ask you to be angels of light on earth, but everything that is born beautiful needs purification, do not ask yourselves too many questions, my Jesus has given so much grace and it was all for you. I am with you, take advantage of these moments to reflect in particular on humility, still for some the road is long and tiring, stay close to each other brothers and help each other. Pray for peace in the world, pray a lot. Now I bless you in the name of the Father and the Son and the Holy Spirit, Amen.", dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 28)), "Dear children, thank you for answering my call in your hearts and for bending your knees in prayer. My children, my little ones, not all of you are so ready for the trials that come in your lives, you lose your minds and let the devil lead you without thinking, you do not yet understand that you will be forged like iron, until you are completely submitted to God, who can do everything, even what seems impossible in your eyes, but you children are stubborn and often conceited. This Christmas, who really prayed with the heart for the birth of Jesus? You were too caught up in the things of the world, not in prayer, reflect and watch because the time is here, grow spiritually.  I want to save you because you are my children, true faith is seen in the storm, the road to God is full of stumbling blocks, but you keep looking for shortcuts and easy things, and this is not the right way. Pray with an open heart and not with fear and anxiety, offer everything to Jesus and trust Him. Now I leave you with my motherly blessing in the name of the Father and the Son and the Holy Spirit, Amen.", dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 29)), "My children, thank you for responding to my call in your hearts. Dear children, this is a time of justice. My children, how beautiful will be the renewed world! When everything is over, you will see that the heavens and the earth will have a wonderful light, where only peace and love will prevail. My children, these are the times when evil will reveal itself, you will see with your own eyes, those who have lived pretending and those who have now chosen to be kidnapped by darkness, you will see the separation between good and evil, do not be afraid, this is the time of harvest. Be strong, for the trials are not over and you must be ready to face all this and when you think that all seems lost, I and my Jesus will intervene together with my angels. Come My children, drink from the fountain of love, I will always be with you. Now I bless you in the name of the Father and the Son and the Holy Spirit, Amen.", dataset["text_en"])




# POLISH
dataset["text_pl"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 3)), "Drogie dzieci, dziękuję wam, że odpowiedzieliście na moje wezwanie w waszych sercach. Moje małe dzieci, zegnijcie kolana w modlitwie i poczujcie ducha ofiary. Moje dzieci, widzę wasze serce i wiem, że nie jesteście gotowi na to, co ma się wydarzyć, lecz ileż to moich dzieci posłańców ostrzegało was, a wy wciąż jesteście głusi na moje matczyne wołanie, patrzycie na wszystkie znaki, które są wokół was, lecz nie chcecie widzieć, bo boicie się podjąć decyzję, podczas gdy diabeł kłuje was swoją trucizną. Zmieniliście się w swoich nawykach, w swoim życiu, w swojej rodzinie i wszystko zmierza ku przepaści, błagam was, abyście wrócili do Boga, waszego jedynego ratunku, czy jeszcze nie nauczyliście się, że nie ma pokoju, prawdy i miłości bez mojego słodkiego Jezusa? Przygotujcie się na spotkanie z Nim, a powstaniecie do nowego życia. Teraz błogosławię was w imię Ojca i Syna i Ducha Świętego. Miejcie odwagę dawać świadectwo swojej wiary. Wiele będzie łask, które dziś na was spłyną.", dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 7)), "Moje dzieci, dziękuję wam, że odpowiedzieliście na moje wezwanie w waszych sercach. Dzieci moje, proszę was, abyście nie szli za fałszywymi światłami świata, nie tak wyjdziecie z ciemności, ale z największą ufnością w Bogu, On was ochroni, nie bójcie się. Przygotujcie swoje schronienia, szczególnie w domach. Módlcie się za Kościół, który zostanie zniszczony, by potem się odrodzić, Jezus jest blisko was. Uwierzcie w słowa Matki, wszystko będzie cudowne i będzie to odrodzenie dla was i dla świata. Módlcie się mocno, bądźcie nadal światłem, aby moi aniołowie mogli was rozpoznać. Będę przechodził obok was, aby was wszystkich błogosławić i aby pokój zstąpił do waszych serc; nie bądźcie zdezorientowani, ale otwórzcie się na miłość Bożą, a niczego wam nie zabraknie. Teraz błogosławię was w imię Ojca i Syna i Ducha Świętego, Amen. Orędzie dla Polski: 'Drogie dzieci, trzymajcie się za ręce, nawet jeśli wszystko stało się dla was niemożliwe, zaufajcie Bogu, który was nie opuści. Użyj sprytu węża i czystości gołębicy, a niczego wam nie zabraknie'.", dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 8)), "Dzieci moje, dziękuję wam, że uklękneliście. Dziś jestem tu z wami i zwracam się do nawróconych i nienawróconych, wierzących w moje objawienia i niewierzących, modlę się, abyście w czasie ostrzeżenia odpowiedzieli na ostatni akt miłosierdzia. Dzieci moje, przygotujcie się, bo niewiele czasu upłynie, a ja pragnę, abyście w tym dniu mogli uklęknąć, aby prosić o przebaczenie i uznać Zbawiciela świata. Pamiętajcie, że Jego śmierć służyła waszemu zbawieniu i że on powróci ponownie, aby was zbawić i uwolnić z łańcuchów złego. Będę z wami aż do końca modlitwy. Zostawiam was z moim matczynym błogosławieństwem, w imię Ojca i Syna i Ducha Świętego, Amen.", dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 13)), "Rano 13 grudnia z figury przedstawiającej Najświętsze Serce Jezusa zaczął wydobywać się wonny olejek, który utrzymywał się przez kilka następnych godzin. Wiele osób przyszło do naszego domu na modlitwę różańcową, wtedy Jezus zostawił swoje przesłanie dla Giselli. Przesłanie Jezusa: 'Dzieci moje i bracia, patrzę na was, jak klękacie do modlitwy i napełniacie mnie szczęściem. Módlcie się za moje Cierpiące Serce, pomóżcie mi! Moje dzieci, ta łaska przyciąga was do mnie, ale gdybyście wiedzieli, jak blisko jest czas, aby was znowu objąć! Weźcie trochę tego błogosławionego oleju i przynieście go do waszych domów na mroczne czasy. A teraz, bracia moi zbliżcie się do mnie, a ja was pobłogosławię, niech pokój będzie z wami. Proszę o wiele kręgów modlitewnych w tym błogosławionym domu, w którym jestem'.", dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 21)), "Drogie dzieci, dziękuję wam, że jesteście tutaj na modlitwie i że odpowiedzieliście na moje wezwanie w waszych sercach. Dzieci moje, ileż to pytań zadajecie sobie! Musicie ofiarować, ofiarować wszystko, ochronię was przed najgorszym złem. Wy, moje dzieci, cieszycie się, kiedy proszę was, abyście byli aniołami światłości na ziemi, ale wszystko, co rodzi się piękne, potrzebuje oczyszczenia; nie zadawajcie sobie zbyt wielu pytań, mój Jezus dał tyle łask i to wszystko dla was. Jestem z wami, wykorzystajcie te chwile, aby zastanowić się szczególnie nad pokorą, jeszcze dla niektórych droga jest długa i męcząca, bądźcie blisko siebie bracia i pomagajcie sobie nawzajem. Módlcie się o pokój na świecie, módlcie się mocno. Teraz błogosławię was w imię Ojca i Syna i Ducha Świętego, Amen.", dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 28)), "Drogie dzieci, dziękuję wam, że odpowiedzieliście na moje wezwanie w waszych sercach i że uklękneliście do modlitwy. Moje dzieci, moje maleństwa, nie wszyscy z was są tak gotowi na próby, które przychodzą w waszym życiu, tracicie głowę i pozwalacie się prowadzić diabłu bez refleksji, nie rozumiecie jeszcze, że będziecie kutymi jak żelazo, aż do całkowitego poddania się Bogu, który może uczynić wszystko, nawet to, co wydaje się niemożliwe dla waszych oczu, ale wy, dzieci, jesteście uparci i często zarozumiali. W te święta, kto naprawdę modlił się z sercem o narodziny Jezusa? Byliście zbyt zajęci sprawami świata, a nie modlitwą; zastanawiajcie się i czuwajcie, bo czas jest tutaj, wzrastajcie duchowo. Chcę was uratować, bo jesteście moimi dziećmi, prawdziwa wiara jest widoczna w burzy, droga do Boga jest pełna potknięć, ale wy nadal szukacie skrótów i łatwych rzeczy, a to nie jest właściwa droga. Módlcie się z otwartym sercem, a nie z lękiem i udręką, ofiarujcie wszystko Jezusowi i zaufajcie Mu. Teraz, zostawiam was z moim matczynym błogosławieństwem, w imię Ojca i Syna i Ducha Świętego, Amen.", dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 12) & (dataset["day"] == 29)), "Moje dzieci, dziękuję wam, że odpowiedzieliście na moje wezwanie w waszych sercach. Drogie dzieci, to jest czas sprawiedliwości. Dzieci moje, jakże piękny będzie odnowiony świat! Kiedy wszystko się skończy, zobaczycie, że niebiosa i ziemia będą miały cudowne światło, gdzie panować będzie tylko pokój i miłość. Dzieci moje, to są czasy, kiedy zło się ujawni, zobaczycie na własne oczy tych, którzy żyli, udając i tych, którzy teraz wybrali porwanie przez ciemność, zobaczycie rozdział między dobrem i złem, nie bójcie się, to jest czas żniwa. Bądźcie silni, ponieważ próby jeszcze się nie skończyły i musicie być gotowi stawić temu wszystkiemu czoła, a kiedy będziecie myśleć, że wszystko wydaje się stracone, Ja i mój Jezus będziemy interweniować wraz z moimi aniołami. Chodźcie, moje dzieci, pijcie ze źródła miłości; Ja zawsze będę z wami. Teraz błogosławię was w imię Ojca i Syna i Ducha Świętego, Amen.", dataset["text_pl"])


import goslate
gs = goslate.Goslate()

dataset["text_es"] = dataset["text_it"].apply(lambda x: gs.translate(x,'es'))
dataset["text_fr"] = dataset["text_en"].apply(lambda x: gs.translate(x,'fr'))
dataset["text_zh"] = dataset["text_en"].apply(lambda x: gs.translate(x,'zh'))


dataset.to_csv("december_2021.csv", encoding="utf-8", index=False)
######

dataset["text_de"] = dataset["text_en"].apply(lambda x: gs.translate(x,'de'))

dataset["text_pt"] = dataset["text_en"].apply(lambda x: gs.translate(x,'pt'))


dataset.to_csv("december_2021.csv", encoding="utf-8", index=False)







