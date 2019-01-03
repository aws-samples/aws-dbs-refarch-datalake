# Query Data lake using EMR and External Hive Metastore in VPC

## Overview

[Amazon EMR](https://aws.amazon.com/emr/) is a managed Hadoop framework in AWS. Hive is a data infrastructure tool to process structured/semistructured data in Hadoop using SQL like query language. Hive stores and manages schema metadata using a 'metastore' service backed by a relational database. In a datalake environment, it is essential to have a centralized schema repository which translates storage locations on S3 or HDFS into a model of Databases, Tables, and Partitions that can be used in SQL. Most AWS customers [leverage AWS Glue](../multi-emr-on-glue-catalog) as an external catalog due to ease of use. However, customers may want to set up their own self-managed Data Catalog due to reasons outlined [here](../../../README.md).

In this architecture, we will provide a walkthrough of how to set up a centralized schema repository using EMR with [Amazon RDS Aurora](https://aws.amazon.com/rds/aurora). Once created, multiple EMR clusters can execute queries against the same schema metadata. To avoid accidental schema metadata loss/corruption, it is recommended that you provide database write access to one EMR cluster only.

![Query Data lake using EMR and External Hive Metastore](analytics-emr-hive-metastore.png)

## Architecture  Walkthrough


1. RDS database is used to store metadata information in a VPC.
2. Single EMR Cluster is set up with Hive metastore on RDS database in same VPC but preferably in a different subnet and [security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html). This EMR cluster has write access on the the database. The permissions can be managed using database users.
3. Multiple EMR clusters can be deployed with read-only access to schema metadata on the database. These EMR clusters can execute queries against the S3 using an [Internet Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) or [S3 Endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-s3.html) on the VPC.

## References

* [Setting up an external database as metastore on EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hive-metastore-external.html)
