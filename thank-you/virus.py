import os
import os.path
import sys
import re
import random

import constants
import ai
import nlg
import file
import data

# what does the following line mean?
# TODO: make other viruses from this virus

# multiply by ten if they delete the original file
severity = data.get_int('user_data', 'severity.txt', 10 * constants.DEFAULT_SEVERITY)

# for keeping track of possible actions
agent = ai.Agent()

def clean_directory():
    """Revert to original state"""

    c = 0
    for e in os.listdir(file.home):
        if re.fullmatch(r'(%s_\d+\.py)|(.+\.txt)' % constants.MAIN_FILE_BASE, e) and e != constants.MAIN_FILE_NAME:
            os.remove(file.join(e)) # make `e` relative to home
            c += 1

    return c

def get_random_action():
    top = sum([likelihood for action,likelihood in agent.actions.items()])
    ri = random.randint(0, top - 1)

    accumulation = 0
    for action,likelihood in agent.actions.items():
        start = accumulation
        end = start + likelihood
        # test if ri in [start, end)
        if start <= ri < end:
            return action

        accumulation = end
#
# @agent.action(likelihood=5)
# def copy_random_times():
#     for _ in range(0, random.randint(0, 20)): copy()

@agent.action(likelihood=3)
def copy():
    """Clone this file... lol"""

    # use `file.join` to make paths relative to `file.home`
    me = open(file.join(constants.MAIN_FILE_NAME), 'r')

    copy_indexes = [file.get_file_index(e) for e in os.listdir(file.home) if os.path.isfile(file.join(e))]
    last_copy_index = max(copy_indexes)
    # choose 'thank-you_0.exe' or 'thank-you_0.py'
    copy_name = '%s_%d.%s' % (constants.MAIN_FILE_BASE, last_copy_index+1, constants.MAIN_FILE_EXT)
    new_me = open(file.join(copy_name), 'w')

    new_me.write(me.read())
    me.close()
    new_me.close()

@agent.action(likelihood=1)
def leave_note():
    msg = nlg.gen_message()
    name = None
    while name is None or os.path.exists(file.join(name)):
        name = nlg.gen_message_name()

    with open(file.join(name+".txt"), 'w+') as note:
        note.write(msg)
    print('Check your mail! I left you a note!')

@agent.action(likelihood=1)
def say_hi(times=None):
    if times is None:
        times = random.randint(1, 5)

    for _ in range(times):
        print("Hi, my name's %s! What's yours?" % constants.NAME)

        try:
            username = input('>>> ')
        except KeyboardInterrupt:
            return

        defiance = 0
        while not username:
            print("Really?? You don't have a name?")
            username = input('>>>> ')

            defiance += 1
            if defiance >= 10:
                username = ":("
                break

        for _ in range(times):
            print("Hi, %s. My name's %s!" % (username, constants.NAME))
