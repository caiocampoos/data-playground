from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, col
from functools import reduce
from pyspark.ml.stat import Correlation
from pyspark.ml.feature import VectorAssembler
import os

spark = SparkSession.builder \
    .appName("Correlation Analysis") \
    .getOrCreate()

csv_directory = "./tickers"

csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv')]

dfs = []

for csv_file in csv_files:
    csv_path = os.path.join(csv_directory, csv_file)
    df_temp = spark.read.csv(csv_path, header=True, inferSchema=True)
    ticker = os.path.splitext(csv_file)[0]
    df_temp = df_temp.withColumn("Ticker", lit(ticker))
    dfs.append(df_temp)

df = reduce(lambda x, y: x.union(y), dfs)

# Select numeric columns only
numeric_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
df = df.select([col(column).cast("double").alias(column) for column in numeric_columns])

# Drop rows with null values
df = df.dropna()

assembler = VectorAssembler(inputCols=numeric_columns, outputCol="features")

df_assembled = assembler.transform(df).select("features")

correlation_matrix = Correlation.corr(df_assembled, "features").head()

correlation_array = correlation_matrix[0].toArray()

print("Correlation Matrix:")
for i, row in enumerate(correlation_array):
    for j, value in enumerate(row):
        print(f"{numeric_columns[i]} - {numeric_columns[j]}: {value}")
