"""
**Author** : Robin Camarasa

**Institution** : Erasmus Medical Center

**Position** : PhD student

**Contact** : r.camarasa@erasmusmc.nl

**Date** : 2020-04-03

**Project** : project_handler

**Entry points of the project**
"""
import click
from project_handler.settings import *
import os
import json
import subprocess
from pathlib import Path
from project_handler.utils import *


@click.command()
@click.option(
    '--git-url', '-g',
    required=True,
    type=str,
    help='Remote url of the project'
)
@click.option(
    '--path', '-p',
    type=str,
    default='./',
    help='Path to lauch the project'
)
@click.option(
    '--author', '-a',
    type=str,
    default=AUTHOR,
    help='Author(s) of the project'
)
@click.option(
    '--data', '-d',
    type=str,
    default=None,
    help='Path to the data'
)
def newpythonproject(git_url, path, author, data):
    """
    Generate new code project
    """
    # Create abspath of path
    path = os.path.abspath(path)

    # Launch git commands
    subprocess.call(
        'git clone {}'.format(git_url),
        cwd=os.path.join(path),
        shell=True
    )

    # List path
    name = git_url.split('/')[-1].split('.')[0]

    # Create repositories
    for dir_ in ['results', 'src', 'related_documents']:
        os.makedirs(os.path.join(path, dir_))

    # Create link to the data
    if not data is None:
        os.symlink(data, os.path.join(path, 'data'))

    # Create virtualenv
    subprocess.call(
        'python3 -m virtualenv {}_env'.format(name),
        cwd=os.path.join(path),
        shell=True
    )

    # Create .project_handler.json
    config = {
        'AUTHOR': author,
        'NAME': name,
        'GITURL': git_url,
        'DESCRIPTION': ''
    }
    with open(
        os.path.join(path, '.config.json'), 'w+'
    ) as handle:
        json.dump(config, handle, indent=4)


@click.command()
@click.option(
    '--path', '-p',
    type=str,
    default='./',
    help='Path to lauch the project'
)
def applyconfig(path):
    # Get configuration dict
    path, configuration_dict = get_config(os.path.abspath(path))

    # Change folder names
    for path_, _, _ in os.walk(path):
        change_filename(
            path_, configuration_dict
        )

    # Change path names and paths content
    for path_, _, files in os.walk(path):
        for file in files:
            # Change file content
            change_content(
                os.path.join(path_, file),
                configuration_dict
            )
            change_filename(
                os.path.join(path_, file),
                configuration_dict
            )

