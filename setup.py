import re
from os.path import join, dirname

from setuptools import setup, find_packages


with open(join(dirname(__file__), 'coding-style', '__init__.py')) as v_file:
    package_version = re.compile('.*__version__ = \'(.*?)\'', re.S)\
        .match(v_file.read()).group(1)


dependencies = [
    'restfulpy >= 2.7.3',
]


setup(
    name='coding-style',
    author='mohammad',
    author_email='mohammad',
    version=package_version,
    install_requires=dependencies,
    packages=find_packages(),
    test_suite='coding-style.tests',
    entry_points={
        'console_scripts': [
            'coding-style = coding-style:coding-style.cli_main'
        ]
    }
)

