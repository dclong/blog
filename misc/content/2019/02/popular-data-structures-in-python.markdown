Status: published
Date: 2019-10-04 20:14:52
Author: Benjamin Du
Slug: popular-data-structures-in-python
Title: Popular Data Structures in Python
Category: Computer Science
Tags: programming, Python, data structure, list, dict, tuple

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## list

1. `list` is essentially a resizable array of objects in Python.

1. Almosts all methods of list are in-place.

2. use `+` to concatenate 2 lists.

3. `list.pop` is inplace and returns the removed element.

4. To get unique elements in a list,
    you can first coerce the list to a set and then convert the set back to a list.

        unique_list = list(set(alist))

2. To check whether an object `x` is a in a list `alist`,
    you can use

        x in alist

    If you want to know the position of the element,
    use a Look Before You Leap (LBYL) style with a conditional expression as below.

        i = alist.index(x) if x in alist else None

## tuple

`tuple` is the immutable version of list.

## dict

`dict` is ordered hash table in Python 3.6+.

## str

## pandas.DataFrame




## Data Structure

1. The list object in Python does not have a `find` method which is inconvenient.
    To do a clean "find" in a list in Python,
    you can use the following style of code.

        if x in alist:
            index = alist.index(x)

2. You can use `set(alist)` to get unique values of a list.
    If you want to return a list (rather than a set) of unique values,
    you can use `list(set(alist))`.
    Another way is to use the method `numpy.unique`.

3. The difference between list and tuple in Python is that
    a list is mutable while a tuple is immutable.
    So you can think of tuple as immutable version of list.
    Tuples can be used in dictionarys in Python as keys
    while lists cannot.

## Collections

1. defaultdict

2. namedtuple

