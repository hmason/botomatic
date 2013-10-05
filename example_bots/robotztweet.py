from botomatic import TBot

class RobotzTweet(TBot):
    debug_mode = True

    def __init__(self):
        handle = "robotztweet"
        super(RobotzTweet, self).__init__(handle)

    def run(self):
        for tweet in self.search("robot"):
            if tweet.lang != 'en': # english only
                continue 

            if not tweet.entities['urls']: # there must be a link
                continue

            if tweet.retweet_count == 0 and tweet.favorite_count == 0: # someone likes this
                continue

            tweet.retweet() # only retweet one each time the script is run
            break
            
        self.wrap_up()

if __name__ == '__main__':
    r = RobotzTweet()

