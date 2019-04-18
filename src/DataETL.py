#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import itertools
from datetime import datetime
from datetime import timedelta
from src.response_query import extend_url, request_api, get_response_content
from src.response_query import save_response_content, fix_nielsen_content, empty_file_content
from src.cluster import push_file
from src.run_command import run_command
from src.date_range import get_date_range
from lib.NielsenTechnicalAPI import nielsen_config as cfg


def main(app):
    '''
    Set configurations.
    Build a date list.
    Build the url.
    Request data from url.
    '''
    job_name = app.args['job_name']
    job_type = app.args['job_args'][0]
    # print(app.args)
    # job_type = 'programRatings'
    # 'commercialRatings' 'originators' 'demographics' 'marketBreaks' 'dataAvailability'

    # Configurations: params, headers
    config = cfg[job_name][job_type]
    positions = cfg[job_name]['positions']
    output_dir = config['output_dir'] + job_type
    cluster_dir = config['cluster_dir']
    outfile_type = config['output_file_type']
    date_format = config['date_format']
    delay = config['delay']
    base_url = config['url']
    params = config['params']
    headers = config['headers']
    num_weeks = config['num_weeks']
    first_run = 0

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print("job_name: ", job_name)
    print("job_type: ", job_type)
    print("Destination: ", output_dir)
    print('base_url: ', base_url)

    # Date:
    # start_date = datetime.strptime(config['startDate'], date_format)
    start_date = datetime.strptime(app.args['job_args'][1], date_format)
    date_list = [str(start_date + timedelta(days=-1*6*i))[0:10] for i in range(0, num_weeks)]
    print('Dates: ', len(date_list), date_list)
    # sys.exit()

    # Generate all combinations of queries to the url api.
    # keys = sorted(['contributions', 'dataStreams', 'demographics', 'mediaSources', 'originators', 'sample', 'startDate'])
    # order = [6, 4, 2, 5, 3, 0, 1]
    # korder = list(sorted(zip(order, keys)))
    # print(keys)
    # print(korder)
    # korder = sorted([k for k in korder if k[1] in params.keys()])
    # print(korder)
    # queries = [params[pm[1]] for pm in korder]
    # queries = [params[pm[1]] for pm in korder if pm != 'startDate']
    queries = [params[pm] for pm in params.keys() if pm != 'startDate']
    queries.insert(1, date_list)
    combinations = list(itertools.product(*queries))
    print("Number of combinations: ", len(combinations))
    print("Example: ", combinations[0])
    count_files_exist = 0
    start_index = 0

    for i, combo in enumerate(combinations[start_index:]):
        # print(i, combo)
        # if i != 623:
        #     continue
        i += start_index

        # Build query:
        query = ''.join(combo) + '.' + outfile_type
        query = query.replace('%', '_')
        query = query.replace(' ', '')
        query = query.replace('/', '')

        print(i, " of ", len(combinations))

        # Date:
        start_date, end_date = get_date_range(combo[1], days=-6)
        print('Dates: ', start_date, " - ", end_date)
        date_dir = os.path.join(output_dir, end_date)
        if not os.path.exists(date_dir):
            os.makedirs(date_dir)
        # print(combo)
        # break

        # Existence check:
        query_file = os.path.join(date_dir, query)
        if os.path.exists(query_file):
            count_files_exist += 1
            continue

        # Build url:
        my_url = ''
        my_url = extend_url(base_url, 'sample=', combo[0], '&')
        if job_type not in ['marketBreaks', 'dataAvailability']:
            my_url = extend_url(my_url, 'startDate=', start_date, '&')
            my_url = extend_url(my_url, 'endDate=', end_date, '&')

        for k in params.keys():
            if k in ['sample', 'startDate', 'endDate']:
                continue
            # print(k)
            # print(positions[k])
            # print(combo)
            my_url = extend_url(my_url, '{}='.format(k), combo[positions[k]], '&')
            # print(my_url)

        # strip final '&'
        my_url = my_url[0:-1]
        # print(my_url)
        # sys.exit()

        # Request & Save!
        response, response_code = request_api(my_url, None, headers)
        if response_code != 200:
            continue
        else:
            content = get_response_content(response)

        text = fix_nielsen_content(content)
        save_response_content(query, text, date_dir)

        # cluster
        dest_dir = os.path.join(cluster_dir, job_type, end_date)
        if first_run == 0:
            command_dest_dir = ['hadoop', 'fs', '-mkdir', '-p', dest_dir]
            result = run_command(command_dest_dir)
            first_run += 1
            if not result:
                print(result)
                # sys.exit(1)

        result = push_file(query_file, dest_dir)
        if result:
            empty_file_content(query_file)
        else:
            print(query_file, " -->  REMOVED!")
            os.remove(query_file)

        # save_response_content(query, response, response_text, output_dir, outfile_type)
        # max 15 per minute.
        time.sleep(delay)

    print("Files that exist: ", count_files_exist)
