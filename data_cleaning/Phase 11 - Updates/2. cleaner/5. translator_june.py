# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np
from google_trans_new import google_translator



dataset = pd.read_csv("june_cleaned.csv", encoding="utf-8")

dataset["text_pl"] = ""
dataset["text_en"] = ""
dataset["text_it"] = ""

dataset["author"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 12)), "Holy Mary", dataset["author"] )
dataset["author"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 15)), "Jesus Christ", dataset["author"] )
dataset["author"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 19)), "Holy Mary", dataset["author"] )
dataset["author"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 22)), "Holy Mary", dataset["author"] )
dataset["author"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 26)), "Holy Mary", dataset["author"] )



# ITALIAN
dataset["text_it"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 1)), "Cari figli amati dal cielo, grazie per essere qui nella preghiera e grazie per aver ascoltato la mia chiamata nel vostro cuore. Figli miei, vi chiedo di seguire Dio che è amore, l’unico vero e infinito amore, siate voi uniti nel Suo amore, solo cosi tutto potrà essere slegato dalle trappole infernali. Figli miei, abbiate un cuore puro e potrete entrare nel regno dei cieli, infatti Io fui affidata a Giovanni, un ragazzo dal cuore di bambino, solo lui avrebbe potuto proteggere la grazia. Figli, abbiate fede in Dio e seguite i suoi comandamenti, non lasciatevi distrarre dalle cose del mondo, ma abbiate sempre lo sguardo rivolto al cielo. Ora vi benedico nel nome della Santissima Trinità, Amen.", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 3)), "Figli benedetti, grazie per essere qui nella preghiera e per aver ascoltato la mia chiamata nel vostro cuore. Figli miei se sapeste quanto è grande il mio amore di madre per voi!   Figli, Io sono qui a chiedere ancora la conversione del vostro cuore. Figli cari, siate vicini al mio cuore e a quello di mio Figlio Gesù, solo così avrete la salvezza. Figli miei, ormai la persecuzione è in atto, ma non dovete temere se siete in Cristo, perché nulla vi mancherà. La carestia si sentirà arrivare, eppure chi è con Gesù dovrà stare tranquillo. Figli miei, pregate affinché le chiese non vengano chiuse e affinché il cibo di vita eterna non vi sia tolto. Pregate per i miei figli prediletti (sacerdoti) e per coloro che Io ho chiamato per la salvezza dell’umanità, li riconoscerete dal volto dell’amore. Ora vi lascio con la mia benedizione materna, nel nome del Padre, del Figlio e dello Spirito Santo. Amen. La Madonna  era vestita di bianco e aveva in una mano il cuore di Gesù.", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 8)), "Cari figli, grazie per essere qui nella preghiera. Figli amati, vi chiedo spesso di essere fiamme accese per il mondo, ma a volte siete indifferenti. Figli, come disse Gesù ai suoi apostoli: che il vostro parlare sia si si, no no; il di più viene dal maligno. Convertitevi e fatevi trovare pronti per ciò che sta per arrivare. Figli amati,  non ragionate quando siete nella fede,  il ragionamento umano non arriverà  mai a capire ciò che Dio ha preparato per voi, a volte vi guardo mentre cercate date e tempi che solo Dio conosce, ma una cosa voglio svelarla: guardatevi  intorno, anche se a voi sembra un caso,  Io sto provvedendo ad avvicinarvi tutti, ricordate che non è una vostra decisione, ma la Mia. Vorrei che tutti i miei figli prediletti possano stare vicini per aiutarsi l’uno con l’altro per quando arriverà il momento e voglio mettervi insieme per combattere l’ultima battaglia. Figli miei, Dio ha preparato tutto per voi, nuovi cieli e nuova terra, dove ci sarà serenità e gioia, spariranno malattie e lamenti e tutto sarà preghiera e amore per Dio. Ora vi lascio con la mia santa benedizione nel nome del Padre, del Figlio e dello Spirito Santo, amen.", dataset["text_it"] )
dataset["text_it"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 12)), "Figli miei, grazie per essere qui nella preghiera. Figli, vi chiedo di ascoltare i miei consigli e la voce di mio Figlio, affinché possiate salvarvi. I miei profeti hanno scritto tanto e hanno parlato molto per la salvezza dell’umanità, ma non ascoltate. Alcuni dei miei figli prediletti (sacerdoti), sì sono allontanati da me e da Dio senza comprendere che questo non porterà alla salvezza, ma alla perdizione. Figli, pregate molto per questo mondo ormai ricoperto dalle tenebre, la luce della fede è molto flebile e quindi non si potrà più evitare il giudizio di Dio, che arriverà presto. Figli miei, vi chiedo amorevolmente di fare scorte perché la carestia è in arrivo e potreste trovarvi nella più totale disperazione. La provvidenza arriverà da ogni parte, non abbiate paura, fidatevi delle parole di Gesù e conservatele nel vostro cuore. Vivete questi messaggi, siate fedeli alla parola di Dio e al Vangelo. Il cuore di mio Figlio sanguina per i peccati dell’umanità, si salverà, chi fino alla fine dei tempi avrà ascoltato i miei richiami. Ricordate, Io vi amo tanto, chi è con Dio non dovrà temere nulla. Ora vi lascio con la mia benedizione materna nel nome del Padre, del Figlio e dello Spirito Santo, amen.", dataset["text_it"] )
dataset["text_it"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 15)), "Figli miei e fratelli miei amati, grazie per avere ascoltato il mio appello, mi avete consolato con la vostra presenza e con le vostre preghiere intense e dettate dal vostro cuore.  Guardate, oggi avete riempito la mia casa, quanto vorrei che tutte le chiese fossero così piene dei miei fratelli e di lodi e di canti, ma questo non accade più e il mio corpo spesso viene profanato.  Cari fratelli, siamo nel tempo della giustizia del Padre mio, pensavate che questo tempo non   arrivasse mai,  invece ecco ci siamo, vi chiedo di moltiplicare le preghiere perché prestissimo sentirete la terra ribellarsi e i mari agitarsi in tutto il mondo. Voi non mi avete creduto, ma avete ascoltato chi diceva che tutto avrebbe preso una piega diversa e tutto sarebbe tornato come prima, ma non è stato così, eppure continuate a non credere e a pensare  che la misericordia salva tutto, si è corretto, ma il Padre mio è stanco di tutta la malvagità umana, siete indifferenti a tutto e vi siete abituati anche alle cose più atroci,  perché avete lo sguardo rivolto solo alle cose terrene. Aprite gli occhi, siate coraggiosi e risvegliate le vostre coscienze addormentate. Fratelli miei, molti di voi che oggi hanno pregato con il cuore sentiranno scendere lo Spirito Santo. Ora vi lascio con la mia Santa benedizione nel nome del Padre nel mio Nome e dello Spirito Santo amen. Il vostro caro Gesù.", dataset["text_it"] )
dataset["text_it"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 19)), "Amati figli, grazie per essere qui nella preghiera e per aver ascoltato la mia chiamata nel vostro cuore. Figli, sento i vostri cuori turbati per questi tempi, c’è tanta confusione, allora vorrei darvi delle indicazioni per riconoscere quando mio Figlio Gesù arriverà tra voi e per capire meglio: quando sentirete guerre che scoppieranno in molti luoghi vicini e lontani, quando vedrete l’apostasia  dilagare nella chiesa,  dove i grandi teologi nascondono la verità  portando il gregge nel peccato, negando la giustizia di Dio; quando la carestia (scarsità di cibi alimentari)  sarà una delle tante notizie passate  inosservate, quando le epidemie si diffonderanno sull’umanità, quando i terremoti saranno forti, quando vedrete le acque invadere le città, quando vedrete  i segni del cielo che non avete mai visto, ecco, questi saranno i tempi maturi in cui  il Figlio di Dio, tornerà in tutta la sua gloria. Figli, queste sono le mie indicazioni, siate con il cuore   aperto a Dio affinché possiate sentire la sua voce, trovare conforto e comprendere il suo amore che è per ognuno di voi. Chi sarà fedele non dovrà temere nulla. Vi amo e vi i benedico nel nome del Padre, del Figlio e dello Spirito Santo, amen. Dopo l’apparizione di Maria Santissima, Gesù è passato tra noi, benedicendo uno per uno. Gloria al Re dei Re.", dataset["text_it"] )
dataset["text_it"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 22)), "Cari figli, grazie per avere ascoltato la mia chiamata nel vostro cuore. Amati figli, pregate, pregate, pregate, la guerra è alle porte, pregate per i potenti della terra affinché possano prendere decisioni diverse da quelle già stabilite. Pregate per l’America che verrà punita per avere accettato tutto ciò che è contro Dio. Ancora una volta vi dico: se nella vostra vita non c’è Dio e la preghiera non avrete speranze, innalzate Lodi e durante il giorno leggete la Bibbia. Amati figli miei, la massoneria ecclesiale vuole una chiesa unica, con una religione unica, la chiesa invece deve seguire le orme dei suoi padri, perché è santa, cattolica, apostolica,  fondata da Pietro, non riconoscono più Gesù vivo nell’Eucarestia e molti di loro conducono i miei figli tra le grinfie del demonio. Figli, ci sarà la persecuzione, anche a causa del nome di Gesù, ma chi ha fede non dovrà mai temere nulla perché Gesù sarà il vostro conforto e la vostra serenità ed Io che sono vostra Madre, proteggerò sempre il mio piccolo resto, insieme ai miei angeli. Ora vi lascio con la mia benedizione materna nel nome del Padre, del Figlio e dello Spirito Santo, amen.", dataset["text_it"] )
dataset["text_it"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 26)), "Amati figli miei, grazie per la preghiera e per aver risposto alla mia chiamata nel vostro cuore. Figli miei, vedo la gioia, i dolori e la fede nei vostri cuori. Figli miei ecco, Io vi unisco all’unisono per la nuova pentecoste, tutto ciò che arriverà servirà per purificare voi e la terra da ogni male, che purtroppo è sempre più forte in questi tempi, prendendo le menti e le anime di molti dei miei poveri figli. Cari figli miei, non abbiate mai paura, questo è il tempo dove molte saranno le malattie che arriveranno, ma è anche il tempo dove Gesù vi proteggerà, in particolare a coloro che hanno la vera fede, verrà un turbine (Lo Spirito Santo) che colpirà tutti i vostri cuori. Figli miei, pregate per la Russia, per l’America e la Cina. Ora vi lascio con la mia santa benedizione nel nome del Padre, del Figlio e dello Spirito Santo, Amen.", dataset["text_it"] )
dataset["text_it"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 29)), "Figli miei, grazie per essere qui nella preghiera e per aver risposto alla mia chiamata nel vostro cuore. Amati figli miei, i demoni stanno oscurando i cieli per oscurare le vostre menti.  Figli, questi tempi sono pronti per il verificarsi delle profezie che sono state rivelate in questi anni. Figli, pregate per la Chiesa perché presto una notizia eclatante verrà rivelata, la mia amata Chiesa è in piena confusione. Figli miei, pregate perché presto il mondo tremerà molto forte, affidatevi a Gesù, Lui non vi lascerà mai soli e pregate per Il mio cuore Immacolato che soffre molto. Ora vi benedico nel nome del Padre, del Figlio e dello Spirito Santo, Amen.", dataset["text_it"])


