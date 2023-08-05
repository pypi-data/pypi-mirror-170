from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'This package can make temp email from https://inboxkitten.com/'
LONG_DESCRIPTION = 'This package can make temp email from https://inboxkitten.com/'

# Setting up
setup(
    name="inboxkitten",
    version=VERSION,
    author="Tufaah",
    author_email="yazanemails@gmail.com",
    description=DESCRIPTION,
    project_urls={
        "Github": "https://github.com/01270/inboxkitten",
    },
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['inboxkitten','inbox','kitten','temp mail', 'temp', 'temp email', 'email', 'emails'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)