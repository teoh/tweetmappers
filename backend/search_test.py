import tweepy
import json

print 'hello'

with open('./credentials.json') as credentials_file:
	credentials = json.load(credentials_file)
	consumer_key, consumer_secret = credentials['consumer_key'],credentials['consumer_secret']
	access_token, access_secret = credentials['access_token'],credentials['access_secret']

print consumer_key
print consumer_secret
print access_token
print access_secret

au = tweepy.OAuthHandler(consumer_key,consumer_secret)
au.set_access_token(access_token,access_secret)

api = tweepy.API(au)

tweets = api.search(q='hillary clinton filter:safe',
					lang='en',
					geocode='39.8,-95.583068847656,2500km'
					)

for t in tweets:
	print '===='
	print t.text