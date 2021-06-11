Status: published
Date: 2020-08-06 00:59:06
Author: Ben Chuanlong Du
Slug: python-packages-for-caching
Title: Serialization and Caching in Python
Category: Computer Science
Tags: programming, Python, packages, caching, lru_cache, diskcache, memcached
Modified: 2020-08-06 00:59:06

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Serialization

1. Pickle is preferred to marshall.

2. Use Parquet for pandas DataFrame.

pickle: geneal purpose serialization/deserialization which supports almost all Python objects. 

Parquet (via PyArrow): specific for DataFrame objects. 

JSON: safe, human readable but limited to simple data types in Python.

## functools.lru_cache

https://docs.python.org/3/library/functools.html#functools.lru_cache

## cachetools

https://cachetools.readthedocs.io/en/latest/
https://github.com/tkem/cachetools

## diskcache sounds like a good options!!!

DiskCache: Disk Backed Cache
http://www.grantjenks.com/docs/diskcache/tutorial.html



## pickle 

pickle is a Python object serialization package. 

## shelve 

shelve is a package for persisting Python object 

## joblib

`joblib` is a package for running Python functions as pipeline jobs.
It supports transparent disk-caching of functions and lazy re-evaluation (memoize pattern).


## memcached & pymemcache

https://pypi.org/project/pymemcache/

http://memcached.org/

Free & open source, high-performance, distributed memory object caching system, generic in nature, 
but intended for use in speeding up dynamic web applications by alleviating database load.

## References 

https://docs.python-guide.org/scenarios/serialization/