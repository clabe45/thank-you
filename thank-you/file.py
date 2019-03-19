import os.path

import constants

class FileManager():
    def __init__(self, home, main_file_base):
        self.home = home
        self.main_file_base = main_file_base
        self.ext = 'py' if constants.TESTING else 'exe'
        self.main_file_name = self.main_file_base + '.' + self.ext

    def join(self, *parts):
        return os.path.join(self.home, *parts)

    @staticmethod
    def get_file_index(name):
        return int(name[:-len('.py')].split('_')[1]) if '_' in name else 0

    @staticmethod
    def get_script_directory():
        """Retrieve location of currently executed script (not necessarily the same as current working directory)"""

        return os.path.dirname(os.path.abspath(__file__))
