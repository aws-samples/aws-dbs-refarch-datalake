# Data Ingestion From On-Premise NFS using Amazon DataSync

## Overview

[AWS DataSync](https://aws.amazon.com/datasync/) is a fully managed data transfer service that simplifies, automates, and accelerates moving and replicating data between on-premises storage systems and AWS storage services over the internet or AWS Direct Connect. In a datalake environment, AWS DataSync can be used to sync files securely from on premise storage servers like NFS to S3 based datalake automatically.

In the current architecture, we would walk you through how to use AWS Datasync and Datasync Agent to migrate data to datalake in AWS.

![Data Ingestion Amazon Glue](aws-datasync-from-nfs-on-prem.png)

## Architecture Component Walkthrough

1. Network attached file storage server(NFS) inside an on premise data center.

2. A Datasync agent is a user owned [Virtual Machine](https://en.wikipedia.org/wiki/Virtual_machine) that's deployed on  VMware ESXi [hypervisor](https://en.wikipedia.org/wiki/Hypervisor). Agent should have read access on the NFS server.

3. AWS DataSync executes synchronization tasks and transfers files from on-premise server to AWS.

4. Amazon S3 data lake stores data transferred by AWS DataSync.

## References

* [How AWS DataSync works](https://docs.aws.amazon.com/datasync/latest/userguide/how-datasync-works.html)
