# Fine-grained Access Control With Amazon Lake Formation

### Access Control Using Amazon LakeFormation

#### Overview

Data lakes are complex systems. They not only get data data from many source systems but also many systems and users consume data from them. For large-scale implementations it becomes complicated for custtomers to manage thousands of IAM roles and policy that controls access to the datalake data. AWS LakeFormation simplifies datalake access management by providing finegrained access control mechanisms on the data lake catalog.

In this model, a set of initial data stewards represented by IAM roles and users  known as  [ Datalake Administrators](https://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-setup.html#create-data-lake-admin) can grant Lake Formation permissions on data locations and Data Catalog resources to any principal \(including self\). Once the permissions on various data lake objects are created, users \(IAM Users, Roles\) can access to the datalake objects through their prefered compute engines like [EMR](https://aws.amazon.com/emr/), [Glue](https://aws.amazon.com/glue/), [Athena](https://aws.amazon.com/athena/) that's integrated with AWS LakeFomation. 



![](../.gitbook/assets/image%20%284%29.png)

### Access policy options with Amazon LakeFormatiom



### How it works under the hood?

![](../.gitbook/assets/image%20%283%29.png)

