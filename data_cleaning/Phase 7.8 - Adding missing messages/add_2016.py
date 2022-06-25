# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np
from google_trans_new import google_translator


dataset_2016 = pd.read_json("trevignano2016.js")



missing_2016 = pd.read_csv("missing_2016.csv")


#Italian
missing_2016["text_it"] = np.where(((missing_2016["month"] == 10) & (missing_2016["day"] == 19)), "Cari figli, grazie per essere riuniti qui in preghiera. Figli adorati, guardate il cielo e ascoltate la terra che si apre, le perdite umane sono grande segno di purificazione della terra. Gli angeli e gli arcangeli stanno combattendo contro i demoni su una sfera più alta del cielo, ormai il Settimo sigillo e stato aperto e mio figlio lo vedrete tra poco. Figli miei presto un asteroide si abbatterà sulla terra. Pregate per l’italia, l’Inghilterra e la Cina dove la terra tremerà, Io vi sono vicino, vi amo e vi benedico nel nome del Padre del Figlio e dello spirito santo. Amen", missing_2016["text_it"])
missing_2016["text_it"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 3)), "Cari figli, grazie per essere riuniti qui sul posto da me prescelto. Vi invito alla preghiera e alla conversione, Vi prego aprite i vostri cuori, solo così potrete ricevere le grazie da voi richieste. Amati figli nutritevi del corpo di mio Figlio e confessatevi, scegliete il giusto sacerdote e confessatevi. Figli miei le vostre testimonianze sono importanti per gli altri, quindi testimoniate, testimoniate,  testimoniate con coraggio la vostra fede. Un asteroide colpirà la terra togliendo la presa della tecnologia.  Dio donandovi la tecnologia voleva darvi un aiuto,  ma questa,  sta portando le famiglie alla perdizione perché è usata male. Pregate per l’ Italia,  dove la terra tremerà ancora,  ma chi avrà fede non dovrà aver paura perché io gli sarò accanto. Pregate per gli Stati Uniti dove ci sarà una disunione molto forte. Nel nome della Trinità scenda su di voi e sulle vostre famiglie la benedizione, nel nome del Padre del Figlio e dello Spirito Santo. Amen.", missing_2016["text_it"])
missing_2016["text_it"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 8)), "Amata sorella, Io mando mia madre affinché i suoi messaggi possano servire per la salvezza di tante anime. Purtroppo il nome di mia Madre,  pian piano non verrà piu menzionato perché l’anticristo non lo permetterà, ma voi siate fedeli a me e sarete salvati. Il vostro Gesù.", missing_2016["text_it"])
missing_2016["text_it"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 12)), "Figli miei, oggi sono felice nel vedervi riuniti tutti qui e sono felice per le nuove persone che hanno sentito la mia chiamata nel loro cuore. Oggi io sarò con voi per tutta la durata della recita del Santo Rosario. Figli amati,  non c è più tempo per le cose materiali, staccatevi, purtroppo non tutti credono ai miei appelli e questo li porterà a non potersi preparare al momento in cui mio Figlio li chiamerà uno ad uno, scegliete e convertitevi,  non avete più tempo. I miei figli consacrati e giusti amati da Gesù, pian piano saranno perseguitati dai loro stessi confratelli, ma io li esorto e desidero che continuino a leggere ed insegnare SOLO il vangelo. Purtroppo l’ anticristo sta per fare il suo trionfante ingresso. Figli amati, pregate per l’Italia perché una regione rischia di essere sommersa dalle acque. Io sarò con voi sempre e vi proteggerò, siate puri di cuore e di spirito. Andate avanti con forza e coraggio, Vi amo tutti. Vi benedico nel nome del Padre del Figlio e dello Spirito Santo. Amen.", missing_2016["text_it"])
missing_2016["text_it"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 15)), "Cari figli,  pregate,  pregate,  pregate senza sosta in questo tempo di grande avvertimento,  non solo i miei figli non credono ai messaggi che amorevolmente gli lascio,  ma non riconoscono neanche mio figlio. Il male vi sta attaccando violentemente,  Vi invito ad aprire gli occhi. Pregate per il Perù,  perché i vulcani si stanno risvegliando,   pregate per il mondo perché la terra non smetterà di tremare e le catastrofi sono in avvicinamento,  ma io saro sempre con voi per proteggervi non ignorate le mie parole, Vi  amo tutti e invio la mia santa benedizione nel nome del Padre del Figlio e dello Spirito Santo. Amen", missing_2016["text_it"])
missing_2016["text_it"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 19)), "Cari figli, in questo momento l’inferno è vuoto,  i demoni sono tutti sulla terra perché sanno di non avere molto tempo a disposizione. Figli miei,  in questo momento il grande scisma della chiesa si sentirà in maniera forte,  tanto che i miei figli consacrati non si fideranno l’uno dell’altro. Figli miei,  anche la natura inizia a ribellarsi,  miei amati desidero che i giusti non scappino davanti alla persecuzione ma affrontatela con amore verso Dio,  sarete protetti,  fidatevi di mio Figlio perché Lui è l’unica verità e la vita. Questo sarà un momento dove ci saranno tante grazie, accoglietele perché e l’ultima possibilità che avrete per avvicinarvi alla preghiera. Adesso, tutti vedranno le profezie avverarsi. Vi amo miei apostoli e andate avanti con forza e coraggio,  grazie piccoli miei, Vi benedico nel nome del Padre del Figlio e dello Spirito Santo. Amen", missing_2016["text_it"])
missing_2016["text_it"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 22)), "Cari figli,  oggi sono felice per i nuovi arrivati che hanno sentito la mia chiamata nel loro cuore. Figli miei purtroppo non avete più tempo. Quel tempo a disposizione per tutti coloro che ne hanno avuto molto per poter scegliere, volge al termine. Iniziate a guardare i segni del cielo. Non ascoltate chi vi dà delle date, siate sempre pronti , oggi più di prima. Mio Figlio,  ha anticipato ancora una volta la sua venuta,   è molto stanco dei comportamenti dell’uomo, vivete come Sodoma e Gomorra.Piccoli miei,  seguite soltanto le sacre scritture perché la confusione della  Chiesa vi sta destabilizzando, la massoneria sta avanzando velocemente e anche Dio sta velocizzando i suoi tempi. Figli adorati , stringetevi al mio cuore immacolato ed io vi proteggerò sempre, sono qui tra voi e vi benedico uno per volta nel nome del padre del Figlio e dello spirito santo. Amen", missing_2016["text_it"])
missing_2016["text_it"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 26)), "Fratelli amati,  siate pieni della mia misericordia,  non ascoltate chi vi dice di avermi visto ad oriente o occidente, Io arriverò presto,  ci saranno tanti falsi profeti,  aprite gli occhi. La falsa pace tra le nazioni,  sarà di grande attualità, ricordate che le vostre preghiere possono cambiare il corso degli eventi anche se ciò che dovrà accadere,  è scritto. Amatemi come Io amo Voi,  e seguite soltanto le mie parole e le istruzioni che vi darà la mia amata Madre,  Io vi proteggerò sempre. Vi dico, che oggi ,sono stati perdonati i vostri peccati, ma continuate a confessarvi e a nutrirvi di me. Miei amati, sia il luogo dove arriveranno milioni di pellegrini , sia  la Santa Croce , sono stati  benedetti  da Dio Padre. Adesso, Vi benedico nel nome del Padre del Figlio e dello Spirito Santo, Amen.", missing_2016["text_it"])
missing_2016["text_it"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 29)), "Cari figli , oggi sono molto gioiosa nel vedervi qui con il cuore aperto. I Miei figli ascoltano davvero la mia chiamata ed io li ringrazio fervidamente. Figli amati,  mio Figlio soffre perché la Chiesa e alla deriva ma io sono qui per sconfiggere il serpente che Vi alberga, il mio cuore immacolato è già al trionfo,  preparatevi in questo tempo di avvento e di grazia,  al Natale confessate tutti i vostri peccati specialmente quelli mortali con il più sincero pentimento. Presto vivrete nella gioia e nella pace. Pregate, pregate,  pregate sopratutto per l italia per il Giappone miei apostoli. Vi benedico nel nome del Padre del Figlio e dello Spirito Santo. Amen", missing_2016["text_it"])



