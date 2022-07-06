from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from file_templates import setup_cfg_templates
from file_templates.gitignore_template import gitignore_template
from file_templates.pre_commit_config_template import pre_commit_config_template
from file_templates.pyproject_toml_template import pyproject_toml_template
from file_templates.requirements_dev_txt_template import requirements_dev_txt_template
from file_templates.setup_py_template import setup_py_template
from file_templates.tox_init_template import tox_ini_template


def main() -> int:
    raise NotImplementedError


def create_root_level_structure(current_working_dir: str | Path) -> None:
    root_level_files = [
        "setup.cfg",
    ]
    root_level_dirs = ["src", "tests"]
    for file in root_level_files:
        with open(os.path.join(current_working_dir, file), "w") as writer:
            pass  # creating empty files
    for my_dir in root_level_dirs:
        os.mkdir(os.path.join(current_working_dir, my_dir))


def reformat_project_name(current_working_dir: Path) -> str:
    project_name = current_working_dir.parts[-1]
    return project_name.replace(
        "-", "_"
    )  # Todo: implement to support other naming formats


def create_project_lib_folder_in_src(current_working_dir: Path) -> Path:
    project_name = reformat_project_name(current_working_dir)
    lib_path = Path(os.path.join(current_working_dir.joinpath("src"), project_name))
    lib_path.mkdir()
    return lib_path


def create_dunder_init_in_project_lib_folder(lib_path: Path) -> None:
    with open(lib_path.joinpath("__init__.py"), "w") as file:
        file.write('__version__ = "0.0.1"')


def create_setup_py(current_working_dir: Path) -> None:
    with open(os.path.join(current_working_dir, "setup.py"), "w") as file:
        file.write(setup_py_template)


def create_pyproject_toml(current_working_dir: Path) -> None:
    with open(os.path.join(current_working_dir, "pyproject.toml"), "w") as file:
        file.write(pyproject_toml_template)


def create_contribution_md(current_working_dir: Path) -> None:
    with open(os.path.join(current_working_dir, "CONTRIBUTION.md"), "w"):
        pass  # Create empty file


def create_readme_md(current_working_dir: Path) -> None:
    with open(os.path.join(current_working_dir, "README.md"), "w"):
        pass  # Create empty file


def create_requirements_dev_txt(current_working_dir: Path) -> None:
    with open(os.path.join(current_working_dir, "requirements-dev.txt"), "w") as file:
        file.write(requirements_dev_txt_template)


def create_tox_ini(current_working_dir: Path, py_versions: list[str]) -> None:
    template = tox_ini_template.format(envlist=", ".join(py_versions))
    with open(os.path.join(current_working_dir, "tox.ini"), "w") as file:
        file.write(template)


def create_gitignore(current_working_dir: Path) -> None:
    with open(os.path.join(current_working_dir, ".gitignore"), "w") as file:
        file.write(gitignore_template)


def create_pre_commit_config(current_working_dir: Path) -> None:
    with open(
        os.path.join(current_working_dir, ".pre-commit-config.yaml"), "w"
    ) as file:
        file.write(pre_commit_config_template)


def create_setup_cfg(current_working_dir: Path, params: dict[str, Any]) -> None:

    if not params:
        return
    project_name = reformat_project_name(current_working_dir)
    version_nums = [int(version[2:]) for version in params["python_versions"]]
    version_nums.sort()
    with open(os.path.join(current_working_dir, "setup.cfg"), "w") as file:
        file.write(
            setup_cfg_templates.meta_data_headers.format(
                project_name=project_name,
                description_file=params["long_description_file"],
                description_file_type=params["long_description_file_type"],
                project_url=params["url"],
                author_name=params["author"],
                author_email=params["author_email"],
            )
            + "\n"
        )
        if "license" in params:
            file.write(
                setup_cfg_templates.setup_license.format(license=params["license"])
                + "\n"
            )
            file.write(
                setup_cfg_templates.license_file.format(
                    license_file=params["license_file"]
                )
                + "\n"
            )
        file.write("classifiers =\n")
        if "private_org" in params:
            file.write(
                setup_cfg_templates.private_classifier.format(org=params["private_org"])
                + "\n"
            )
        if "license" in params:
            file.write(
                setup_cfg_templates.license_classifier.format(license=params["license"])
                + "\n"
            )
        file.write(setup_cfg_templates.python_constant_classifiers + "\n")
        for version_num in version_nums:
            _version = version_to_decimal(version_num)
            file.write(
                setup_cfg_templates.python_version_classifier_template.format(
                    py_version=str(_version) + "0" if version_num == 310 else _version
                )
                + "\n"
            )
        file.write(setup_cfg_templates.implementation_classifier + "\n")
        file.write(
            setup_cfg_templates.topic_classifier.format(topic=params["topic"]) + "\n"
        )
        if "description" in params:
            file.write(f"descriptions = {params['description']}\n\n")
        file.write(
            setup_cfg_templates.options.format(
                py_version=version_to_decimal(version_nums[0])
            )
            + "\n\n"
        )
        file.write(
            setup_cfg_templates.console_scripts.format(
                entry_name=params["entry_point_name"], project_name=project_name
            )
            + "\n\n"
        )
        file.write(setup_cfg_templates.extras_require + "\n\n")
        file.write(setup_cfg_templates.bdist_and_mypy)


def version_to_decimal(version_num: int) -> int:
    return version_num / pow(10, len(str(version_num)) - 1)


if "__main__" == "main":
    raise SystemExit(main())
