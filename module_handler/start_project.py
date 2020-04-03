"""
**Author** : Robin Camarasa

**Institution** : Erasmus Medical Center

**Position** : PhD student

**Contact** : r.camarasa@erasmusmc.nl

**Date** : 2020-04-03

**Project** : module_handler

**File that launches the creation of the project**

"""
from virtualenv import create_environment
from pathlib import Path
from settings import *
from utils import *


if __name__ == '__main__':
    # Get configuration dict
    configuration_dict = get_config()

    # Create virtualenv
    create_environment(
        ROOT_PATH, '{}_env'.format(configuration_dict['NAME'])
    )

    for path in os.walk():
        if not 'module_handler' in path:
            change_content(path)
            change_filename(path)
