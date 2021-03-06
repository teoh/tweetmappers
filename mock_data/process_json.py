import json
from pprint import pprint
import time
import random

from repustate import Client
repustate_client = Client(api_key='61f177d260b047b2626537561dc9920c305cb242', version='v3')

def strip_non_ascii(text):
	new_text = [c for c in text if ord(c) < 128]
	return ''.join(new_text)

def get_sentiment(text):
    return repustate_client.sentiment(strip_non_ascii(text))['score']
    # return random.uniform(-1.0, 1.0)

class Tweet(object):

	def __init__(self, tid_, text_, location_str_, label_):
		self.tid = tid_
		self.text = text_
		self.location_str = location_str_
		self.label = label_


def treat_quotes(input_file):

	output_file = input_file.replace('.json', '_treated.json')
	target = open(output_file, 'w')

	with open(input_file) as f:
		lines = f.readlines()
		# for each line:
		# "key": "value with "some" "double" "quotes" inside",
		# "key": "value with \"some\" \"double\" \"quotes\" inside",
		for line in lines:
			if '": "' in line:
				entry = line.split('": "')
				key = entry[0]
				value = entry[1]
				end = -3 if '",\n' in value else -2
				value = value[:end]
				value = value.replace('"', '\\"')
				target.write(key + '": "' + value + ('",\n' if end==-3 else '"\n'))
			else:
				if line[0] in ['{', ' ', '}']:
					target.write(line)

	return output_file
	
def parse_json(input_file):
	with open(input_file) as data_file:
	    return json.load(data_file)


def get_tweets(data):
	tweets = []
	for d in data['statuses']:
		# print json.dumps(d, indent=4)
		tid = d.pop('id', 0)
		text = strip_non_ascii(d.pop('text', {})).replace('\n', ' ')
		user = d.pop('user', {})
		location_str = user.pop('location', '')
		label = 0
		tweets.append(Tweet(tid, text, location_str, label))

	return tweets

def process_tweets(candidate):
	treated_file = treat_quotes('tweets_%s.json' % candidate)
	data = parse_json(treated_file)

	with open('tweets_%s.txt' % candidate, 'w') as f:
		id_set = set()  # Avoid duplicates
		for tweet in get_tweets(data):
			if tweet.tid not in id_set:
				f.write(tweet.text + '\n')
				id_set.add(tweet.tid)
		print "Number of distinct tweets processed = ", len(id_set)


def classify_tweets(candidate):

	with open('tweets_%s.txt' % candidate, 'r') as r:
		with open('classified_tweets_%s.csv' % candidate, 'w') as w:
			tweets = r.readlines()
			for tweet in tweets:
				score = get_sentiment(tweet)
				w.write('"%f","%s"\n' % (score, tweet[:-1]))


start = time.time()
classify_tweets('trump')
print "Done, time elapsed (s) = ", time.time() - start


