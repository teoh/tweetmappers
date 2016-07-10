import tweepy
import states
import geocode
import app
import json
import pprint
import re

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from wordfilter import Wordfilter

with open('../credentials.json') as credentials_file:
    credentials = json.load(credentials_file)
    consumer_key, consumer_secret = credentials['consumer_key'], credentials['consumer_secret']
    access_token, access_secret = credentials['access_token'], credentials['access_secret']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

wordfilter = Wordfilter()
with open('../sensitivewords.json') as sensitive_file:
    sensitive_words = json.load(sensitive_file)['badwords']
    wordfilter.add_words(sensitive_words)

class TweetSubject(object):
    clinton = 1
    trump = 2
    other = 3

clinton_first = 'hillary'
trump_first = 'donald'

clinton_last = 'clinton'
trump_last = 'trump'

def tweet_subject(tweet):
    processed = tweet.get('text')
    if processed is None:
        processed = ''
    processed = processed.lower()

    if clinton_first in processed and clinton_last in processed:
        if trump_first in processed or trump_last in processed:
            return TweetSubject.other
        return TweetSubject.clinton

    if trump_first in processed and trump_last in processed:
        if clinton_first in processed or clinton_last in processed:
            return TweetSubject.other
        return TweetSubject.trump

    return TweetSubject.other

def tweet_in_us(tweet):
    user = tweet.get('user')
    if user is None:
        user = {}
    location = user.get('location')
    if location is None:
        location = ''
    return states.in_us(location)

class PrintTweetsListener(StreamListener):
    def on_data(self, data):
        tweet = json.loads(data)
        if tweet_in_us(tweet):
            subject = tweet_subject(tweet)
            if subject != TweetSubject.other:
                location = geocode.geocode(tweet)
                if location:
                    lon = location['lon']
                    lat = location['lat']
                    if wordfilter.blacklisted(tweet['text']):
                        exp = '(%s)' % '|'.join(wordfilter.blacklist)
                        r = re.compile(exp, re.IGNORECASE)
                        tweet['text'] = r.sub('***', tweet['text'])
                    print '################# Text ###################'
                    print tweet['text']
                    tweet_package = {
                            'tweet': tweet,
                            'lon': lon,
                            'lat': lat
                    }
                    app.write(json.dumps(tweet_package))
        return True

    def on_error(self, error):
        print '################# Error ######################'
        print json.dumps(json.loads(error), indent=4)
        print '################# End Error ######################'
        return True

stream = Stream(auth, PrintTweetsListener())
stream.filter(track=['donald trump', 'hillary clinton', 'hillary', 'clinton', 'donald', 'trump'])
