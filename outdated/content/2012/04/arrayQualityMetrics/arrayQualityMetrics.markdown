UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2016-06-11 19:11:28
Slug: arrayQualityMetrics
Author: Ben Chuanlong Du
Title: Install the R Package "arrayQualityMetrics"
Category: Programming
Tags: research, programming, biostatistics, package, arrayQualityMetrics, R, CRAN
Modified: 2016-06-11 19:11:28

I had to use the R package "arrayQualityMetrics" to check the quality of some gene chips. 
Installing this package in Linux takes a few steps. 
The following is the brief instruction on how to install R package "arayQualityMetrics" in Debian.    

```R
# install the graphics library cairo
sudo apt-get install libcairo2-dev
# install X toolkit intrinsiscs development files
sudo apt-get install libxt-dev
# install development files for the Gnome XML library
sudo apt-get install libxml2-dev
# if you have installed BiocInstaller 
library(BiocInstaller)
biocLite('arrayQualityMetrics')
# if you haven't installed R package BiocInstaller
source("http://bioconductor.org/biocLite.R")
biocLite('arrayQualityMetrics')
```

Installing R package "arrayQualityMetrics" takes a while, so be patient. 

