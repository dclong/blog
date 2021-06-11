UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-02-13 22:47:56
Author: Ben Chuanlong Du
Slug: easy-made-mistake-with-cpp-iterator
Title: Easy-Made Mistake with C++ Iterator
Category: Computer Science
Tags: programming, C++, iterator, mistake, error
Modified: 2016-07-13 22:47:56

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


the wrong way

```
for(auto it=l.cbegin(); it!=l.cend(); ++it){
    for(auto jt=++it; jt!=l.cend(); ++jt){
        cout << *it << " <-> " << *jt << endl;
    }
}
```

it is increased again in the inner loop!!!


the correct way

    for(auto it=l.cbegin(); it!=l.cend(); ++it){
        for(auto jt=next(it); jt!=l.cend(); ++jt){
            cout << *it << " <-> " << *jt << endl;
        }
    }

it is very tricky to iterate a container and delete elements
blog about it
