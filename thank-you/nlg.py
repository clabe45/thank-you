import os.path
import random

import markovify

class TextGenerator:
    def __init__(self, file_man):
        self.file_man = file_man

        with open(file_man.join('data', 'sample.txt'), 'r') as file:
            self.model = markovify.Text(file.read())

    def gen_message(self):
        """Generate note text"""

        def gen_sent():
            s = None
            while s is None:
                s = self.model.make_sentence()
            return s

        m = None
        while m is None:
            m = ' '.join([gen_sent() for _ in range(random.randint(0, 10))])
        return m

    def gen_message_name(self):
        """Generate note name"""

        n = None
        while n is None:
            n = self.model.make_sentence()
        return n.split(' ')[0].lower()
