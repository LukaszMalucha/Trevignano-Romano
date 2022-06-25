# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np
from google_trans_new import google_translator



dataset = pd.read_csv("may_cleaned.csv", encoding="utf-8")

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



# ITALIAN
dataset["text_it"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 12)), "Amati figli miei, grazie per essere qui nella preghiera e per aver ascoltato la mia chiamata nel vostro cuore. Figli miei, i tempi in cui andate incontro saranno di dolore, questo è il motivo per cui Io tocco la terra, per poter riunire tutti i miei figli sparsi in tutto il mondo, vi prego figli abbiate pietà del mio Gesù, che più di prima viene bestemmiato e trattato male, questo comportamento continua a flagellarlo senza alcuna pietà. Amati figli, presto arriverà un uomo che sarà osannato dai potenti di tutte le nazioni, ma lui sarà l’anticristo, questo tempo è ormai vicino, la persecuzione avrà inizio in tutte le parti del mondo, ma non temete perché Io sarò sempre con voi per proteggervi. Figli miei, non abbiate paura della verità e della vostra fede, raccomando di seguire sempre il Santo Vangelo. Oggi scenderanno grazie su di voi. Vi lascio con la mia benedizione materna nel nome del Padre, del Figlio e dello Spirito Santo, Amen.", dataset['text_it'])
dataset["text_it"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 13)), "Amati figli miei, grazie per essere qui nella preghiera in questo giorno molto speciale. Figli amati, cosi come a Fatima, oggi vi chiedo di convertirvi al più presto perché ormai il tempo è nella sua conclusione. Figli miei, oggi avete consolato il mio Santissimo Cuore con la preghiera e con la vostra fede, che chiedo di mantenere sempre salda, ed Io, vi prometto la mia santa protezione. Ora vi benedico nel nome del Padre, del Figlio e dello Spirito Santo, Amen.", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 18)), 'Figli miei, grazie per essere qui nella preghiera e per aver ascoltato la mia chiamata nel vostro cuore. Figli amati, non attendete gli ultimi momenti, ma afferrate le mie mani e fatevi portare dove non c’è iniquità, orgoglio e superbia. Figli, la terra presto subirà la più grande purificazione, le acque invaderanno la Terra e il fuoco scenderà dal cielo, abbiate coraggio nella fede e sottomettetevi a Gesù vostro Dio, la salvezza sarà per il mio popolo, non temete, ma siate pronti. Pregate per la Chiesa, da lì sono arrivate le divisioni e dico loro: PENTITEVI prima che sia troppo tardi, ed è per questo che Gesù soffre. Pregate figli miei, perché le guerriglie saranno sempre più forti, pregate per i sacerdoti santi perché ne avranno molto bisogno. Ora vi lascio con la mia santa benedizione nel nome del Padre, del Figlio e dello Spirito Santo, amen.', dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 22)), 'Figli amati, grazie per essere qui nella preghiera e per avere ascoltato la mia chiamata nel vostro cuore. Figli miei, quanto soffro nel vedere i miei figli prediletti accettare le leggi di satana. A volte anche i credenti si sono lasciati coinvolgere in questa lotta contro Dio, ma credete di saperne più di Dio? Credete di poter ricevere tutte le grazie solo per aver pregato distrattamente senza aprire il vostro cuore? Figli amati, nelle apparizioni vi ho preparati per questo momento, ma non sono stata ascoltata, anzi derisa e accusata di oscurare mio Figlio Gesù; ma Gesù, mentre stava sulla croce, non disse che sarei stata vostra Madre? Perché rinnegate tutto ciò che accaduto? Cosa vi è successo figli miei, piccoli miei? Eppure Dio è più forte di satana, ma voi preferite vivere nel mondo senza alcun sacrificio. Figli, pregate per la Chiesa e per i sacerdoti, perché dovranno affrontare il male. Domani, durante la messa se avrete il cuore aperto scenderà lo Spirito Santo su di voi. Pregate per il Venezuela. Ora vi lascio con la mia materna benedizione nel nome del Padre, del Figlio e dello Spirito Santo, Amen.', dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 25)), 'Fratelli miei, grazie per essere qui nella preghiera. Oggi vorrei ricordarvi: Io assisto a tutte le messe, sento un forte dolore quando mi infliggete continuamente, quando vedo molti dei miei figli, soprattutto i miei prediletti, profanare il mio corpo con la mancanza di rispetto, prendendo Me con le vostre mani sudicie, Io in quel momento vi guardo e piango, piango tanto. Arriverà la carestia e altri virus peggiori, ma se non vi affiderete a Me, e se non prenderete le mani della mia Santissima Madre, dove andrete da soli?  Tutto vi è stato rivelato, ma siete ciechi e sordi. Un forte vento spazzerà questo virus, vi chiedo di pregare la divina misericordia, altrimenti un altro virus terribile vi colpirà e non ci sarà alcuna cura. Pregate affinché non vi venga tolta l’Eucarestia. Ascoltate la verità gridata dal pulpito di una collina Benedetta del Padre mio e la vostra vita insieme al vostro corpo brilleranno di luce immensa. “Gesù mi invita a leggere la seconda lettera di Giovanni.  cap. 1 ” Ora vi benedico nel nome del Padre, nel Mio nome e dello Spirito Santo. Il vostro Gesù.', dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 29)), 'Cari figli, grazie per aver ascoltato la mia chiamata nel vostro cuore. Figli amati, avete accettato la conoscenza come vostra salvezza, ma pochi hanno creduto nell’unica vera medicina, che è Dio e la Fede, vi hanno fatto assaggiare il frutto della perdizione, facendovi credere che sia la vostra   unica salvezza. Così come accadde un tempo, siete caduti nella tentazione e nella trappola infernale. Ricordate figli: la Croce salva. Figli, pregate per la Chiesa dove si è chiusa la parola di Dio a causa dei miei figli prediletti che con arroganza e superbia non credono alle apparizioni e ai miei consigli, ma credono all’unico dio, quello di loro stessi e non riconoscono più la mia presenza. Amati figli, pregate perché la terra presto si ribellerà. Figli, oggi gli angeli vi osservano dal cielo. Ormai la confusione è tra i politici e tra voi fratelli, solo la preghiera potrà liberarvi da queste catene. Ora vi lascio con la mia benedizione materna nel nome del Padre, del Figlio e dello Spirito Santo, Amen.', dataset["text_it"])

