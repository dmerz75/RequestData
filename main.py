# main.py
import os
import sys
from shared.Application import Application

def main(job):
    App = Application(job)
    App._get_args()
    # App.args = ['Nielsen']
    # App._printAttributes()
    App._run_job()
    sys.exit()


if __name__ == '__main__':
    my_dir = os.path.abspath(os.path.dirname(__file__))
    main(sys.argv[2])
