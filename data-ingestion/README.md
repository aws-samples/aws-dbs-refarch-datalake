# Ingestion Architectures for Datalakes on AWS

### Overview

One of the core values of a data lake is that it is a collection point and repository for all of an organizations data assets, in whatever their native formats are. This enables quick ingestion, elimination of data duplication and data sprawl, and centralized governance and management. After data assets are collected, they need to be transformed into normalized formats to be used by a variety of data analytics and processing tools. During this phase, customers will typically choose to standardize on a scheme for data compression, encryption of their data, and layout of information at the prefix level in S3.

The key to ‘democratizing’ data, and making it available to the widest number of users - of varying skill sets and responsibilities - is to transform data assets into a format that allows for efficient ad hoc SQL queries. As discussed earlier, when a data lake is built on AWS, we recommend transforming log-based data assets into Columnar formats. AWS provides multiple services to quickly and efficiently achieve this.

 In this section, we would share some of the common architectural patterns for ingestion that we see with  many of our customers' data lakes.

### Reference _Architectures for Ingesting Data into a Data Lake_

1. _\*\*\*\*_[_**Ingest events and logs data using Kinesis Firehose**_](kinesis-firehose-and-kpl.md)_\*\*\*\*_
2. _\*\*\*\*_[_**Ingest database changes using Database Migration Service**_](dms-and-lambda.md)_\*\*\*\*_
3. _\*\*\*\*_[_**Ingest data from JDBC sources using Amazon Glue**_](aws-glue.md)_\*\*\*\*_
4. _\*\*\*\*_[_**Ingest datafiles using Amazon DataSync**_](aws-datasync-on-prem-nfs.md)_\*\*\*\*_

