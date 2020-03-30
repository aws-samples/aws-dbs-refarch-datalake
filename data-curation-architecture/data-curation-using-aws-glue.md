# Merge/Upsert  Datasets  Using AWS Glue

#### Scenario

Upsert or Merging data in a datalake is a very common requirement. Organizations frequently perform upserts in the data lakes to support the various use cases as outlined below. 

* **Data Protection Regulation compliance\(GDPR/CCPA\):** With the introduction of the right to be forgotten in defferent regulations, organizations must remove a user’s information upon request. 
* **Change data capture from traditional databases:** Most online applications use SQL/NoSQL databases to store application data ans support lowlatency operations. One of the biggest challenges organizations face is being able to analyze data from various different applications and hence they build pipelines to ingest and transform data coming from all data sources into a central data lake to facilitate analytics. These pipelines receive data mutations from a traditional SQL/NoSQL table that includes addition of new data records, updation and deletion of existing records and apply them to corresponding tables in the data lake.  
* **Sessionization:** Understanding user behaviour from online websites and clickstream data needs gouping multiple events into a single session. This information then can be used to suppor product analytics,targeted advertising etc. Building continuous applications to track sessions and recording the results that write into data lakes is difficult because data lakes have always been optimized for appending data.
* **Deduplication:** A common data pipeline use case is to collect system logs into a Databricks Delta table by appending data to the table. However, often the sources can generate duplicate records and downstream de duplication steps are needed to take care of them.

#### Architecture Overview:







