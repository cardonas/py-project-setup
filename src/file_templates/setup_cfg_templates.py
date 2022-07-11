meta_data_headers = """[metadata]
name = {project_name}
version = attr: {project_name}.__version__
long_description = file: {description_file}
long_description_content_type = text/{description_file_type}
url = {project_url}
author = {author_name}
author_email = {author_email}"""


setup_license = "license = {license}"
license_file = "license_file = {license_file}"

license_classifier = "\tLicense :: OSI Approved :: {license} License"

python_constant_classifiers = """\tProgramming Language :: Python :: 3
\tProgramming Language :: Python :: 3 :: Only"""

python_version_classifier_template = (
    """\tProgramming Language :: Python :: {py_version}"""
)

implementation_classifier = (
    "\tProgramming Language :: Python :: Implementation :: CPython"
)

topic_classifier = "\tTopic :: {topic}"

private_classifier = "\tPrivate :: {org}"

options = """[options]
packages = find:
python_requires = >={py_version}
package_dir =
    =src
setup_requires =
    packaging

[options.packages.find]
where = src"""

console_scripts = """[options.entry_points]
console_scripts =
    {entry_name} = {project_name}.main:main"""

extras_require = """[options.extras_require]
toml =
    toml"""

bdist_and_mypy = """[bdist_wheel]
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
