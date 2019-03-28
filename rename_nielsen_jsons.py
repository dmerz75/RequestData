#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from glob import glob
import shutil

my_dir = os.path.abspath(os.path.dirname('__file__'))

# subdir = 'api_programRatings'
# subdir = 'api_commercialRatings'
# subdir = 'tests/data'
subdir = sys.argv[1]
print("Searching directory: ", subdir)
# sys.exit()

lst_api_raw = glob(os.path.join(my_dir, subdir, '*.json'))

for json_file in lst_api_raw:

    if '%' in json_file:
        # .contains("%"):
        # print(json_file)
        # new_file = json_file.replace('%2B3','_')
        new_file = json_file.replace('%','_')
        shutil.copy(json_file, new_file)
        os.remove(json_file)

    # if os.path.exists(new_file):
    #     os.remove(json_file)
    # else:

    # os.rename(json_file,new_file)
