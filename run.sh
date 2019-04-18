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
    echo "Running local."
    python main.py -j 'DataETL' \
    -n Nielsen \
    -t programRatings \
    -d 2019-03-13
}

run_cluster ()
{
    echo "Running cluster."
}

run_local
#run_cluster