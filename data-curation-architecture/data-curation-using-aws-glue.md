# Overwrite Table Partitions Using PySpark

#### Scenario

In the current example, we are going to understand the process of curation of data in a data lake that are backed by append only storage services like Amazon S3. Since update semantics are not available in these storage services, we are going to run transformation using PySpark transformation on  datasets to create new snapshots for  target partitions and overwrite them.  This example can be executed using Amazon EMR or AWS Glue. For simplicity, we are assuming that all [IAM roles](../data-security-and-access-control-architecture/data-security-and-access-control-using-iam.md) and/or[ LakeFormation permissions](../data-security-and-access-control-architecture/fine-grained-access-control-with-amazon-lake-formation.md) have been pre-configured. 

#### **Source:**

1. Catalog table `orders.i_order_input` is created on raw ingested datasets in CSV format. 
2. The table is partitioned by `feed_arrival_date`.It receives change records everyday in a new folder in S3 e.g. `s3://<bucket_name>/input/<yyyy-mm-dd>/`.
3. There can be duplicates due to multiple updates to the same order in a day.
4.  `order_update_timestamp` represents the time when the order was updated

#### Target

1. Catalog table `orders.c_order_output` is a curated  deduplicated table  that is  partitioned by `order_date`.

#### Example Datasets 

You can use Glue crawlers to create tables in your catalog after uploading the files to S3

{% file src="../.gitbook/assets/2020-01-01.csv" caption="Orders data feed for 2020-01-01" %}

{% file src="../.gitbook/assets/2020-01-02.csv" caption="Orders data feed for 2020-01-02" %}

#### Solution Walk through

_**Import necessary spark libraries.**_

```python
import os
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.context import SparkContext
from pyspark.sql import functions as F, types as T
spark.conf.set("spark.sql.sources.partitionOverwriteMode","dynamic")
```

_**Read source table `orders.i_orders_input` and creare a dataframe `stg_df`**_

```python
stg_df = sqlContext.table("refarch_database.i_orders_input")
```

_**Optional transformations to cast datatypes if the datatypes in the catalog are different.**_

```python
stg_df_cast = stg_df.withColumn('order_date', F.to_date('order_date', 'yyyy-MM-dd HH:mm:ss')).withColumn('order_update_timestamp', F.to_timestamp('order_update_timestamp', 'yyyy-MM-dd HH:mm:ss')).filter(stg_df["feed_arrival_date"] == '2020-01-02')
stg_df_final = stg_df_cast.filter(stg_df_cast["order_id"] > 0) 

```

_**Read target table from data catalog to dataframe `target_tbl`**_

```python
target_tbl = sqlContext.table("refarch_database.c_orders_output")
```

#### _Merge the source and target dataframes by column name_

```python
final_df = stg_df_final.unionByName(target_tbl)
```

#### _Deduplicate  dataframe using `row_number()` and `window()` and select the most latest record for each `order_id`_

```python
rownum = F.row_number().over(Window.partitionBy("order_id")\
									.orderBy(final_df["order_update_timestamp"].desc()))
final_union = final_df.select('*',rownum.alias("row_num"))
final_union_dedupe = final_union.filter(target_df["row_num"] == 1)
```

#### _**Overwrite the partitions with new curated datasets to output location**_

```python
final_union_dedupe.drop("row_num").coalesce(2).write.partitionBy(["order_date"]).mode("overwrite").parquet("s3://<YOUR_BUCKET>/output")
```

#### _Putting it all together in one script_

```python

import os
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.context import SparkContext
from pyspark.sql import functions as F, types as T
spark.conf.set("spark.sql.sources.partitionOverwriteMode","dynamic")
stg_df = sqlContext.table("refarch_database.i_orders_input")
stg_df_cast = stg_df.withColumn('order_date', F.to_date('order_date', 'yyyy-MM-dd HH:mm:ss')).withColumn('order_update_timestamp', F.to_timestamp('order_update_timestamp', 'yyyy-MM-dd HH:mm:ss')).filter(stg_df["feed_arrival_date"] == '2020-01-02')
stg_df_final = stg_df_cast.filter(stg_df_cast["order_id"] > 0) 
target_tbl = sqlContext.table("refarch_database.c_orders_output")
final_df = stg_df_final.unionByName(target_tbl)
rownum = F.row_number().over(Window.partitionBy("order_id")\
									.orderBy(final_df["order_update_timestamp"].desc()))
final_union = final_df.select('*',rownum.alias("row_num"))
final_union_dedupe = final_union.filter(target_df["row_num"] == 1)
final_union_dedupe.drop("row_num").coalesce(2).write.partitionBy(["order_date"]).mode("overwrite").parquet("s3://<YOUR_BUCKET>/output")
    
```

#### Considerations

1. This solution is useful forsmall to medium datasets. Generally in the order of 10s of GBs.
2. Use this method when number of partition impacted is very less.
3. This method can be used for large tables only of number of partitions impacted is small. 
4. Can be executed for frequently arriving datasets as the process is idempotent.

