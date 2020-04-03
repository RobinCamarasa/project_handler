"""
**Author** : Robin Camarasa

**Institution** : Erasmus Medical Center

**Position** : PhD student

**Contact** : r.camarasa@erasmusmc.nl

**Date** : 2020-04-03

**Project** : module_handler

**Settings of module handler**

"""
import sys
import os

# Path used in module handler
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(ROOT_PATH, 'module_handler', 'data')

sys.path.append(ROOT_PATH)

