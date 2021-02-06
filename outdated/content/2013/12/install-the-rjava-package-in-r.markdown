UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Title: Install the rJava Package in R
Author: Ben Chuanlong Du
Date: 2016-12-10 01:44:32
Slug: install-the-rjava-package-in-r
Category: Software
Tags: R, rJava, Java, Linux

 
The most convenient way is to install the corresponding Linux package if exists.

```R
sudo apt-get install r-cran-rjava
```

However, this Linux package is often outdated.
Follow the steps below if you'd rather install rJava manually.

1. Install OpenJDK and configure Java. 

        sudo apt-get install openjdk-7-*
        sudo R CMD javareconf

2. Install the `rJava` package in R.
    
        install.packages("rJava").

If it does not work, 
please set the `JAVA_HOME` environment variable manually in step 1
and then try step 2 again.
```Bash
export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64/jre
```