# ENGLISH
dataset["text_en"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 1)), "Dear beloved children of Heaven, thank you for being here in prayer and thank you for listening to my call in your hearts. My children, I ask you to follow God who is love, the only true and infinite love, be united in His love, only in this way can everything be freed from the traps of hell. My children, have a pure heart and you will be able to enter the Kingdom of Heaven, in fact I was entrusted to John, a boy with a child's heart, only he could have protected grace. My children, have faith in God and follow His commandments, do not let yourselves be distracted by the things of the world, but always have your eyes turned to Heaven. Now I bless you in the name of the Most Holy Trinity, Amen.", dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 3)), "Blessed children, thank you for being here in prayer and for listening to my call in your hearts. My children, if you only knew how great is my motherly love for you! My children, I am here still asking for the conversion of your hearts. Dear children, be close to my heart and to that of my Son Jesus, only in this way will you have salvation. My children, by now the persecution is underway, but you must not fear if you are in Christ, for nothing will be lacking. The famine will be felt coming, yet those who are with Jesus must rest assured. My children, pray that the churches will not be closed and that the food of eternal life will not be taken from you. Pray for my beloved children (priests) and for those whom I have called for the salvation of mankind; you will recognize them by the face of love. Now I leave you with my motherly blessing, in the name of the Father and the Son and the Holy Spirit. Amen. Our Lady was dressed in white and had the heart of Jesus in one hand.", dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 8)), "Dear children, thank you for being here in prayer. Beloved children, I often ask you to be bright flames for the world, but at times you are indifferent. My children, as Jesus said to His apostles: let your speech be yes yes, no no; more comes from the evil one. Convert and be ready for what is coming. Beloved children, do not reason when you are in the faith, human reasoning will never come to understand what God has prepared for you, sometimes I watch you while you look for dates and times that only God knows, but I want to reveal one thing: look around you, even if it seems to you to be a coincidence, I am providing to bring you all closer, remember that it is not your decision, but Mine. I want all My beloved children to be able to stay close to help each other for when the time comes and I want to put you together to fight the last battle. My children, God has prepared everything for you, new heavens and new earth, where there will be serenity and joy, sickness and lamentations will disappear and everything will be prayer and love for God. Now I leave you with my holy blessing in the name of the Father and the Son and the Holy Spirit, Amen.", dataset["text_en"] )
dataset["text_en"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 12)), "My children, thank you for being here in prayer. My children, I ask you to listen to my advice and to the voice of my Son, that you may be saved. My prophets have written much and spoken much for the salvation of mankind, but you do not listen. Some of my favorite sons (priests) have turned away from me and from God without understanding that this will not lead to salvation but to perdition. My children, pray a lot for this world which is now covered by darkness, the light of faith is very weak and therefore it will not be possible to avoid God's judgment, which will come soon. My children, I lovingly ask you to stock up because the famine is coming and you may find yourselves in total despair. Providence will come from everywhere, do not be afraid, trust the words of Jesus and keep them in your heart. Live these messages, be faithful to the word of God and the Gospel. The heart of my Son bleeds for the sins of mankind, he will be saved, who until the end of time will have listened to my calls. Remember, I love you so much, whoever is with God will have nothing to fear. Now I leave you with my motherly blessing in the name of the Father and the Son and the Holy Spirit, Amen.", dataset["text_en"] )
dataset["text_en"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 15)), "My beloved children and brothers, thank you for having listened to my call, you have consoled me with your presence and with your intense prayers dictated by your heart.  Look, today you have filled my house, how I wish all the churches were so full of my brothers and sisters and of praises and songs, but this does not happen anymore and my body is often desecrated.  Dear brothers, we are in the time of My Father's justice, you thought that this time would never come, but here we are, I ask you to multiply your prayers because very soon you will feel the earth rebel and the seas churn all over the world. You did not believe me, but you listened to those who said that everything would take a different turn and everything would go back to the way it was before, but it was not so, yet you continue not to believe and to think that mercy saves everything, it is correct, but my Father is tired of all human wickedness, you are indifferent to everything and you have become accustomed to even the most atrocious things, because you have your eyes turned only to earthly things. Open your eyes, be courageous and awaken your sleeping consciences. My brothers, many of you who have prayed with your hearts today will feel the Holy Spirit descending. Now I leave you with my Holy Blessing in the name of the Father, in my Name and the Holy Spirit, Amen. Your dear Jesus.", dataset["text_en"] )
dataset["text_en"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 19)), "Beloved children, thank you for being here in prayer and for listening to my call in your hearts. My children, I feel your hearts troubled by these times, there is so much confusion, so I would like to give you some indications to recognize when my Son Jesus will come among you and to understand better: when you hear wars breaking out in many places near and far, when you see apostasy running rampant in the church, where great theologians hide the truth leading the flock into sin, denying God's justice; when famine (food shortage) will be one of the many news items that have gone unnoticed, when epidemics will spread over humanity, when earthquakes will be strong, when you will see the waters invade the cities, when you will see the signs of heaven that you have never seen, behold, these will be the ripe times when the Son of God, will return in all His glory. My children, these are my indications, be with an open heart to God so that you may hear His voice, find comfort and understand His love that is for each one of you. Whoever is faithful will have nothing to fear. I love you and I bless you in the name of the Father, the Son and the Holy Spirit, Amen. After the apparition of Mary Most Holy, Jesus passed among us, blessing one by one. Glory to the King of Kings.", dataset["text_en"] )
dataset["text_en"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 22)), "Dear children, thank you for having listened to my call in your heart. Beloved children, pray, pray, pray, war is at the gates, pray for the powerful of the earth that they may make different decisions from those already established. Pray for America which will be punished for having accepted everything that is against God. Once again I say to you: if in your life there is no God and prayer you will have no hope, raise Lauds and during the day read the Bible. My beloved children, the ecclesiastical freemasonry wants a single church, with a single religion, the church instead must follow in the footsteps of its fathers, because it is holy, catholic, apostolic, founded by Peter, they no longer recognize Jesus alive in the Eucharist and many of them lead my children into the clutches of the devil. My children, there will be persecution, also because of the name of Jesus, but those who have faith will never have to fear anything because Jesus will be your comfort and your serenity and I, who am your Mother, will always protect my little remnant, together with my angels. Now I leave you with my motherly blessing in the name of the Father and the Son and the Holy Spirit, Amen.", dataset["text_en"] )
dataset["text_en"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 26)), "My beloved children, thank you for your prayers and for answering my call in your hearts. My children, I see the joy, the sorrows and the faith in your hearts. My children, behold, I unite you in unison for the new Pentecost, all that will come will serve to purify you and the earth from all evil, which unfortunately is growing stronger in these times, taking the minds and souls of many of my poor children. My dear children, never be afraid, this is the time where many diseases will come, but it is also the time where Jesus will protect you, especially to those who have the true faith, a whirlwind (The Holy Spirit) will come and strike all your hearts. My children, pray for Russia, for America and China. Now I leave you with my holy blessing in the name of the Father and the Son and the Holy Spirit, Amen.", dataset["text_en"] )
dataset["text_en"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 29)), "My children, thank you for being here in prayer and for answering My call in your hearts. My beloved children, demons are darkening the heavens to darken your minds.  My children, these times are ready for the fulfillment of the prophecies that have been revealed in these years. My children, pray for the Church because soon striking news will be revealed, my beloved Church is in complete confusion. My children, pray because soon the world will tremble very strongly, entrust yourselves to Jesus, He will never leave you alone and pray for my Immaculate Heart which suffers much. Now I bless you in the name of the Father and the Son and the Holy Spirit, Amen.", dataset["text_en"])


