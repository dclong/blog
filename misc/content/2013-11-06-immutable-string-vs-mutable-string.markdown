UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2016-07-13 22:22:11
Slug: immutable-string-vs-mutable-string
Title: Immutable String vs Mutable String
Category: Computer Science
Tags: programming, string, mutable, immutable

**Things on this page are fragmentary and immature notes/thoughts of the author. It is not meant to readers but rather for convenient reference of the author and future improvement.**
 

advantage of immutable string:

    trivially thread safe
        more secure
            more memory efficient in most use cases.
                cheap substrings (tokenizing and slicing)

however, if one has to create many small string, 
e.g., concatenate strings a lot, immutable string has no advantage.
That's why we have StringBuffer and StringBuilder in Java.
Note that String in Java don't have any mutator methods. 
A new string is returned ....
Java String is not suitable for manipulating elements,
use StringBuffer or StringBuilder instead.
The difference is that StringBuffer is synchronized 
while StringBuilder is not.
StringBuilder has length method instead of size method.


Java char array has a fixed length, but for printing, 
you do can use '\0' (C-style ending of char array) to indicate the end of a string.

StringBuilder in Java is somehow similar to String in C++.
