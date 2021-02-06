Status: published
Date: 2020-10-30 10:39:05
Author: Benjamin Du
Slug: serialize-data-using-pickle-in-python
Title: Serialize Data Using Pickle in Python
Category: Computer Science
Tags: Computer Science, pickle, serialization, deserialization, JSON, cloudpickle

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. JSON is a simple serialization and deserialization tool in Python.
    However, 
    JSON is very limited as lots of objects in Python cannot be serialized into JSON (out of the box).

2. Pickle is the most popular serialization and deserialization tool in Python.

3. Dill extends Python's pickle module for serializing and de-serializing Python objects to the majority of the built-in python types. 
    It also provides some good diagnostic tools for pickling, 
    the best of which is the pickle trace.
    For more discussions,
    please refer to
    [How to check which detail of a complex object cannot be pickled](https://stackoverflow.com/questions/22233478/how-to-check-which-detail-of-a-complex-object-cannot-be-pickled)
    .

4. cloudpickle

## References

[How to check which detail of a complex object cannot be pickled](https://stackoverflow.com/questions/22233478/how-to-check-which-detail-of-a-complex-object-cannot-be-pickled)