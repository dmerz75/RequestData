#!/bin/bash

LOCAL=$1
YEAR=$2
REMOTE=/enterprise_data/dev/tv_media/nielsen_api/raw/

commercial () {
  echo hdfs dfs -ls $REMOTE/$LOCAL/$YEAR | wc -l
  echo ls api_$LOCAL/$YEAR/* | wc -l
}

commercial
