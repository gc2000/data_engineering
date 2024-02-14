import json, os
from download import download_file
from upload import upload_s3
import environment_variables

def lambda_handler(event, context):
    file = '2015-01-01-15.json.gz'
    download_res = download_file(file)
    bucket = environment_variables.BUCKET_NAME
    upload_res = upload_s3 (
        download_res.content, 
        bucket, 
        file)
    return upload_res