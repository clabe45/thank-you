import sys
import random

import constants
import virus

if __name__ == '__main__':
    if len(sys.argv) > 2:
        # too many args
        print("I don't like more than one arguments! So, no thank you.")
        sys.exit(1)

    # init virus
    virus = virus.Virus('Thank you', 'main' if constants.TESTING else 'thank-you')
    if len(sys.argv) == 2:
        subcmd = sys.argv[1]
        if subcmd == 'clean':
            print('Removed %d virus files. No need to thank me.' % virus.clean_directory())
        else:
            print('Unknown subcommand: \'%s\'' % subcmd)
    else:
        # do work
        for _ in range(random.randint(0, 5)):
            fn = virus.get_random_action()
            fn()
