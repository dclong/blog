Status: published
Date: 2019-02-11 20:55:07
Author: Benjamin Du
Slug: osquery-tips
Title: Osquery Tips
Category: Software
Tags: software, osquery, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


## Information About Network Cards
```
osqueryi 'select * from interface_details'
```
`friendly_name`, `description` and `manufacturer` information are not populated yet.
```
osqueryi 'select interface, friendly_name, description, manufacturer from interface_details'
```