# -*- coding: utf-8 -*-
from setuptools import setup

REPOSITORY = 'https://github.com/shoeffner/openccg-gum-cooking'

setup(
    name='owl2types',
    version='1.0',
    description='Converts owl files to OpenCCG types.xml files.',
    author='Sebastian Höffner',
    author_email='shoeffner@tzi.de',
    url=REPOSITORY,
    entry_points={
        'console_scripts': [
            'owl2types = owl2types:owl2types',
        ],
    },
    py_modules=['owl2types'],
    package_dir={'': 'tools'},
    install_requires=[
        'owlready2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
)
