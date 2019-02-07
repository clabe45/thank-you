import os
import os.path
import re

import constants
import nlg
import file

# TODO: make other viruses from this virus

class Virus:
    def __init__(self, name, main_file_base, home='.'):
        self.name = name
        self.file_man = file.FileManager(home, main_file_base)    # file manager
        self.text_gen = nlg.TextGenerator(self.file_man)
        self.severity = self.file_man.get_severity()

    def copy(self):
        """Clone this file lol"""

        ext = 'py' if constants.TESTING else 'exe'
        me = open('%s.%s' % (self.file_man.main_file_base, ext), 'r')

        copy_indexes = [file.FileManager.get_file_index(e) for e in os.listdir(self.file_man.home) if os.path.isfile(e)]
        last_copy_index = max(copy_indexes)
        # choose 'thank-you_0.exe' or 'thank-you_0.py'
        copy_name = '%s_%d.%s' % (self.file_man.main_file_base, last_copy_index+1, ext)
        new_me = open(copy_name, 'w')

        new_me.write(me.read())
        me.close()
        new_me.close()

    def clean_directory(self):
        """Revert to original state"""

        c = 0
        for e in os.listdir(self.file_man.home):
            if re.fullmatch(r'(%s_\d+\.py)|(.+\.txt)' % self.file_man.main_file_base, e) and e != self.name+'.py':
                os.remove(e)
                c += 1
        return c

    def leave_note(self):
        msg = self.text_gen.gen_message()
        name = None
        while name is None or os.path.exists(os.path.join(self.file_man.home, name)):
            name = self.text_gen.gen_message_name()

        with open(os.path.join(self.file_man.home, name+".txt"), 'w+') as file:
            file.write(msg)

    def do_random_action(self):
        raise NotImplementedError() # TODO

    def say_hi(self, times=20):
        for _ in range(times):
            print("Hi, my name's %s! What's yours?" % self.name)

            username = input('>>> ')
            for _ in range(times):
                print("Hi, %s. My name's %s!" % (username, self.name))
