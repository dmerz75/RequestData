#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
from lib.hdfs_config import config as hdfs_config
from src.run_command import run_command2

def main(app):
    """
    :param app: the point of entry for Application
    :return:
    """
    job_name = app.args['job_name']
    config = hdfs_config[job_name]
    date = app.args['job_args'][0]
    print(job_name, date)

    path = os.path.join(config['path'], job_name, date)
    local_path = os.path.join(config['prefix'] + job_name, date)
    print(path)
    print(local_path)

    # Get File List!
    command = ['hdfs', 'dfs', '-ls', path]
    stdout, stderr = run_command2(command)
    stdout = stdout.decode("utf-8")
    if stderr is not None:
        print(stderr)
        sys.exit(1)

    lines = stdout.split("\n")
    hdfs_list = []

    for i, line in enumerate(lines):
        # print(i, line)
        hdfs_list.append(line.split("/")[-1])

    local_list = os.listdir(local_path)

    # Delete from local:
    # del_list = local_list - hdfs_list
    del_list = [x for x in local_list if x not in hdfs_list]

    print("hdfs:      ", len(hdfs_list))
    print("local:     ", len(local_list))
    print("to delete: ", len(del_list))

    for fp in del_list:
        print(fp)
        # os.remove(fp)

