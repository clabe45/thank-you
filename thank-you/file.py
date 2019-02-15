import os.path

import constants

def join(*parts):
    return os.path.join(home, *parts)

# TODO: make the following get functions more DRY than WET

def get_str(location, name, default_value=''):
    path = join(location, name)
    try:
        with open(path, 'r') as file:
            return file.read()

    except (FileNotFoundError, ValueError) as e:
        # error-specific messages
        if type(e) == FileNotFoundError:
            print('Hmm... it looks like someone *deleted a file*! Who would DO THAT??')
        elif type(e) == ValueError:
            print("Someone changed the data.. it's invalid")

        with open(path, 'w+') as file:
            file.write(default_value)
        return default_value

def get_int(location, name, default_value=0):
    path = join(location, name)
    try:
        with open(path, 'r') as file:
            return int(file.read())

    except (FileNotFoundError, ValueError) as e:
        # error-specific messages
        if type(e) == FileNotFoundError:
            print('Hmm... it looks like someone *deleted a file*! Who would DO THAT??')
        elif type(e) == ValueError:
            print("Someone changed the data.. it's invalid")

        with open(path, 'w+') as file:
            file.write(str(default_value))
        return default_value

def get_bool(location, name, default_value=False):
    path = join(location, name)
    try:
        with open(path, 'r') as file:
            s = file.read().strip().lower()
            if s == 'true':
                return True
            elif s == 'false':
                return False
            else:
                raise ValueError('Not a boolean value (with manual conversion)')

    except (FileNotFoundError, ValueError) as e:
        # error-specific messages
        if type(e) == FileNotFoundError:
            print('Hmm... it looks like someone *deleted a file*! Who would DO THAT??')
        elif type(e) == ValueError:
            print("Someone changed the data.. it's invalid")

        with open(path, 'w+') as file:
            file.write(str(default_value))
        return default_value

def get_file_index(name):
    return int(name[:-len('.py')].split('_')[1]) if '_' in name else 0

def get_script_directory():
    """Retrieve location of currently executed script"""

    return os.path.dirname(os.path.abspath(__file__))

home = get_script_directory()
