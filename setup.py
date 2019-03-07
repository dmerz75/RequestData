#!/usr/bin/env python

# from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='RequestData',
    version='0.1',
    description='Python Request Data',
    author='Dale Merz',
    author_email='merz.d@pg.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dmerz75/RequestData",
    install_requires=[
        "requests",
        "json",
        ],
    packages=setuptools.find_packages('main_etl'),
)

# setuptools.setup(
#     name="example-RequestData-merz.d",
#     version="0.0.1",
#     description="A small request data package",
#     author="Dale Merz",
#     author_email="merz.d@pg.com",
#     long_description=long_description,
#     long_description_content_type="text/markdown",
#     url="https://github.com/dmerz75/RequestData",
#     packages=setuptools.find_packages(),
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
# )

        #   "requests==0.10.4",
        #   "pyspark==2.2.0",
        #   "pyspark_shared_libs_8451==1.0.19"


#   packages=['distutils', 'distutils.command'],
#   py_modules=['resources'],
#   )

# setup(name='Distutils',
#       version='1.0',
#       description='Python Distribution Utilities',
#       url='https://www.python.org/sigs/distutils-sig/',
#       packages=['distutils', 'distutils.command'],
#      )
