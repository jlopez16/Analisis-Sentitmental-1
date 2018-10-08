# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 14:36:38 2018

@author: jlope
"""

from textblob import TextBlob
import re

positivo=0
negativo = 0
neutral = 0

def clean_tweet(tweet):
    '''
    Utility function to clean the text in a tweet by removing 
    links and special characters using regex.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analize_sentiment(tweet):
    '''
    Utility function to classify the polarity of a tweet
    using textblob.
    '''
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1
    
file = open('tweets_separados.txt','r')
file.seek(0)
tweets = file.read().splitlines()

tweets_minuscula=[]
for w in tweets:
    nodo = []
    nodo.append(w.lower())
    aux = analize_sentiment(w.lower())
    if aux == 1:
        positivo+=1
    elif aux == 0:
        neutral+=1
    else:
        negativo+=1
    nodo.append(aux)
    tweets_minuscula.append(nodo)
    
for x in tweets_minuscula:
    print(x[0])
    print(x[1])
    

print('Las estadìsticas son : ')
print("Positivos >> %d" % positivo)
print("Negativos >> %d" % negativo)
print("Neutros >> %d" % neutral)
print("Total >> %d" % (positivo+negativo+neutral))