```python
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import timedelta
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import rank, first, last,max
from awsglue.dynamicframe import DynamicFrame
import pyspark.sql.functions as sf


glueContext = GlueContext(SparkContext.getOrCreate())

initialDyF = glueContext.create_dynamic_frame.from_options(
        's3',
        {'paths': ['s3://pheaa-initial-load/']},
        'csv',
        {'withHeader': True, 'separator': '|'})

cdcDyF = glueContext.create_dynamic_frame.from_options(
        's3',
        {'paths': ['s3://pheaa-cdc-load/']},
        'csv',
        {'withHeader': True, 'separator': '|'})

initialDf=initialDyF.toDF()

cdcDf=cdcDyF.toDF()

initialDf = initialDf.\
withColumn("year",sf.year("tpep_pickup_datetime")).\
withColumn("month",sf.month("tpep_pickup_datetime")).\
withColumn("day",sf.dayofmonth("tpep_pickup_datetime"))

initialDyf = DynamicFrame.fromDF(initialDf, glueContext, "initialDynamicFrame")

glueContext.write_dynamic_frame.from_options(
    frame = initialDyf,
    connection_type = "s3",    
    connection_options = {"path": "s3://pheaa-base-partitioned/partitionedtable/","partitionKeys": ["year","month","day"]},
    format = "parquet")

window = Window.\
              partitionBy(cdcDf.pk1).\
              orderBy(cdcDf.transaction_time).\
              rangeBetween(-sys.maxsize, sys.maxsize)

window2 = Window.\
              partitionBy(cdcDf.pk1)

temp1Df= cdcDf.\
withColumn("f_val",first(cdcDf.op_cd).over(window)).\
withColumn("l_val",last(cdcDf.op_cd).over(window)).\
withColumn("max_dt",max(cdcDf.transaction_time).over(window2))

udDf = temp1Df.filter("transaction_time= max_dt").filter("op_cd IN ('U','D')").\
withColumnRenamed("op_cd",'b_op_cd').\
withColumnRenamed("pk1",'b_pk1').\
withColumnRenamed("vendorid",'b_vendorid').\
withColumnRenamed("tpep_pickup_datetime",'b_tpep_pickup_datetime').\
withColumnRenamed("tpep_dropoff_datetime",'b_tpep_dropoff_datetime').\
withColumnRenamed("passenger_count",'b_passenger_count').\
withColumnRenamed("trip_distance",'b_trip_distance').\
withColumnRenamed("ratecodeid",'b_ratecodeid').\
withColumnRenamed("store_and_fwd_flag",'b_store_and_fwd_flag').\
withColumnRenamed("pulocationid",'b_pulocationid').\
withColumnRenamed("dolocationid",'b_dolocationid').\
withColumnRenamed("payment_type",'b_payment_type').\
withColumnRenamed("fare_amount",'b_fare_amount').\
withColumnRenamed("extra",'b_extra').\
withColumnRenamed("mta_tax",'b_mta_tax').\
withColumnRenamed("tip_amount",'b_tip_amount').\
withColumnRenamed("tolls_amount",'b_tolls_amount').\
withColumnRenamed("improvement_surcharge",'b_improvement_surcharge').\
withColumnRenamed("total_amount",'b_total_amount').\
withColumnRenamed("transaction_time",'b_transaction_time')

baseDf = spark.read.parquet('s3://pheaa-base-partitioned/partitionedtable/')

yearList=[p[0] for p in udDf.select(sf.year(udDf.b_tpep_pickup_datetime)).distinct().collect()]

monthList=[p[0] for p in udDf.select(sf.month(udDf.b_tpep_pickup_datetime)).distinct().collect()]

dayList=[p[0] for p in udDf.select(sf.dayofmonth(udDf.b_tpep_pickup_datetime)).distinct().collect()]

fiteredBaseDf = baseDf.\
filter(baseDf.year.isin(yearList)).\
filter(baseDf.month.isin(monthList)).\
filter(baseDf.day.isin(dayList))

cond = [fiteredBaseDf.pk1==udDf.b_pk1]

joinedUdDf = fiteredBaseDf.\
join(udDf,cond, 'left')

finalUdDf = joinedUdDf.selectExpr("b_op_cd",
"CASE WHEN b_pk1	='D' OR b_pk1	IS NULL THEN	pk1	ELSE	b_pk1	END	pk1",
"CASE WHEN b_vendorid	='D' OR b_vendorid	IS NULL THEN	vendorid	ELSE	b_vendorid	END	vendorid",
"CASE WHEN b_tpep_pickup_datetime	='D' OR b_tpep_pickup_datetime	IS NULL THEN	tpep_pickup_datetime	ELSE	b_tpep_pickup_datetime	END	tpep_pickup_datetime",
"CASE WHEN b_tpep_dropoff_datetime	='D' OR b_tpep_dropoff_datetime	IS NULL THEN	tpep_dropoff_datetime	ELSE	b_tpep_dropoff_datetime	END	tpep_dropoff_datetime",
"CASE WHEN b_passenger_count	='D' OR b_passenger_count	IS NULL THEN	passenger_count	ELSE	b_passenger_count	END	passenger_count",
"CASE WHEN b_trip_distance	='D' OR b_trip_distance	IS NULL THEN	trip_distance	ELSE	b_trip_distance	END	trip_distance",
"CASE WHEN b_ratecodeid	='D' OR b_ratecodeid	IS NULL THEN	ratecodeid	ELSE	b_ratecodeid	END	ratecodeid",
"CASE WHEN b_store_and_fwd_flag	='D' OR b_store_and_fwd_flag	IS NULL THEN	store_and_fwd_flag	ELSE	b_store_and_fwd_flag	END	store_and_fwd_flag",
"CASE WHEN b_pulocationid	='D' OR b_pulocationid	IS NULL THEN	pulocationid	ELSE	b_pulocationid	END	pulocationid",
"CASE WHEN b_dolocationid	='D' OR b_dolocationid	IS NULL THEN	dolocationid	ELSE	b_dolocationid	END	dolocationid",
"CASE WHEN b_payment_type	='D' OR b_payment_type	IS NULL THEN	payment_type	ELSE	b_payment_type	END	payment_type",
"CASE WHEN b_fare_amount	='D' OR b_fare_amount	IS NULL THEN	fare_amount	ELSE	b_fare_amount	END	fare_amount",
"CASE WHEN b_extra	='D' OR b_extra	IS NULL THEN	extra	ELSE	b_extra	END	extra",
"CASE WHEN b_mta_tax	='D' OR b_mta_tax	IS NULL THEN	mta_tax	ELSE	b_mta_tax	END	mta_tax",
"CASE WHEN b_tip_amount	='D' OR b_tip_amount	IS NULL THEN	tip_amount	ELSE	b_tip_amount	END	tip_amount",
"CASE WHEN b_tolls_amount	='D' OR b_tolls_amount	IS NULL THEN	tolls_amount	ELSE	b_tolls_amount	END	tolls_amount",
"CASE WHEN b_improvement_surcharge	='D' OR b_improvement_surcharge	IS NULL THEN	improvement_surcharge	ELSE	b_improvement_surcharge	END	improvement_surcharge",
"CASE WHEN b_total_amount	='D' OR b_total_amount	IS NULL THEN	total_amount	ELSE	b_total_amount	END	total_amount",
"CASE WHEN b_transaction_time	='D' OR b_transaction_time	IS NULL THEN	transaction_time	ELSE	b_transaction_time	END	transaction_time"
                                 )                    

iDf = temp1Df.filter("transaction_time= max_dt").filter("f_val ='I'").\
drop('op_cd').\
withColumnRenamed("l_val",'op_cd')

finalIDf=iDf.select("pk1","vendorid","tpep_pickup_datetime","tpep_dropoff_datetime","passenger_count",
                    "trip_distance","ratecodeid","store_and_fwd_flag","pulocationid","dolocationid",
                    "payment_type","fare_amount","extra","mta_tax","tip_amount","tolls_amount",
                    "improvement_surcharge","total_amount","transaction_time")

finalUdDf = finalUdDf.drop('b_op_cd')


finalTable = finalUdDf.unionAll(finalIDf).\
withColumn("year",sf.year("tpep_pickup_datetime")).\
withColumn("month",sf.month("tpep_pickup_datetime")).\
withColumn("day",sf.dayofmonth("tpep_pickup_datetime"))

spark.conf.set("spark.sql.sources.partitionOverwriteMode","dynamic")

numPart = int(finalTable.count()/100000)

finalTable.coalesce(numPart).write.partitionBy(["year","month","day"]).\
mode("overwrite").parquet("s3://pheaa-base-partitioned/partitionedtable/")

    
```

