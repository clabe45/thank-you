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

    def get_str(self, name, default_value=''):
        path = self.join('data', name)
        try:
            with open(path, 'r') as file:
                return file.read()

        except (FileNotFoundError, ValueError) as e:
            # error-specific messages
            if type(e) == FileNotFoundError:
                print("Hmm... it looks like something's missing. Lemme fix that real quick.")
            elif type(e) == ValueError:
                print('Hmm... it looks like someone *deleted a file*! Who would DO THAT??')

            with open(path, 'w+') as file:
                file.write(default_value)
            return default_value

    def get_int(self, name, default_value=0):
        path = self.join('data', name)
        try:
            with open(path, 'r') as file:
                return int(file.read())

        except (FileNotFoundError, ValueError) as e:
            # error-specific messages
            if type(e) == FileNotFoundError:
                print("Hmm... it looks like something's missing. Lemme fix that real quick.")
            elif type(e) == ValueError:
                print('Hmm... it looks like someone *deleted a file*! Who would DO THAT??')

            with open(path, 'w+') as file:
                file.write(str(default_value))
            return default_value

    @staticmethod
    def get_file_index(name):
        return int(name[:-len('.py')].split('_')[1]) if '_' in name else 0

    @staticmethod
    def get_script_directory():
        """Retrieve location of currently executed script"""

        return os.path.dirname(os.path.abspath(__file__))
