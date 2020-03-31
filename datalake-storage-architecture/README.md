# Datalake Storage Services FAQs

## What  features to look for while selecting a cloud datalake storage platform?

Selecting a data storage solution is  always driven by the data retrieval pattern, scalability, performance cost and  durability characteristics. In case of a datalake,  characteristics like data-retrieval pattern, performance are  unclear at the beginning. So, it is recommended to select a solution that is secure, durable, distributed and  decoupled from data processing compute infrastructure. [Amazon S3](https://aws.amazon.com/s3/) provides you all the above characteristics with seem-less integration with other AWS and open source data analytic services. Amazon S3 provides secure APIs for programmatic access, so it is easy to build new integrations where required.

## Why Hadoop HDFS or data warehouse storage are not great choices for datalake? 

There are 3 primary reasons why solutions like HDFS storage and data warehouse\(DW\) storage systems are not suitable for datalakes.

1. **Scalability:** Datalakes are supposed to store all data of an organization. As the data volume grows. HDFS or data warehouse storage systems needs to be scaled from time to time. 
2. **Open data format support and storage-compute couple:** HDFS supports open data format, however it comes coupled with compute services. Similarly, DW systems store data in proprietary format that is not accessible to external computes for analytics.

\*\*\*\*



