import os
import shutil

from py_project_setup import main


def test_create_pyproject_toml(create_test_dir):
    test_dir = create_test_dir
    expected_contents = """[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"""
    main.create_pyproject_toml(test_dir)
    assert os.listdir(test_dir) == ["pyproject.toml"]
    with open(os.path.join(test_dir, "pyproject.toml"), "r") as file:
        actual_contents = file.read()
    assert actual_contents == expected_contents
    shutil.rmtree(test_dir)
