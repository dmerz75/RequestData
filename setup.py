#!/usr/bin/env python

# from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='RequestData',
    version='0.1',
    description='Request Data API',
    author='Dale Merz',
    author_email='merz.d@pg.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dmerz75/RequestData",
    install_requires=[
        "requests",
        "json",
        ],
    # packages=setuptools.find_packages('main'),
    packages = ['lib', 'shared', 'main'],
)
