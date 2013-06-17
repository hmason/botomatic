import sys
import os
import pickle
import tweepy

import settings

class TBot(object):
    handle = None
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

        self.history['last_dm_id'] = dms[0].id
        return dms

    def handle_mentions(self):
        mentions = self.api.mentions()

        self.history['mentions'] = mentions

        print mentions

    def search(self, query):
        pass

    def handle_stream(self):
        pass

    def handle_followers(self):
        pass

    def publish_tweets(self):
        if self.tweets:
            for tweet in self.tweets:
                #self.api.update_status(tweet[:140]) # cap length at 140 chars
                print "TWEETED: " + tweet[:140] 

        self.history['tweets'].extend(self.tweets)

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

    def wrap_up(self):
        pickle.dump(self.history, open(self.history_filename, 'w'))
        self.publish_tweets()


if __name__ == '__main__':
    pass
