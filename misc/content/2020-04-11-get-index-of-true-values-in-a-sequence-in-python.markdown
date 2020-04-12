Status: published
Date: 2020-04-11 14:48:46
Author: Benjamin Du
Slug: get-index-of-true-values-in-a-sequence-in-python
Title: Get Index of True Values in a Sequence in Python
Category: Computer Science
Tags: Computer Science, pandas, Series, index, boolean, numpy, where, which

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

Using Boolean Indexing
>>> s = pd.Series([True, False, True, True, False, False, False, True])
>>> s[s].index
Int64Index([0, 2, 3, 7], dtype='int64')
If need a np.array object, get the .values

>>> s[s].index.values
array([0, 2, 3, 7])
Using np.nonzero
>>> np.nonzero(s)
(array([0, 2, 3, 7]),)
Using np.flatnonzero
>>> np.flatnonzero(s)
array([0, 2, 3, 7])
Using np.where
>>> np.where(s)[0]
array([0, 2, 3, 7])
Using np.argwhere
>>> np.argwhere(s).ravel()
array([0, 2, 3, 7])
Using pd.Series.index
>>> s.index[s]
array([0, 2, 3, 7])
Using python's built-in filter
>>> [*filter(s.get, s.index)]
[0, 2, 3, 7]
Using list comprehension
>>> [i for i in s.index if s[I]]
[0, 2, 3, 7]

## References

https://stackoverflow.com/questions/52173161/getting-a-list-of-indices-where-pandas-boolean-series-is-true/52173171

https://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html