import os
import shutil

from py_project_setup.main import create_requirements_dev_txt


def test_create_requirements_dev_txt(create_test_dir):
    test_dir = create_test_dir
    expected_contents = """black
build
mypy
pre-commit
pytest
tox"""
    expected_path = os.path.join(test_dir, "requirements-dev.txt")
    create_requirements_dev_txt(test_dir)
    assert os.path.exists(expected_path)
    with open(expected_path, "r") as file:
        actual_contents = file.read()
    assert actual_contents == expected_contents
    shutil.rmtree(test_dir)
