# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np
from google_trans_new import google_translator


dataset_2018 = pd.read_json("trevignano2018.js")



missing_2018 = pd.read_csv("missing_2018.csv")


#Italian
missing_2018["text_it"] = np.where(((missing_2018["month"] == 2) & (missing_2018["day"] == 24)), "Amati Figli, grazie per aver risposto alla mia chiamata nel vostro cuore. Figli miei, il mio cuore è affranto perché so a cosa state andando incontro. Verranno tempi molto difficili, ma vi dico che dovrete sopportare queste croci con l’amore nel cuore verso mio Figlio. I nemici di Dio stanno organizzando l’ingresso in Vaticano e sarà molto doloroso. Soltanto con la preghiera potrete mitigare ciò che avverrà. Pregate, pregate, pregate tanto. Dio è molto offeso soprattutto dall’Italia, la nazione che lo ha tradito pensando a tutto tranne che a Dio, nonostante ci sia la Chiesa fondata da Pietro! Guardate spesso il cielo, perché è dal cielo che arriveranno tutti i segni prima della grande tribolazione. Ora vi benedico nel nome del Padre del Figlio e dello Spirito Santo. Amen. Stasera tante saranno le grazie che scenderanno su di voi.", missing_2018["text_it"])
missing_2018["text_it"] = np.where(((missing_2018["month"] == 3) & (missing_2018["day"] == 17)), "Cari figli amati, grazie per essere riuniti qui nella preghiera. Io vengo per la pace e per amore, tutti i miei insegnamenti e la mia guida, servono a voi per non farvi camminare nel buio delle tenebre. Amati figli miei, le vostre preghiere sono delle bombe di amore per il mondo, ma a chi fosse ancora nel peccato, chiedo di confessarsi e convertirsi, non avete tanto tempo, tutto ciò che è stato predetto accadrà, questo è il tempo. Figlia mia recita un Padre nostro con me. Ora vi benedico nel nome del Padre del figlio e dello Spirito Santo. Amen", missing_2018["text_it"])
missing_2018["text_it"] = np.where(((missing_2018["month"] == 3) & (missing_2018["day"] == 20)), "Cari figli, grazie per essere riuniti qui nella preghiera. Amati miei amate la croce, mio Figlio quando arriverà vuole che tutti siano purificati. Questa sarà una Pasqua speciale. Miei cari figli sacerdoti,  oh! quanto avrete da soffrire, sarete costretti ad obbedire, ma non dimenticate, siate esempio nel raccontare e parlare di Gesù, non siate libri e regole, ma cuore, amore, speranza e carità. Non lasciatevi confondere. Ora vi benedico nel nome del Padre del Figlio e dello Spirito Santo. Amen. Desidero che ci sia una catena di preghiera per la Russia, perché è da lì che la scintilla si accenderà.", missing_2018["text_it"])
missing_2018["text_it"] = np.where(((missing_2018["month"] == 3) & (missing_2018["day"] == 22)), "Cari figli prediletti, grazie per essere qui in preghiera, in questa casa Consacrata da mio Figlio. Figli, le vostre preghiere e la vostra fede asciugano le mie lacrime e alleviano le sofferenze di mio Figlio Gesù. Quanta tristezza sento nel cuore per ciò che l’umanità va incontro. Vi chiedo figli amati, quando la parola del Vangelo verrà distorta, in quel momento stanno bestemmiando contro Dio, svegliatevi e ascoltate. Le mie benedizioni questa sera scenderanno su di voi e sulle vostre famiglie. Vi amo e pregate per proteggervi oggi e sempre. Ora vi benedico nel nome del Padre del Figlio e dello Spirito Santo. Amen", missing_2018["text_it"])
missing_2018["text_it"] = np.where(((missing_2018["month"] == 4) & (missing_2018["day"] == 28)), "Amati figli, grazie per aver ascoltato la mia chiamata nel vostri cuori. Amati miei, presto il buio verrà su questa umanità che ha perso Dio nel proprio cuore. Mi chiedete spesso se il vostro modo di pregare è quello giusto, allora io vi dico, ogni vostra preghiera per i figli ammalati e per i più sofferenti vanno direttamente al Padre,non vi accorgete delle Grazie che ricevete tutti i giorni! Cari bambini miei, invocate i vostri angeli custodi e arriveranno in vostro soccorso. Seguite le leggi di Dio e non l’ego umano. Presto i vulcani erutteranno e la natura si ribellerà. Ora vi lascio con la mia benedizione materna, nel nome del Padre, del Figlio e dello Spirito Santo. Amen", missing_2018["text_it"])
missing_2018["text_it"] = np.where(((missing_2018["month"] == 5) & (missing_2018["day"] == 29)), "Fratelli miei, grazie per aver ascoltato il richiamo alla preghiera del Santo Rosario. Io vi invito a riflettere. Quando mia Madre, vi chiede di farvi trovare pronti alla mia seconda venuta, spesso voi pensate, 'ma io prego!' Fatevi un esame di coscienza. Quante volte mi portate le vostre gioie e i vostri dolori, quante volte mi ringraziate per le cose belle che vi dono? Vi chiedete se avete giudicato ingiustamente i vostri fratelli? Quante opere buone avete fatto nella vostra vita e quante opere di carità? Quante anime avete portato a me strappandole al demonio? Fratelli e sorelle questi sono i motivi per cui verrete giudicati, sappiate che coloro che bestemmieranno, non vedranno mai il mio volto. Siate uniti e pregate per l’Italia, perché grande sarà la sua sofferenza , anche la natura si ribellerà contro l’uomo. Ora vi benedico nel nome della Santissima Trinità, Padre , Figlio e Spirito Santo, Amen.", missing_2018["text_it"])
missing_2018["text_it"] = np.where(((missing_2018["month"] == 6) & (missing_2018["day"] == 10)), "Amati figli, grazie per aver ascoltato la mia chiamata nel vostro cuore. Io,  insieme a Gesù, siamo qui per benedirvi e vi chiedo di essere sempre fedeli a mio Figlio. Non dimenticate,  che cosa ha fatto lui per voi e per i vostri peccati, non fatevi distogliere dai modernismi, presto sentirete il suono di tromba che suonerà nei cieli e sarà udito in tutto il mondo. Figli miei, noi siamo quì per chiedervi di pregare per la pace. Ora, vi benedico nel nome del Padre, del Figlio e dello Spirito Santo, Amen.", missing_2018["text_it"])
missing_2018["text_it"] = np.where(((missing_2018["month"] == 12) & (missing_2018["day"] == 4)), "Fratelli  miei, grazie per essere qui nella preghiera, la vostra Fede allevia il mio grande dolore. Amati miei, io verrò con tutta la mia Gloria e la mia Potenza,  lì dove appare la mia Santissima Madre, vedrete i segni dal cielo! Mentre voi pregate, Io apro i cuori più duri e con le vostre preghiere consolate il cuore Immacolato di mia Madre, fatevi sempre seguire da Lei, è guida sicura, forte e giusta per tutti coloro che non conoscono la vera fede. Vi amo e vi benedico nel nome del Padre, nel Mio nome e nel nome dello Spirito Santo, Amen.  Il vostro Gesù!", missing_2018["text_it"])




