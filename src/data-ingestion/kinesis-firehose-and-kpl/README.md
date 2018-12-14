# Data Ingestion using Kinesis Firehose and Kinesis Producer Library(KPL)

## Overview
Kinesis is a  scalable and managed real-time data streaming service. Kinesis firehose is fully managed service that delivers data from Kinesis streams to target locations like S3. Kinesis Producer Library(KPL) is an application that writes data to Kinesis stream with high throughput. In this example, KPL is used to write data to kinesis stream from the producer application. Kinesis Firehose batches incoming records into files and delivers them to S3 based on file buffer size/time limit defined in Firehose configuration.

![Ingestion using Kinesis Firehose and KPL](ingestion-kinesis-and-kpl.png)

## Architecture Component Walkthrough

1. EC2 instances within a VPC with Kinesis Producer Library to collect records and write to Kinesis/ Kinesis Firehose stream.

2. Kinesis Firehose with VPC endpoint in the above mentioned VPC.

3. Kinesis firehose role with write access to target S3 bucket.

4. S3 datalake to store incoming records as file objects with partition based on record incoming timestamp.
