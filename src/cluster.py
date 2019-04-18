import subprocess

def run_command(invocation):
    # print(type(invocation),invocation)
    try:
        pipe = subprocess.Popen(invocation,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = pipe.communicate()
        print('stdout >> ', stdout)
        # print('stderr >> ', stderr)

        if stderr != None:
            print('stderr >> ', stderr)
            return False
        else:
            return True
    except FileNotFoundError:
        print("Unable to execute: ", invocation)
        return False


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