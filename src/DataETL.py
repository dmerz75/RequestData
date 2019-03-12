#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import requests
import json
import re
import itertools
# import random
from datetime import datetime
from datetime import timedelta
from pprint import pprint

from src.nielsen_response import *
from lib.NielsenTechnicalAPI import nielsen_config as config
# from lib.originators import


def main(app):

    # job_type
    job_name = app.args[0]

    # Receive URL, params.
    base_url = config[job_name]['url']
    final_url = config[job_name]['urlfinal']
    params = config[job_name]['params'] # headers
    headers = config[job_name]['headers']
    print('base_url:\n', base_url)

    # Date:
    start_date = datetime.strptime(params['startDate'][0], '%Y-%m-%d')
    # date_list = [str(start_date)[0:10]]
    date_list = [str(start_date + timedelta(days=-1*6*i))[0:10] for i in range(2,3)]
    print(date_list)
    # sys.exit()

    # Originators:
    # print(params['originators'])
    if 0:
        originators = json.load(open('lib/originators.json'))
        params['originators'] = [o['originator'] for o in originators]
        print(params['originators'])
    # sys.exit()


    queries = [params['sample'],
               date_list,
               params['demographics'],
               params['originators'],
               params['dataStreams'],
               params['mediaSources'],
               params['contributions']]
    combinations = list(itertools.product(*queries))
    print("The total number of combinations: ",len(combinations))
    # print(combinations[0:3])
    # sys.exit()

    start_index = 0
    for i,combo in enumerate(combinations[start_index:]):
        i += start_index
        # print(i)

        # Query / File exists?
        query = re.sub(' ', '', ''.join(combo)) + '.json'
        query = re.sub('\/', '', query)
        if os.path.exists(os.path.join('api_downloads',query)):
            continue
        # print(query)
        # sys.exit()

        # Date:
        end_dt = datetime.strptime(combo[1], '%Y-%m-%d')
        start_dt = end_dt + timedelta(days=-6)
        end_date = str(end_dt)[0:10]
        start_date = str(start_dt)[0:10]
        # print(start_dt, end_dt)
        print(i," of ",len(combinations),' dates:  ', start_date, "  ", end_date)
        # break

        my_url = ''
        my_url = build_nielsen_url(base_url,'sample=',combo[0],'&')
        my_url = build_nielsen_url(my_url,'startDate=',start_date,'&')
        my_url = build_nielsen_url(my_url,'endDate=',end_date,'&')
        my_url = build_nielsen_url(my_url,'demographics=',combo[2],'&')
        my_url = build_nielsen_url(my_url,'originators=',combo[3],'&')
        my_url = build_nielsen_url(my_url,'dataStreams=',combo[4],'&')
        my_url = build_nielsen_url(my_url,'mediaSources=',combo[5],'&')
        my_url = build_nielsen_url(my_url,'contributions=',combo[6])
        print(my_url)
        # break
        # print(final_url)
        # print('test:', my_url == final_url)
        # sys.exit()

        # Request & Save!
        response, response_code = request_nielsen(my_url,None,headers)
        if response_code != 200:
            print("This query:\n\t",query,"\n  Failed.")
            print(str(response.content))
            # continue
        else:
            save_nielsen_json(query,response,path='api_downloads')

        # max 15 per minute.
        time.sleep(1.1)