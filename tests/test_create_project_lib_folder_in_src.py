from __future__ import annotations

import os
import shutil

from py_project_setup.main import create_dunder_init_in_project_lib_folder
from py_project_setup.main import create_project_lib_folder_in_src


def test_create_project_lib_folder_in_src(create_test_dir):
    test_dir = create_test_dir
    src_path = test_dir.joinpath("src")
    src_path.mkdir()
    expected = src_path.joinpath("py_project_setup_test")
    actual = create_project_lib_folder_in_src(test_dir)
    assert actual == expected
    shutil.rmtree(test_dir)


def test_create_dunder_init_in_project_lib_folder(create_test_dir):
    test_dir = create_test_dir
    project_lib = test_dir.joinpath("src")
    project_lib.mkdir()
    project_lib = project_lib.joinpath("py_project_setup_test")
    project_lib.mkdir()
    final_path = project_lib.joinpath("__init__.py")
    create_dunder_init_in_project_lib_folder(project_lib)
    assert os.listdir(project_lib) == ["__init__.py"]
    with open(final_path, "r") as file:
        line = file.readline()
    assert line == '__version__ = "0.0.1"'
