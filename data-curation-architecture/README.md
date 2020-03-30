# Data Curation Architectures

### Overview

[Data curation](https://en.wikipedia.org/wiki/Data_curation) is the process of organization and integration of [data](https://en.wikipedia.org/wiki/Data) collected from various sources. It involves process of applying transformation to your datasets within a data lake to create enriched datasets to support business intelligence and advanced analytics like machine learning. All data lake storage services support semi-structuret  and unstructured data. So, it is imperative to develope robust architecture for data curation that can scale with the growth of the data lake and demand of an organization.

This section would go over some reference architectures that are recommended and widely used by AWS customer in different scenarios. This section is intentionally designed to be scenario based and would try to cover common data curation requirements and sample solutions.

1. Merge relational databases changes within the datalake.
   1. [Using AWS Glue](data-curation-using-aws-glue.md)

