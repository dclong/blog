UUID: e244122f-1524-481c-b8a8-9ea7669551b0
Status: published
Date: 2017-02-20 23:46:45
Author: Ben Chuanlong Du
Slug: install-the-latest-version-of-R-in-ubuntu
Title: Install the Latest Version of R in Ubuntu
Category: Programming
Tags: programming, R, CRAN, Ubuntu, install, latest

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

```bash
sudo apt-add-repository -y "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/"
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
sudo apt-get update
sudo apt-get install r-base-dev
```

If `apt-add-repository` is not install yet, 
you can install it with the following command.
```bash
sudo apt-get install software-properties-common
```
