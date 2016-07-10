import nltk
import csv

# parse the tweets 

data_raw = []

with open('./data/hillary_sample.csv') as csvfile:
	trainreader = csv.reader(csvfile,delimiter=',',quotechar='"')
	for row in trainreader:
		data_raw.append((row[1],row[0]))

print type(data_raw[0])
# train model




# output the representation

print "hello"