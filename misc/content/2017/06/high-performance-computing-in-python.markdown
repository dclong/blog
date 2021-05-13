Status: published
Date: 2021-05-12 09:26:31
Author: Ben Chuanlong Du
Slug: high-performance-computing-in-python
Title: High Performance Computing in Python
Category: Computer Science
Tags: programming, Python, HPC, high performance computing, pybind11, numba, Cython, mars, Apache Ray

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Computing Frames

## [Apache Ray](https://github.com/ray-project/ray)

A fast and simple framework for building and running distributed applications.

Ray does not handle large data well (as of 2018/05/28).
Please refer to 
[the discussion](https://groups.google.com/forum/#!topic/ray-dev/8E03APnG_zg)
for details.

https://ray.readthedocs.io/en/latest/serialization.html

https://ray.readthedocs.io/en/latest/configure.html#using-the-object-store-with-huge-pages

https://arrow.apache.org/blog/2017/08/08/plasma-in-memory-object-store/

[Comparison of Ray to Dask](https://github.com/ray-project/ray/issues/642)

## [pai](https://github.com/microsoft/pai)
Resource scheduling and cluster management for AI.

## [Horovod](https://github.com/horovod/horovod)

A framework for distributed training (on GPU) 
for TensorFlow, Keras, PyTorch, and Apache MXNet. https://eng.uber.com/horovod/

## [PetaStorm](https://github.com/uber/petastorm)

Petastorm is a parquet access library 
that may be used from TF, PyTorch or pure Python
to load data from parquet stores directly into ML framework.

## [AiiDa](http://www.aiida.net/)

Automated interactive infrastructure and database for computational science.

## [mars](https://github.com/mars-project/mars)

It sems to me that mars focus on tensor computation.
Mars is a tensor-based unified framework for large-scale data computation which scales Numpy, Pandas and Scikit-learn. 

## [modin-project/modin](https://github.com/modin-project/modin)

Modin is scaling pandas pipeline specifically.
Modin is a DataFrame for datasets from 1KB to 1TB+.
Notice that modin leverages the Apache Ray project.

Modin seems to be a better solution than Dask if you work with data frames.
[Query: What is the difference between Dask and Modin?](https://github.com/modin-project/modin/issues/515)

## Celery

http://www.celeryproject.org/

https://github.com/celery/celery

## [RQ](http://python-rq.org/)

RQ (Redis Queue) is a simple Python library for queueing jobs 
and processing them in the background with workers. 
It is backed by Redis and it is designed to have a low barrier to entry. 
It can be integrated in your web stack easily.

## Dask

## GPU Computing

Please refer to 
[GPU Computing in Python](http://www.legendu.net/misc/gpu-computing-in-python)
for more details.

## Array Specific 

numpy

[sparse](https://github.com/pydata/sparse)

## DataFrame Specific

cudf, dask, 
[modin](https://github.com/modin-project/modin), numba, PySpark DataFrame

## References

http://matthewrocklin.com/blog/work/2016/09/13/dask-and-celery

https://stackoverflow.com/questions/13440875/pros-and-cons-to-use-celery-vs-rq/13441828

https://groups.google.com/forum/#!topic/ray-dev/8E03APnG_zg
