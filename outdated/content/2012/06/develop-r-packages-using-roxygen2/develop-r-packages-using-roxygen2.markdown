UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Develop R Packages Using "roxygen2" 
Date: 2017-07-27 12:41:29
Category: Programming
Tags: R, package, programming, tags, CRAN, roxygen2, develop
Slug: develop-r-packages-using-roxygen2
Author: Ben Chuanlong Du


You have to install the R package `roxygen2` first.
```R
install.packages('roxygen2')
```
Roxygenize the package for compiling.
```R
library(roxygen2)
roxygenize(path_to_package)
```

The following are some roxygen2 tags that I use frequently for writing R packages.

1. Some R example code can take a long time to run. 
    To prevent the illustration code from running 
    when checking the package, 
    you can surround the example code with `\dontrun{}`.
    The following is such an example.

        #' @examples
        #' \dontrun{
        #' rnorm(100000)
        #' }

    However, 
    be careful that it is `@examples` not `@example`. 
    If you accidentally use `@example`, 
    then you will get errors like `file cannot be open (or doesn't exist) ...`
    when you check the R package. 

2. By default roxygen2 does not export a function. To export a function
    so that package users can use it, add tag `@export` before the definition
    of the function.

3. Use the tag `@title` to specify the title of a help document. 

4. Use the tag `@description` to start the description part of a help document.

5. To import a package, use the tag `@import pkg_name`. To import `fun1` 
    and `fun2` from a package, use the tag `@importFrom pkg_name fun1 fun2`.

2. By default roxygen2 creates a Rd document for each exported function
    with the same name as the function name. 
    You can use the tag `@rdname` to override the name of the Rd document.

3. Roxygen parses comments that start with `#'`. 
    Comment start with `#` but not `#'` won't be parsed.
    You can take advantage of this to put comment that do not need to parsed into lines starting with `#` but not `#'`.

## Compile and Install R Packages

1. Compile and install package on Windows.
    
        R CMD INSTALL --build package_dir

    Notice that `INSTALL` must be in upper case.


2. The following LaTex packages `texlive`, `texinfo` and `texlive-fonts-extra` (on Linux) 
    are need to compile R packages 
    if you want to generate and check PDF manuals. 

        wajig install texlive texinfo texlive-fonts-extra

    If you do not want (or have permissions) to install them,
    you can compile R packages without generating PDF manuals.

        R CMD build --no-manual ...
        R CMD check --no-manual ...

    For more details on R package build options, 
    please refer to the post 
    [Customizing Package Build Options](https://support.rstudio.com/hc/en-us/articles/200486518-Customizing-Package-Build-Options).

