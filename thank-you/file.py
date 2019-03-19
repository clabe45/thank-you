import os.path

import constants

def join(*parts):
    return os.path.join(home, *parts)

def get_file_index(name):
    return int(name[:-len('.py')].split('_')[1]) if '_' in name else 0

def get_script_directory():
    """Retrieve location of currently executed script"""

    return os.path.dirname(os.path.abspath(__file__))

home = get_script_directory()
