---
description: >-
  AWS Lake Formation helps you create a organization wide data catalog on top of
  your data lake for  data security, discovery, metadata management, single
  source of truth and schema management.
---

# Centralized Data Catalog using AWS Lake Formation

Building a datalake for an organization is a difficult task. If done right, it involves many activities such as ingestion, storage, curation, consumption, metadata management, security implementation and many more. AWS Lake Formation makes it easy to set up a secure data lake. Creating a data lake with Lake Formation is simple as it provides building blocks for each lifecycle of a datalake implementation. 

## AWS Lake Formation Definitions

* **Region**: Amazon cloud computing resources are hosted in multiple locations world-wide. These locations are composed of AWS [Regions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html) and Availability Zones. Each AWS Region is a separate geographic area. Each AWS Region has multiple, isolated locations known as Availability Zones.
* **Data Lake**:  A data lake in AWS Lakeformation is a schematic and organized representation of your registered corporate data assets stored in Amazon S3 in the form of databases, tables and columns. 
* **Blueprint**:  AWS Lake formation blueprint is a data ingestion template designed to easily ingest un-transformed data from various data sources like relational dbs\(JDBC\), load balancer logs etc into Amazon S3 to build a datalake. 
* **Data catalog**:  A data catalog  contains information about all assets that have been ingested into or curated in the S3 data lake. It is designed to provide an interface for easy discovery of data assets,  security control and to provide a single source of truth for the contents of a data lake.
  * **User**: An user is a persona who performs an activity on a data lake like creating data assets, provide access to other users etc.
  * **Database:** A database is a namespace withing a data catalog  the catalog metadata resides. 
  * **Table:** A table is a schema representation of a data asset registered in AWS LakeFormation**.**
  * **Column:** A column represents a data attribute and its properties \(like name,datatype, metadata etc\) of a table.

## Designing your Data lake Catalog

The challenges that inhibited building a data lake were keeping track of all  raw assets as they were ingested into S3 and then new data assets and versions that were created by data transformation, data processing, and analytics. So, it became essential to register assets at a single location to easily discover assets, manage metadata and define consistent access control policies for all its consumers. The AWS LakeFormation catalog provides a query-able interface of all assets stored in the data lake’s S3 buckets. 

### How many data catalogs do I need?

Number of catalogs that you need for your corporate is entirely dependent on your use case and analytics culture. However, we highly recommend our customers to build a single data catalog on top of their S3 data lake to avoid data silos, ensure single source of truth and provide users with a single interface for data discovery and metadata management. 

It is possible that customers might have a huge amount of data already stored in S3 in different AWS accounts. You create a single data catalog in one AWS account irrespective of where your data sits. For ease of data discovery, customers may want to organize their data subjects in different **databases** within the same data catalog.  For setting up a single lake formation data catalog with data in different S3 buckets across different AWS accounts, please refer to the blog [here](https://aws.amazon.com/blogs/big-data/access-and-manage-data-from-multiple-accounts-from-a-central-aws-lake-formation-account/).

### How do I organize my data catalog?

The recommended approach for organizing bdata in 

## Securing your data lake







