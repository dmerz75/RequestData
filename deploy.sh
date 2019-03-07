#!/usr/bin/env bash
# python setup.py sdist bdist_wheel
python setup.py bdist_wheel
scp dist/* s1:~/jobs
scp dist/* s2:~/jobs