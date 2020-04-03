"""
**Author** : Robin Camarasa

**Institution** : Erasmus Medical Center

**Position** : PhD student

**Contact** : r.camarasa@erasmusmc.nl

**Date** : 2020-03-23

**Project** : project_handler

**Code that creates a module out of the the code**

"""
import os
import sys
from subprocess import check_output

from setuptools import find_packages, setup

# Main path
root = os.path.dirname(os.path.abspath(__file__))

# Get long description
try:
    long_description = ''
    readme_path = os.path.join(root, 'README.md')
    with open(readme_path, 'r') as readme_handler:
        long_description += readme_handler.read()
except:
    long_description = ''


# Get version
try:
    command = 'git --git-dir {}/.git rev-parse HEAD'.format(
        root
    )
    with os.popen(cmd=command) as stream:
          version = stream.read()[:-1]
except:
    version='pytest'

# Get requirements
try:
    requirements_path = os.path.join(root, 'requirements.txt')
    with open(requirements_path, 'r') as requirements_handler:
        requirements = [
            dependency
            for dependency in requirements_handler.readlines()
            if not 'project_handler' in dependency
        ]
except:
    requirements=[]

setup(
    name='project_handler',
    author='Robin Camarasa',
    version=version,
    packages=find_packages(),
    description='project_handler is a tiny librairie that handles project management',
    long_description=long_description,
    install_requires=requirements,
    author_email='r.camarasa@erasmusmc.nl',
    entry_points={
        'console_scripts':[
            'newpythonproject = project_handler.entry_points:newpythonproject',
            'applyconfig = project_handler.entry_points:applyconfig',
        ]
    }
)

