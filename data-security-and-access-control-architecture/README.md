# Data Security and Access Control Architecture



A data lake platform  has various components that store data, execute jobs, orchestration tools and data consumption services, etc. Security for each type or even each component varies. Let's assume your data lake uses S3 as a storage .  platform. Here are some examples of the kind of security to be used in some of the components at the platform level:

* **Data catalog access and users' roles** - What accounts have access to a particular datasets in a data catalog and what roles do they use
* **Direct access to datasets**- Either, objects stored in S3 or those used by the programs running as part of your data lake system, should have restricted access. Any system that has direct access to the datasets  within a data lake should have fine grained  access control
* **Jobs execution** - Permissions to execute Jobs, YARN, or similar applications.
* **Administration utilities** - Permissions to access and manage data platform’s components management utilities.

Primarily, access control and data security in datalakes within AWS can be enforced by

1. [Access control using IAM](./)
2. Fine grained access control using AWS Lakeformation

