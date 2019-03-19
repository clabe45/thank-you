import random
import sys

import constants
import virus
import data

def start():
    check_agreement()

    if len(sys.argv) > 2:
        # too many args
        print("I don't like arguments! So, no thank you.")
        sys.exit(1)

    elif len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg == 'clean':
            print("Deleted %d virus file(s). No problem." % virus.clean_directory())
        else:
            print("Invalid argument '%s'.. idk what you were thinking lol" % arg)

    else:
        n = random.randint(0, 16) # number of "actions" performed
        for _ in range(n):
            fn = virus.get_random_action()
            fn()

        if n == 0:
            print("Oops! Try again next time!")

def check_agreement():
    if not data.get_bool('user_data', 'agreement.txt', False):
        print('IMPORTANT: THE CONTENTS OF THE FOLDER CONTAINING %s WILL BE MODIFIED!\n' % constants.MAIN_FILE_NAME
            + "Set the contents of user_data/agreement.txt to 'true' (without the 's) to confirm this fact.")
        sys.exit(1)
