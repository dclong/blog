UUID: 9eb644ae-ae2f-470c-895c-c2fc8737c510
Status: published
Date: 2015-12-16 00:05:32
Author: Ben Chuanlong Du
Slug: sorting-functions-in-c++
Title: Sorting Functions in C++
Category: Computer Science
Tags: programming, C++, sort

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

`std::sort`
`std::stable_sort`
`std::partial_sort`

Notice that only `std::stable_sort` is stable sort (at the cost of additional time/space complexity).
It is easy to achive stable sort using `std::sort` or `std::qsort` by add extra criterias for sorting. 
For example, if you have to sort some nodes by size and want to have stable results, 
you want use the index/name of the nodes as a secondary sorting criteria. 
You can do this by comparing `std::pair` of node size and node index/name. 
