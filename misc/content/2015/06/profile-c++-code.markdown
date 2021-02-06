UUID: 24f570f2-7c20-4396-9b8d-35016e83ee2d
Status: published
Date: 2015-06-22 22:01:47
Author: Ben Chuanlong Du
Slug: profile-c++-code
Title: Profile C++ Code
Category: Computer Science
Tags: programming, C++, profile, profiling, speed, performance, Valgrind, kcachegrind

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**



You can use valgrind with the following options

```bash
valgrind --tool=callgrind ./(Your binary)
```

It will generate a file called callgrind.out.x. 
You can then use kcachegrind tool to read this file. 
It will give you a graphical analysis of things with results like which lines cost how much.
