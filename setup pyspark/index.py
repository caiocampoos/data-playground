from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder \
    .appName("Exemplo PySpark") \
    .getOrCreate()

schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

data = [("joão", 20),
        ("carlos", 30),
        ("savio", 20),
        ("felipe", 35),
        ]

df = spark.createDataFrame(data, schema=schema)

df.show()

df_filtered = df.where("age > 21").select("name")

df_filtered.show()

spark.stop()
