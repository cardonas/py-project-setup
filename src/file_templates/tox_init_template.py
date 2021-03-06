tox_ini_template = r"""[tox]
envlist = {envlist}

[pytest]
minversion = 6.0
testpaths =
    tests

[testenv]
deps = pytest
commands =
    pytest -vv {{posargs:--junitxml=result.xml}}

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
    python -m twine upload dist/* {{posargs}}

[testenv:local]
skip_install = true
deps = -rrequirements-dev.txt
setenv =
    PYTHONPATH = {{toxinidir}}/src
commands =
    pytest {{posargs}}"""
