import os.path
import random

import markovify

import constants
import data

model = markovify.Text(data.get_str('data', 'sample_text.txt', 'You broke me.'))

def gen_message():
    """Generate note text"""

    def gen_sent():
        s = None
        while s is None:
            s = model.make_sentence()
        return s

    m = None
    while m is None:
        m = ' '.join([gen_sent() for _ in range(random.randint(0, 10))])
    return m

def gen_message_name():
    """Generate note name"""

    n = None
    while n is None:
        n = model.make_sentence()
    return n.split(' ')[0].lower()
