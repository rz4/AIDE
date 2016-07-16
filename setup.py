#! /usr/bin/env python3

__author__ = 'Rafael Zamora, rz4@hood.edu'


from setuptools import setup, find_packages

setup(
    name="PyAIDE",
    version="0.9.1",
    description="Python library for the development and testing of intelligent agents.",
    license="GNU",
    keywords="Artificial Intelligence Testing Development",
    packages=find_packages(exclude=['images','examples']),
    install_requires = ["pygame"],
)
