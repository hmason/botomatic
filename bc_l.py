from botomatic import TBot
import subprocess

class bc_l(TBot):
    debug_mode = False

    def __init__(self):
        handle = "bc_l"
        super(bc_l, self).__init__(handle)

    def bc_l(self, input_text):
        p = subprocess.Popen("bc -l", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        try:
            out, err = p.communicate(input_text + "\n")
        except UnicodeEncodeError:
            return ''

        return out


    def run(self):
        for dm in self.handle_DMs():
            out = self.bc_l(dm.text)
            if out.strip():
                reply = "@%s %s = %s" % (dm.sender_screen_name, dm.text, out.strip())
                self.tweets.append(reply)

        for msg in self.handle_mentions():
            expression = msg.text[5:] # assuming the @bc_l is a prefix
            out = self.bc_l(expression)
            if out.strip():
                reply = "@%s %s = %s" % (msg.user.screen_name, expression, out.strip())
                print reply
                self.tweets.append(reply)


        self.wrap_up()

if __name__ == '__main__':
    b = bc_l()
