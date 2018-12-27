# Data Ingestion From On-Premise NFS using Amazon DataSync

## Overview

AWS DataSync is a fully managed data transfer service that simplifies, automates, and accelerates moving and replicating data between on-premises storage systems and AWS storage services over the internet or AWS Direct Connect. In a datalake environment AWS DataSync can be used to sync datafiles securely from on premise storage servers like NFS to datalake automatically.

In the current architecture, we would walk you through how to use AWS Datasync and Datasync Agent to migrate data to datalake in AWS.

![Data Ingestion Amazon Glue](datalake_reference_architecture.png)

## Architecture Component Walkthrough

1. Network attached file storage server(NFS) inside an on premise data cente.

2. A Datasync agent is a VM that's deployed on  VMware ESXi hypervisor. Agent should have read access on the NFS server

3.  AWS datasync executes sync tasks in AWS and transfers files from on-premise server to AWS.

4. Amazon S3 data lake stores data transferred by AWS DataSync
