Status: published
Date: 2020-11-28 11:12:45
Author: Benjamin Du
Slug: json-parsing-libraries-in-python
Title: JSON Parsing Libraries in Python
Category: Computer Science
Tags: Computer Science, programming, Python, JSON, serialization, deserialization, orjson, json

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. [orjson](https://github.com/ijl/orjson) 
    is the best option so far.

## [orjson](https://github.com/ijl/orjson) 
[orjson](https://github.com/ijl/orjson) 
is a fast, correct JSON library for Python. 
It benchmarks as the fastest Python library for JSON 
and is more correct than the standard json library or other third-party libraries. 
It serializes dataclass, datetime, numpy, and UUID instances natively.

## [ujson](https://github.com/ultrajson/ultrajson)
[ujson](https://github.com/ultrajson/ultrajson)
is an ultra fast JSON encoder and decoder written in pure C with bindings for Python 3.6+.

## [python-rapidjson](https://github.com/python-rapidjson/python-rapidjson)
[python-rapidjson](https://github.com/python-rapidjson/python-rapidjson)
is a Python module wraps 
[rapidjson](https://github.com/Tencent/rapidjson)
which is an extremely fast C++ JSON parser and serialization library.

## json

## simplejson


