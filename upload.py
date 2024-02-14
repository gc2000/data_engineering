import os
import boto3
import requests
import environment_variables

# aws_access_key_id=environment_variables.aws_access_key_id
# aws_secret_access_key=environment_variables.aws_secret_access_key
# aws_session_token=environment_variables.aws_session_token

# Create a boto3 session with your temporary credentials
# session = boto3.Session(
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
#     aws_session_token=aws_session_token
# )

# os.environ.setdefault('AWS_DEFAULT', 'gc')
# s3_client = boto3.client('s3')
# file = '2021-01-29-0.json.gz'
def get_client():
    s3_client = environment_variables.session.client('s3') 
    return s3_client

def upload_s3(body, bucket, file):
    s3_client = get_client()
    print ("Bucket:", type(bucket))
    print ("File:", type(file))
    print ("Body:", type(body))
    res = s3_client.put_object(Bucket=bucket, Key=file, Body=body)
    return res