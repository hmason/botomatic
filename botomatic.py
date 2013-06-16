import sys
import os
import pickle
import tweepy

import settings

class TBot(object):
    handle = None
    settings = {}

    def __init__(self, handle):
        self.auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
        try:
            self.settings = pickle.load(open(handle + "_settings.pickle",'r'))
        except IOError:
            self.authenticate()
            pickle.dump(self.settings, open(handle + "_settings.pickle",'w')) # right place to save settings?

        try:
            self.history = pickle.load(open(handle + "_history.pickle",'r'))
        except IOError:
            self.history = {}

        self.auth.set_access_token(self.settings['key'], self.settings['secret'])
        self.api = tweepy.API(self.auth)

    def handle_DMs(self):
        pass

    def handle_replies(self):
        pass

    def search(self, query):
        pass

    def handle_stream(self):
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


if __name__ == '__main__':
    b = TBot('realtime_dev')
