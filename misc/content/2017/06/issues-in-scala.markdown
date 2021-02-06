UUID: 5bada210-2cbb-4750-8dd3-8ceb09649540
Status: published
Date: 2017-10-22 13:32:43
Author: Ben Chuanlong Du
Slug: issues-in-scala
Title: Issues in Scala
Category: Computer Science
Tags: programming, Scala, issue

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## 2.12

1. Avoid using view of collections.

## 2.11

1. Iterator `++` non lazy, might cause stack overflow issues. 
This issue has been fixed in 2.12.

2. `Stream.filterNot`, not lazy, might cause stack overflow issues. 
`Stream.filter` is good.
This isssue has been fixed in 2.12.

3. Avoid using `view` of collections. 
Iterator is a better alternative most of the time.


