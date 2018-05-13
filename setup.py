from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'nsga-2',
  version = '0.1',
  description = 'A NSGA-II implementation',
  long_description='A NSGA-II implementation',
  url='https://github.com/baopng/NSGA-II',
  author='Pham Ngo Gia Bao, Tram Loi Quan, Quan Thanh Tho, Akhil Garg',
  author_email='ngogiabaopham@gmail.com',
  packages = find_packages(exclude=['contrib', 'docs', 'tests']),
  keywords='nsga2 nsga ga multi-objective',
  license='MIT',
)
