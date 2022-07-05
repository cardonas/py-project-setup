from __future__ import annotations

import os
import shutil

from py_project_setup.main import create_root_level_structure


def test_create_root_folders(create_test_dir):
    test_dir = create_test_dir
    root_level_files = [
        "tests",
        "setup.cfg",
        "src",
    ]
    create_root_level_structure(test_dir)
    actual = os.listdir(test_dir)
    for item in actual:
        assert item in root_level_files
    shutil.rmtree(test_dir)
