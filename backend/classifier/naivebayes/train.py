import nltk
import csv
from time import time as tt
import pickle

from cleaning import *
from features import *

trained_model_pickle_path = './model/classif_model.p'

def collect_tweets(candidate, raw_tweets, labels):
	with open('./data/%s_classified.csv' % candidate) as csvfile:
		trainreader = csv.reader(csvfile,delimiter=',',quotechar='"')
		for row in trainreader:
			label = float(row[0])
			if label != 0.0:
				raw_tweets.append(row[1])
				labels.append(1 if label > 0.0 else -1)

# ======================

# collect the tweets
print 'Collecting the tweets...'
raw_tweets = []
labels = []
collect_tweets('hillary', raw_tweets, labels)
collect_tweets('trump', raw_tweets, labels)

# clean the tweets 

t = tt()
print 'Cleaning the tweets...'
cleaned_tweets = batch_get_legit_tokens(raw_tweets)

# extract features

print 'Extracting the features...'
create_features(get_all_words(cleaned_tweets))

assert len(cleaned_tweets) == len(labels)

print 'Constructing training set...'
training_set = nltk.classify.apply_features(extract_features,zip(cleaned_tweets,labels))

# train model

print 'Training the model...'
classifier = nltk.NaiveBayesClassifier.train(training_set)
print tt() - t

# print classifier.show_most_informative_features()

tweet_str = 'RT @sunlorrie: Imagine if this had gone to a jury: Poll: 54 %% of Voters Think FBI Should have Criminally Indicted Hillary Clinton https://t'
tweet_ft = [ extract_features(t) for t in batch_get_legit_tokens([tweet_str]) ]
print classifier.classify( tweet_ft[0])

# output the representation

pickle.dump(classifier,open(trained_model_pickle_path,'wb'))