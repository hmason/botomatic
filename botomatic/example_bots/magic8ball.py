import random

from botomatic import TBot

RESPONSES = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it yes',
             'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 
             'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Don\'t count on it', 'My reply is no', 
             'My sources say no', 'Outlook not so good', 'Very doubtful']

class Magic8Ball(TBot):
    debug_mode = False

    def __init__(self):
        handle = "dodecaDecider"
        super(Magic8Ball, self).__init__(handle)

    def run(self):
        for msg in self.handle_mentions():
            reply = "@%s %s" % (msg.user.screen_name, random.choice(RESPONSES))
            self.tweets.append((reply, msg.id))

        self.wrap_up()

if __name__ == '__main__':
    m = Magic8Ball()

