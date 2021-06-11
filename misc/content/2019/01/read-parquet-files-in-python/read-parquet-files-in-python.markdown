Status: published
Date: 2019-01-30 20:47:36
Author: Ben Chuanlong Du
Slug: read-and-write-parquet-files-in-python
Title: Read and Write Parquet Files in Python
Category: Computer Science
Tags: programming, Python, Parquet, pyarrow, fastparquet
Modified: 2020-05-30 20:47:36

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Read in Parquet Files

It is suggested that you go with pyarrow.

## pyarrow

```bash
sudo pip3 install pyarrow
```

## fastparquet

```bash
wajig install python3-snappy
pip3 install fastparquet 
```

## Write a DataFrame into Parquet Files

https://github.com/pandas-dev/pandas/issues/21228

## Output Type of Columns

null object -> null int when read into PySpark!!

https://stackoverflow.com/questions/49172428/how-to-specify-logical-types-when-writing-parquet-files-from-pyarrow

https://stackoverflow.com/questions/50110044/how-to-force-parquet-dtypes-when-saving-pd-dataframe

## References 

https://spark.apache.org/docs/latest/sql-data-sources-parquet.html#partition-discovery
