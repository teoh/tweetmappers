import sys
sys.path.insert(0, './classifier/naivebayes/')

from repustate import Client
import cleaning
import features
import pickle

model_pickle_path = './classifier/naivebayes/model/classif_model.p'


repustate_client = Client(api_key='61f177d260b047b2626537561dc9920c305cb242', version='v3')
classifier = pickle.load(open(model_pickle_path))

def strip_non_ascii(text):
	new_text = [c for c in text if ord(c) < 128]
	return ''.join(new_text)

def get_sentiment_api(text):
    return repustate_client.sentiment(strip_non_ascii(text))['score']

def get_sentiment_naive_bayes(text):
	return classifier.classify(features.extract_features(cleaning.get_legit_token_one_tweet(strip_non_ascii(text)), False))

def get_sentiment(text):
	return get_sentiment_naive_bayes(text)