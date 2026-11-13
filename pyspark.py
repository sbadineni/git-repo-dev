from pyspark.sql.functions import row
df = spark.createdDataFrame(row(a=1, b=2, name="sanjeev"))
display(df)