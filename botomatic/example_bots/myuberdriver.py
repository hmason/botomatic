import urllib
import urllib2
import json
import re
import sys

from botomatic import TBot

class MyUberDriver(TBot):
    debug_mode = False

    def __init__(self):
        handle = "myuberdriverbot"
        self.query = "my uber driver"
        super(MyUberDriver, self).__init__(handle)


    def run(self):
        # find other people's stuff on twitter and fav/retweet
        for tweet in self.search("my uber driver"):
            if tweet.lang != 'en': # english only
                continue 

            if "uber driver" not in tweet.text:
                continue

            try:
                tweet.retweet() # only retweet one each time the script is run
            except:
                pass
            
            break

        
        self.wrap_up()

if __name__ == '__main__':
    r = MyUberDriver()
