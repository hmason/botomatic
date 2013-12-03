botomatic
=========

The botomatic package makes it easy to create Twitter bots in python. The package handles authentication, 
retrieving messages, processing the output, and publishing back to Twitter. I want to make it as easy as possible
to create fun and creative bots. The world needs more awesome bots!

Usage
=====

First, register the twitter account you want to use.

Second, subclass the TBot class. Overload the ```run``` method to process the input messages (via handle_messages()) and add 
any messages that you want to publish to the self.tweets list.

For our hello world example, say hi to a Magic 8 Ball bot (alive [@dodecaDecider](https://twitter.com/dodecaDecider)):


```python
import random
from botomatic import TBot

RESPONSES = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

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
```

Additional Information
======================
You will need to create a file called "settings.py" containing the following:
```BITLY_LOGIN = ""
BITLY_APIKEY = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
```

The CONSUMER_KEY and CONSUMER_SECRET can be obtained by registering the app at https://dev.twitter.com/apps and following the directions.

