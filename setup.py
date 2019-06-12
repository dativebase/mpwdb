import codecs
import os
import re
from setuptools import find_packages, setup


HERE = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(HERE, 'README.rst')) as readme:
    README = readme.read()



def read(*parts):
    with codecs.open(os.path.join(HERE, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='dativebase-morpho-parser-tutorial',
    version=find_version('mpwdb', '__init__.py'),
    packages=find_packages(),
    include_package_data=True,
    description='Tutorials and code for creating morphological parsers using DativeBase.',
    long_description=README,
    author='Joel Dunham',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'mpwdb = mpwdb:main',
        ],
    },
)
