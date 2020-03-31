# Data Curation Architectures

### Overview

[Data curation](https://en.wikipedia.org/wiki/Data_curation) is the process of organization and integration of [data](https://en.wikipedia.org/wiki/Data) collected from various sources. It involves process of applying transformation to your datasets within a data lake to create enriched datasets to support business intelligence and advanced analytics like machine learning. All data lake storage services support semi-structuret  and unstructured data. So, it is imperative to develope robust architecture for data curation that can scale with the growth of the data lake and demand of an organization.

This section would go over some reference architectures that are recommended and widely used by AWS customer in different use cases. This section is intentionally designed to be scenario based and would try to cover common data curation requirements and sample solutions.

### Merge relational databases changes within the datalake.

#### Use Cases

Upsert or Merging data in a datalake is a very common requirement. Organizations frequently perform upserts in the data lakes to support the various use cases as outlined below. 

* **Data Protection Regulation compliance\(**[**GDPR**](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)**/**[**CCPA**](https://en.wikipedia.org/wiki/California_Consumer_Privacy_Act)**\):** With the introduction of the right to be forgotten in different regulations, organizations must remove a user’s information upon request. 
* \*\*\*\*[**Change data capture**](https://en.wikipedia.org/wiki/Change_data_capture) **from  databases:** Most online applications use SQL/NoSQL databases to store application data ans support low latency operations. One of the biggest challenges organizations face is being able to analyze data from various different applications and hence they build pipelines to ingest and transform data coming from all data sources into a central data lake to facilitate analytics. These pipelines receive data mutations from a traditional SQL/NoSQL table that includes addition of new data records, updation and deletion of existing records and apply them to corresponding tables in the data lake.  
* **Sessionization:** Understanding user behaviour from online websites and clickstream data needs gouping multiple events into a single [session](https://en.wikipedia.org/wiki/Session_%28web_analytics%29). This information then can be used to support product analytics,targeted advertising etc. Building continuous applications to track sessions and recording the results that write into data lakes is difficult because data lakes have always been optimized for appending data.
* **Deduplication:** A common data pipeline use case is to collect system logs into a  table by appending data to the table. However, often the sources can generate duplicate records and downstream de duplication steps are needed to take care of them.



