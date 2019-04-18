from src.run_command import run_command

def get_file_list(dest):
    """
    :param dest: the directory being queried
    :return: the file listing for the dest directory
    """
    print(dest)

def push_file(src, dest):
    # return False
    # print(commands)
    # print(src)
    # print(dest)
    # command_dir = ['hdfs', 'dfs', '-mkdir -p']
    # command_dir = ['hadoop', 'fs', '-mkdir', '-p']
    # command_dir.append(dest)
    # run_command(command_dir)
    command_put = ['hdfs', 'dfs', '-put']
    command_put.append(src)
    command_put.append(dest)
    result = run_command(command_put)
    return result