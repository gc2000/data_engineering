import os
import boto3
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

aws_access_key_id = os.getenv("ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("SECRET_ACCESS_KEY")
aws_session_token = os.getenv("SESSION_TOKEN")
BUCKET_NAME = os.getenv("BUCKET_NAME")

session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token
)