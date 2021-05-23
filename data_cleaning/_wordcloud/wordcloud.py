# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:01:33 2021

@author: LukaszMalucha
"""



import pandas as pd

import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

dataset = pd.read_csv("MERGED.csv", encoding="utf-8")

dataset = dataset[dataset["author"] == "Holy Mary"]

dataset = dataset[["text_en"]]

# Remove greeting and last sentence

dataset["text_en"] = dataset["text_en"].str.split(".").str[1:-1].str.join(".")
dataset["text_en"] = dataset["text_en"].str.replace(" in the name of the Father and the Son and the Holy Spirit, Amen", "")
dataset["text_en"] = dataset["text_en"].str.replace("Now I leave you with my Motherly blessing", "")
dataset["text_en"] = dataset["text_en"].str.replace("in the name of the Father of the Son and of the Holy Spirit", "")
dataset["text_en"] = dataset["text_en"].str.replace(r'[^\w\s]', '')
dataset["text_en"] = dataset["text_en"].str.strip()
dataset["text_en"] = dataset["text_en"].str.split(" ")


greetings = {"I", "My", "daughter", "Beloved", "children", "ones", "things", "make", "name", "many", "The", "Dear", "little",
             "listening", "Blessing", "blessing", "beloved", 
             "dear", "Children", "Amen", "He", "As", "And", "Again",
             "But", "Not", "didnt", "doesnt", "dont", "100", "15th", "1730", "230", "300", "3rd", 
             
             }


def stopwords_check(lst):
    clean_lst = []
    for element in lst:
        if element not in set(stopwords.words('english')) and element not in greetings:
            clean_lst.append(element)
    return clean_lst        


dataset["text_en"] = dataset["text_en"].apply(lambda x: stopwords_check(x))        



word_list = dataset["text_en"].to_list()




word_cloud_lst = []

for lst in word_list:
    for element in lst:
        if len(element) > 2:              
            word_cloud_lst.append(element)
            
            
        


wordcloud = pd.DataFrame(word_cloud_lst, columns=["word"])
wordcloud["word"] = wordcloud["word"].str.replace("Gods", "God")
wordcloud["word"] = wordcloud["word"].str.replace("GOD", "God")
wordcloud["word"] = wordcloud["word"].str.replace("CONVERT", "convert")
wordcloud["word"] = wordcloud["word"].str.replace("NOW", "now")
wordcloud["word"] = wordcloud["word"].str.replace("asks", "ask")
wordcloud["word"] = wordcloud["word"].str.replace("battles", "battle")
wordcloud["word"] = wordcloud["word"].str.replace("believed", "believe")
wordcloud["word"] = wordcloud["word"].str.replace("believed", "believe")
wordcloud["word"] = wordcloud["word"].str.replace("believes", "believe")
wordcloud["word"] = wordcloud["word"].str.replace("believing", "believe")
wordcloud["word"] = wordcloud["word"].str.replace("blasphemes", "blaspheme")
wordcloud["word"] = wordcloud["word"].str.replace("bleeds", "bleed")
wordcloud["word"] = wordcloud["word"].str.replace("built", "build")
wordcloud["word"] = wordcloud["word"].str.replace("changed", "change")
wordcloud["word"] = wordcloud["word"].str.replace("changing", "change")
wordcloud["word"] = wordcloud["word"].str.replace("conversions", "conversion")
wordcloud["word"] = wordcloud["word"].str.replace("converted", "convert")
wordcloud["word"] = wordcloud["word"].str.replace("converting", "convert")
wordcloud["word"] = wordcloud["word"].str.replace("coredemptrix", "Coredemptrix")
wordcloud["word"] = wordcloud["word"].str.replace("created", "create")
wordcloud["word"] = wordcloud["word"].str.replace("creates", "create")
wordcloud["word"] = wordcloud["word"].str.replace("crucifying", "crucify")
wordcloud["word"] = wordcloud["word"].str.replace("deaths", "death")
wordcloud["word"] = wordcloud["word"].str.replace("died", "die")
wordcloud["word"] = wordcloud["word"].str.replace("diseases", "disease")
wordcloud["word"] = wordcloud["word"].str.replace("exits", "exit")
wordcloud["word"] = wordcloud["word"].str.replace("falsehoods", "falsehood")
wordcloud["word"] = wordcloud["word"].str.replace("fasts", "fast")
wordcloud["word"] = wordcloud["word"].str.replace("feels", "feel")
wordcloud["word"] = wordcloud["word"].str.replace("fills", "fill")
wordcloud["word"] = wordcloud["word"].str.replace("helps", "help")
wordcloud["word"] = wordcloud["word"].str.replace("hours", "hour")
wordcloud["word"] = wordcloud["word"].str.replace("priests", "priest")
wordcloud["word"] = wordcloud["word"].str.replace("protecting", "protect")
wordcloud["word"] = wordcloud["word"].str.replace("protection", "protect")
wordcloud["word"] = wordcloud["word"].str.replace("protects", "protect")
wordcloud["word"] = wordcloud["word"].str.replace("purifications", "purification")
wordcloud["word"] = wordcloud["word"].str.replace("rosaries", "rosary")
wordcloud["word"] = wordcloud["word"].str.replace("Churches", "Church")
wordcloud["word"] = wordcloud["word"].str.replace("Accepting", "accepting")
wordcloud["word"] = wordcloud["word"].str.replace("Abandon", "abandon")
wordcloud["word"] = wordcloud["word"].str.replace("Baptism", "baptism")
wordcloud["word"] = wordcloud["word"].str.replace("Benedict", "benedict")
wordcloud["word"] = wordcloud["word"].str.replace("Bishop", "bishop")
wordcloud["word"] = wordcloud["word"].str.replace("Blaspheming", "blaspheming")
wordcloud["word"] = wordcloud["word"].str.replace("Bride", "bride")
wordcloud["word"] = wordcloud["word"].str.replace("Catholics", "catholics")
wordcloud["word"] = wordcloud["word"].str.replace("Charity", "charity")
wordcloud["word"] = wordcloud["word"].str.replace("Choice", "choice")
wordcloud["word"] = wordcloud["word"].str.replace("Cities", "cities")
wordcloud["word"] = wordcloud["word"].str.replace("Cling", "cling")
wordcloud["word"] = wordcloud["word"].str.replace("Come", "come")
wordcloud["word"] = wordcloud["word"].str.replace("Archangels", "archangels")
wordcloud["word"] = wordcloud["word"].str.replace("Christians", "Christian")
wordcloud["word"] = wordcloud["word"].str.replace("churches", "Churches")
wordcloud["word"] = wordcloud["word"].str.replace("church", "Church")
wordcloud["word"] = wordcloud["word"].str.replace("Churches", "churches")


wordcloud.to_csv("wordcloud.csv", index=False)

unique = list(wordcloud["word"].unique())

words = list(wordcloud["word"])


occ_dict = {}

for item in words:
    if item not in occ_dict:
        occ_dict[item] = 1
    else:
        occ_dict[item] +=1
        
wordcloud_occurence = pd.DataFrame.from_dict(occ_dict, orient="index")   

wordcloud_occurence["word"] = wordcloud_occurence.index
wordcloud_occurence = wordcloud_occurence.reset_index(drop=True)
wordcloud_occurence["occurence"] = wordcloud_occurence[0]

wordcloud_occurence = wordcloud_occurence[["word", "occurence"]]
wordcloud_occurence["word"] = " " + wordcloud_occurence["word"] + " "

wordcloud_occurence.to_csv("wordcloud_occurence.csv", index=False)

single_occurence = []
for key, value in occ_dict.items():
    if value == 1:
        single_occurence.append(key)
        
    
    
    






















