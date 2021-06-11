UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-01-23 22:27:25
Author: Ben Chuanlong Du
Slug: install-essential-and-useful-r-packages
Title: Install Essential and Useful R Packages
Category: Programming
Tags: CRAN, R, package, essential, Bioconductor
Modified: 2016-10-23 22:27:25

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

```R
pkgs = ("data.table", "ggplot2", "RJDBC", "xlsx", "rmarkdown", "Rcpp", "inline")
install.packages(pkgs)
## biostatistics
source("http://bioconductor.org/biocLite.R")
```
```R
update.packages(ask = FALSE, checkBuilt = TRUE)
```

unfortunately sometimes fail to upgrade bioconductor packages ... and have to use biocLite('pkg') ...
the problem is largely caused by the fact that you used a single persoanl R libary ....
if you used different R libraries for different versions of R, then you won't have the problem ...
remove.packages("BiocInstaller") and then

I guess the best way is just to remove R and its library completely and have a branch new installation ....
