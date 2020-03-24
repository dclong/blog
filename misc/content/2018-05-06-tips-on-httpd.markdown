Status: published
Date: 2020-03-24 13:33:50
Author: Ben Chuanlong Du
Slug: httpd-tips
Title: Tips on httpd
Category: Internet
Tags: software, httpd, HTTP, tips, web, internet

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
1. A directory must be executable by others in order to show up.
    Even if a directory show up,
    it does NOT mean that you can access it.
    It must be readable by others (at the same)
    so that it can be accessed using HTTP.

2. A directory/file must be readable by others on the host
    so that it can be accessed using HTTP,
    otherwise you will encounter error messages like the one below.

    > You don't have permission to access /wwwroot/somedir/ on this server.


## Docker Image 
    
The Docker image [httpd](https://hub.docker.com/_/httpd/)
is a good one.

Pull the image. 

    :::bash
    docker pull httpd

Start a docker container.

    :::bash
    docker run --hostname httpd -dit -p 80:80 -v $(pwd):/usr/local/apache2/htdocs/ httpd
