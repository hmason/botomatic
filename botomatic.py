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
            self.settings = pickle.load(open(handle + "_settings.json",'r'))
        except IOError:
            self.settings = self.authenticate()

    def handle_DMs(self):
        pass

    def handle_replies(self):
        pass

    def search(self, query):
        pass

    def handle_stream(self):
        pass

    def authenticate(self):
        return None

    def run(self):
        pass


if __name__ == '__main__':
    b = TBot('testbot')