#English
missing_2016["text_en"] = np.where(((missing_2016["month"] == 10) & (missing_2016["day"] == 19)), "Dear children, thank you for being gathered here in prayer. Beloved children, look to the heavens and listen to the earth opening, human losses are great sign of purification of the earth.The angels and archangels are fighting against the demons on a sphere higher than the sky, now the Seventh seal has been opened and you will see my Son soon. My children, soon an asteroid will strike the Earth. Pray for Italy, England and China where the earth will tremble, I am close to you, I love you and I bless you in the name of the Father and the Son and the Holy Spirit, Amen.", missing_2016["text_en"])
missing_2016["text_en"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 3)), "Dear children, thank you for being gathered here in the place chosen by me. I call you to prayer and conversion, I beg you to open your hearts, only in this way will you be able to receive the graces you request. Beloved children, nourish yourselves with the body of my Son and confess, choose the right priest and confess. My children, your testimonies are important for others, so witness, witness, witness with courage your faith. An asteroid will strike the earth removing the grip of technology.  God, by giving you technology, wanted to give you help, but this technology is leading families to perdition because it is used badly. Pray for Italy, where the earth will shake again, but whoever has faith should not fear because I will be beside him. Pray for the United States where there will be a very strong disunity. In the name of the Trinity, may blessings descend upon you and your families, in the name of the Father and the Son and the Holy Spirit, Amen.", missing_2016["text_en"])
missing_2016["text_en"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 8)), "Beloved sister, I am sending my Mother so that her messages may serve for the salvation of many souls. Unfortunately, my Mother's name will gradually be no longer mentioned because the antichrist will not allow it, but be faithful to me and you will be saved. Your Jesus.", missing_2016["text_en"])
missing_2016["text_en"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 12)), "My children, today I am happy to see you all gathered here and I am happy for the new people who have heard my call in their hearts. Today I will be with you throughout the recitation of the Holy Rosary. Beloved children, there is no more time for material things, detach yourselves, unfortunately, not all believe in my calls and this will lead them to not being able to prepare for the moment when my Son will call them one by one, choose and convert, you have no more time. My consecrated and righteous children loved by Jesus will be persecuted little by little by their own brethren, but I urge them and desire that they continue to read and teach ONLY the Gospel. Unfortunately, the Antichrist is about to make his triumphant entrance. Beloved children, pray for Italy because a region is in danger of being submerged by the waters. I will always be with you and I will protect you; be pure in heart and spirit. Go forward with strength and courage, I love you all. I bless you in the name of the Father and the Son and the Holy Spirit, Amen.", missing_2016["text_en"])
missing_2016["text_en"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 15)), "Dear children, pray, pray, pray without ceasing in this time of great warning; not only do my children not believe the messages that I lovingly leave them, but they do not even recognize my Son. Evil is violently attacking you, I invite you to open your eyes. Pray for Peru, because the volcanoes are awakening, pray for the world because the earth will not stop shaking and catastrophes are approaching, but I will always be with you to protect you, do not ignore my words, I love you all and I send my holy blessing in the name of the Father, the Son and the Holy Spirit. Amen.", missing_2016["text_en"])
missing_2016["text_en"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 19)), "Dear children, at this time hell is empty, the demons are all on earth because they know they do not have much time. My children, at this time the great schism in the church will be felt so strongly that my consecrated children will not trust each other. My children, even nature is beginning to rebel, my beloved ones I desire that the righteous do not run away before persecution but face it with love towards God, you will be protected, trust my Son because He is the only truth and life. This will be a time when there will be many graces, accept them because it is the last chance you will have to approach prayer. Now, everyone will see the prophecies come true. I love you my apostles and go forward with strength and courage, thank you my little ones, I bless you in the name of the Father and the Son and the Holy Spirit, Amen.", missing_2016["text_en"])
missing_2016["text_en"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 22)), "Dear children, today I am happy for the newcomers who have heard my call in their hearts. My children, unfortunately you have no more time. That time available to all who have had much to choose from is coming to an end. Begin to look at the signs in the sky. Do not listen to those who give you dates, always be ready, today more than before. My Son, has once again advanced His coming, He is very tired of man's behaviors, you are living like Sodom and Gomorrah. My little ones, follow only the sacred scriptures because the confusion of the Church is destabilizing you, Freemasonry is advancing fast and even God is speeding up His times. I am here among you and I bless you one by one in the name of the Father and the Son and the Holy Spirit. Amen.", missing_2016["text_en"])
missing_2016["text_en"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 26)), "Beloved brothers, be full of My mercy, do not listen to those who tell you they have seen Me in the East or West, I will come soon, there will be many false prophets, open your eyes. The false peace among the nations, will be of great concern, remember that your prayers can change the course of events even if what is to happen is written. Love me as I love you, and follow only my words and the instructions that my beloved Mother will give you, I will always protect you. I tell you that today, your sins have been forgiven, but continue to confess and feed on Me. My beloved ones, both the place where millions of pilgrims will arrive and the Holy Cross have been blessed by God the Father. Now, I bless you in the name of the Father and the Son and the Holy Spirit, Amen.", missing_2016["text_en"])
missing_2016["text_en"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 29)), "Dear children, today I am very joyful to see you here with an open heart. My children are truly listening to my call and I thank them fervently. Beloved children, my Son suffers because the Church is adrift but I am here to defeat the serpent that dwells in you, my immaculate heart is already in triumph, prepare yourselves in this time of Advent and grace, at Christmas confess all your sins especially the mortal ones with the most sincere repentance. Soon you will live in joy and peace. Pray, pray, pray especially for Italy and Japan, my apostles. I bless you in the name of the Father and the Son and the Holy Spirit. Amen.", missing_2016["text_en"])