# ENGLISH

dataset["text_en"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 1)), "Dear children, thank you for having responded to my call in your hearts. Beloved children, you have been warned of all that is to come, I only ask you to grasp my hands without any fear, you know what you are facing in these times, violence, blasphemy and confusion are already in the world, but for you it is time to witness and accept the Holy Spirit. Children, today your tenacity will be repaid with multitudes of graces.  Now I bless you in the name of the Father and the Son and the Holy Spirit, Amen." , dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 3)), "Dear children, thank you for listening to my call in your hearts and thank you for bending your knees. Beloved children, you are in the midst of a spiritual battle that humanity has never experienced. My children, be steadfast in faith and pray, pray much to be ready when the time comes. Remember that tribulations will be part of these times, but do not forget that the greater the suffering, the greater the graces will be. My children, the war between good and evil is on earth, as it was in heaven, but you must not fear because whoever asks for His help will have Him as the first consoler, love and the One who is victorious and you together with Him. Do not feed the darkness, but convert quickly, time is at its end. Wherever Jesus will call you, go without hesitation and nothing will be lacking; be prophets of these times, go and preach the infinite love of God, including mine as Mother. My children, many will be the graces that will descend here today. Always have the courage of Faith. Everything is ready for my little remnant. Remember that if God allows all this, it is to give you the possibility to always choose with free will. Now I give you my motherly blessing in the name of the Father and the Son and the Holy Spirit, Amen." , dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 8)), "Cenacle in Poland. Beloved children, thank you for being here in prayer and for listening to my call in your hearts. Beloved children, I ask you to pray for Eastern Europe, because your sufferings will come from there, I ask all mankind and all nations to kneel often and to make sacrifices, this will be your only salvation. I ask you beloved children, you must never fear, as long as you are steadfast in faith. I will send this daughter of mine wherever possible to open your hearts and for your conversion, for there is no more time. Everything is ready for you. My children, remember that you are in the world, but you are not of the world. Now I leave you with my motherly blessing in the name of the Father, the Son and the Holy Spirit, Amen. Many will be the graces that will descend upon you today." , dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 12)), "My beloved children, thank you for being here in prayer and for listening to My call in your heart. My children, the times you are going through will be times of sorrow, this is why I am touching the earth, so that I can gather all my children scattered all over the world, I beg you children to have mercy on my Jesus, who more than before is blasphemed and treated badly, this behavior continues to scourge him without any mercy. Beloved children, soon a man will come who will be hailed by the powerful of all nations, but he will be the antichrist, this time is near, the persecution will begin in all parts of the world, but do not fear because I will always be with you to protect you. My children, do not be afraid of the truth and of your faith, I recommend that you always follow the Holy Gospel. Today graces will descend upon you. I leave you with my motherly blessing in the name of the Father and the Son and the Holy Spirit, Amen." , dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 13)), "My beloved children, thank you for being here in prayer on this very special day. Beloved children, just as in Fatima, today I ask you to convert as soon as possible because time is now in its conclusion. My children, today you have consoled my Most Holy Heart with prayer and with your faith, which I ask you to keep always firm, and I promise you my holy protection. Now I bless you in the name of the Father and the Son and the Holy Spirit, Amen." , dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 18)), "My children, thank you for being here in prayer and for listening to my call in your hearts. Beloved children, do not wait for the last moments, but grasp my hands and let me take you where there is no iniquity, pride and arrogance. My children, the earth will soon undergo the greatest purification, the waters will invade the earth and fire will come down from heaven, have courage in faith and submit to Jesus your God, salvation will be for my people, do not fear, but be ready. Pray for the Church, from there the divisions came and I say to them, repent before it is too late, and that is why Jesus suffers. Pray my children, because the fights will be getting stronger, pray for the holy priests because they will be in great need. Now I leave you with my holy blessing in the name of the Father and the Son and the Holy Spirit, Amen." , dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 22)), "Beloved children, thank you for being here in prayer and for listening to my call in your hearts. My children, how much I suffer to see my beloved children accept the laws of Satan. Sometimes even believers have become involved in this struggle against God, but do you think you know better than God? Do you think you can receive all the graces just because you prayed absent-minded without opening your heart? Beloved children, in the apparitions I prepared you for this moment, but I was not listened to, rather I was mocked and accused of obscuring my Son Jesus; but did not Jesus say while He was on the cross that I would be your Mother? Why do you deny all that has happened? What has happened to you, my children? Yet God is stronger than Satan, but you prefer to live in the world without any sacrifice. My children, pray for the Church and for priests, for they will have to face evil. Tomorrow, during Mass, if you have an open heart, the Holy Spirit will descend upon you. Pray for Venezuela. Now I leave you with my motherly blessing in the name of the Father and the Son and the Holy Spirit, Amen." , dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 25)), "My brothers, thank you for being here in prayer. Today I would like to remind you: I attend all Masses, I feel a strong pain when you continually inflict Me, when I see many of My children, especially My beloved ones, defiling My body with disrespect, taking Me with your filthy hands, I at that moment look at you and weep, I weep so much. Famine and other worse viruses will come, but if you do not entrust yourselves to Me, and if you do not take the hands of My Most Holy Mother, where will you go alone?  All has been revealed to you, but you are blind and deaf. A strong wind will sweep this virus, I ask you to pray to the divine mercy, otherwise another terrible virus will strike you and there will be no cure. Pray that the Eucharist will not be taken away from you. Listen to the truth shouted from the pulpit of a blessed hill of My Father and your life together with your body will shine with immense light. Jesus invites me to read the second letter of John. ch. 1. Now I bless you in the name of the Father, My name and the Holy Spirit. Your Jesus." , dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 29)), "Dear children, thank you for listening to my call in your hearts. Beloved children, you have accepted knowledge as your salvation, but few have believed in the only true medicine, which is God and Faith; they have made you taste the fruit of perdition, making you believe that it is your only salvation. Just as it happened in the past, you have fallen into temptation and into the infernal trap. Remember my children: the Cross saves. My beloved children, pray for the Church where the word of God has been closed because of my beloved children who, with arrogance and pride, do not believe in apparitions and my counsels, but believe in the self-made god and no longer recognize my presence. Beloved children, pray because the earth will soon wake up. My children, today the angels are watching you from heaven. By now there is confusion among politicians and among you brothers, only prayer will be able to free you from these chains. Now I leave you with my motherly blessing in the name of the Father and the Son and the Holy Spirit, Amen." , dataset["text_en"])
# POLISH

