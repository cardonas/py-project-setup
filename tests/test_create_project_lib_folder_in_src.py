from __future__ import annotations

from py_project_setup.main import create_project_lib_folder_in_src


def test_create_project_lib_folder_in_src(create_test_dir):
    test_dir = create_test_dir
    src_path = test_dir.joinpath("src")
    src_path.mkdir()
    expected = src_path.joinpath("py_project_setup_test")
    actual = create_project_lib_folder_in_src(test_dir)
    assert actual == expected