# POLISH
dataset["text_pl"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 1)), "Drogie ukochane dzieci Nieba, dziękuję wam, że jesteście tutaj na modlitwie i dziękuję wam, że słuchacie mojego wołania w waszych sercach. Dzieci moje, proszę was, naśladujcie Boga, który jest miłością, jedyną prawdziwą i nieskończoną miłością, bądźcie zjednoczeni w Jego miłości, tylko w ten sposób wszystko może być uwolnione z sideł piekła. Dzieci moje, miejcie serce czyste, a będziecie mogli wejść do Królestwa Niebieskiego; w rzeczywistości powierzono mnie Janowi, chłopcu o sercu dziecka, tylko on mógł ochronić łaskę. Dzieci moje, miejcie wiarę w Boga i postępujcie według Jego przykazań; nie dajcie się rozproszyć sprawom tego świata, ale zawsze miejcie wzrok zwrócony ku Niebu. Teraz błogosławię was w imię Trójcy Przenajświętszej, Amen.", dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 3)), "Błogosławione dzieci, dziękuję wam, że jesteście tutaj na modlitwie i że słuchacie mojego wołania w waszych sercach. Dzieci moje, gdybyście tylko wiedziały, jak wielka jest moja matczyna miłość do was! Dzieci moje, jestem tu nadal prosząc o nawrócenie waszych serc. Drogie dzieci, bądźcie blisko mojego serca i serca mojego Syna Jezusa, tylko w ten sposób dostąpicie zbawienia. Moje dzieci, teraz prześladowanie jest w toku, ale nie wolno wam się bać, jeśli jesteście w Chrystusie, bo niczego wam nie zabraknie. Głód będzie odczuwalny w nadchodzącym czasie, jednak ci, którzy są z Jezusem, mogą być spokojni. Dzieci moje, módlcie się, aby kościoły nie zostały zamknięte i aby pokarm życia wiecznego nie został wam odebrany. Módlcie się za moje ukochane dzieci (kapłanów) i za tych, których powołałam dla zbawienia ludzkości; poznacie ich po obliczu miłości. A teraz zostawiam was z moim matczynym błogosławieństwem, w imię Ojca i Syna i Ducha Świętego. Amen. Matka Boża była ubrana na biało, a w ręce trzymała Serce Jezusa.", dataset["text_pl"])       
dataset["text_pl"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 8)), "Drogie dzieci, dziękuję wam, że jesteście tutaj na modlitwie. Umiłowane dzieci, często proszę was, abyście byli rozpalonymi płomieniami dla świata, jednak czasami jesteście obojętni. Moje dzieci, jak powiedział Jezus do swoich apostołów: niech wasza mowa będzie tak, tak, nie, nie; więcej pochodzi od złego. Nawróćcie się i bądźcie gotowi na to, co nadchodzi. Umiłowane dzieci, nie próbujcie ogarnąć umysłem waszej wiary, ludzkie rozumowanie nigdy nie pozwoli wam zrozumieć tego, co Bóg dla was przygotował, czasami obserwuję was, gdy szukacie dat i godzin, które zna tylko Bóg, ale chcę wam objawić jedną rzecz: zobaczcie co się dzieje wokół was, nawet jeśli wydaje się wam to przypadkiem, Ja działam, aby was wszystkich zbliżyć, pamiętajcie, że to nie jest wasza decyzja, ale Moja. Chcę, aby wszystkie Moje ukochane dzieci mogły pozostać blisko siebie, aby pomagać sobie nawzajem, bo kiedy nadejdzie czas, chcę was połączyć, aby stoczyć ostatnią bitwę. Moje dzieci, Bóg przygotował dla was wszystko, nowe niebo i nową ziemię, gdzie będzie spokój i radość, znikną choroby i lamenty, a wszystko będzie modlitwą i miłością do Boga. Teraz zostawiam was z moim świętym błogosławieństwem w imię Ojca i Syna i Ducha Świętego, Amen.", dataset["text_pl"] )
dataset["text_pl"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 12)), "Dzieci moje, dziękuję wam, że jesteście tutaj na modlitwie. Dzieci moje, proszę was, abyście słuchali moich rad i głosu mojego Syna, abyście byli zbawieni. Moi prorocy wiele napisali i wiele przepowiadali dla zbawienia ludzkości, ale wy nie słuchacie. Niektórzy z moich ulubionych synów (kapłanów) odwrócili się ode mnie i od Boga, nie rozumiejąc, że to nie prowadzi do zbawienia, ale do zguby. Dzieci moje, dużo się módlcie za ten świat, który jest obecnie pogrążony w ciemnościach; światło wiary jest bardzo słabe i dlatego nie będzie już można uniknąć sądu Bożego, który wkrótce nadejdzie. Dzieci moje, z miłością proszę was, abyście się zaopatrzyli, ponieważ nadchodzi głód i możecie znaleźć się w całkowitej rozpaczy. Opatrzność przyjdzie ze wszystkich stron, nie bójcie się, zaufajcie słowom Jezusa i zachowajcie je w swoim sercu. Żyjcie tymi orędziami, bądźcie wierni Słowu Bożemu i Ewangelii. Serce mojego Syna krwawi za grzechy ludzkości, ten będzie zbawiony, kto będzie słuchał moich wezwań aż do końca czasów. Pamiętaj, tak bardzo cię kocham, kto jest z Bogiem, nie będzie się niczego obawiał. Teraz zostawiam was z moim matczynym błogosławieństwem w imię Ojca i Syna i Ducha Świętego, Amen.", dataset["text_pl"] )
dataset["text_pl"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 15)), "Moje kochane dzieci i bracia, dziękuję wam, że wysłuchaliście mojego wołania, że pocieszaliście mnie swoją obecnością i waszymi intensywnymi modlitwami płynącymi z waszego serca.  Popatrzcie, dziś napełniliście mój dom, jakże bym chciał, aby wszystkie kościoły były tak pełne moich braci, chwały i pieśni, ale to już się nie zdarza, a moje ciało jest często bezczeszczone.  Drodzy bracia, znajdujemy się w czasie sprawiedliwości Mojego Ojca, myśleliście, że ten czas nigdy nie nadejdzie, ale oto jesteśmy, proszę was, abyście pomnożyli swoje modlitwy, ponieważ wkrótce poczujecie, że ziemia się zbuntuje, a morza będą wzburzone na całym świecie. Nie uwierzyliście mi, lecz słuchaliście tych, którzy mówili, że wszystko przybierze inny obrót i wszystko wróci do poprzedniego stanu, lecz tak nie było, a jednak nadal nie wierzycie i uważacie, że miłosierdzie wszystko ocala, to prawda, lecz mój Ojciec jest zmęczony wszelką ludzką niegodziwością, jesteście obojętni na wszystko i przyzwyczailiście się nawet do najokropniejszych rzeczy, bo macie oczy zwrócone tylko na rzeczy ziemskie. Otwórzcie oczy, bądźcie odważni i obudźcie swoje śpiące sumienia. Bracia moi, wielu z was, którzy modliliście się dziś sercem, odczuje zstępowanie Ducha Świętego. Teraz zostawiam was z moim Świętym Błogosławieństwem w Imię Ojca, w moim Imieniu i Ducha Świętego, Amen. Wasz drogi Jezus.", dataset["text_pl"] )
dataset["text_pl"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 19)), "Drogie dzieci, dziękuję wam, że jesteście tutaj na modlitwie i że słuchacie mojego wołania w waszych sercach. Moje dzieci, czuję, że wasze serca są strapione tymi czasami pełnymi zamieszania, dlatego chciałabym dać wam kilka wskazówek, abyście mogli rozpoznać, kiedy mój Syn Jezus przyjdzie do was i lepiej zrozumieć: kiedy słyszysz, że w wielu miejscach blisko i daleko wybuchają wojny, kiedy widzisz, że w kościele szerzy się apostazja, gdzie wielcy teologowie ukrywają prawdę, prowadząc trzodę do grzechu, zaprzeczając Bożej sprawiedliwości; kiedy głód (niedostatek żywności) będzie jedną z wielu wiadomości, które przeszły niezauważone, kiedy epidemie rozprzestrzenią się nad ludzkością, kiedy trzęsienia ziemi będą silne, kiedy zobaczycie wody wdzierające się do miast, kiedy zobaczycie znaki na niebie, których nigdy nie widzieliście, oto będą to dojrzałe czasy, kiedy Syn Boży, powróci w całej swojej chwale. Moje dzieci, to są moje wskazania, miejcie serca otwarte na Boga, abyście mogli usłyszeć Jego głos, znaleźć pocieszenie i zrozumieć Jego miłość, która jest dla każdego z was. Kto jest wierny, nie będzie miał się czego obawiać. Kocham was i błogosławię was w imię Ojca i Syna i Ducha Świętego, Amen. Po objawieniu się Najświętszej Maryi Panny, Jezus przeszedł między nami, błogosławiąc nas po kolei. Chwała Królowi Królów.", dataset["text_pl"] )
dataset["text_pl"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 22)), "Drogie dzieci, dziękuję wam, że wsłuchaliście się w moje wołanie w waszych sercach. Umiłowane dzieci, módlcie się, módlcie się, módlcie się, wojna jest u bram, módlcie się za potężnych ziemi, aby mogli podjąć inne decyzje niż te, które już zostały ustalone. Módlcie się za Amerykę, która zostanie ukarana za to, że przyjęła wszystko, co jest przeciwne Bogu. Jeszcze raz mówię wam: jeśli w waszym życiu nie ma Boga i modlitwy, nie będziecie mieli nadziei, wznoście Jutrznię, a w ciągu dnia czytajcie Biblię. Moje kochane dzieci, masoneria kościelna chce jednego Kościoła, z jedną religią, Kościół natomiast musi podążać śladami swoich ojców, ponieważ jest święty, katolicki, apostolski, założony przez Piotra: nie uznają już Jezusa żywego w Eucharystii i wielu z nich prowadzi moje dzieci w szpony diabła. Moje dzieci, będą prześladowania, także z powodu imienia Jezusa, ale ci, którzy mają wiarę, nigdy nie będą musieli się niczego obawiać, ponieważ Jezus będzie waszym pocieszeniem i waszym ukojeniem, a ja, która jestem waszą Matką, zawsze będę chronić moją małą resztkę, razem z moimi aniołami. Teraz zostawiam was z moim matczynym błogosławieństwem w imię Ojca i Syna i Ducha Świętego, Amen.", dataset["text_pl"] )
dataset["text_pl"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 26)), "Moje kochane dzieci, dziękuję wam za modlitwę i za odpowiedź na moje wezwanie w waszych sercach. Moje dzieci, widzę w waszych sercach radość, smutek i wiarę. Moje dzieci, oto jednoczę was na nową Pięćdziesiątnicę, wszystko, co nadejdzie, posłuży do oczyszczenia was i ziemi z wszelkiego zła, które niestety w tych czasach jest coraz silniejsze, zabierając umysły i dusze wielu moich biednych dzieci. Moje drogie dzieci, nie bójcie się, to jest czas, w którym przyjdzie wiele chorób, ale jest to również czas, w którym Jezus będzie was chronił, szczególnie tych, którzy mają prawdziwą wiarę, przyjdzie wicher (Duch Święty) i uderzy we wszystkie wasze serca. Moje dzieci, módlcie się za Rosję, za Amerykę i Chiny. Teraz zostawiam was z moim świętym błogosławieństwem w imię Ojca i Syna i Ducha Świętego, Amen.", dataset["text_pl"] )       
dataset["text_pl"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 29)), "Dzieci moje, dziękuję wam, że jesteście tutaj na modlitwie i że odpowiadacie na Moje wezwanie w waszych sercach. Moje ukochane dzieci, demony przysłaniają niebiosa, aby zaciemnić wasze umysły.  Moje dzieci, te czasy są gotowe na wypełnienie się proroctw, które zostały objawione w tych latach. Moje dzieci, módlcie się za Kościół, ponieważ wkrótce zostaną ujawnione uderzające wieści, mój ukochany Kościół jest w całkowitym zamieszaniu. Moje dzieci, módlcie się, bo wkrótce świat zadrży bardzo mocno, powierzcie się Jezusowi, On nigdy nie zostawi was samych i módlcie się za moje Niepokalane Serce, które bardzo cierpi. Teraz błogosławię was w imię Ojca i Syna i Ducha Świętego, Amen.", dataset["text_pl"])       
       
translator = google_translator()  

# BROKEN

#dataset["text_es"] = dataset["text_it"].apply(lambda x: translator.translate(x,lang_tgt='es'))
#dataset["text_fr"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='fr'))
#dataset["text_zh"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='zh'))
#dataset["text_de"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='de'))
#dataset["text_pt"] = dataset["text_en"].apply(lambda x: translator.translate(x,lang_tgt='pt'))



import goslate
gs = goslate.Goslate()

dataset["text_es"] = dataset["text_it"].apply(lambda x: gs.translate(x,'es'))
dataset["text_fr"] = dataset["text_en"].apply(lambda x: gs.translate(x,'fr'))
dataset["text_zh"] = dataset["text_en"].apply(lambda x: gs.translate(x,'zh'))
dataset["text_de"] = dataset["text_en"].apply(lambda x: gs.translate(x,'de'))
dataset["text_pt"] = dataset["text_en"].apply(lambda x: gs.translate(x,'pt'))





dataset.to_csv("june_2021.csv", encoding="utf-8", index=False)















