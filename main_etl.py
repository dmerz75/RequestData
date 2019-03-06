#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import os
# import sys
# import time
import requests
import json
from pprint import pprint
# from resources.databases import config as config
from resources.NielsenTechnicalAPI import nielsen_config as config


def main(job_name):

    # Receive URL, params.
    myurl = config[job_name]['url']
    params = config[job_name]['params']
    print(myurl)
    pprint(params)

    # Get request, keep response object
    response = requests.get(url=myurl, params=params)
    # r = requests.get(urls['TestingSite']['url'],
    #                  auth = (urls['TestingSite']['user'],
    #                          urls['TestingSite']['password'])
    print('response:', response)


    # Read, Load, Save in json format
    # data = r.json() # after token is received.
    # with open('NielsenLibs/NielsenSampleData.json',encoding='utf-8') as f:
    #     # data = json.load(f)['ProgramRatings']
    #     data = json.load(f)

    # print('Data:\n',data,type(data))
    # # print(data['ProgramRatings'])
    # # print(type(data['ProgramRatings']))

    # program = data['ProgramRatings'][0]
    # print(program,type(program))
    # print('Keys:\n',program.keys())


if __name__ == '__main__':
    # main(sys.argv[1])
    main('TestingSite')