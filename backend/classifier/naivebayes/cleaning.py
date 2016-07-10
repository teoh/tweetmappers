import re

from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


negation_words = set(['hardly', 'lack', 'lacking', 'lacks', 'neither', 'nor', 'never', 'no', 'nobody', 'none', 'nothing', 'nowhere', 'not', 'without', 'aint', 'cant', 'cannot', 'darent', 'dont', 'doesnt', 'didnt', 'hadnt', 'hasnt', 'havent', 'havnt', 'isnt', 'mightnt', 'mustnt', 'neednt', 'oughtnt', 'shant', 'shouldnt', 'wasnt', 'wouldnt'])
stopword_list = [s for s in stopwords.words('english') if s not in negation_words]

def handle_negation(tokens):
	negate = False
	treated_tokens = []
	for token in tokens:
		if re.match(r"""[.\?!,]+$""", token):
			negate = False
			continue
		if token in negation_words:
			negate = True
		elif negate:
			treated_tokens.append('not_' + token)
		else:
			treated_tokens.append(token)

	return treated_tokens



def get_legit_tokens(tweet_str, tknzr):
	raw_tokens = tknzr.tokenize(tweet_str)
	stemmer = SnowballStemmer("english")

	legit_tokens = [w.replace("'", "") for w in raw_tokens if not re.search(r"""[^a-z.!\?,\']""", w) and w not in stopword_list]
	treated_tokens = handle_negation(legit_tokens)

	return [stemmer.stem(w) for w in treated_tokens]


def batch_get_legit_tokens(tweet_str_list):
	tknzr = TweetTokenizer(strip_handles=1,reduce_len=1,preserve_case=0)

	return [get_legit_tokens(tweet, tknzr) for tweet in tweet_str_list]

