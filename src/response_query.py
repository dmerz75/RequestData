import os
import requests
import json
import re


def extend_url(base_url, *args):

    url_components = [base_url] + [x for x in args]
    nielsen_url = ''.join(url_components)

    return nielsen_url


def request_api(url, params, headers):

    # Request & get response = requests.get(url=myurl, params=params, headers=)
    response = requests.get(url, params=params, headers=headers)
    response_code = int(re.search(r"\d+", str(response)).group())

    # print('Response[code]:', response_code)

    # if response_code == 200:
    #     print("Completed:" + str(len(str(response.content))))
    # else:
    #     print(query, "  Query Failed.")
    #     print(str(response.content))

    # Response:
    # print('Response:', response,type(response))
    # print('Headers:', response.request.headers)

    # if response_code != 200:
    #     print("response_code: ", response_code)
    #     print("response:\n", response.content)
    #     return None, None
    # else:
    #     print("response_code: ", response_code, " content: ", len(str(response.content)))

    return response, response_code


def get_response_content(response, file_type='json'):

    if file_type == 'json':
        content = json.dumps(str(response.content))
    else:
        content = str(response.content)

    return content


def fix_nielsen_content(content):

    pos = content.find("[")
    pos2 = max([pos for pos, char in enumerate(content) if char == "]"])
    # print(pos,pos2)
    # text = text[pos+1:pos2] # remove []
    text = content[pos:pos2+1]
    # keep []
    text = text.replace("\\", '')
    # print(text)
    return text


def save_response_content(filename, content, path=None):

    if path is not None:
        write_path = os.path.join(path, filename)
    else:
        write_path = filename

    # if file_type == 'json':
    #     content = json.dumps(str(response.content))
    # else:
    #     content = str(response.content)

    try:
        with open(write_path, "w") as fp:
            fp.write(content)
        print("{}  written successfully.".format(filename))
        # return cfg['delay']
    except IOError:
        print("{}  write FAILED.".format(filename))
        return 0
    return

def empty_file_content(filename, path=None):

    if path is not None:
        write_path = os.path.join(path, filename)
    else:
        write_path = filename

    try:
        with open(write_path, "w") as fp:
            fp.write('')
        print("{}  emptied.".format(filename))
    except IOError:
        print("{}  not emptied.".format(filename))
        return 0
    return
