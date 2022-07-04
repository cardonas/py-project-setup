import os
import shutil

from py_project_setup.main import create_contribution_md
from py_project_setup.main import create_readme_md


def test_create_contribution_md(create_test_dir):
    test_dir = create_test_dir
    create_contribution_md(test_dir)
    assert os.listdir(test_dir) == ["CONTRIBUTION.md"]
    shutil.rmtree(test_dir)


def test_create_readme_me(create_test_dir):
    test_dir = create_test_dir
    create_readme_md(test_dir)
    assert os.listdir(test_dir) == ["README.md"]
    shutil.rmtree(test_dir)
