import os
import os.path
import sys
import re
import random

import markovify

import constants

# TODO: make other viruses from this virus

class Virus:
    def __init__(self, name, home='.'):
        self.name = name
        self.home = home
        with open(os.path.join(self.home, 'sample.txt'), 'r') as file:
            self.text_model = markovify.Text(file.read())

    def copy(self):
        me = open(os.path.basename(__file__), 'r')

        copy_indexes = [Virus.get_file_index(e) for e in os.listdir(self.home) if os.path.isfile(e)]
        last_copy_index = max(copy_indexes)
        ext = 'py' if constants.TESTING else 'exe'
        copy_name = '%s_%d.%s' % (self.base_file_name(), last_copy_index+1, ext)
        new_me = open(copy_name, 'w')

        new_me.write(me.read())
        me.close()
        new_me.close()

    def base_file_name(self):
        return self.name.lower().replace(' ', '-')

    def clean_directory(self):
        c = 0
        for e in os.listdir(self.home):
            if re.fullmatch(r'(%s_\d+.py)|(?!(sample).txt)' % self.base_file_name(), e) and e != self.name+'.py':
                os.remove(e)
                c += 1
        return c

    def say_hi(self, times=20):
        for _ in range(times):
            print("Hi, my name's %s! What's yours?" % self.name)

        username = input('>>> ')
        for _ in range(times):
            print("Hi, %s. My name's %s!" % (username, self.name))

    def leave_note(self):
        msg = self.gen_message()
        name = None
        while name is None or os.path.exists(os.path.join(self.home, name)):
            name = self.gen_message_name()

        with open(os.path.join(self.home, name+".txt"), 'w+') as file:
            file.write(msg)

    def gen_message(self):
        def gen_sent():
            s = None
            while s is None:
                s = self.text_model.make_sentence()
            return s

        m = None
        while m is None:
            m = ' '.join([gen_sent() for _ in range(random.randint(0, 10))])
        return m

    def gen_message_name(self):
        n = None
        while n is None:
            n = self.text_model.make_sentence()
        return n.split(' ')[0].lower()

    @staticmethod
    def get_file_index(name):
        return int(name[:-len('.py')].split('_')[1]) if '_' in name else 0

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print("I don't like more than one arguments! So, no thank you.")
        sys.exit(1)

    virus = Virus('Thank you')
    if len(sys.argv) == 2:
        subcmd = sys.argv[1]
        if subcmd == 'clean':
            virus.clean_directory()
    else:
        for _ in range(random.randint(0, 5)):
            r = random.randint(0, 3)
            if r == 0:
                for _ in range(0, random.randint(0, 20)): virus.copy()
            elif r == 1:
                virus.leave_note()
            else: virus.say_hi()
