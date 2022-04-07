import os
from setuptools import setup


def get_long_description():
    with open(
        os.path.join(os.path.dirname(__file__), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="reticulok",
    version="0.1.1",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    description="Python utilities package",
    author="Michael Lok",
    url="https://github.com/michael-lok",
    license="GNU General Public License v3.0"
)
