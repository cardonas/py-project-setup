import os

from py_project_setup.main import create_setup_cfg
from pytest import mark

expected_contents_with_private = """[metadata]
name = py_project_setup_test
version = attr: py_project_setup_test.__version__
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/cardonas/py-project-setup
author = Steven Cardona
author_email = cardona.sj@gmail.com
license = MIT
license_file = LICENSE
classifiers =
\tPrivate :: Company
\tLicense :: OSI Approved :: MIT License
\tProgramming Language :: Python :: 3
\tProgramming Language :: Python :: 3 :: Only
\tProgramming Language :: Python :: 3.9
\tProgramming Language :: Python :: 3.10
\tProgramming Language :: Python :: Implementation :: CPython
\tTopic :: Utilities
descriptions = Tool to generate a python project skeleton

[options]
packages = find:
python_requires = >=3.9
package_dir =
    =src
setup_requires =
    packaging

[options.packages.find]
where = src

[options.entry_points]
console_scripts =
    setup-py-project-test = py_project_setup_test.main:main

[options.extras_require]
toml =
    toml

[bdist_wheel]
universal = True

[mypy]
check_untyped_defs = True
disallow_any_generics = True
disallow_incomplete_defs = True
disallow_untyped_defs = True
no_implicit_optional = True
warn_redundant_casts = True
warn_unused_ignores = True

[mypy-tests.*]
disallow_untyped_defs = False"""

expected_contents_without_private = """[metadata]
name = py_project_setup_test
version = attr: py_project_setup_test.__version__
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/cardonas/py-project-setup
author = Steven Cardona
author_email = cardona.sj@gmail.com
license = MIT
license_file = LICENSE
classifiers =
\tLicense :: OSI Approved :: MIT License
\tProgramming Language :: Python :: 3
\tProgramming Language :: Python :: 3 :: Only
\tProgramming Language :: Python :: 3.9
\tProgramming Language :: Python :: 3.10
\tProgramming Language :: Python :: Implementation :: CPython
\tTopic :: Utilities
descriptions = Tool to generate a python project skeleton

[options]
packages = find:
python_requires = >=3.9
package_dir =
    =src
setup_requires =
    packaging

[options.packages.find]
where = src

[options.entry_points]
console_scripts =
    setup-py-project-test = py_project_setup_test.main:main

[options.extras_require]
toml =
    toml

[bdist_wheel]
universal = True

[mypy]
check_untyped_defs = True
disallow_any_generics = True
disallow_incomplete_defs = True
disallow_untyped_defs = True
no_implicit_optional = True
warn_redundant_casts = True
warn_unused_ignores = True

[mypy-tests.*]
disallow_untyped_defs = False"""


@mark.parametrize(
    "private_org, python_versions, expected_contents",
    [
        ["Company", ["py39", "py310"], expected_contents_with_private],
        [None, ["py310", "py39"], expected_contents_without_private],
    ],
)
def test_create_setup_cfg(
    create_test_dir, private_org, python_versions, expected_contents
):
    test_dir = create_test_dir
    params = {
        "long_description_file": "README.md",
        "long_description_file_type": "markdown",
        "url": "https://github.com/cardonas/py-project-setup",
        "author": "Steven Cardona",
        "author_email": "cardona.sj@gmail.com",
        "license": "MIT",
        "license_file": "LICENSE",
        "python_versions": python_versions,
        "topic": "Utilities",
        "description": "Tool to generate a python project skeleton",
        "entry_point_name": "setup-py-project-test",
    }
    if private_org:
        params["private_org"] = private_org
    create_setup_cfg(test_dir, params)
    with open(os.path.join(test_dir, "setup.cfg"), "r") as file:
        actual_contents = file.read()
    assert actual_contents == expected_contents
