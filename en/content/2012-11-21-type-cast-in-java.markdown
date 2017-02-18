UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2014-10-02 10:50:55
Slug: type-cast-in-java
Author: Ben Chuanlong Du
Title: Type Cast in Java
Category: Programming
Tags: type cast, programming, Java


1. You cannot cast between integer and boolean values. 
However it is trivia to convert data between integer and boolean. 
For example,
`int i = b ? 1 : 0;` convert a boolean value `b` into an integer value `i`, 
and `boolean b = i != 0` convert an integer value `i` into a boolean value `b`.
