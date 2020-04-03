"""
**Author** : Robin Camarasa

**Institution** : Erasmus Medical Center

**Position** : PhD student

**Contact** : r.camarasa@erasmusmc.nl

**Date** : 2020-03-23

**Project** : project_handler

**File that test scripting module**
"""
import os
import shutil

from project_handler import MODULE
from project_handler.scripting.test_manager import set_test_folders
from project_handler.entry_points import *
from project_handler.settings import RESSOURCES_ROOT, TEST_ROOT
from click.testing import CliRunner


@set_test_folders(
    current_module=MODULE, ressources_root=RESSOURCES_ROOT,
    output_root=TEST_ROOT
)
def test_new_python_project(
        ressources_file_structure: dict, output_root: str
) -> None:
    """
    Function that test new_python_project

    :return: None
    """
    cli_runner = CliRunner()
    assert cli_runner.invoke(
        newpythonproject,
        [
            '--path', output_root, '--git-url',
            'https://github.com/RobinCamarasa/python_module.git'
        ]
    ).exit_code == 0
    for dir_ in [
        'results', 'python_module', 'related_documents', 'python_module_env'
    ]:
        assert os.path.isdir(os.path.join(output_root, dir_))

    for file_ in [
        '.config.json'
    ]:
        assert os.path.isdir(os.path.join(output_root, dir_))


@set_test_folders(
    current_module=MODULE, ressources_root=RESSOURCES_ROOT,
    output_root=TEST_ROOT
)
def test_apply_config(
        ressources_file_structure: dict, output_root: str
) -> None:
    """
    Function that test apply_config

    :return: None
    """
    cli_runner = CliRunner()
    assert cli_runner.invoke(
        newpythonproject,
        [
            '--path', output_root, '--git-url',
            'https://github.com/RobinCamarasa/python_module.git'
        ]
    ).exit_code == 0

    cli_runner = CliRunner()
    assert cli_runner.invoke(
        applyconfig, ['-p', output_root]
    ).exit_code == 0
