#!/usr/bin/env bash

# example:
# python ['main.py', '-j', 'DataETL', '-n', 'Nielsen', '-t', 'programRatings', '-d', '2019-03-13']

# output:
#DataETL
#job_name:  Nielsen
#job_type:  programRatings
#Destination:  api_programRatings
#base_url:  https://api.developer.nielsen.com/watchapi/national/analytics/api/v1/programRatings?
#Dates:  1 ['2019-03-13']

run_local ()
{
    python main.py -j DataETL \
    -n Nielsen \
    -t programRatings \
    -d 2019-03-13
}

run_cluster ()
{
    # programRatings, commercialRatings, demographics, originators, marketBreaks, dataAvailability
    klist || kinit
    /home/merz.d/activestate/py36/bin/python3.6 main.py \
    -j DataETL \
    -n Nielsen \
    -t programRatings \
    -d 2019-03-25
}

#run_local
run_cluster