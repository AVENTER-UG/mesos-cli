try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

from distutils.command.install import install
import os
import json

here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, "README.md")) as f:
        README = f.read()
except UnicodeDecodeError:
    with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        README = f.read()
config = {
    'name': 'mesos',
    'version': '@PACKAGE_VERSION@',
    'description': 'Python bindings for mesos',
    'author': 'Apache Mesos',
    'author_email': 'dev@mesos.apache.org',
    'url': 'http://pypi.python.org/pypi/mesos',
    'packages': [ 'mesos' ],
    'package_dir': { '': 'src' },
    'install_requires': [
        'mesos.interface == @PACKAGE_VERSION@',
        'mesos.native == @PACKAGE_VERSION@'
    ],
    'license': 'Apache 2.0',
    'keywords': 'mesos',
    'classifiers': [ ]
}

setup(
    name="mesos-cli",
    version="1.11.0",
    description="Python bindings for mesos",
    long_description=README,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    packages=[ 'lib', 'bin' ],
    package_dir={ '': 'cli' },
    author="Apache Mesos",
    author_email="support@aventer.biz",
    url="https://www.aventer.biz/",
    python_requires=">=3.6",
)
