#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import requests
import json
import re
import itertools
from pprint import pprint
from datetime import datetime
from datetime import timedelta
from src.response_query import *
from src.date_range import get_date_range
from lib.NielsenTechnicalAPI import nielsen_config as cfg


def main(app):
    '''
    Set configurations.
    Build a date list.
    Build the url.
    Request data from url.
    '''

    job_name = app.args[0]
    job_type = 'programRatings'
    # job_type = 'commercialRatings'

    # Configurations: params, headers
    config = cfg[job_name][job_type]
    output_dir = config['output_dir'] + job_type
    outfile_type = config['output_file_type']
    date_format = config['date_format']
    delay = config['delay']
    base_url = config['url']
    params = config['params']
    headers = config['headers']

    print("job_name: ", job_name)
    print("job_type: ", job_type)
    print("Destination: ", output_dir)
    print('base_url: ', base_url)


    # Date:
    num_weeks = 6
    start_date = datetime.strptime(params['startDate'][0],date_format)
    date_list = [str(start_date + timedelta(days=-1*6*i))[0:10] for i in range(2, num_weeks)]
    print(len(date_list), date_list[0:3])


    # Generate all combinations of queries to the url api.
    queries = [params[pm] for pm in params.keys()]
    queries.append(date_list)
    combinations = list(itertools.product(*queries))
    print("Number of combinations: ", len(combinations))
    print("Example: ", combinations[0])


    start_index = 0

    for i, combo in enumerate(combinations[start_index:]):

        i += start_index

        # Build query:
        query = ''.join(combo) + '.' + outfile_type
        query = query.replace(' ', '')
        query = query.replace('/', '')
        if os.path.exists(os.path.join(output_dir, query)):
            continue

        print(i, " of ", len(combinations))

        # Date:
        start_date, end_date = get_date_range(combo[1],days=-6)
        print('Dates: ', start_date, " - ", end_date)


        # Build url:
        my_url = ''
        my_url = extend_url(base_url,'sample=',combo[0],'&')
        my_url = extend_url(my_url,'startDate=',start_date,'&')
        my_url = extend_url(my_url,'endDate=',end_date,'&')
        my_url = extend_url(my_url,'demographics=',combo[2],'&')
        my_url = extend_url(my_url,'originators=',combo[3],'&')
        my_url = extend_url(my_url,'dataStreams=',combo[4],'&')
        my_url = extend_url(my_url,'mediaSources=',combo[5],'&')
        my_url = extend_url(my_url,'contributions=',combo[6])
        print(my_url)


        # Request & Save!
        response, response_code = request_api(my_url, None, headers)
        save_response_content(query, response, path=output_dir, file_type =outfile_type)
        time.sleep(delay) # max 15 per minute.