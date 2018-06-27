from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.rst')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'resosuma', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='resosuma',
    version=version['__version__'],
    description=('A module providing mappings of the '
                 'research software sustainability space.'),
    long_description=long_description,
    author='Stephan Druskat',
    author_email='mail@sdruskat.net',
    url='https://github.com/research-software/resosuma',
    license='Apache-2.0',
    packages=['resosuma', 'resosuma.graph'],
    install_requires=[
        'graphviz==0.8.3'
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.6']
)
