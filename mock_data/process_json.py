import json
from pprint import pprint

class Tweet(object):

	def __init__(self, text_, location_str_, label_):
		self.text = text_
		self.location_str = location_str_
		self.label = label_


	def print_tweet(self):
		print self.text
		print 'Location = ' + self.location_str
		print '########################################################################################################################'


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
		text = d.pop('text', {})
		user = d.pop('user', {})
		location_str = user.pop('location', '')
		label = 0
		tweets.append(Tweet(text, location_str, label))

	return tweets


treated_file = treat_quotes('100_tweets_happy_hillary.json')
data = parse_json(treated_file)

for tweet in get_tweets(data):
	tweet.print_tweet()