dataset["text_pl"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 1)), "Drogie dzieci, dziękuję wam, że odpowiedzieliście na moje wezwanie w waszych sercach. Umiłowane dzieci, zostaliście ostrzeżeni przed tym wszystkim, co ma nadejść, proszę was tylko, abyście bez lęku trzymali mnie za rękę. Wiecie, co was czeka w tych czasach, przemoc, bluźnierstwo i zamieszanie są już na świecie, ale dla was nadszedł czas, aby dać świadectwo i przyjąć Ducha Świętego. Moje dzieci, dzisiaj wasza wytrwałość zostanie wynagrodzona wieloma łaskami. A teraz błogosławię was w imię Ojca i Syna i Ducha Świętego, Amen." , dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 3)), "Drogie dzieci, dziękuję wam, że słuchacie mojego wołania w waszych sercach i dziękuję wam, że uklękneliście. Umiłowane dzieci, jesteście w samym środku duchowej walki, jakiej ludzkość nigdy nie doświadczyła. Dzieci moje, bądźcie wytrwałe w wierze i módlcie się, módlcie się mocno, abyście byli gotowi, gdy nadejdzie czas. Pamiętajcie, że uciski będą częścią tych czasów, ale nie zapominajcie, że im większe cierpienia, tym większe łaski. Dzieci moje, wojna między dobrem a złem toczy się na ziemi, tak jak kiedyś w niebie, ale nie lękajcie się, bo kto prosi Go o pomoc, będzie miał Go jako pierwszego pocieszyciela, miłość i Tego, który zwycięża, a wy razem z Nim. Nie karmcie ciemności, ale nawracajcie się szybko, czas się kończy. Gdziekolwiek Jezus was wezwie, idźcie bez wahania, a niczego wam nie zabraknie; bądźcie prorokami tych czasów, idźcie i głoście nieskończoną miłość Boga, także moją jako Matki. Dzieci moje, wiele będzie łask, które tu dzisiaj zstąpią. Zawsze miejcie odwagę wiary. Wszystko jest gotowe dla Mojego małej resztki. Pamiętaj, że jeśli Bóg pozwala na to wszystko, to po to, żeby dać ci możliwość zawsze wybierać z wolną wolą. Teraz daję wam moje matczyne błogosławieństwo w imię Ojca i Syna i Ducha Świętego, Amen." , dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 8)), "Wieczernik w Polsce. Drogie kochane dzieci, dziękuję wam, że jesteście tutaj na modlitwie i że usłyszeliście moje wezwanie w waszych sercach. Umiłowane dzieci, proszę was o modlitwę za Europę Wschodnią, ponieważ stamtąd przyjdą wasze cierpienia, proszę całą ludzkość i wszystkie narody, aby często klękały i składały ofiary, to będzie waszym jedynym ratunkiem. Proszę was, umiłowane dzieci, nie lękajcie się, dopóki jesteście mocni w wierze. Poślę tę moją córkę wszędzie, gdzie to możliwe, aby otworzyła wasze serca i abyście się nawrócili, bo nie ma już czasu. Wszystko jest dla Ciebie gotowe. Dzieci moje, pamiętajcie, że jesteście na świecie, ale nie jesteście ze świata. Teraz zostawiam was z moim matczynym błogosławieństwem w imię Ojca i Syna i Ducha Świętego, Amen. Wiele będzie łask, które dziś na was zstąpią." , dataset["text_pl"])

