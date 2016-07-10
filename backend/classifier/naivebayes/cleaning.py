import re
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


negation_words = {'hardly', 'lack', 'lacking', 'lacks', 'neither', 'nor', 'never', 'no', 'nobody', 'none', 'nothing', 'nowhere', 'not', 'without', 'aint', 'cant', 'cannot', 'darent', 'dont', 'doesnt', 'didnt', 'hadnt', 'hasnt', 'havent', 'havnt', 'isnt', 'mightnt', 'mustnt', 'neednt', 'oughtnt', 'shant', 'shouldnt', 'wasnt', 'wouldnt'}

def handle_negation(tokens):
	negate = False
	treated_tokens = []
	for token in tokens:
		if token in negation_words:
			negate = True
		elif negate:
			treated_tokens.append('not_' + token)
		elif re.search("[.\?!,]", token):
			negate = False
	return treated_tokens


def get_legit_tokens(tweet_str,
					tknzr,
					legit_word_re,
					stopword_list):
	raw_tokens = tknzr.tokenize(tweet_str)
	stemmer = SnowballStemmer("english")
	legit_tokens = [stemmer.stem(re.sub(r"""[^a-z\-.!\?,]""",'',w)) for w in raw_tokens if legit_word_re.match(w)]
	treated_tokens = handle_negation(legit_tokens)
	return [stemmer.stem(re.sub(r"""[.!\?,]""",'',w)) for w in treated_tokens]


def batch_get_legit_tokens(tweet_str_list):
	tknzr = TweetTokenizer(strip_handles=1,reduce_len=1,preserve_case=0)
	stopword_list = stopwords.words('english')
	legit_word_re = re.compile(r"""[a-z]+(\-[a-z]+)?[.!\?,]*$""")

	return [get_legit_tokens(tweet,
					tknzr,
					legit_word_re,
					stopword_list) for tweet in tweet_str_list]