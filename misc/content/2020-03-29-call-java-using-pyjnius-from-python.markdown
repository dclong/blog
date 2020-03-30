Status: published
Date: 2020-03-29 23:59:05
Author: Benjamin Du
Slug: call-java-using-pyjnius-from-python
Title: Call Java Using PyJNIus from Python
Category: Computer Science
Tags: Computer Science, Python, PyJNIus, Java, JVM

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


PyJNIus is a simple-to-use Java interface for Python.
However,
JPype is more popular.

### Installation

```bash
pip install Cython
pip install pyjnius
```

### Example with Imported Jar

```
import os
os.environ['CLASSPATH'] = "/path/to/your.jar"
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

- [PyJNIus](https://github.com/kivy/pyjnius)