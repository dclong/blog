Status: published
Date: 2020-10-25 20:15:13
Author: Benjamin Du
Slug: call-java-using-pyjnius-from-python
Title: Call Java Using PyJNIus from Python
Category: Computer Science
Tags: Computer Science, Python, PyJNIus, Java, JVM

PyJNIus is a simple-to-use Java interface for Python.
However,
[JPype](https://github.com/jpype-project/jpype)
is a better alternative.

### Installation

```bash
pip install Cython
pip install pyjnius
```

### Example with Imported Jar

```
import os
os.environ["CLASSPATH"] = "/path/to/your.jar"
from jnius import autoclass
YourClass = autoclass(path.to.YourClass)
yourObj = YourClass()
```

Note: Avoid using the same name for an instance varialbe and a method in the same class.
Even though Java is able to distinguish between them 
PyJNIus is not able to. 
A method will be hide by the instance variable with the same name 
if you use the Jar via PyJNIus in Python.
Generally speaking,
it is a bad idea to have the same for an instance variable and a method
as it might confuse other programming languages (e.g., Kotlin) and frameworks too.

## References 

- [Java Interfaces for Python](http://www.legendu.net/misc/blog/java-interfaces-for-python)

- [PyJNIus](https://github.com/kivy/pyjnius)