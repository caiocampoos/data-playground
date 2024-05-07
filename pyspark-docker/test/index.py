from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Teste de Database com PySpark") \
    .getOrCreate()

df = spark.read.csv("dados.csv", header=True, inferSchema=True)


df.show()
