#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import requests
from NielsenLibs.NielsenTechnicalAPI import urls
import json
from pprint import pprint
# import PyPDF2
# import urllib.request
# from NielsenLibs import NielsenSampleData # foo, SampleData, ProgramRatings

# Begin here!
print("\nExe:\n",sys.executable)

def main():
    # import urls as dict
    # print(urls)
    # print(urls.keys())
    # print(urls['get'].keys())
    # print(urls['get']['DataAvailability'])

    # Perform Requests: (for now, only "ProgramRatings")
    # myurl = urls['get']['ProgramRatings']
    # defining a params dict for the parameters to be sent to the API
    # params = {'example':''}

    # 1
    # myurl = urls['ProgramRatings']['url']
    # params = urls['ProgramRatings']['params']
    # 2
    myurl = urls['TestingSite']['url']
    params = urls['TestingSite']['params']

    print(myurl)
    pprint(params)

    # sending get request and saving the response as response object
    r = requests.get(url=myurl,params=params)
    # r = requests.get(urls['TestingSite']['url'],
    #                  auth = (urls['TestingSite']['user'],
    #                          urls['TestingSite']['password'])
    print('request:',r)

    # print("urllib:")
    # request = urllib.request.urlopen('https://demo.ckan.org/api/3/action/dashboard_activity_list')
    # request.add_header('Authorization', 'XXX')
    # response_dict = json.loads(urllib2.urlopen(request, '{}').read())

    # # extracting data in json format
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

    sys.exit()

    # creating a pdf file object
    pdf_file = open('Nielsen Audience API v1.3 Technical Reference.pdf','rb')

    pdfReader = PyPDF2.PdfFileReader(pdf_file)
    print(pdfReader.numPages)

    fields = pdfReader.getFields()
    pageObj = pdfReader.getPage(0)

    print(fields) # none

    text = pageObj.extractText()
    print(text)
    # text = pdf_file.read()
    # print(text)

    # closing the pdf file object
    pdf_file.close()
    pass


if __name__ == '__main__':
    main()

# #!/usr/bin/env python
# import urllib2
# import urllib
# import json
# import pprint

# # Put the details of the dataset we're going to create into a dict.
# dataset_dict = {
#     'name': 'my_dataset_name',
#     'notes': 'A long description of my dataset',
#     'owner_org': 'org_id_or_name'
# }

# # Use the json module to dump the dictionary to a string for posting.
# data_string = urllib.quote(json.dumps(dataset_dict))

# # We'll use the package_create function to create a new dataset.
# request = urllib2.Request('http://www.my_ckan_site.com/api/action/package_create')

# # Creating a dataset requires an authorization header.
# # Replace *** with your API key, from your user account on the CKAN site
# # that you're creating the dataset on.
# request.add_header('Authorization', '***')

# # Make the HTTP request.
# response = urllib2.urlopen(request, data_string)
# assert response.code == 200

# # Use the json module to load CKAN's response into a dictionary.
# response_dict = json.loads(response.read())
# assert response_dict['success'] is True

# # package_create returns the created package as its result.
# created_package = response_dict['result']
# pprint.pprint(created_package)
