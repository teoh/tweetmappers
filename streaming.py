import tweepy
import json
import pprint

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

with open('./credentials.json') as credentials_file:
    credentials = json.load(credentials_file)
    consumer_key, consumer_secret = credentials['consumer_key'], credentials['consumer_secret']
    access_token, access_secret = credentials['access_token'], credentials['access_secret']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
tweet_api = tweepy.API(auth)

class PrintTweetsListener(StreamListener):
    def on_data(self, data):
        print json.dumps(json.loads(data), indent=4)
        return True

    def on_error(self, error):
        print json.dumps(json.loads(error), indent=4)
        return True

stream = Stream(auth, PrintTweetsListener())
stream.filter(track=['hillary', 'clinton', 'donald', 'trump'])
