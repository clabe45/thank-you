class DataManager():
    def __init__(self, file_man):
        self.file_man = file_man

    def get_str(self, name, default_value=''):
        path = self.file_man.join('data', name)
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
        path = self.file_man.join('data', name)
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
