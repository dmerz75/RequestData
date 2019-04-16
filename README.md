# RequestData
Retrieve data from websites

## Workflow
Facilitate the download of data from a host API, process/transform it, write it, repeat in a non-duplicated manner. 

### GET, POST
Retrieve data via an API.

### Params
Import a dictionary with the following keys:
- output_dir: download directory
- output_file_type: json, csv etc.
- delay: used if the API limits the query rate
- date_format: ex. %Y-%m-%d
- url: the host API address 
- headers: Authorization tokens, requirements.
- params: queried parameters.

### Process
Manipulate the downloaded content to match an acceptable structured format.

### Write
Write/save the data in a manageable way for upload to HDFS.


