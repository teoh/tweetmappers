import nltk

# ==== THIS IS FOR TRAINING =======
def get_all_words(list_of_token_lists):
	total_words = []
	for words in list_of_token_lists:
		total_words.extend(words)
	return total_words


def create_features(word_list):
	word_list = nltk.FreqDist(word_list)
	feats = word_list.keys()
	return feats