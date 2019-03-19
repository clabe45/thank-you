import file

# TODO: make the following get functions more DRY than WET

def get_str(location, name, default_value=''):
    path = file.join(location, name)
    try:
        with open(path, 'r') as f:
            return f.read()

    except (FileNotFoundError, ValueError) as e:
        # error-specific messages
        if type(e) == FileNotFoundError:
            print('Hmm... it looks like someone *deleted a file*! Who would DO THAT??')
        elif type(e) == ValueError:
            print("Someone changed the data.. it's invalid")

        with open(path, 'w+') as f:
            f.write(default_value)
        return default_value

def get_int(location, name, default_value=0):
    path = file.join(location, name)
    try:
        with open(path, 'r') as f:
            return int(f.read())

    except (FileNotFoundError, ValueError) as e:
        # error-specific messages
        if type(e) == FileNotFoundError:
            print('Hmm... it looks like someone *deleted a file*! Who would DO THAT??')
        elif type(e) == ValueError:
            print("Someone changed the data.. it's invalid")

        with open(path, 'w+') as f:
            f.write(str(default_value))
        return default_value

def get_bool(location, name, default_value=False):
    path = file.join(location, name)
    try:
        with open(path, 'r') as f:
            s = f.read().strip().lower()
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

        with open(path, 'w+') as f:
            f.write(str(default_value))
        return default_value
