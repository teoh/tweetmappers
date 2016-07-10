import nltk
import pickle

words_for_feature_extraction_pickle_path = './model/words_for_feature_extraction.p'

# ==== THIS IS FOR TRAINING =======
def get_all_words(list_of_token_lists):
	total_words = []
	for words in list_of_token_lists:
		total_words.extend(words)
	return total_words


def create_features(word_list):
	word_list = nltk.FreqDist(word_list)
	words_for_features = word_list.keys()
	pickle.dump(words_for_features,open(words_for_feature_extraction_pickle_path,'wb'))
	return words_for_features

# ====== BOTH TRAINING AND TESTING ======= 
def extract_features(tweet_token_list):
	words_for_features = pickle.load(open(words_for_feature_extraction_pickle_path))
	tweet_words = set(tweet_token_list)
	features = {}
	for w in words_for_features:
		features['contains(%s)' % w] = (w in tweet_words)
	return features