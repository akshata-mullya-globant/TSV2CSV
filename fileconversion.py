import boto3
import pandas as pd 
import glob
import os
import sys
import io

s3 = boto3.resource("s3")
#s3 = boto3.client("s3")
AWS_REGION = "us-east-2"
S3_BUCKET_NAME = os.getenv("BUCKET_NAME")
S3_KEY_NAME = os.getenv("KEY_NAME")
path = f"s3://{S3_BUCKET_NAME}/{S3_KEY_NAME}"
csv_table = pd.read_table(path,sep='\t',dtype='unicode')
csv_table.to_csv(f"{path}.output.csv",index=False)


