#!/usr/bin/env python
import boto3
import boto
from datetime import timedelta, datetime
import math
from boto.s3.connection import S3Connection

[default]
region = us-east-1

s3_connection = S3Connection(
    aws_access_key_id = 'AWS_ACCESS_KEY_ID',
    aws_secret_access_key = 'AWS_SECRET_ACCESS_KEY'
)

cloudwatch = boto3.client('cloudwatch')
s3 = boto3.resource('s3')

def bucket_size_cloudwatch(bucket):
    try:
        return cloudwatch.get_metric_statistics(
            Namespace='AWS/S3', MetricName='BucketSizeBytes',
            StartTime=datetime.utcnow() - timedelta(days=7) ,
            EndTime=datetime.utcnow(), Period=86400,
            Statistics=['Average'], Unit='Bytes',
            Dimensions=[
                {'Name': 'BucketName', 'Value': bucket},
                {u'Name': 'StorageType', u'Value': 'StandardStorage'}
            ])['Datapoints'][0]['Average']
    except IndexError:
        return 0
    
def convertSize(size):
    if size == 0:
        return '0B'
    size_name = ("B", "KB", "MB", "GB", "TB", "PB")
    i = int(math.floor(math.log(size,1024)))
    p = math.pow(1024,i)
    s = round(size/p,2)
    if (s > 0):
        return '{0} {1}'.format(s,size_name[i])
    else:
        return '0B'
        
def obj_last_modified():
    for bucket in s3.buckets.all():
        for obj in bucket.objects.all(): 
            return obj.last_modified
            

def s3_analisys():
    buckets = list(s3.buckets.all())
    for bucket in buckets:
        #print(bucket.objects.all())
        print('Name: {0} | Creation Date: {1} | Objects: {2} | Size: {3} | Last Modified: {4}'.format(bucket.name, bucket.creation_date, len(list(bucket.objects.all())), convertSize(bucket_size_cloudwatch(bucket.name)), obj_last_modified()))
        print('--------------------------')


if __name__ == '__main__':
    s3_analisys()

   