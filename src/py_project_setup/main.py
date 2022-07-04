from __future__ import annotations

import os
from pathlib import Path

from file_templates.pyproject_toml_template import pyproject_toml_template
from file_templates.setup_py_template import setup_py_template


def main() -> int:
    raise NotImplementedError


def create_root_level_structure(current_working_dir: str | Path) -> None:
    root_level_files = [
        "CONTRIBUTION.md",
        ".pre-commit-config.yaml",
        "README.md",
        "requirements-dev.txt",
        ".gitignore",
        "tox.ini",
        "setup.cfg",
    ]
    root_level_dirs = ["src", "tests"]
    for file in root_level_files:
        with open(os.path.join(current_working_dir, file), "w") as writer:
            pass  # creating empty files
    for my_dir in root_level_dirs:
        os.mkdir(os.path.join(current_working_dir, my_dir))


def create_project_lib_folder_in_src(current_working_dir: Path) -> Path:
    project_name = current_working_dir.parts[-1]
    project_name = project_name.replace(
        "-", "_"
    )  # Todo: implement to support other naming formats
    lib_path = Path(os.path.join(current_working_dir.joinpath("src"), project_name))
    lib_path.mkdir()
    return lib_path


def create_dunder_init_in_project_lib_folder(lib_path: Path) -> None:
    with open(lib_path.joinpath("__init__.py"), "w") as file:
        file.write('__version__ = "0.0.1"')


if "__main__" == "main":
    raise SystemExit(main())


def create_setup_py(current_working_dir: Path) -> None:
    with open(os.path.join(current_working_dir, "setup.py"), "w") as file:
        file.write(setup_py_template)


def create_pyproject_toml(current_workign_dir: Path) -> None:
    with open(os.path.join(current_workign_dir, "pyproject.toml"), "w") as file:
        file.write(pyproject_toml_template)
