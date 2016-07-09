import json
from pprint import pprint

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

def get_locations(data):
	locations = []
	for d in data['statuses']:
		# print json.dumps(d, indent=4)
		user = d.pop('user', {})
		locations.append(user.pop('location', ''))
	return locations


treated_file = treat_quotes('100_tweets_happy_hillary.json')
data = parse_json(treated_file)

for location in get_locations(data):
	print "Location = " + location

