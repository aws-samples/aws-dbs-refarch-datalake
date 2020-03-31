# Fine-grained Access Control With AWS LakeFormation

### Access Control Using Amazon LakeFormation

#### Overview

[Data lakes](../) are complex systems. They not only get data  from many source systems but also many systems and users consume data from them. For large-scale implementations it becomes complicated for customers to manage thousands of IAM roles and policy that controls access to their datalake. [AWS LakeFormation ](https://aws.amazon.com/lake-formation/)simplifies datalake access management by providing [fine grained access control mechanisms](https://docs.aws.amazon.com/lake-formation/latest/dg/access-control-overview.html) on the data lake catalog. Please refer to various AWS LakeFormation terminologies [here](https://docs.aws.amazon.com/lake-formation/latest/dg/how-it-works.html#how-it-works-terminology).

In this model, a set of initial [data stewards](https://en.wikipedia.org/wiki/Data_steward) represented by IAM roles and users  known as  [ Datalake Administrators](https://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-setup.html#create-data-lake-admin) can grant Lake Formation permissions on data locations and Data Catalog resources to any principal \(including self\). Once the permissions on various data lake objects are created, users \(IAM Users, Roles\) can access to the datalake objects through their preferred compute engines like [EMR](https://aws.amazon.com/emr/), [Glue](https://aws.amazon.com/glue/), [Athena](https://aws.amazon.com/athena/) that's integrated with [AWS LakeFomation](https://aws.amazon.com/lake-formation/). Lake formation authorizes access to datalake resources when the [integrated compute engines](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html#service-integrations)  execute workloads on data catalog.

![](../.gitbook/assets/image%20%284%29.png)

### Access policy options with AWS LakeFormation

[Access control in AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/access-control-overview.html) is divided into the following two areas:

* Metadata access control – Permissions on Data Catalog resources \(_Data Catalog permissions_\).

  These permissions enable principals to create, read, update, and delete metadata databases and tables in the Data Catalog.

* Underlying data access control – Permissions on locations in [Amazon Simple Storage Service \(Amazon S3\)](https://aws.amazon.com/s3/) \(_data access permissions_ and _data location permissions_\).

  Data access permissions enable principals to read and write data to underlying Amazon S3 locations. Data location permissions enable principals to create metadata databases and tables that point to specific Amazon S3 locations.

For both areas, Lake Formation uses a combination of Lake Formation permissions and [AWS Identity and Access Management \(IAM\)](https://aws.amazon.com/iam/) permissions. The IAM permissions model consists of IAM policies. The Lake Formation permissions model is implemented as DBMS-style GRANT/REVOKE commands, such as `Grant SELECT on` _`tableName`_ `to` _`userName`_.

As of 03/31/2020, AWS Lake formation provides prermissions at various levels.

1. **Catalog level permissions**
   1. CREATE\_DATABASE
2. **Database level permissions**
   1. CREATE
   2. ALTER
   3. DROP
3. **Tables level permissions**
   1. ALTER
   2. DROP
   3. SELECT - Applicable to underlying data
   4. DELETE - Applicable to underlying data
   5. INSERT - Applicable to underlying data
4. **Column level permissions**
   1. SELECT - Applicable to underlying data

### How it works under the hood?

When an user runs a workload on Lakeformation catalog using an integrated compute service,  the compute service requests for access to Lakeformation. Based on the access level defined on the catalog objects, AWS Lake formation vends short-term credentials to the compute service.  The compute service  then uses the temporary credentials to directly access S3 objects and execute the workload. For column level access control, the compute engine filters out attributes that the user/role  don't have access to after the objects have been downloaded from S3 as part processing\(as of 03/31/2020\).

![](../.gitbook/assets/image%20%283%29.png)

