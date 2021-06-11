Status: published
Date: 2019-02-17 19:15:35
Author: Ben Chuanlong Du
Slug: preferred-python-version-in-shebang
Title: Preferred Python Version in Shebang
Category: Computer Science
Tags: programming, shell, Python, shebang, version
Modified: 2019-02-17 19:15:35

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**



```
#!/bin/sh
''''which python2 >/dev/null 2>&1 && exec python2 "$0" "$@" # '''
''''which python  >/dev/null 2>&1 && exec python  "$0" "$@" # '''
''''exec echo "Error: I can't find python anywhere"         # '''
```

## Reference

https://stackoverflow.com/questions/18993438/shebang-env-preferred-python-version
