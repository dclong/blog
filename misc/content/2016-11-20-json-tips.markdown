Status: published
Date: 2021-01-21 15:55:05
Author: Ben Chuanlong Du
Title: Tips on JSON
Slug: json-tips
Category: Computer Science
Tags: Computer Science, programming, Python, JSON, serialization, deserialization, orjson, json, database, Java, C++, JavaScript

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. Empty rows are not allowed in a list in JSON.

2. No comments allowed in a JSON file.
    However, 
    you can put comments into a field.
    Another better option is to use YAML 
    or JSON5 (if you use JavaScript).

## JSON Parsing Libraries in Python

1. [orjson](https://github.com/ijl/orjson) 
    is currently the best JSON parsing library for Python.
    It is very fast and is able handle large (<10G) JSON files.

2. [simdjson](https://github.com/simdjson/simdjson)
    is a C++ library for parsing JSON 
    which supports on-demand APIs. 
    [pysimdjson](https://github.com/TkTech/pysimdjson)
    is a Python wrapping over 
    [simdjson](https://github.com/simdjson/simdjson)
    .
    It is another good choice of JSON parsing library for Python.
    However, 
    simdjson is unable to handle JSON files larger than 10G.


### [orjson](https://github.com/ijl/orjson) 
[orjson](https://github.com/ijl/orjson) 
is a fast, correct JSON library for Python. 
It benchmarks as the fastest Python library for JSON 
and is more correct than the standard json library or other third-party libraries. 
It serializes dataclass, datetime, numpy, and UUID instances natively.

### [ujson](https://github.com/ultrajson/ultrajson)
[ujson](https://github.com/ultrajson/ultrajson)
is an ultra fast JSON encoder and decoder written in pure C with bindings for Python 3.6+.

### [python-rapidjson](https://github.com/python-rapidjson/python-rapidjson)
[python-rapidjson](https://github.com/python-rapidjson/python-rapidjson)
is a Python module wraps 
[rapidjson](https://github.com/Tencent/rapidjson)
which is an extremely fast C++ JSON parser and serialization library.

### [hyperjson](https://github.com/mre/hyperjson)
[hyperjson](https://github.com/mre/hyperjson)
is a hyper-fast, safe Python module to read and write JSON data. 
Works as a drop-in replacement for Python's built-in json module. 
This is alpha software and there will be bugs, 
so maybe don't deploy to production just yet.

### json

### simplejson

## JavaScript

JSON5

## Java

Below are Java libraries for parsing JSON.

## [google/gson](https://github.com/google/gson)

https://stackoverflow.com/questions/2779251/how-can-i-convert-json-to-a-hashmap-using-gson

A great JSON parsing library developed by Google.

## [stleary/JSON-java](https://github.com/stleary/JSON-java)

## Scala

### [circe/circe](https://github.com/circe/circe)

### [json4s/json4s](https://github.com/json4s/json4s)

https://stackoverflow.com/questions/29908297/how-can-i-convert-a-json-string-to-a-scala-map

There are an dependency issue using json4s with Spark. 
This issue was somehow fixed in the plugin 
[johnrengelman/shadow](https://github.com/johnrengelman/shadow) v4.0.3.
However, 
I can confirm that there are issue in 
[johnrengelman/shadow](https://github.com/johnrengelman/shadow) v5.1.0.


https://github.com/json4s/json4s/issues/316

https://github.com/json4s/json4s/issues/418

### [argonaut-io/argonaut](https://github.com/argonaut-io/argonaut)

## References

- [10 Online JSON Tools](http://www.jquery4u.com/json/10-online-json-tools/)

http://json-schema.org/implementations.html

https://medium.com/@djoepramono/how-to-parse-json-in-scala-c024cb44f66b

