#!/usr/bin/env python3
# coding: utf-8
"""Installation script for pydimacs"""


from setuptools import setup, find_packages


setup(
    name="pydimacs",
    version="0.1",
    description="Python API to manipulate CNF DIMACS formulas",
    packages=find_packages(),
    setup_requires=[],
    install_requires=['networkx', 'click'],
    tests_require=[],
    license="Apache 2",
    author="Robin David",
    classifiers=[
        'Environment :: Console',
        'Operating System :: OS Independent',
    ],
    test_suite="",
    scripts=['bin/pydimacs'],
)
