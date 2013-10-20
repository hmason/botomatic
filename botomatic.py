import sys
import os
import pickle
import tweepy #requires version 2.1+
import urllib
import urllib2
import json
import re

import settings

def bitlify(match):
    if settings.BITLY_LOGIN and settings.BITLY_APIKEY:
        response = urllib2.urlopen("http://api.bitly.com/v3/shorten?" + urllib.urlencode({'longUrl': match.group(0), 'apiKey': settings.BITLY_APIKEY, 'login': settings.BITLY_LOGIN}))
        data = response.read()
        try:
            url = json.loads(data)['data']['url']
        except ValueError:
            url = match.group(0)

        return url


class TBot(object):
    handle = None
    debug_mode = True
    bitlify_links = True
    settings = {}
    tweets = []

    def __init__(self, handle):
        self.history_filename = handle + "_history.pickle"
        self.auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
        try:
            self.settings = pickle.load(open(handle + "_settings.pickle",'r'))
        except IOError:
            self.authenticate()
            pickle.dump(self.settings, open(handle + "_settings.pickle",'w')) # right place to save settings?

        try:
            self.history = pickle.load(open(self.history_filename,'r'))
        except IOError:
            self.history = {}

        self.auth.set_access_token(self.settings['key'], self.settings['secret'])
        self.api = tweepy.API(self.auth)

        self.run()

    def handle_DMs(self, new_only=True):
        if new_only and self.history.get('last_dm_id', None):
            dms = self.api.direct_messages(since_id=self.history['last_dm_id'])
        else:
            dms = self.api.direct_messages()

        if dms:
            self.history['last_dm_id'] = dms[0].id

        return dms

    def handle_mentions(self, new_only=True):
        if new_only and self.history.get('last_mention_id', None):
            mentions = self.api.mentions_timeline(since_id=self.history['last_mention_id'])
        else:
            mentions = self.api.mentions_timeline()
        
        if mentions:
            self.history['last_mention_id'] = mentions[0].id

        return mentions

    def search(self, query, lang='en'):
        return self.api.search(q=query, lang=lang)

    def handle_stream(self):
        return self.api.home_timeline()

    def handle_followers(self):
        pass

    def process_tweets(self):
        http_re = re.compile(r'http://\S+')
        processed_tweets = []
        for tweet in self.tweets:
            if 'http://' in tweet:
                tweet = http_re.sub(bitlify, tweet)
            processed_tweets.append(tweet)
        self.tweets = processed_tweets
                

    def publish_tweets(self, limit=None):
        tweeted_count = 0

        if self.tweets:
            for tweet in self.tweets:
                if self.debug_mode:
                    print "FAKETWEET: " + tweet[:140] # for debug mode
                else:
                    try:
                        if limit and tweeted_count <= limit:
                            status = self.api.update_status(tweet[:140]) # cap length at 140 chars
                            self.history['last_tweet_id'] = status.id
                            tweeted_count += 1
                    except tweepy.error.TweepError: # prob a duplicate
                        pass

    def authenticate(self):
        print self.auth.get_authorization_url()
        verifier = raw_input('Verification code: ')
        try:
            self.auth.get_access_token(verifier)
        except tweepy.TweepError:
            print 'Error: failed to get access token.'

        self.settings['key'] = self.auth.access_token.key
        self.settings['secret'] = self.auth.access_token.secret

    def run(self):
        pass

    def wrap_up(self, tweet_limit=None):
        self.process_tweets()
        self.publish_tweets(tweet_limit)
        pickle.dump(self.history, open(self.history_filename, 'w'))


if __name__ == '__main__':
    pass
