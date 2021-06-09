Status: published
Date: 2021-04-09 11:14:19
Author: Benjamin Du
Slug: tips-on-apache-ray
Title: Tips on Apache Ray
Category: Computer Science
Tags: programming, Apache Ray, distributed computing

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Deploy Apache Ray

Please refer to 
[Deploy Apache Ray](http://www.legendu.net/misc/blog/deploy-apache-ray/)
for details.

## Tutorials and Examples

[How to scale Python multiprocessing to a cluster with one line of code](https://medium.com/distributed-computing-with-ray/how-to-scale-python-multiprocessing-to-a-cluster-with-one-line-of-code-d19f242f60ff)
demonstrates how you can scale a Python multiprocess application 
to run on an Apache Ray cluster 
with only one line change of your code 
(change `import multiprocessing.Pool` to `ray.util.multiprocessing.Pool`).
Of course,
you have to export the environment variable `RAY_ADDRESS=auto` 
before running the Python code 
or you have to make an another line of change 
which is to change `Pool()` to `Pool(ray_address="auto")`.
For more details,
please refer to
[Distributed multiprocessing.Pool](https://ray.readthedocs.io/en/latest/multiprocessing.html)
.

https://github.com/ray-project/tutorial


## References

[Fault Tolerance](https://ray.readthedocs.io/en/latest/fault-tolerance.html#fault-tolerance)

[Development Tips](https://ray.readthedocs.io/en/latest/development.html)

[Distributed Iterators](https://ray.readthedocs.io/en/latest/iter.html)

[Distributed Scikit-learn / Joblib](https://ray.readthedocs.io/en/latest/joblib.html)

[https://ray.readthedocs.io/en/latest/multiprocessing.html](Distributed multiprocessing.Pool)

https://github.com/ParallelSSH/parallel-ssh

https://ray.readthedocs.io/en/latest/walkthrough.html#remote-functions-tasks

https://arrow.apache.org/docs/python/plasma.html#the-plasma-in-memory-object-store

https://readthedocs.org/projects/ray/downloads/pdf/latest/

https://ray.readthedocs.io/en/latest/package-ref.html

https://towardsdatascience.com/benchmarking-python-distributed-ai-backends-with-wordbatch-9872457b785c

https://ray.readthedocs.io/en/latest/tune.html

https://ray.readthedocs.io/en/latest/rllib.html
