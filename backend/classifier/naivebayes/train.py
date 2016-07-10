import nltk
import csv
from time import time as tt

from cleaning import *
from features import *

# ======================

# collect the tweets

raw_tweets = []
labels = []

with open('./data/hillary_sample.csv') as csvfile:
	trainreader = csv.reader(csvfile,delimiter=',',quotechar='"')
	for row in trainreader:
		raw_tweets.append(row[1])
		labels.append(row[0])


# clean the tweets 

t = tt()
cleaned_tweets = batch_get_legit_tokens(raw_tweets)

# extract features
word_features = create_features(get_all_words(cleaned_tweets))

print len(word_features)

print cleaned_tweets[0]

print extract_features(cleaned_tweets[0])

print tt() - t




# train model




# output the representation

print "hello"