"""
**Author** : Robin Camarasa

**Institution** : Erasmus Medical Center

**Position** : PhD student

**Contact** : r.camarasa@erasmusmc.nl

**Date** : 2020-04-03

**Project** : project_handler

**Utils functions for project_handler**

"""
from typing import Dict
import os
import json


def get_config(path: str) -> Dict:
    """
    Function that parse the config json file

    :param path: Path of the of folder
    :return: The configuration dictionnary
    """
    if os.path.abspath(path) == os.path.dirname(os.path.abspath(path)):
        return None
    try:
        # Get configuration path
        configuration_path = os.path.join(
            path, '.config.json'
        )
        with open(configuration_path, 'r') as handler:
            configuration_dict = json.load(handler)
        return path, configuration_dict
    except:
        return get_config(os.path.dirname(os.path.abspath(path)))


def change_filename(
        filename: str, configuration_dict: dict
    ) -> None:
    """
    Change the filenames with the configuration

    :param filename: Path of a file
    :param configuration_dict: Configuration dictionnary
    """
    # Filename modified
    filename_modified = filename[:]
    for key, value in configuration_dict.items():
        filename_modified = filename_modified.replace('##__{}__##'.format(key), value)
    os.rename(filename, filename_modified)


def change_content(
        filename: str, configuration_dict: dict
    ) -> None:
    """
    Change the filenames with the configuration

    :param filename: Path of a file
    :param configuration_dict: Configuration dictionnary
    """
    # Get file content
    try:
        with open(filename, 'r') as handle:
            lines = handle.readlines()

        # Update file line by line
        updated_lines = []
        for line in lines:
            for key, value in configuration_dict.items():
                line = line.replace('##__{}__##'.format(key), value)
            updated_lines.append(line)

        # Write line
        with open(filename, 'w+') as handle:
            handle.writelines(updated_lines)
    except Exception as e:
        print(e)

