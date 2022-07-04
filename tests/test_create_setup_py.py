import os
import shutil

from py_project_setup.main import create_setup_py


def test_create_setup_py(create_test_dir):
    test_dir = create_test_dir
    expected_contents = """from setuptools import setup

setup()
"""
    create_setup_py(test_dir)
    assert os.listdir(test_dir) == ["setup.py"]
    with open(os.path.join(test_dir, "setup.py"), "r") as file:
        actual = file.read()
    assert actual == expected_contents
    shutil.rmtree(test_dir)
