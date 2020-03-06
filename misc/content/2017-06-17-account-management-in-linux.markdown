UUID: 80bbd1f8-625d-4b40-860c-8dfb79c23d24
Status: published
Date: 2017-10-22 13:30:05
Author: Ben Chuanlong Du
Slug: account-management-in-linux
Title: Account Management in Linux
Category: OS
Tags: Linux, account management, group managment, adduser, useradd, gpasswd, getent

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Create a User 

Both `adduser` and `useradd` can be used to create a new user. 
`adduser` is interactive while `useradd` is non-interactive.
It is suggested that you use `useradd` in batch mode
and `adduser` in non-batch mode.

```sh
useradd -o -m -u -g -d 
groupadd -o -g 
```

## Group

Add a user to a group.
```sh
gpasswd -a user_name group_name
```

Get information about a group.
```sh
getent group group_name
getent group group_id
```