#Polish
missing_2016["text_pl"] = np.where(((missing_2016["month"] == 10) & (missing_2016["day"] == 19)), "Drogie dzieci, dziękuję wam, że jesteście tutaj zgromadzeni na modlitwie. Umiłowane dzieci, patrzcie na niebo i słuchajcie jak ziemia się otwiera, straty ludzkie są wielkim znakiem oczyszczania ziemi. Aniołowie i archaniołowie walczą z demonami w sferze wyższej niż niebiosa, teraz Siódma Pieczęć została otwarta i wkrótce ujrzycie mojego syna. Moje dzieci, wkrótce asteroida uderzy w Ziemię. Módlcie się za Włochy, Anglię i Chiny, gdzie ziemia będzie drżeć, jestem blisko was, kocham was i błogosławię was w imię Ojca i Syna i Ducha Świętego. Amen.", missing_2016["text_pl"])
missing_2016["text_pl"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 3)), "Drogie dzieci, dziękuję wam, że jesteście zgromadzeni tutaj, w moim wybranym miejscu. Wzywam was do modlitwy i nawrócenia, błagam was, abyście otworzyli swoje serca, tylko w ten sposób będziecie mogli otrzymać łaski, których pragniecie. Umiłowane dzieci, karmcie się Ciałem mojego Syna i spowiadajcie się, wybierzcie właściwego kapłana i spowiadajcie się. Moje dzieci, wasze świadectwa są ważne dla innych, więc z odwagą dawajcie świadectwo, dawajcie świadectwo, dawajcie świadectwo waszej wiary. Asteroida uderzy w Ziemię, pozbawiając ją możliwości korzystania z technologii.  Dając wam technologię, Bóg chciał wam pomóc, ale ona prowadzi rodziny do zguby, ponieważ jest źle używana. Módlcie się za Włochy, gdzie znowu zatrzęsie się ziemia, ale kto ma wiarę, niech się nie lęka, bo Ja będę z nim. Módlcie się za Stany Zjednoczone, gdzie będzie bardzo silny rozłam. W imię Trójcy Przenajświętszej niech zstąpi błogosławieństwo na was i na wasze rodziny, w imię Ojca i Syna i Ducha Świętego. Amen.", missing_2016["text_pl"])
missing_2016["text_pl"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 8)), "Ukochana siostro, wysyłam moją Matkę, aby jej orędzia służyły zbawieniu wielu dusz. Niestety, imię mojej Matki stopniowo nie będzie już wspominane, ponieważ antychryst na to nie pozwoli, ale bądźcie mi wierni, a będziecie zbawieni. Twój Jezus.", missing_2016["text_pl"])
missing_2016["text_pl"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 12)), "Dzieci moje, cieszę się, że dzisiaj widzę was tu zgromadzonych i cieszę się z nowych ludzi, którzy usłyszeli w swoich sercach moje wezwanie. Dzisiaj będę z wami przez cały czas odmawiania Różańca Świętego. Umiłowane dzieci, nie ma już czasu na rzeczy materialne, odłączcie się, niestety nie wszyscy wierzą w moje wezwania i to doprowadzi do tego, że nie będą mogli przygotować się na moment, kiedy mój Syn wezwie ich pojedynczo, wybierzcie i nawróćcie się, nie macie już czasu. Moje poświęcone i sprawiedliwe dzieci umiłowane przez Jezusa, stopniowo będą prześladowane przez swoich braci, ale zachęcam je i pragnę, aby nadal czytały i nauczały TYLKO Ewangelii. Niestety, Antychryst ma właśnie dokonać swojego triumfalnego wejścia. Umiłowane dzieci, módlcie się za Włochy, ponieważ jeden z regionów jest zagrożony zalaniem przez wodę. Ja zawsze będę z wami i będę was strzegła; bądźcie czystego serca i ducha. Idźcie naprzód z siłą i odwagą, kocham was wszystkich. Błogosławię Was w imię Ojca, Syna i Ducha Świętego. Amen.", missing_2016["text_pl"])
missing_2016["text_pl"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 15)), "Drogie dzieci, módlcie się, módlcie się, módlcie się bez przerwy w tym czasie wielkiego ostrzeżenia; moje dzieci nie tylko nie wierzą w wiadomości, które z miłością im zostawiam, ale nawet nie rozpoznają mojego Syna. Zło gwałtownie was atakuje, zapraszam was do otwarcia oczu. Módlcie się za Peru, ponieważ budzą się wulkany, módlcie się za świat, ponieważ ziemia nie przestanie się trząść i zbliżają się katastrofy, ale ja zawsze będę z wami, aby was chronić, nie lekceważcie moich słów, kocham was wszystkich i przesyłam moje święte błogosławieństwo w imię Ojca i Syna i Ducha Świętego. Amen.", missing_2016["text_pl"])
missing_2016["text_pl"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 19)), "Drogie dzieci, w tym czasie piekło jest puste, wszystkie demony są na ziemi, ponieważ wiedzą, że nie mają dużo czasu. Moje dzieci, w tym czasie wielki rozłam w Kościele będzie odczuwalny tak mocno, że moje konsekrowane dzieci nie będą ufać sobie nawzajem. Moje dzieci, nawet natura zaczyna się buntować, moi kochani pragnę, aby sprawiedliwi nie uciekali przed prześladowaniami, ale stawiali im czoła z miłością do Boga, będziecie chronieni, zaufajcie mojemu Synowi, bo On jest jedyną prawdą i życiem. To będzie czas, w którym będzie wiele łask, przyjmijcie je, ponieważ jest to ostatnia możliwość, aby zbliżyć się do modlitwy. Teraz wszyscy zobaczą, że proroctwa się spełniły. Kocham was moi apostołowie, idźcie naprzód z siłą i odwagą, dziękuję wam moje maleństwa, błogosławię was w imię Ojca i Syna i Ducha Świętego, Amen.", missing_2016["text_pl"])
missing_2016["text_pl"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 22)), "Drogie dzieci, dzisiaj cieszę się z nowo przybyłych, którzy usłyszeli w swoich sercach moje wezwanie. Moje dzieci, niestety nie macie już więcej czasu. Kończy się czas dostępny dla wszystkich, którzy mieli dużo czasu na wybór. Zacznijcie patrzeć na znaki na niebie. Nie słuchajcie tych, którzy podają wam daty; bądźcie zawsze gotowi, dziś bardziej niż przedtem. Mój Syn przyspieszył swoje ponowne przyjście, jest bardzo zmęczony zachowaniem człowieka, żyjecie jak Sodoma i Gomora. Moi mali, kierujcie się tylko Pismem Świętym, ponieważ zamęt w Kościele was destabilizuje, masoneria szybko postępuje naprzód i nawet Bóg przyspiesza swoje czasy. Umiłowane dzieci, przylgnijcie do mego niepokalanego serca, a ja zawsze będę was strzegła; jestem pośród was i błogosławię każdego z was w imię Ojca i Syna i Ducha Świętego, Amen.", missing_2016["text_pl"])
missing_2016["text_pl"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 26)), "Umiłowani bracia, bądźcie pełni mojego miłosierdzia, nie słuchajcie tych, którzy mówią wam, że widzieli mnie na Wschodzie lub na Zachodzie, przyjdę wkrótce, będzie wielu fałszywych proroków, otwórzcie oczy. Fałszywy pokój między narodami, będzie miał wielkie znaczenie, pamiętajcie, że wasze modlitwy mogą zmienić bieg wydarzeń, nawet jeśli to, co ma się wydarzyć, jest zapisane. Kochajcie mnie tak, jak ja was kocham i kierujcie się tylko moimi słowami i wskazówkami, które da wam moja ukochana Matka; zawsze będę was chronić. Mówię wam, że dzisiaj wasze grzechy zostały odpuszczone, ale nadal wyznajcie je i karmcie się Mną. Moi umiłowani, zarówno miejsce, do którego przybędą miliony pielgrzymów, jak i Krzyż Święty zostały pobłogosławione przez Boga Ojca. Teraz błogosławię was w imię Ojca i Syna i Ducha Świętego, Amen.", missing_2016["text_pl"])
missing_2016["text_pl"] = np.where(((missing_2016["month"] == 11) & (missing_2016["day"] == 29)), "Drogie dzieci, dzisiaj jestem bardzo szczęśliwa, że widzę was tutaj z otwartym sercem. Moje dzieci naprawdę słuchają mojego wezwania i gorąco im za to dziękuję. Umiłowane dzieci, mój Syn cierpi, ponieważ Kościół jest rozproszony, ale ja jestem tutaj, aby pokonać węża, który mieszka w was, moje niepokalane serce już triumfuje, przygotujcie się w tym czasie Adwentu i łaski, w Boże Narodzenie wyznajcie wszystkie wasze grzechy, zwłaszcza śmiertelne, z najszczerszą skruchą. Wkrótce będziecie żyć w radości i pokoju. Moi apostołowie, módlcie się, módlcie się, módlcie się szczególnie za Włochy i Japonię. Błogosławię was w imię Ojca i Syna i Ducha Świętego. Amen.", missing_2016["text_pl"])




translator = google_translator()  




import goslate
gs = goslate.Goslate()

missing_2016["text_es"] = missing_2016["text_it"].apply(lambda x: gs.translate(x,'es'))
missing_2016["text_fr"] = missing_2016["text_en"].apply(lambda x: gs.translate(x,'fr'))
missing_2016["text_zh"] = missing_2016["text_en"].apply(lambda x: gs.translate(x,'zh'))
missing_2016["text_de"] = missing_2016["text_en"].apply(lambda x: gs.translate(x,'de'))
missing_2016["text_pt"] = missing_2016["text_en"].apply(lambda x: gs.translate(x,'pt'))





dataset_merged = pd.concat([dataset_2016, missing_2016])



dataset_merged["month_string"] = np.where(dataset_merged["month"] == 10, "October", dataset_merged["month_string"]) 
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 11, "November", dataset_merged["month_string"]) 



dataset_merged = dataset_merged.sort_values(by=["month", "day"])




dataset_merged.to_json("trevignano2016.js",orient="records")













