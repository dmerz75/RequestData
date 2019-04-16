#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
# import requests
# import json
# import re
import itertools
# from pprint import pprint
from datetime import datetime
from datetime import timedelta
from src.response_query import extend_url, request_api, save_response_content
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
    # job_type = 'originators'
    # job_type = 'demographics'
    # job_type = 'marketBreaks'
    # job_type = 'dataAvailability'

    # Configurations: params, headers
    config = cfg[job_name][job_type]
    output_dir = config['output_dir'] + job_type
    outfile_type = config['output_file_type']
    date_format = config['date_format']
    delay = config['delay']
    base_url = config['url']
    params = config['params']
    headers = config['headers']

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print("job_name: ", job_name)
    print("job_type: ", job_type)
    print("Destination: ", output_dir)
    print('base_url: ', base_url)

    # Date:
    num_weeks = 3 # 2-6
    start_date = datetime.strptime(params['startDate'][0], date_format)
    date_list = [str(start_date + timedelta(days=-1*6*i))[0:10] for i in range(2, num_weeks)]
    print(len(date_list), date_list)

    # Generate all combinations of queries to the url api.
    queries = [params[pm] for pm in params.keys() if pm != 'startDate']
    # print(queries)
    queries.insert(1, date_list)
    it_list = itertools.product(*queries)
    print(it_list)


    combinations = list(itertools.product(*queries))
    print("Number of combinations: ", len(combinations))
    print("Example: ", combinations[0])
    count_files_exist = 0
    start_index = 0
    sys .exit()

    for i, combo in enumerate(combinations[start_index:]):
        # print(i, combo)
        # continue
        i += start_index

        # Build query:
        query = ''.join(combo) + '.' + outfile_type
        # query = query.replace('%2B3','_')
        query = query.replace('%', '_')
        query = query.replace(' ', '')
        query = query.replace('/', '')
        if os.path.exists(os.path.join(output_dir, query)):
            count_files_exist += 1
            continue

        print(i, " of ", len(combinations))

        # Date:
        start_date, end_date = get_date_range(combo[1], days=-6)
        print('Dates: ', start_date, " - ", end_date)
        # print(combo)
        # break

        # Build url:
        my_url = ''
        my_url = extend_url(base_url, 'sample=', combo[0], '&')
        if job_type not in ['marketBreaks', 'dataAvailability']:
            my_url = extend_url(my_url, 'startDate=', start_date, '&')
            my_url = extend_url(my_url, 'endDate=', end_date, '&')

        for i, k in enumerate(params.keys()):
            if k in ['sample', 'startDate', 'endDate']:
                continue
            my_url = extend_url(my_url, '{}='.format(k), combo[i], '&')

        # strip final '&'
        my_url = my_url[0:-1]
        print(my_url)
        sys.exit()

        # Request & Save!
        response, response_code = request_api(my_url, None, headers)
        save_response_content(query, response, path=output_dir, file_type=outfile_type)
        # # max 15 per minute.
        time.sleep(delay)

    print("Files that exist: ", count_files_exist)
