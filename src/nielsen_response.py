import os
import sys
import requests
import json
import re


def build_nielsen_url(base_url,*args):

    url_components = [base_url] + [x for x in args]
    nielsen_url = ''.join(url_components)
    return nielsen_url


def request_nielsen(url,params,headers):

    # Request & get response = requests.get(url=myurl, params=params, headers=)
    response = requests.get(url,params=params,headers=headers)

    response_code = int(re.search(r"\d+",str(response)).group())

    # Response:
    # print('Response:', response,type(response))
    print('Response[code]:', response_code)
    # print('Headers:', response.request.headers)
    print("Completed:" + str(len(str(response.content))))

    return response, response_code


def save_nielsen_json(filename,response,path=None):

    json_content = json.dumps(str(response.content))

    if path != None:
        write_path = os.path.join(path,filename)
    else:
        write_path = filename

    try:
        with open(write_path,"w") as fp:
            fp.write(json_content)
        print("{}\n\twas written.".format(filename))
    except:
        print("{}\n\twas FAILED to write.".format(filename))
        # print("", filename, "\n was NOT written.")
    # fp.close()
    return
