import subprocess

def run_command(invocation):
    # print(type(invocation),invocation)
    pipe = subprocess.Popen(invocation, stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = pipe.communicate()
    print('stdout >> ', stdout)
    if stderr != None:
        print('stderr >> ', stderr)


def push_file(src, dest):
    # print(commands)
    # print(src)
    # print(dest)
    # command_dir = ['hdfs', 'dfs', '-mkdir -p']
    command_dir = ['hadoop', 'fs', '-mkdir', '-p']
    command_dir.append(dest)
    run_command(command_dir)

    command_put = ['hdfs', 'dfs', '-put']
    command_put.append(src)
    command_put.append(dest)
    run_command(command_put)