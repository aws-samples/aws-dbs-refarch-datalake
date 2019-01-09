from datetime import datetime
import boto3
import os

s3 = boto3.client('s3')
target_bucket = os.environ['TARGET_S3_BUCKET']
target_s3_prefix = os.environ['TARGET_S3_PREFIX']# Please don't use '/' at the end of TARGET_S3_PREFIX variable

def lambda_handler(event, context):

    print("Initializing S3 copy utility for DMS...")
    for object in event['Records']:
        try:
            input_bucket_name=object['s3']['bucket']['name']
            input_key = object['s3']['object']['key']
            print("Initializing copy of input file: s3://{}/{}".format(input_bucket_name, input_key))
            input_file_basename = os.path.basename(object['s3']['object']['key'])
            if target_s3_prefix is None or target_s3_prefix == '':
                partitioned_prefix = s3.head_object(Bucket=input_bucket_name,Key=input_key)['LastModified'].strftime("/year=%Y/month=%m/day=%d/hour=%H/")
            else:
                partitioned_prefix =  target_s3_prefix + s3.head_object(Bucket=input_bucket_name,Key=input_key)['LastModified'].strftime("/year=%Y/month=%m/day=%d/hour=%H/")
                #S3 headObject API is used to fetch LastModified metadata from the S3 object.
            print("Starting copy of input S3 object to s3://{}/{}/{}".format(target_bucket, partitioned_prefix, input_file_basename))
            s3.copy_object(CopySource = {'Bucket': object['s3']['bucket']['name'], 'Key': object['s3']['object']['key']}, Bucket=target_bucket, Key=partitioned_prefix + input_file_basename )
            print("S3 key was successfully copied to {}".format(target_bucket))

        except Exception as e:
            print(e)
            print('Error copying object to {}'.format(target_bucket))
            raise e
