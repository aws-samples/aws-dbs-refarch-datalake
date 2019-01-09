# Data Ingestion using Database Migration Service(DMS) and Lambda

## Overview

The [AWS Database Migration Service(DMS)](https://aws.amazon.com/dms/) is a managed service to migrate data into AWS. It can replicate data from operational databases and data warehouses (on premises or AWS) to a variety of targets, including S3 datalakes. In this architecture, DMS is used to capture changed records from relational databases on RDS or EC2 and write them into S3. [AWS Lambda](https://aws.amazon.com/lambda/), a serverless compute service, is used to transform and partition datasets based on their arrival time in S3 for better query performance.

![Data Ingestion using DMS and Lambda](ingestion-dms.png)

## Architecture Component Walkthrough

1. Create a Relational databases on EC2 or RDS within a VPC.
2. Create a Staging S3 location to store changes captured by DMS.
2. [Create a Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html#CHAP_GettingStarted.ReplicationInstance) using the DMS API's or console
3. [Specify the Source & Target Endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html#CHAP_GettingStarted.Endpoints) for the Replication Instance.
4. [Create an IAM role for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html) which has read access on the staging S3 bucket and write access on target datalake location.
4. [Create a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html) to trigger [custom code](staging_to_datalake_loader_lambda.py) execution with `s3:ObjectCreated:*` requests to the staging S3 bucket. The function writes the same objects to the target datalake location on S3 with partitions based on the [`LastModified`](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-metadata) metadata attribute of S3 objects.
2. [Create a DMS Task](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.Creating.html) to migrate data from your source system to target location.
2. The DMS Replication Instance will then connect to the source via [elastic network interface(ENI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html), and write to the S3 staging location. AWS Lambda will receive the PutObject events, and use the [S3 Copy API](https://docs.aws.amazon.com/AmazonS3/latest/dev/CopyingObjectsExamples.html) to reorganise the data into your datalake.
