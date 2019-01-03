# AWS Datalake  Reference Architectures

## Overview

A [**data lake**](https://en.wikipedia.org/wiki/Data_lake) is a data repository that stores data in its raw format until it is used for analytics. It is designed to store massive amount of data at scale. A schema to the dataset in data lake is given as part of transformation while reading it. Below is a pictorial representation of a typical data lake on AWS cloud.

![Datalake Overview](src/data-lake-overview.png)

Data lakes are ideally designed with the following characteristics:

* **Schemaless**: They store structured, semi-structured and unstructured data in the same format as it is generated in the source systems. Such source systems can be SQL. NoSQL databases, audio/video files, log files or freeform text stored in  applications. It provides a way to describe any large data pool in which the schema and data requirements are not defined until the data is queried: “just in time” or “**schema on read**”
* **All data in one place:**  Data lakes are designed to store all data in one place.  They allow **collection of data** that you may or may not use for analytics.
* It stores unlimited amounts of data in any format **inexpensively**.
* **It complements enterprise data warehouse(EDW)** and is commonly a data source for the EDW – **capturing all data but only passing relevant data to the EDW**.
* Allows for data exploration without data model design and ingestion to support **quick user access**.

_**Please NOTE**: All content in this reference achitecture has been developed prior to the general availability of [AWS Lake Formation](https://aws.amazon.com/lake-formation). AWS Lake Formation specific content will be added once it is available for production use, and in the meantime please see the [Datalake Solution](https://aws.amazon.com/answers/big-data/data-lake-solution) for a fully automated data lake that you can run as-is, or extend to meet your requirements_

## Amazon Simple Storage Service (S3): Foundation Storage for Datalakes

[**Amazon S3**](https://aws.amazon.com/s3) provides an optimal foundation for a data lake because of its virtually unlimited capacity and scalability. You can seamlessly increase your storage from gigabytes to petabytes without availability disruption and paying only for what you use. Amazon S3 is designed to provide 99.999999999% durability.

 It has **scalable performance, ease-of-use features, and native encryption and access control capabilities**. Amazon S3 integrates with a broad portfolio of AWS and third-party data processing tools.

Key data lake enabling features of Amazon S3 include the following:

* [**Data Security and Protection**](src/data-security-and-protection) – Data security in AWS is controlled by the [Identity and Access Management (IAM) service](https://aws.amazon.com/iam). Fine grained access control on S3 objects can be defined by using IAM users, roles and groups. Tagging can be used to manage access on group of objects. S3 can further protect data through the use of server side encryption (SSE), or Client side encryption (CSE) with KMS key or customer managed keys. 
* **Storage and compute is decoupled** – In traditional big data and data warehouse solutions, storage and compute are tightly coupled in a way that can limit scalability. With Amazon S3, you can cost-effectively store data in original application formats such as XML, JSON, or CSV, as well as read-optimized columnar formats like Parquet and ORC. You can then launch as many or as few virtual servers as you need using Amazon [Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2) or [Elastic MapReduce (EMR)](https://aws.amazon.com/emr/) to process this data. Alternatively, you can use AWS analytics tools like [Amazon Athena](https://aws.amazon.com/athena), [Amazon Redshift](https://aws.amazon.com/redshift) or [AWS Glue](https://aws.amazon.com/glue) to process and analyze your data without having to manage servers. 
* **Centralized data architecture** – Amazon S3 makes it easy to build a multi-tenant environment, where many users can bring their own data analytic tools to a common set of data. This improves both cost and data governance over that of traditional solutions, which require multiple copies of data to be distributed across multiple processing platforms.
* **Integration with other AWS services** – Use Amazon S3 with [Amazon Athena](https://aws.amazon.com/athena/), [Amazon Redshift](https://aws.amazon.com/redshift/), [Amazon Rekognition](https://aws.amazon.com/rekognition/), [Amazon Transcribe](https://aws.amazon.com/transcribe/) and [AWS Glue](https://aws.amazon.com/glue/) etc. to analyze and process data. Amazon S3 also integrates with [AWS Lambda](https://aws.amazon.com/lambda/) serverless computing to run code without provisioning or managing servers. With all of these capabilities, you only pay for the actual amounts of data you process or for the compute time that you consume.
* **Standardized APIs** – [Amazon S3 APIs](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) are simple, easy to use, and supported by most major third-party software tools, including Hadoop, Spark, and Kafka distributions. This allows customers to bring the tools they are most comfortable with and knowledgeable about to perform analytics on data in Amazon S3.

## Schema Management Architectures

Keeping track of all of the raw assets that are loaded into S3, and then tracking all of the new data assets and versions that are created by data transformation, data processing, and analytics can be a major challenge. An essential component of an Amazon S3 based data lake is a data catalog. A data catalog is designed to provide a single source of truth about the contents of the data lake, and rather than end users reasoning about storage buckets and prefixes, a data catalog lets them interact with more familiar structures of databases, tables, and partitions.

There are two general forms of a data catalog:

* Fully Managed: [AWS Glue Catalog](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html) is a fully managed data catalog whose contents are generated by running crawlers over S3 datasets. The Glue Data Catalog contains information about data assets that have been transformed into formats and table definitions that are usable by analytics tools like Amazon Athena, Amazon Redshift, Amazon Redshift Spectrum, and Amazon EMR.
* End User Managed: A Hive Metastore Catalog (HCatalog) provides the ability to consume storage locations on Amazon S3 and on HDFS filesystems through the lanugage of databases and tables. However, it is managed and maintained by the operator of the AWS Account, and can be run through [Amazon EMR and Amazon RDS](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-metastore-external-hive.html). In most cases, AWS does not recommend user managed HCatalogs due to the requirement for you top operate it, as well as the need to scale the solution, and the lack of native integration with some AWS analytic tools.

Customers typically use the managed Glue Crawler to populate the catalog with the contents of Amazon S3. Then, multiple AWS services can run query the contents of the datalake via the Glue catalog.

![Glue Data Catalog](src/working-with-schema/working-with-schemas.png)

### Schema Management with AWS Glue Catalog

AWS Glue Catalog can support datalake schema evolution, which means that it can understand the definition of a table over time, even when new columns and attributes are added. 

<img src="src/working-with-schema/glue-schema-evolution.png" width=700/>

You can read more about dealing with schemas that change over time in the [Athena user guide](https://docs.aws.amazon.com/athena/latest/ug/handling-schema-updates-chapter.html).

### [Data Security and Access Control Architectures](/src/data-security-and-protection)

<table><tr><td><a href="src/data-security-and-protection"><img src="src/data-security-and-protection/data-security-data-protection-using-iam.png"/></a></td><td>Data security and data protection is considered to be of paramount importance for data governance in a datalake. AWS has a extensive set of services to secure data in S3. AWS IAM and AWS KMS are widely used to control access and protect content.</td></tr></table>

## Data Ingestion Architectures

One of the core values of a data lake is that it is a collection point and repository for all of an organization’s data assets, in whatever their native formats are. This enables quick ingestion, elimination of data duplication and data sprawl, and centralized governance and management. After the data assets are collected, they need to be transformed into normalized formats to be used by a variety of data analytics and processing tools.

The key to ‘democratizing’ data, and making it available to the widest number of users - of varying skill sets and responsibilities - is to transform data assets into a format that allows for efficient ad hoc SQL queries. As discussed earlier, when a data lake is built on AWS, we recommend transforming log-based data assets into Columnar formats. AWS provides multiple services to quickly and efficiently achieve this.

### [Using Kinesis Firehose and Kinesis Producer Library (KPL)](/src/data-ingestion/kinesis-firehose-and-kpl)
<table><tr><td><a href="/src/data-ingestion/kinesis-firehose-and-kpl"><img src="/src/data-ingestion/kinesis-firehose-and-kpl/ingestion-kinesis-and-kpl.png"/></a></td><td>Amazon Kinesis is a massively scalable and durable real-time data streaming service. Amazon Kinesis Data Firehose is a fully managed service that delivers data in kinesis streams to target locations like S3. Kinesis firehose is commonly used to ingest data into S3 datalakes and automatically partition them by data arrival timestamp.</td></tr></table>

### [File Ingestion Using AWS Glue](/src/data-ingestion/aws-glue)
<table><tr><td><a href="/src/data-ingestion/aws-glue"><img src="/src/data-ingestion/aws-glue/ingestion-aws-glue.png"/></a></td><td>AWS Glue is a fully managed ETL service that is commonly used to run batch ETL jobs. AWS Glue is the most preferred tool to ingest and transform data in a S3 datalake. This architecture is an example of data extraction from data from RDBMS source and ingestion into a datalake using AWS Glue.</td></tr></table>

### [Capture Database Changes with DMS (Database Migration Service)](/src/data-ingestion/dms-and-lambda)
<table><tr><td><a href="/src/data-ingestion/dms-and-lambda"><img src="/src/data-ingestion/dms-and-lambda/ingestion-dms.png"/></a></td><td>CDC(Change data capture)  from relational databases are a very important dataset that are ingested in datalakes. DMS is a CDC tool that's widely used to capture changes from databases. This architecture demonstrates how to use DMS and AWS Lambda to collect and partition dataset in a datalake.  </td></tr></table>

### [Ingest Data from On-Premise NFS servers using AWS DataSync](/src/data-ingestion/aws-datasync-on-prem-nfs)
<table><tr><td><a href="src/data-ingestion/aws-datasync-on-prem-nfs"><img src="src/data-ingestion/aws-datasync-on-prem-nfs/aws-datasync-from-nfs-on-prem.png"/></a></td><td>AWS DataSync is a fully managed data transfer service that simplifies, automates, and accelerates moving and replicating data between on-premises storage systems and AWS storage services over the internet or AWS Direct Connect. In this architecture we are leveraging AWS DataSync to ingest data into a datalake</td></tr></table>

## Data Analytic Architectures

S3 datalake efficiently decouples storage and compute which makes it is easy to build analytics applications that scale out with increases in demand. To analyze data in your datalake easily and efficiently, AWS has developed several managed and serverless big data services. Most commonly used services to run analytics on S3 data are: Amazon Athena, Redshift Spectrum, Amazon EMR, and other 3rd party and open source services. Some common reference architectures are outlined below.

### [AWS Athena on Glue Catalog](/src/data-analytics/amazon-athena)
<table><tr><td><a href="/src/data-analytics/amazon-athena"><img src="/src/data-analytics/amazon-athena/analytics-athena.png"/></a></td><td>Amazon Athena is a serverless query engine to query data in a S3 datalake. Athena uses the Glue Catalog as its schema repository by default. This architecture provides insight on how to setup an analytics system using Amazon Athena.</td></tr></table>

### [Redshift Spectrum on Glue Catalog](/src/data-analytics/multi-emr-on-hive-metastore)
<table><tr><td><a href="src/data-analytics/redshift-spectrum"><img src="/src/data-analytics/redshift-spectrum/analytics-redshift-spectrum.png"/></a></td><td>Amazon Redshift Spectrum is an AWS service to run queries against S3 datalake by leveraging the power of Amazon Redshift through external tables managed by Glue catalog. This architecture provides an end to end set up to query your datalake using Redshift spectrum and Glue catalog. </td></tr></table>

### Scaling Out with Multiple EMR Clusters

Scaling out analytics workloads using multiple EMR clusters is a common implementation for many of our customers. A frequent design pattern is to run the Glue Crawler on S3 data to define data schema in Glue Catalog, and then use EMR clusters to use tools such as Spark, Hive and Presto to query the data.

In some cases, customers may want to define their own data catalog in a Hive metastore, backed by a highly available RDS database. This solution offers extended and custom schema definitions defined by the users, support for Hive Thrift Server, and the ability to customise the Hive stack being used to support the metastore. Whether self managed or fully managed, all you EMR clusters can refer to the same metastore to execute data analytics against S3.

#### [With Glue Catalog for Schema Management](/src/data-analytics/multi-emr-on-glue-catalog)
<table><tr><td><a href="/src/data-analytics/multi-emr-on-glue-catalog"><img src="/src/data-analytics/multi-emr-on-glue-catalog/analytics-emr-glue-catalog.png"/></a></td><td>This architecture demonstrates how to architect an analytics solution with multiple EMR clusters to query S3 datalake via Glue Catalog.</td></tr></table>

#### [With Hive Metastore on RDS for Schema Management](/src/data-analytics/multi-emr-on-hive-metastore)
<table><tr><td><a href="/src/data-analytics/multi-emr-on-hive-metastore"><img src="/src/data-analytics/multi-emr-on-hive-metastore/analytics-emr-hive-metastore.png"/></a></td><td>In this architecture, we show you how to build your own Metastore using EMR and Amazon RDS, and then leverage that platform from other analytics tools</td></tr></table>
