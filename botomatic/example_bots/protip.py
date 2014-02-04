import pickle
import tweepy
from botomatic import TBot

class Protip(TBot):
    debug_mode = True

    def __init__(self):
        handle = "protipbot"
        super(Protip, self).__init__(handle)

    def run(self):
        results = self.search('"pro-tip" protip')
        for result in results:
            try:
                result.retweet()
            except tweepy.error.TweepError: # private status update?
                continue


        self.wrap_up()

if __name__ == '__main__':
    p = Protip()
