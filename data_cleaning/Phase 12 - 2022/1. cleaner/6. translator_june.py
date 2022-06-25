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

#dataset["text_it"] = np.where(((dataset["month"] == 9) & (dataset["day"] == 3)), "", dataset["text_it"])



dataset = pd.read_csv("june_cleaned.csv", encoding="utf-8")




# ITALIAN
dataset["text_it"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 3)), "Cari figli, grazie per aver risposto alla mia chiamata nel vostro cuore. Figli miei, grazie per aver piegato le ginocchia durante la preghiera. Figli, attendete l’Avvertimento ,che è più vicino di quanto voi pensiate, ma attendetelo con grande gioia, l’amore di Dio vi farà vedere cose meravigliose, chi avrà paura è perché non si è ancora liberato dal peccato, nonostante il mio continuo richiamo. Figli miei, questo è il momento della vostra purificazione e dovete viverla con accettazione piena. Figli, vi prego, Io tocco ancora la terra perché vi voglio salvi. voi vivete i miei messaggi con umiltà, preghiera e fratellanza, sarete come il piccolo resto, che rimase vicino al mio Gesù, siate apostoli e abbiate il coraggio della fede. Ora vi lascio con la mia benedizione materna nel nome del Padre, del Figlio e dello Spirito Santo, amen. Sarò con voi fino alla fine della preghiera.", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 4)), "Figlia mia, nonostante le mie lacrime, continuate a vivere nell’indifferenza, anche i miei figli prediletti non hanno l’umiltà del silenzio e della contemplazione. Figli, piango perché Io so cosa arriverà a breve e voi continuate a vivere come se non conosceste la verità. Figli miei, nella Chiesa, sarà versato sangue. Pregate per i potenti perché vogliono portarvi alla morte. Il substrato della terra si riscalderà così tanto, che anche molti pesci del mare moriranno. Figli miei, tornate a Dio, vostra unica salvezza e convertitevi. Ora vi benedico, nel nome del Padre, del Figlio e dello Spirito Santo, amen.", dataset["text_it"])
dataset["text_it"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 7)), "Figli miei, grazie per aver risposto alla mia chiamata nel vostro cuore. Figli miei, la Chiesa Di Pietro sarà molto attaccata anche dall’interno, quanti sono i traditori! anche tra coloro che sono stati chiamati alla vocazione, ma che adesso tradiscono mio Figlio. Figli, la guerra continuerà e prenderà molti paesi, pregate per la Francia e per l’Italia, saranno coloro che subiranno molte perdite.  Pregate per l’America, perché sarà cancellata una buona parte di essa. Figli, vi chiedo di guardare sempre la luce di Dio, anche quando tutto sarà più difficile, non perdete mai la speranza. Pregate per coloro che hanno i cuori chiusi, affinché possano essere salvati durante l’Avvertimento, i tempi sono sempre più vicini. Pregate, perché anche i peggiori dei peccatori potrebbero salvarsi davanti al Re dei Re. Figli, fate attenzione, la carestia si diffonderà velocemente, così come altre malattie in arrivo. Figli, non barattate mai la vostra anima per un pezzo di pane, ascoltate le mie parole. Figli miei, tutto questo dolore smetterà, ma adesso abbiamo bisogno del vostro coraggio di soldati di luce che urlano la verità, non abbiate mai paura, Io sono qui per proteggervi. Guardate le variazioni climatiche, dal forte caldo ci sarà un forte freddo, dai tornadi si passerà alla forte grandine, abituatevi ai cambiamenti, perché saranno molteplici. Ora vi lascio con la mia benedizione materna nel nome del Padre, del Figlio e dello Spirito Santo, amen", dataset["text_it"])

#dataset["text_it"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 1)), "", dataset["text_it"])
#dataset["text_it"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 1)), "", dataset["text_it"])

# ENGLISH
dataset["text_en"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 3)), "Dear children, thank you for responding to my call in your hearts. My children, thank you for kneeling in prayer. My children, await the Warning ,which is closer than you think, but await it with great joy, God's love will show you wonderful things, those who will be afraid is because they have not yet freed themselves from sin, despite my continuous call. My children, this is the time of your purification and you must live it with full acceptance. Children, please, I still touch the earth because I want you to be saved. you live my messages with humility, prayer and brotherhood, you will be like the little remnant, who stayed close to my Jesus, be apostles and have the courage of faith. Now I leave you with my motherly blessing in the name of the Father and the Son and the Holy Spirit, Amen. I will be with you until the end of prayer.", dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 4)), "My child, despite My tears, you continue to live in indifference, even My beloved children do not have the humility of silence and contemplation. My children, I weep because I know what is coming soon and you continue to live as if you do not know the truth. My children, in the Church, blood will be shed. Pray for the powerful because they want to bring you to death. The subterranean earth will heat up so much that even many fish in the sea will die. My children, return to God, your only salvation, and be converted. Now I bless you, in the name of the Father and the Son and the Holy Spirit, Amen.", dataset["text_en"])
dataset["text_en"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 7)), "My children, thank you for responding to my call in your hearts. My children, the Church of Peter will also be much attacked from within, how many are the traitors! even among those who were called to vocational ministry but are now betraying my Son. My children, the war will continue and will take many countries, pray for France and Italy, they will be the ones who will suffer many losses.  Pray for America, for a good part of it will be wiped out. Children, I ask you to always look at God's light, even when everything will be more difficult, never lose hope. Pray for those whose hearts are closed, that they may be saved during the Warning, the times are getting closer. Pray, for even the worst of sinners may be saved before the King of kings. Children, be careful, famine will spread quickly, as will other coming diseases. Children, never barter your souls for a piece of bread, listen to my words. My children, all this pain will stop, but now we need your courage as soldiers of light shouting the truth, never be afraid, I am here to protect you. Watch the weather changes, from strong heat there will be strong cold, from tornadoes there will be strong hail, get used to the changes, for they will be manifold. Now I leave you with my motherly blessing in the name of the Father and the Son and the Holy Spirit, Amen.", dataset["text_en"])

