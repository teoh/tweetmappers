import tweepy
import json

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

with open('/Users/bilisun/tweetmappers/credentials.json') as credentials_file:
    credentials = json.loads(credentials_file)
    consumer_key, consumer_secret = credentials['consumer_key'], credentials['consumer_secret']
    access_token, access_secret = credentials['access_token'], credentials['access_secret']

print consumer_key
print consumer_secret
print access_token
print access_secret

#auth = OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_secret)
#tweet_api = tweepy.API(auth)
