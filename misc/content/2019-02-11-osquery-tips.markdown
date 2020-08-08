Status: published
Date: 2020-05-22 15:27:24
Author: Benjamin Du
Slug: osquery-tips
Title: Query and Monitor OS Information using osquery
Category: Software
Tags: software, osquery, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. [osquery-python](https://github.com/osquery/osquery-python)
    is a Python bindings for osquery's Thrift API.

## Information About Network Cards

```
osqueryi 'select * from interface_details'
```

`friendly_name`, `description` and `manufacturer` information are not populated yet.
```
osqueryi 'select interface, friendly_name, description, manufacturer from interface_details'
```


## References

https://github.com/osquery/osquery-python

https://libraries.io/github/osquery/osquery-python

https://holdmybeersecurity.com/2020/02/11/creating-my-first-osquery-extension-to-generate-communityids-with-osquery-python-on-windows/