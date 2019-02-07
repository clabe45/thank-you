import os.path

import constants

class FileManager():
    def __init__(self, home, main_file_base):
        self.home = home
        self.main_file_base = main_file_base

    def join(self, *parts):
        return os.path.join(self.home, *parts)

    def get_severity(self):
        path = self.join('data', 'severity.txt')
        try:
            with open(path, 'r') as file:
                return int(file.read())

        except (FileNotFoundError, ValueError) as e:
            # error-specific messages
            if type(e) == FileNotFoundError:
                print("Hmm... it looks like something's missing. Lemme fix that real quick.")
            elif type(e) == ValueError:
                print('Hmm... it looks like someone messed with the SEVERITY LEVEL!!. Who would DO THAT??')
                
            with open(path, 'w+') as file:
                file.write(str(constants.DEFAULT_SEVERITY))
            return constants.DEFAULT_SEVERITY

    @staticmethod
    def get_file_index(name):
        return int(name[:-len('.py')].split('_')[1]) if '_' in name else 0