dataset["text_pl"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 12)), "Moje kochane dzieci, dziękuję wam, że jesteście tutaj na modlitwie i że słuchacie mojego wołania w waszych sercach. Dzieci moje, czasy, które przeżywacie, będą smutne, dlatego dotykam ziemi, aby zgromadzić wszystkie moje dzieci rozproszone po całym świecie, błagam was, dzieci, miejcie litość nad moim Jezusem, który jest bluźniony i jest traktowany gorzej niż kiedyś, to zachowanie nadal go dręczy bez żadnej litości. Umiłowane dzieci, wkrótce przyjdzie człowiek, który będzie wychwalany przez potężnych wszystkich narodów, ale on będzie antychrystem, ten czas jest bliski, prześladowania zaczną się we wszystkich częściach świata, ale nie bójcie się, bo ja zawsze będę z wami, aby was chronić. Dzieci moje, nie bójcie się prawdy i waszej wiary; polecam wam, abyście zawsze szli za świętą Ewangelią. Dziś zstąpią na was łaski. Zostawiam was z moim matczynym błogosławieństwem w imię Ojca i Syna i Ducha Świętego, Amen." , dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 13)), "Moje kochane dzieci, dziękuję wam, że jesteście tutaj na modlitwie w tym szczególnym dniu. Umiłowane dzieci, tak jak w Fatimie, tak i dzisiaj proszę was, abyście się jak najszybciej nawrócili, bo czas już się kończy. Dzieci moje, dzisiaj pocieszyłyście moje Najświętsze Serce modlitwą i waszą wiarą, o którą proszę was, abyście zawsze byli mocni, i obiecuję wam moją świętą opiekę. Teraz błogosławię was w imię Ojca i Syna i Ducha Świętego, Amen." , dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 18)), "Dzieci moje, dziękuję wam, że jesteście tutaj na modlitwie i że słuchacie mojego wołania w waszych sercach. Umiłowane dzieci, nie czekajcie na ostatnie chwile, ale chwyćcie mnie za ręce i pozwólcie mi zabrać was tam, gdzie nie ma nieprawości, pychy i arogancji. Moje dzieci, ziemia wkrótce przejdzie największe oczyszczenie, wody wtargną na ziemię, a ogień zstąpi z nieba, miejcie odwagę w wierze i poddajcie się Jezusowi, waszemu Bogu, zbawienie będzie dla mojego ludu, nie bójcie się, ale bądźcie gotowi. Módlcie się za Kościół, stamtąd przyjdą podziały i mówię wam: nawróćcie się, zanim będzie za późno, bo Jezus cierpi. Módlcie się moje dzieci, bo walki będą coraz silniejsze, módlcie się za świętych kapłanów, bo będą tego bardzo potrzebować. Teraz zostawiam was z moim świętym błogosławieństwem w imię Ojca i Syna i Ducha Świętego, Amen." , dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 22)), "Umiłowane dzieci, dziękuję wam, że jesteście tutaj na modlitwie i że słuchacie mojego wołania w waszych sercach. Moje dzieci, jak bardzo cierpię, kiedy widzę, jak moje ukochane dzieci przyjmują prawa szatana. Czasami nawet wierzący pozwolili sobie na zaangażowanie się w tę walkę z Bogiem, ale czy wierzysz, że wiesz więcej niż Bóg? Czy myślisz, że możesz otrzymać wszystkie łaski tylko dlatego, że modliłeś się roztargniony bez otwierania serca? Umiłowane dzieci, w objawieniach przygotowywałam was na tę chwilę, ale nie słuchano mnie, raczej wyśmiewano mnie i oskarżano o przesłanianie mojego Syna Jezusa; ale czyż Jezus nie powiedział, będąc na krzyżu, że będę waszą matką? Dlaczego zaprzeczasz wszystkiemu, co się wydarzyło? Co się z wami stało, moje dzieci? Bóg jest silniejszy niż szatan, ale wy jednak wolicie żyć w świecie bez żadnych zobowiązań. Dzieci moje, módlcie się za Kościół i za kapłanów, bo oni będą musieli stawić czoła złu. Jutro, podczas Mszy Świętej, jeśli masz otwarte serce, Duch Święty zstąpi na ciebie. Módlcie się za Wenezuelę. Teraz zostawiam was z moim matczynym błogosławieństwem w imię Ojca i Syna i Ducha Świętego, Amen." , dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 25)), "Moi bracia, dziękuję wam za waszą obecność na modlitwie. Dziś pragnę wam przypomnieć: uczestniczę we wszystkich mszach świętych, odczuwam silny ból, który nieustannie Mi zadajecie, gdy widzę, jak wiele Moich dzieci, zwłaszcza Moich umiłowanych, bezcześci Moje Ciało, bierze Mnie w swoje brudne ręce, patrzę na was w tym momencie i płaczę, bardzo mocno płaczę. Przyjdzie głód i inne gorsze wirusy. Jeśli nie powierzycie się Mnie, jeśli nie chwycicie rąk Mojej Najświętszej Matki, dokąd pójdziecie sami?  Wszystko zostało wam objawione, lecz wy jesteście ślepi i głusi. Silny wiatr zmiecie tego wirusa, proszę was o modlitwę do Miłosierdzia Bożego, inaczej uderzy w was kolejny straszny wirus i nie będzie na niego lekarstwa. Módlcie się, aby Eucharystia nie została wam odebrana. Słuchajcie prawdy głoszonej ze szczytu błogosławionego wzgórza Ojca Mego, a wasze życie wraz z ciałem będzie rozświetlone wielkim światłem. Jezus zaprasza mnie do przeczytania drugiego listu św. Jana. rozdz. 1. Teraz błogosławię was w imię Ojca i w Imię moje i w imię Ducha Świętego. Twój Jezus." , dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 5) & (dataset["day"] == 29)), "Drogie dzieci, dziękuję wam, że wsłuchaliście się w moje wołanie w waszych sercach. Umiłowane dzieci, przyjęliście wiedzę jako wasze zbawienie, lecz niewielu uwierzyło w jedyne prawdziwe lekarstwo, którym jest Bóg i wiara; oni sprawili, że zakosztowaliście owocu zatracenia, każąc wam wierzyć, że jest on waszym jedynym zbawieniem. Tak jak to miało miejsce w przeszłości, wpadliście w pokusę i w piekielną pułapkę. Pamiętajcie moje dzieci: Krzyż zbawia. Dzieci moje, módlcie się za Kościół, w którym słowo Boże zostało zamknięte z powodu moich ukochanych dzieci, które z arogancją i pychą nie wierzą w objawienia i moje rady, lecz wierzą w stworzonego przez siebie boga i nie uznają już mojej obecności. Umiłowane dzieci, módlcie się, bo ziemia wkrótce się zbuntuje. Moje dzieci, dzisiaj aniołowie patrzą na was z nieba. Tylko modlitwa będzie w stanie uwolnić cię z tych łańcuchów. Teraz zostawiam was z moim matczynym błogosławieństwem w imię Ojca i Syna i Ducha Świętego, Amen." , dataset["text_pl"])


translator = google_translator()  

dataset["text_es"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='es'))
dataset["text_fr"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='fr'))
dataset["text_zh"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='zh'))
dataset["text_de"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='de'))
dataset["text_pt"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='pt'))





dataset.to_csv("may_2021.csv", encoding="utf-8", index=False)




