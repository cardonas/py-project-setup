import os

from py_project_setup.main import create_gitignore


def test_create_gitignore(create_test_dir):
    test_dir = create_test_dir
    expected_path = os.path.join(test_dir, ".gitignore")
    create_gitignore(test_dir)
    assert os.path.exists(expected_path)
    with open(expected_path, "r") as file:
        actual_contents = file.read()
    assert actual_contents == expected_gitignore


expected_gitignore = """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# test
.tox/
.pytest_cache/
result.xml

# Ultraedit
*.bak

# PyCharm
.idea/
*.pem
*.pfx

# Visual Studio
.vscode/

# virtual env
venv*/*

# build
*.egg-info
/dist
build

#pytest-cov
.coverage

# mypy
.mypy_cache"""
