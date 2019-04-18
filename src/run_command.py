import subprocess

def run_command(invocation):
    # return True
    # print(type(invocation),invocation)
    try:
        pipe = subprocess.Popen(invocation,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = pipe.communicate()
        print('stdout >> ', stdout)
        # print('stderr >> ', stderr)

        if stderr is not None:
            print('stderr >> ', stderr)
            return False
        else:
            return True
    except FileNotFoundError:
        print("Unable to execute: ", invocation)
        return False

def run_command2(invocation):
    pipe = subprocess.Popen(invocation,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    stdout, stderr = pipe.communicate()
    return stdout, stderr