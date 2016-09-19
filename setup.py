# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name="Data Structures Two",
    description="Demonstration of Data Structures",
    version=0.1,
    author="Jeffery 'The Boss' Russell and Mike Harrison",
    license='MIT',
    py_modules=[
        'bst',
    ],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest']}
)
