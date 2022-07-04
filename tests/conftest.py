from pathlib import Path
from shutil import rmtree

from pytest import fixture


@fixture()
def create_test_dir() -> Path:
    current_dir = Path.cwd().joinpath("py-project-setup-test")
    if current_dir.exists():
        rmtree(current_dir)
    current_dir.mkdir()
    yield current_dir
