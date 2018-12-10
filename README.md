# AWS Datalake  Reference Architectures

## Overview

A data lake is a data repository that stores data in its raw format until it is used for analytics. A data lake is designed to store massive amount of data at scale. A schema to the data is given as part of transformation while reading it from the data lake.

![Datalake Overview](src/data-lake-overview.png)


A data lake is ideally designed with the following characteristics:

* **Schema less**: A data lake stores structured, semi-structured and unstructured data in the same format as it is generated in the source systems. Such sources systems can be SQL. NoSQL databases, audio/video files or free form text entered to applications. It provides a way to describe any large data pool in which the schema and data requirements are not defined until the data is queried: “just in time” or “**schema on read**”
* **All data in one place:**  Data lakes are designed to store all data in one place.  They allow *collection of data *that you may or may not use for analytics.
* It stores unlimited amounts of data in any format **inexpensively.**
* **It complements enterprise data warehouse(EDW) **and is commonly a data source for the EDW – capturing all data but only passing relevant data to the EDW
* Allows for data exploration without data model design and ingestion (**Quick user access**)

## S3 : A storage service for Datalake



Amazon S3 provides an optimal foundation for a data lake because of its virtually unlimited capacity and scalability. You can seamlessly increase storage from gigabytes to petabytes of content without availability disruption and paying only for what you use. Amazon S3 is designed to provide 99.999999999% durability. It has scalable performance, ease-of-use features, and native encryption and access control capabilities. Amazon S3 integrates with a broad portfolio of AWS and third-party ISV data processing tools.

Key data lake-enabling features of Amazon S3 include the following:


* **Storage and compute is decoupled** – In traditional Big Data and data warehouse solutions, storage and compute are tightly coupled. With Amazon S3, you can cost-effectively store data in read-optimised formats. You can then launch as many or as few virtual servers as you need using Amazon Elastic Compute Cloud (EC2), and you can use AWS analytics tools to process your data. You can optimize your EC2 instances to provide the right ratios of CPU, memory, and bandwidth for best performance.
* **Centralized data architecture** – Amazon S3 makes it easy to build a multi-tenant environment, where many users can bring their own data analytics tools to a common set of data. This improves both cost and data governance over that of traditional solutions, which require multiple copies of data to be distributed across multiple processing platforms.
* **Integration with other AWS services** – Use Amazon S3 with Amazon Athena, Amazon Redshift Spectrum, Amazon Rekognition, and AWS Glue to query and process data. Amazon S3 also integrates with AWS Lambda serverless computing to run code without provisioning or managing servers. With all of these capabilities, you only pay for the actual amounts of data you process or for the compute time that you consume.
* **Standardized APIs** – Amazon S3 RESTful APIs are simple, easy to use, and supported by most major third-party independent software vendors (ISVs), including leading Apache Hadoop and analytics tool vendors. This allows customers to bring the tools they are most comfortable with and knowledgeable about to help them perform analytics on data in Amazon S3.
* **Data security and data protection** – Data security in AWS is controlled by IAM. Fine grained access control on S3 objects can be defined by using IAM  users, roles and groups. Tagging can be used to manage access on group of objects.  S3 protects data by server side encryption(SSE) and Client side encryption (CSE) with KMS key or custom managed key.

## Working with Data Schemas

The earliest challenges that inhibited building a data lake were keeping track of all of the raw assets as they were loaded into the data lake, and then tracking all of the new data assets and versions that were created by data transformation, data processing, and analytics. Thus, an essential component of an Amazon S3-based data lake is the data catalog. The data catalog provides a query-able interface of all assets stored in the data lake’s S3 buckets. The data catalog is designed to provide a single source of truth about the contents of the data lake.

 There are two general forms of a data catalog: a comprehensive data catalog that contains information about all assets that have been ingested into the S3 data lake, and a Hive Metastore Catalog (HCatalog) that contains information about data assets that have been transformed into formats and table definitions that are usable by analytics tools like Amazon Athena, Amazon Redshift, Amazon Redshift Spectrum, and Amazon EMR. The two catalogs are not mutually exclusive and both may exist. The comprehensive data catalog can be used to search for all assets in the data lake, and the HCatalog can be used to discover and query data assets in the data lake.

### Datalake schema management with AWS Glue catalog

<table><tr><td><a href="/src/multi-az"><img src="/src/multi-az/thumbnail.png"/></a></td><td></td></tr></table>


### Data security and access control


## Data Ingestion

One of the core values of a data lake is that it is the collection point and repository for all of an organization’s data assets, in whatever their native formats are. This enables quick ingestion, elimination of data duplication and data sprawl, and centralized governance and management. After the data assets are collected, they need to be transformed into normalized formats to be used by a variety of data analytics and processing tools.

 The key to ‘democratizing’ the data and making the data lake available to the widest number of users of varying skill sets and responsibilities is to transform data assets into a format that allows for efficient ad hoc SQL querying. As discussed earlier, when a data lake is built on AWS, we recommend transforming log-based data assets into Parquet format. AWS provides multiple services to quickly and efficiently achieve this.


### Using Kinesis firehose and Kinesis producer library (KPL)

### Ingestion using AWS Glue

### Capture DB changes using DMS (Database Migration Service)

## Data Analytics

### Multiple AWS EMR clusters in VPC

#### Hive metastore on EMR

#### Glue Catalog

### AWS Athana on Glue Catalog

### Redshift Spectrum on Glue Catalog