#dataset["text_en"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 1)), "", dataset["text_en"])
#dataset["text_en"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 1)), "", dataset["text_en"])

# POLISH
dataset["text_pl"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 3)), "Drogie dzieci, dziękuję wam, że odpowiedzieliście na moje wezwanie w waszych sercach. Dzieci moje, dziękuję wam, że uklękliście do modlitwy. Dzieci moje, oczekujcie Ostrzeżenia, które jest bliżej, niż myślicie, oczekujcie go z wielką radością, miłość Boża sprawi, że zobaczycie cudowne rzeczy, bać będą się ci, którzy jeszcze nie uwolnili się od grzechu, mimo moich nieustannych wezwań. Moje dzieci, to jest czas waszego oczyszczenia i musicie go przeżyć z pełną akceptacją. Dzieci moje, błagam was, wciąż przebywam na ziemi, bo chcę, abyście byli zbawieni. Żyjąc moimi orędziami w pokorze, modlitwie i braterstwie, będziecie jak ta mała resztka, która pozostała blisko mojego Jezusa, będziecie apostołami i będziecie mieli odwagę wiary. Teraz zostawiam was z moim matczynym błogosławieństwem w imię Ojca i Syna i Ducha Świętego, Amen. Będę z wami aż do końca modlitwy.", dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 4)), "Moje dziecko, mimo moich łez nadal żyjesz w obojętności, nawet moje ukochane dzieci nie mają pokory milczenia i kontemplacji. Dzieci moje, płaczę, bo wiem, co wkrótce nadejdzie, a wy nadal żyjecie tak, jakbyście nie znali prawdy. Dzieci moje, w Kościele poleje się krew. Módlcie się za władców, bo oni chcą was doprowadzić do śmierci. Wnętrze Ziemi rozgrzeje się tak bardzo, że zginie nawet wiele ryb w morzu. Moje dzieci, powróćcie do Boga, waszego jedynego ratunku, i nawróćcie się. Teraz ja was błogosławię w imię Ojca i Syna i Ducha Świętego, Amen.", dataset["text_pl"])
dataset["text_pl"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 7)), "Dzieci moje, dziękuję wam, że odpowiedzieliście na moje wezwanie w waszych sercach. Dzieci moje, Kościół Piotrowy będzie również mocno atakowany od wewnątrz, jak wielu jest zdrajców, nawet wśród tych, którzy zostali powołani, a teraz zdradzają mojego Syna. Dzieci moje, wojna będzie trwała i zajmie wiele krajów, módlcie się za Francję i Włochy, to one poniosą wiele strat. Módlcie się za Amerykę, bo zostanie zmieciona z powierzchni ziemi. Dzieci moje, proszę was, abyście zawsze patrzyli na Boże Światło, nawet gdy wszystko będzie trudniejsze, nigdy nie traćcie nadziei. Módlcie się za tych, których serca są zamknięte, aby zostali zbawieni w czasie Ostrzeżenia, bo czasy się zbliżają. Módlcie się, aby nawet najgorsi grzesznicy mogli zostać zbawieni przed Królem królów. Dzieci, strzeżcie się, głód będzie się szybko rozprzestrzeniał, podobnie jak inne nadchodzące choroby. Moje dzieci, nie przehandlujcie waszych dusz za kawałek chleba, słuchajcie moich słów. Moje dzieci, cały ten ból się skończy, ale teraz potrzebujemy waszej odwagi jako żołnierzy światła, którzy wykrzykują prawdę, nigdy się nie bójcie, jestem tu, aby was chronić. Obserwuj zmiany klimatyczne: od silnych upałów do silnego zimna, od tornad do silnego gradu, przyzwyczajaj się do zmian, bo będzie ich wiele. Teraz zostawiam was z moim matczynym błogosławieństwem w imię Ojca i Syna i Ducha Świętego, Amen.", dataset["text_pl"])

#dataset["text_pl"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 1)), "", dataset["text_pl"])
#dataset["text_pl"] = np.where(((dataset["month"] == 6) & (dataset["day"] == 1)), "", dataset["text_pl"])


dataset = dataset[['year', 'month', 'day', 'author', 'text_it', 'month_string', 'text_pl','text_en']]

dataset_ready = pd.read_csv("june_2022.csv")


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


dataset.to_csv("june_2022.csv", encoding="utf-8", index=False)









