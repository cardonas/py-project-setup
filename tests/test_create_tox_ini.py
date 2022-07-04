import os

from py_project_setup.main import create_tox_ini


def test_create_tox_ini(create_test_dir):
    test_dir = create_test_dir
    python_version_list = ["py39", "py310", "py311"]
    expected_path = os.path.join(test_dir, "tox.ini")
    create_tox_ini(test_dir, python_version_list)
    assert os.path.exists(expected_path)
    with open(expected_path, "r") as file:
        actual_content = file.read()
    assert actual_content == expected_tox_ini


expected_tox_ini = """[tox]
envlist = py39, py310, py311

[pytest]
minversion = 6.0
testpaths =
    tests

[testenv]
deps = pytest
commands =
    pytest -vv {posargs:--junitxml=result.xml}

[testenv:pre-commit]
skip_install = true
deps = -rrequirements-dev.txt
commands =
    pre-commit run --all-files

[testenv:build]
skip_install = true
deps =
    build
    path.py
commands =
    python -c "import path; path.Path('dist').rmtree_p()"
    python -m build --wheel

[testenv:release]
skip_install = true
passenv =
    TWINE_USERNAME
    TWINE_PASSWORD
setenv =
    TWINE_REPOSITORY_URL="Need url for deploying to a package repository"
deps =
    build
    path.py
    twine
commands =
    python -c "import path; path.Path('dist').rmtree_p()"
    python -m build --wheel
    python -m twine upload dist/* {posargs}

[testenv:local]
skip_install = true
deps = -rrequirements-dev.txt
setenv =
    PYTHONPATH = {toxinidir}/src
commands =
    pytest {posargs}"""
