import sys
import argparse
import importlib


class Application:
    '''
    A general application for python job control.
    '''
    def __init__(self, job):
        '''
        An application.
        '''
        self.job = job
        # self.job_args = self_get_args()
        # self._printAttributes()
        # self.job = self._run_job(job_name)
        # _get_args()
        # _printAttributes()
        # _run_job()
    # def _printAttributes(self):

    def _printAttributes(self):
        keys = dir(self)
        for key in keys:
            print(key, ':\t', getattr(self, key))

    def _get_args(self):
        # print(sys.argv)
        parser = argparse.ArgumentParser()
        parser.add_argument("-j", "--job", help="The Job Name, like DataETL")
        parser.add_argument("-n", "--job_name", help="The Job Key: Nielsen")
        parser.add_argument("-t", "--job_type", help="The Job Key: programRatings")
        parser.add_argument("-d", "--date", help="A Date: YYYY-MM-DD. ex. 2019-03-25")
        args = vars(parser.parse_args())
        self.args = args

    def _run_job(self):
        # print(sys.argv)
        print(self.job)

        # Importing our job script
        job_module = importlib.import_module('src.{}'.format(self.job))

        # Calling the main method of our job
        job_module.main(self)

    # def run():
    #     self._get_args()
    #     self._run_job()
