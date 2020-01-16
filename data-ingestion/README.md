# Ingestion Architectures for Datalakes on AWS

Customer applications generate various types of data in the form in form of database change logs, database snapshots, user events, logs etc. Ingesting these datasets with almost no transformation is an important function of a datalake. In this section, we would share some of the common architectural patterns for ingestion that we see with  many of our customers' data lakes.

### Reference _Architectures for Ingesting Data into a Data Lake_

1. _\*\*\*\*_[_**Ingest events and logs data using Kinesis Firehose**_](kinesis-firehose-and-kpl.md)_\*\*\*\*_
2. _\*\*\*\*_[_**Ingest database changes using Database Migration Service**_](dms-and-lambda.md)_\*\*\*\*_
3. _\*\*\*\*_[_**Ingest data from JDBC sources using Amazon Glue**_](aws-glue.md)_\*\*\*\*_
4. _\*\*\*\*_[_**Ingest datafiles using Amazon DataSync**_](aws-datasync-on-prem-nfs.md)_\*\*\*\*_