#English
missing_2018["text_en"] = np.where(((missing_2018["month"] == 2) & (missing_2018["day"] == 24)), "Beloved children, thank you for having responded to my call in your hearts. My children, my heart is broken because I know what you are going through. Very difficult times will come, but I tell you that you will have to bear these crosses with love in your hearts towards my Son. The enemies of God are organizing the entrance into the Vatican and it will be very painful. Only with prayer can you mitigate what will happen. Pray, pray, pray very much. God is very offended especially by Italy, the nation that has betrayed Him by thinking of everything except God, despite the fact that there is the Church founded by Peter! Look often at heaven, for it is from heaven that all the signs will come before the great tribulation. Now I bless you in the name of the Father of the Son and of the Holy Spirit, Amen. Tonight many will be the graces that will descend upon you.", missing_2018["text_en"])
missing_2018["text_en"] = np.where(((missing_2018["month"] == 3) & (missing_2018["day"] == 17)), "Dear beloved children, thank you for being gathered here in prayer. I come for peace and love, all my teachings and guidance are for you not to make you walk in the gloom of darkness. My beloved children, your prayers are bombs of love for the world, but to those who are still in sin, I ask them to confess and convert, you do not have much time, all that has been foretold will happen, this is the time. My daughter, recite an Our Father with me. Now I bless you in the name of the Father and the Son and the Holy Spirit, Amen.", missing_2018["text_en"])
missing_2018["text_en"] = np.where(((missing_2018["month"] == 3) & (missing_2018["day"] == 20)), "Dear children, thank you for being gathered here in prayer. My beloved ones love the cross, my Son when it comes wants everyone to be purified. This will be a special Easter. My dear priest sons, oh! how much you will have to suffer, you will be forced to obey, but do not forget, be an example in telling and speaking about Jesus, do not be books and rules, but heart, love, hope and charity. Do not let yourselves be confused. Now I bless you in the name of the Father and the Son and the Holy Spirit, Amen. I wish there to be a prayer chain for Russia, for it is from there that the spark will be ignited.", missing_2018["text_en"])
missing_2018["text_en"] = np.where(((missing_2018["month"] == 3) & (missing_2018["day"] == 22)), "Dear beloved children, thank you for being here in prayer, in this house consecrated by my Son. Children, your prayers and faith dry my tears and alleviate the suffering of my Son Jesus. How much sadness I feel in my heart for what humanity is going through. I ask you beloved children, when the word of the Gospel is distorted, at that moment they are blaspheming against God, wake up and listen. My blessings tonight will descend upon you and your families. I love you and pray to protect you today and always. I now bless you in the name of the Father and the Son and the Holy Spirit, Amen.", missing_2018["text_en"])
missing_2018["text_en"] = np.where(((missing_2018["month"] == 4) & (missing_2018["day"] == 28)), "Beloved children, thank you for listening to my call in your hearts. Beloved ones, soon darkness will come upon this humanity that has lost God in its heart. You often ask me if your way of praying is the right one, then I tell you, all your prayers for your sick children and for the most suffering ones go directly to the Father, you do not realize the Graces you receive every day! My dear children, invoke your guardian angels and they will come to your rescue. Follow God's laws and not the human ego. Soon volcanoes will erupt and nature will rebel. Now I leave you with my motherly blessing, in the name of the Father and the Son and the Holy Spirit, Amen.", missing_2018["text_en"])
missing_2018["text_en"] = np.where(((missing_2018["month"] == 5) & (missing_2018["day"] == 29)), "My brothers, thank you for listening to the call to prayer of the Holy Rosary. I invite you to reflect. When My Mother asks you to be ready for My Second Coming, you often think, 'But I pray!' Make an examination of conscience. How often do you bring me your joys and sorrows, how often do you thank me for the beautiful things I give you? Do you wonder if you have judged your brothers and sisters unfairly? How many good works have you done in your lives and how many works of kindness? How many souls have you brought to me by snatching them away from the devil? Brothers and sisters, these are the reasons why you will be judged; know that those who blaspheme will never see my face. Be united and pray for Italy, for great will be its suffering, even nature will rebel against man. Now I bless you in the name of the Most Holy Trinity, Father and Son and Holy Spirit, Amen.", missing_2018["text_en"])
missing_2018["text_en"] = np.where(((missing_2018["month"] == 6) & (missing_2018["day"] == 10)), "Beloved children, thank you for listening to my call in your hearts. I, together with Jesus, am here to bless you and ask you to always be faithful to my Son. Do not forget, what He has done for you and for your sins, do not be distracted by modernisms, soon you will hear the trumpet sound that will sound in the heavens and be heard throughout the world. My children, we are here to ask you to pray for peace. Now, I bless you in the name of the Father and the Son and the Holy Spirit, Amen.", missing_2018["text_en"])
missing_2018["text_en"] = np.where(((missing_2018["month"] == 12) & (missing_2018["day"] == 4)), "My brothers, thank you for being here in prayer, your Faith relieves my great sorrow. My beloved ones, I will come with all My Glory and Power, there where My Most Holy Mother appears, you will see the signs from Heaven! While you are praying, I am opening the hardest hearts and with your prayers you are consoling the Immaculate Heart of my Mother, always follow Her, she is a sure, strong and just guide for all those who do not know the true faith. I love you and bless you in the name of the Father, in My name and in the name of the Holy Spirit, Amen. Your Jesus!", missing_2018["text_en"])



