import re
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


def get_legit_tokens(tweet_str,
					tknzr,
					legit_word_re,
					stopword_list):
	raw_tokens = tknzr.tokenize(tweet_str)
	stemmer = SnowballStemmer("english")
	return [stemmer.stem(re.sub(r"""[^a-z\-]""",'',w)) for w in raw_tokens if legit_word_re.match(w) and w not in stopword_list]


def batch_get_legit_tokens(tweet_str_list):
	tknzr = TweetTokenizer(strip_handles=1,reduce_len=1,preserve_case=0)
	stopword_list = stopwords.words('english')
	legit_word_re = re.compile(r"""[a-z]+(\-[a-z]+)?[.!\?,]*$""")

	return [get_legit_tokens(tweet,
					tknzr,
					legit_word_re,
					stopword_list) for tweet in tweet_str_list]