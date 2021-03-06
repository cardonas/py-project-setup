gitignore_template = """# Byte-compiled / optimized / DLL files
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
