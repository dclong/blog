Status: published
Date: 2021-01-12 10:45:08
Slug: collections-and-iterators-in-cpp
Author: Ben Chuanlong Du
Title: Collections and Iterators in C++
Category: Computer Science
Tags: C++, cpp, programming, list, set, map, iterator, collection, C/C++, vector
Modified: 2021-01-12 10:45:08


## Collections

1. Prefer `std::deque` to `std::vector` when the size of the collection is unknow. 

2. Suppose set `A` and `B` are two set with the same type
    and set `C` is another set with the same value type but a different comparison function,
    then it is still valid to insert results of set operations 
    (union, difference, intersection, symmetric difference and so on)
    on A and B into set `C`.
    It is just that values in C are sorted according to 
    the comparison function of `C` not comparison function of `A` and `B`.

2. It is known to all that a set is sorted (according to its comparison function). 
    You cannot sort the set in place using `std::sort` with another comparison function.
    To sort elements in the set with another comparison function, 
    you have to create a new collection (e.g. a vector), copy the elements over and sort them.

3. You can use `std::set::count` to check whether a set contains a value or not.

4. Removing an element from a set/list/map only 
    affects reference to the remove element not references to other elements.
    However, 
    removing an element from a vector affects references to elements after the removed elements. 
    A good way to works with vector is to operate on it backwards. 
    That is iterating a vector backwards, 
    removing elements from a vector backwards, etc. 

5. `std::map` is similar to `std::set` from many aspect. 
    For example, 
    `std::map` contains values with unique and sorted keys while `std::set` contains unique and sorted keys.;
    both `std::map` and `std::set` have a `count` method which helps to check whether a `map/set` contains a key or not;
    both `std::map` and `std::set` have a `find` method which helps to find the position of a key in a `map/set`.
    Actually, 
    a `std::set` can be considered as a special case of `std::map` where the value is of no interest. 

6. The `std::map::at` method is preferred over the `std::map::operator[]`.

7. Associative collections such as `std::map` and `std::set` have methods related binary search 
    (e.g., `count` and `find`) 
    while sequence collections such as `std::vector` and `std::list` do not have these methods. 
    If a sequence collection is sorted (e.g., use `std::sort`), 
    you can apply functions `std::count` and `std::find` on it. 
    Sequence collections have methods which can access and modify elements at the front and back of the collection 
    (e.g., `std::front`, `std::pop_front`, `std::back`, `std::pop_back`) 
    while associative collections do not have such methods. 
    To access the first and last element of an associative collection, 
    you have to use iterators. 
    For example, 
    to get the last element of a set `x`, 
    you can use 

        :::cpp
        *x.rbegin();

## Iterator

1. The difference between points/iterator is of type std::ptrdiff_t,
    which is essentially a "signed" integer.

2. The result of `std::reverse_iterator::base` decreased 
    by 1 is the corresponding (non-reversed) iterator. 
    For example, 
    if you want to erase the last element from a set `s`, 
    you can use 

        :::cpp
        s.erase(--(s.rbegin().base()));
