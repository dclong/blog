Status: published
Date: 2019-06-26 21:56:32
Author: Ben Chuanlong Du
Slug: read-parquet-files-in-python
Title: Read Parquet Files in Python
Category: Computer Science
Tags: programming, Python, Parquet, pyarrow, fastparquet

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

## References 

https://spark.apache.org/docs/latest/sql-data-sources-parquet.html#partition-discovery
