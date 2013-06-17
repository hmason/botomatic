from botomatic import TBot
import subprocess

class bc_l(TBot):

    def __init__(self):
        handle = "bc_l"
        super(bc_l, self).__init__(handle)

    def run(self):
        for dm in self.handle_DMs():
            p = subprocess.Popen("bc -l", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            out, err = p.communicate(dm.text + "\n")
            if out.strip():
                reply = "@%s %s = %s" % (dm.sender_screen_name, dm.text, out.strip())
                self.tweets.append(reply[:140]) #only tweet the first 140 characters of a long response

        self.wrap_up()

if __name__ == '__main__':
    b = bc_l()
