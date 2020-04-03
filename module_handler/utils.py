"""
**Author** : Robin Camarasa

**Institution** : Erasmus Medical Center

**Position** : PhD student

**Contact** : r.camarasa@erasmusmc.nl

**Date** : 2020-04-03

**Project** : module_handler

**Utils functions for module handler**

"""
from settings import *
from typing import Dict, str
import os
import json


def get_config() -> Dict:
    """
    Function that parse the config json file

    :return: The configuration dictionnary
    """
    # Get configuration path
    configuration_path = os.path.join(DATA_PATH, 'config.json')

    with open(configuration_path, 'r') as handler:
        configuration_dict = json.load(handler)
    return configuration_dict


def change_filename(filename: str) -> None:
    """
    Change the filenames with the configuration

    :param filename: Path of a file
    """
    # Get configuration
    configuration_dict = get_config()

    # Filename modified
    filename_modified = filename[:]
    for key, value in configuration_dict.items():
        filename_modified.replace('##__{}__##'.format(key), value)
    os.rename(filename, filename_modified)


def change_content(filename: str) -> None:
    """
    Change the filenames with the configuration

    :param filename: Path of a file
    """
    # Get configuration
    configuration_dict = get_config()

    # Get file content
    with open(filename, 'r') as handle:
        lines = handle.readlines()

    # Update file line by line
    for line in lines:
        for key, value in configuration_dict.items():
            line.replace(
                '##__{}__##'.format(key),
                value
            )

    # Write line
    with open(filename, 'w') as handle:
        handle.writelines(lines)
