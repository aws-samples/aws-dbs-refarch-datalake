# Data Ingestion using Amazon Glue

## Overview

[AWS Glue](https://aws.amazon.com/glue/) is a fully managed extract, transform, and load (ETL) service that makes it easy for customers to prepare and load their data for analytics. It can extract data from heterogeneous data sources like RDBMS (RDS, Aurora), Amazon Redshift, Amazon S3 etc and ingest into a data lake. AWS Glue uses spark processing engine under the hood and supports spark APIs to transform data in-memory,

In this architecture, we are using AWS Glue to extract data from relational datasources in a VPC and ingest them in to a S3 data lake backed by S3.

![Data Ingestion Amazon Glue](ingestion-aws-glue.png)

## Architecture Component Walkthrough

1. Relational databases on [RDS]() and/or Aurora within a VPC.

2. Amazon Glue  can connect to the databases using JDBC through an [Elastic Network Interface(ENI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the same VPC.

3. IAM role for Amazon Glue is created with  write access to S3

4.  S3 data lake stores data captured and optionally transformed by Amazon Glue. It is recommended to write structured data to S3 using compressed columnar format like Parquet/ORC for better query performance. Data in structured format like [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) can be converted into compressed columnar format with Pyspark/Scala using spark APIs in ETL Glue.