#Polish
missing_2018["text_pl"] = np.where(((missing_2018["month"] == 2) & (missing_2018["day"] == 24)), "Umiłowane dzieci, dziękuję wam, że odpowiedzieliście na moje wezwanie w waszych sercach. Moje dzieci, moje serce jest strapione, bo wiem, przez co przechodzicie. Przyjdą bardzo trudne czasy, ale mówię wam, że musicie nieść te krzyże z miłością w waszych sercach do mojego Syna. Wrogowie Boga organizują wejście do Watykanu i będzie to bardzo bolesne. Tylko dzięki modlitwie będziecie mogli złagodzić to, co się wydarzy. Módlcie się, módlcie się, módlcie się bardzo mocno. Bóg jest bardzo obrażany, szczególnie przez Włochy, naród, który Go zdradził, myśląc o wszystkim poza Bogiem, pomimo faktu, że istnieje tam Kościół założony przez Piotra! Patrzcie często na niebo, bo to z nieba będą pochodzić wszystkie znaki przed wielkim uciskiem. Teraz błogosławię was w imię Ojca i Syna i Ducha Świętego, Amen. Dziś wieczorem zstąpi na was wiele łask.", missing_2018["text_pl"])
missing_2018["text_pl"] = np.where(((missing_2018["month"] == 3) & (missing_2018["day"] == 17)), "Drogie kochane dzieci, dziękuję wam, że jesteście tutaj zgromadzeni na modlitwie. Przychodzę dla pokoju i miłości; wszystkie moje nauki i wskazówki są dla was, abyście nie chodzili w mroku ciemności. Moje kochane dzieci, wasze modlitwy są bombami miłości do świata, ale tych, którzy są jeszcze w grzechu, proszę, aby się wyspowiadali i nawrócili, nie macie wiele czasu, wszystko, co zostało przepowiedziane, stanie się, to jest ten czas. Moja córko, odmów ze mną Ojcze Nasz.Teraz błogosławię was w imię Ojca, Syna i Ducha Świętego.  Amen.", missing_2018["text_pl"])
missing_2018["text_pl"] = np.where(((missing_2018["month"] == 3) & (missing_2018["day"] == 20)), "Drogie dzieci, dziękuję wam, że jesteście tu zgromadzeni na modlitwie. Umiłowani moi, umiłujcie krzyż, mój Syn, gdy przyjdzie, chce, aby wszyscy zostali oczyszczeni. To będzie wyjątkowa Wielkanoc. Moi drodzy synowie kapłani, och! jak wiele będziecie musieli cierpieć, będziecie zmuszeni do posłuszeństwa, ale nie zapominajcie, bądźcie przykładem w mówieniu i opowiadaniu o Jezusie, nie bądźcie książkami i regułami, ale sercem, miłością, nadzieją i miłosierdziem. Nie dajcie się zmylić. Teraz błogosławię was w imię Ojca i Syna i Ducha Świętego, Amen. Chcę, aby powstał łańcuszek modlitewny za Rosję, bo tam właśnie zapłonie iskra.", missing_2018["text_pl"])
missing_2018["text_pl"] = np.where(((missing_2018["month"] == 3) & (missing_2018["day"] == 22)), "Drogie kochane dzieci, dziękuję wam, że jesteście tutaj na modlitwie, w tym domu poświęconym przez mojego Syna. Dzieci moje, wasze modlitwy i wiara osuszają moje łzy i łagodzą cierpienia mojego Syna Jezusa. Jak wielki smutek czuję w sercu z powodu tego, przez co przechodzi ludzkość. Proszę was, umiłowane dzieci, kiedy słowo Ewangelii jest zniekształcane, kiedy bluźni się przeciwko Bogu, obudźcie się i słuchajcie. Moje błogosławieństwo zstąpi na was i wasze rodziny tego wieczoru. Kocham was i modlę się, aby was chronić dzisiaj i zawsze. Błogosławię was teraz w imię Ojca i Syna i Ducha Świętego. Amen.", missing_2018["text_pl"])
missing_2018["text_pl"] = np.where(((missing_2018["month"] == 4) & (missing_2018["day"] == 28)), "Umiłowane dzieci, dziękuję wam, że wsłuchaliście się w moje wołanie w waszych sercach. Moi umiłowani, wkrótce nadejdzie ciemność na tę ludzkość, która utraciła Boga w swoim sercu. Często pytacie mnie, czy wasz sposób modlitwy jest właściwy, wtedy mówię wam, że wszystkie wasze modlitwy za wasze chore dzieci i za najbardziej cierpiących idą bezpośrednio do Ojca; nie zdajecie sobie sprawy z łask, które otrzymujecie każdego dnia! Moje drogie dzieci, wzywajcie swoich aniołów stróżów, a przyjdą wam z pomocą. Podążaj za prawami Boga, a nie za ludzkim ego. Wkrótce wybuchną wulkany, a przyroda się zbuntuje. A teraz zostawiam was z moim matczynym błogosławieństwem, w imię Ojca i Syna i Ducha Świętego, Amen.", missing_2018["text_pl"])
missing_2018["text_pl"] = np.where(((missing_2018["month"] == 5) & (missing_2018["day"] == 29)), "Bracia moi, dziękuję wam, że usłuchaliście wezwania do odmawiania Różańca Świętego. Zapraszam was do refleksji. Kiedy moja Matka prosi was, abyście byli gotowi na moje powtórne przyjście, często myślicie: 'Ale ja się modlę!' Zróbcie rachunek sumienia. Jak często przynosisz mi swoje radości i smutki, jak często dziękujesz mi za piękne rzeczy, które ci daję? Czy zastanawiasz się, czy osądziłeś swoich braci niesprawiedliwie? Ile dobrych uczynków wykonałeś w swoim życiu i ile uczynków miłosierdzia? Ile dusz przyprowadziłeś do mnie, wyrywając je diabłu? Bracia i siostry, to są powody, dla których będziecie sądzeni; wiedzcie, że ci, którzy bluźnią, nigdy nie ujrzą mojego oblicza. Bądźcie zjednoczeni i módlcie się za Włochy, bo ich cierpienia będą wielkie, nawet natura zbuntuje się przeciwko człowiekowi. Teraz błogosławię was w imię Trójcy Przenajświętszej, Ojca i Syna i Ducha Świętego, Amen.", missing_2018["text_pl"])
missing_2018["text_pl"] = np.where(((missing_2018["month"] == 6) & (missing_2018["day"] == 10)), "Umiłowane dzieci, dziękuję wam, że wsłuchaliście się w moje wołanie w waszych sercach. Ja wraz z Jezusem, jesteśmy tutaj, aby wam błogosławić i proszę was, abyście zawsze byli wierni mojemu Synowi. Nie zapominajcie, co On zrobił dla was i za wasze grzechy, nie rozpraszajcie się modernizmem, wkrótce usłyszycie dźwięk trąby, który zabrzmi w niebiosach i będzie słyszalny na całym świecie. Moje dzieci, jesteśmy tutaj, aby prosić was o modlitwę w intencji pokoju. Teraz błogosławię was w imię Ojca i Syna i Ducha Świętego, Amen.", missing_2018["text_pl"])
missing_2018["text_pl"] = np.where(((missing_2018["month"] == 12) & (missing_2018["day"] == 4)), "Moi bracia, dziękuję wam za waszą obecność na modlitwie, wasza wiara łagodzi mój wielki smutek. Umiłowani moi, przyjdę z całą moją Chwałą i Mocą, tam, gdzie pojawi się moja Najświętsza Matka, zobaczycie znaki z Nieba! Podczas gdy wy się modlicie, Ja otwieram najtwardsze serca i waszymi modlitwami pocieszacie Niepokalane Serce mojej Matki, pozwólcie sobie Ją zawsze naśladować, Ona jest pewną, silną i sprawiedliwą przewodniczką dla wszystkich, którzy nie znają prawdziwej wiary. Kocham was i błogosławię was w imię Ojca, w imię Moje i w imię Ducha Świętego, Amen. Twój Jezus!", missing_2018["text_pl"])





