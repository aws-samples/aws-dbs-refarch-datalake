# Merge/Upsert  Datasets  Using AWS Glue

#### Scenario

Upsert or Merging data in a datalake is a very common requirement. Organizations frequently perform upserts in the data lakes to support the various use cases as outlined below. 

* **Data Protection Regulation compliance\(**[**GDPR**](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)**/**[**CCPA**](https://en.wikipedia.org/wiki/California_Consumer_Privacy_Act)**\):** With the introduction of the right to be forgotten in defferent regulations, organizations must remove a user’s information upon request. 
* \*\*\*\*[**Change data capture**](https://en.wikipedia.org/wiki/Change_data_capture) **from  databases:** Most online applications use SQL/NoSQL databases to store application data ans support low latency operations. One of the biggest challenges organizations face is being able to analyze data from various different applications and hence they build pipelines to ingest and transform data coming from all data sources into a central data lake to facilitate analytics. These pipelines receive data mutations from a traditional SQL/NoSQL table that includes addition of new data records, updation and deletion of existing records and apply them to corresponding tables in the data lake.  
* **Sessionization:** Understanding user behaviour from online websites and clickstream data needs gouping multiple events into a single [session](https://en.wikipedia.org/wiki/Session_%28web_analytics%29). This information then can be used to support product analytics,targeted advertising etc. Building continuous applications to track sessions and recording the results that write into data lakes is difficult because data lakes have always been optimized for appending data.
* **Deduplication:** A common data pipeline use case is to collect system logs into a  table by appending data to the table. However, often the sources can generate duplicate records and downstream de duplication steps are needed to take care of them.

#### Architecture Overview:

![Overwrite Partitions](../.gitbook/assets/image%20%286%29.png)

1. Sample data
   1. Orders Data for 2020-01-01.

```python
import os
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.context import SparkContext
from pyspark.sql import functions as F, types as T
spark.conf.set("spark.sql.sources.partitionOverwriteMode","dynamic")
stg_df = sqlContext.table("refarch_database.i_orders_input")
stg_df_cast = stg_df.withColumn('order_date', F.to_date('order_date', 'yyyy-MM-dd HH:mm:ss')).withColumn('order_update_timestamp', F.to_timestamp('order_update_timestamp', 'yyyy-MM-dd HH:mm:ss')).filter(stg_df["feed_arrival_date"] == '2020-01-02')
stg_df_final = stg_df_cast.filter(stg_df_cast["order_d"] > 0) # To filer out null blank rows (only applicable to this example)
target_tbl = sqlContext.table("refarch_database.c_orders_output")
final_df = stg_df_final.unionByName(target_tbl)
rownum = F.row_number().over(Window.partitionBy("order_d")\
									.orderBy(final_df["order_update_timestamp"].desc()))
final_union = final_df.select('*',rownum.alias("row_num"))
final_union_dedupe = final_union.filter(target_df["row_num"] == 1)
final_union_dedupe.drop("row_num").coalesce(2).write.partitionBy(["order_date"]).mode("overwrite").parquet("s3://datalake-refarch-sample-us-east-1/upsert_example_data/output")
    
```

