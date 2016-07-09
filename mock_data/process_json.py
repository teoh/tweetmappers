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
				target.write(line)

	return output_file
	
def parse_json(input_file):
	with open(input_file) as data_file:    
	    return json.load(data_file)

def get_location(data):
	d = data['statuses'][0]
	# print json.dumps(d, indent=4)
	user = d.pop('user', {})
	location = user.pop('location', '')
	return location


treated_file = treat_quotes('1_tweet_happy_hillary.json')
data = parse_json(treated_file)

print "The location is = " + get_location(data)