translator = google_translator()  

#missing_2018["text_es"] = missing_2018["text_en"].apply(lambda x: translator.translate(x,lang_tgt='es'))
#missing_2018["text_fr"] = missing_2018["text_en"].apply(lambda x: translator.translate(x,lang_tgt='fr'))
#missing_2018["text_zh"] = missing_2018["text_en"].apply(lambda x: translator.translate(x,lang_tgt='zh'))
#missing_2018["text_de"] = missing_2018["text_en"].apply(lambda x: translator.translate(x,lang_tgt='de'))
#missing_2018["text_pt"] = missing_2018["text_en"].apply(lambda x: translator.translate(x,lang_tgt='pt'))



import goslate
gs = goslate.Goslate()

missing_2018["text_es"] = missing_2018["text_it"].apply(lambda x: gs.translate(x,'es'))
missing_2018["text_fr"] = missing_2018["text_en"].apply(lambda x: gs.translate(x,'fr'))
missing_2018["text_zh"] = missing_2018["text_en"].apply(lambda x: gs.translate(x,'zh'))

#missing_2018.to_csv("missing_2018.csv", index=False)

missing_2018["text_de"] = missing_2018["text_en"].apply(lambda x: gs.translate(x,'de'))
missing_2018["text_pt"] = missing_2018["text_en"].apply(lambda x: gs.translate(x,'pt'))




dataset_merged = pd.concat([dataset_2018, missing_2018])

dataset_merged["month_string"] = np.where(dataset_merged["month"] == 2, "February", dataset_merged["month_string"]) 
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 3, "March", dataset_merged["month_string"]) 
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 4, "April", dataset_merged["month_string"]) 
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 5, "May", dataset_merged["month_string"]) 
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 6, "June", dataset_merged["month_string"])
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 7, "July", dataset_merged["month_string"]) 
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 9, "August", dataset_merged["month_string"]) 
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 10, "October", dataset_merged["month_string"]) 
dataset_merged["month_string"] = np.where(dataset_merged["month"] == 12, "December", dataset_merged["month_string"]) 



dataset_merged = dataset_merged.sort_values(by=["month", "day"])




dataset_merged.to_json("trevignano2018.js",orient="records")






