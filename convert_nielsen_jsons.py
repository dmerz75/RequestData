#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import re
from glob import glob
import json

my_dir = os.path.abspath(os.path.dirname('__file__'))

# subdir = 'api_programRatings'
subdir = 'api_commercialRatings'
outdir = subdir + '_json'
if not os.path.exists(outdir):
        os.makedirs(outdir)

lst_api_raw = glob(os.path.join(my_dir, subdir, '*.json'))

for json_file in lst_api_raw:

    base_name = os.path.basename(json_file)
    write_path = os.path.join(outdir,base_name)
    # write_path = write_path.replace('%2B3','_')
    write_path = write_path.replace('%','_')
    # print(write_path)
    # break

    with open(json_file,'r+') as fp:

        text = fp.read()
        pos = text.find("[")
        pos2 = max([pos for pos, char in enumerate(text) if char == "]"])
        # print(pos,pos2)

        # text = text[pos+1:pos2] # remove []
        text = text[pos:pos2+1] # keep []

        text = text.replace("\\",'')
        # print(text)

    with open(write_path,'w+') as fo:
        fo.write(text)
    # break

    # json_data = json.loads(text)
    # print(type(json_data),len(json_data))
    # print(json_data.keys())

    # for k,v in json_data.items():
    #     print(k,len(v))