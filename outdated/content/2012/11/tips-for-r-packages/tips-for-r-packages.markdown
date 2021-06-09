UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2016-10-23 22:30:01
Author: Ben Chuanlong Du
Slug: tips-for-r-packages
Title: Tips for R Packages
Category: Programming
Tags: programming, repository, package, OmegaHat, CRAN, R, Bioconductor, biocLite

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 
<img src="http://dclong.github.io/media/r/r.png" height="200" width="240" align="right"/>


Popular Repositories for R Packages

[CRAN Task Views](http://cran.r-project.org/web/views/)


1. CRAN

2. OmegaHat
```R
install.packages("SVGAnnotation", repos = "http://www.omegahat.org/R")
```
3. Bioconductor 

If the R package `BiocInstaller` 
(produced by Bioconductor to facilitate installing other packages on Bioconductor) 
has been installed, 
you can use the following code to install a package named `pkgname` on Bioconductor.
```R
#load package BiocInstaller
library(BiocInstaller)
#install package 
biocLite('pkgname')
```

If the R package `BiocInstaller` has not been installed yet, 
you can use the following command to install it.

```R
source("http://bioconductor.org/biocLite.R")
```

It will be automatically loaded after installation. 
Note that you do not have to install package `BiocInstaller` again next time when
you want to install other packages on Bioconductor. 
All you need is just to load it and use the `biocLite` to install packages (see code shown before).
```R
biocLite("limma")
biocLite("arrayQualityMetrics")
biocLite("GO.db")
install.packages('QuasiSeq')
```
4. functions for BioConductor objects, sometimes, it doesn't work, 
because you haven't load the package yet. This is misleading ....

5. Upgrade Bioconductor packages.
```R
biocLite("Upgradable") 
```

1. If you use R on a Linux server which you do not have root access, 
you have to create your own r library to install packages into. 
You can use any directory which you have read and write access as your own R library. 
For example, 
you can create a directory named `.r-lib` in your own home directory 
and to make R attach your library to the beginning of the search path automatically 
(so that you do not have to specify library path or to use `.libPaths` to attach it manually), 
you can put file named `.Renviron` in your home directory with the following content.
```R
R_LIBS="/home/username/r-lib-PATH"
```
where `username` is your user name and `r-lib-path` is your personal R library. 
It is suggested that you create a personal R library even if you use R on your own Linux machine. 
So the above tips also apply if you run R on your own machine with Linux operating system.

3. `library` load a package into R workspace. 
If the package to be load is not in the search path, 
you can specify its path by the option `lib.loc`.

4. The `.libPaths` function gets/sets the library trees within which packages are looked for. 
For example, 
to add a library path to into the library trees, 
you can use `.libPaths(c(.libPaths(), yourNewPath))`. 
The library paths in the library trees are searched in order.

5. If you know the name of the R package that you want to install, 
then you can use `install.packages` to install the package for you. 
For example if you want to install R `xlsx`, 
you can use `install.packages("xlsx")`. 
You can also install a package from local disk use `install.packages` 
by specifying the option `repos=FALSE` or `repos=NULL`. 
For example, 
if file `dclong.String_1.0-1.zip` is a package in the working directory of R, 
you can install it using the following command.
This is no longer required in the latest version of R.
```R
install.packages("dclong.String_1.0-1.zip", repos=F)
```
6. To get all objects whose name do not start with a dot 
(Usually objects start with dots are not intended to be used by users.) 
in a package you can use `ls(pos="package:pkgname")`. 
If you want to see all objects in a package including these objects starting with a dot, 
you can use `ls(pos="package:pkgname", all.names=T)`.

7. To get the the home package of a package, 
you can use `.find.package`. 
For example, 
to get the home folder of `dclong.EasySave`, 
you can use `.find.package("dclong.EasySave")`.
Another more powerful way is to use `system.file`, 
which allows you both directories and files in a package. 
For example, to find the home directory of `dclong.EasySave`, 
you can use `system.file(package = 'animation')`. 
Instead of finding the home directory, 
you might want to know the path of folder `history` in `dclong.EasySave`. 
This can be done simply by using
`system.file('history',package='dclong.EasySave')`.

8. There are huge number of different packages in R and some of them are design for the same purpose, 
so it is inevitable that some functions in different packages have the same name. 
You should very careful when you are using these function. 
It is important to know what packages are load when R is started. 
To avoid confusion, 
we can always add package prefix to the functions that we want to use. 
For example, 
instead of using function `dir` in `base` package, 
we can use `base::dir` if there is another loaded package having function `dir`.

9. You can use functions in a package by its full name 
(i.e. pkgname::funName) even if the package is not loaded. 
For example, 
you can `symbolToString` in `dclong.String` 
by its full name `dclong.String::symbolToString` even if `dclong.String` is not loaded.

10. When you write a package, 
you might want to link some function in other packages. 
To do so, you can use
```R
\code{\link[PkgName]{FunName}}
```
11. To load a package, 
you can use either `library` or `require`, 
and you do not have to pass the name of the package as character 
(i.e. you do not have to put the name of the package into two double/single quotation marks. 
Surely it works if you pass the name of the package as character.).
The difference between `library` and `require` is that `library` returns all loaded packages 
while `require` return a boolean value indicate whether the loading succeed or not. 
If you want to unload a package `pkgName` from the workspace, 
you can use command `detach(package="pkgName")`.

12. Package `MASS` has many useful functions such as `ginv` 
and `mvrnorm` which can be used to generate multivariate normal random variables.

13. Package `Mvtnorm` has functions which can generate multivariate t random variables 
and multivariate normal random variables.

14. Package `LearnBayes` and `coda` are very useful for Bayes. 
And there are many statistics distributions defined in this package `LearnBayes`.

15. Package `xtable` is useful for outputting objects in R in special format, 
e.g. html or latex.

16. `tensor` in package `tensor` can calculate tensor product of arrays.

17. Package `Rweka` supplies an R interface to Weka which is famous for machine learning.

18. genalg R based genetic algorithm for binary and floating point chromosomes.

19. Package `e1071` : support vector maching

20. There are many useful functions in `utils`. 
If you do not know whether there is a function in R which can do your job, 
you can first check functions in `utils`. 
To see all functions in `utils`, 
you can use `ls(package:utils)`.

21. For a package with a namespace, 
these objected not exported cannot be accessed directly by users. 
This is somehow similar to the concept of class in Java. 
Private methods and instances variables of class cannot be accessed by users directly. 
So you can use non-exported functions 
(similar to private/helper methods in Java)
and non-exported variables (similar to private instances in Java) to help make coding easy.

## Bioconductor

1. Bioconductor is a free, open source and open development
software project for the analysis and comprehension of genomic
data generated by wet lab experiments in molecular biology.

2. `limma` is a famous package among these packages in Bioconductor
project. It performs linear model analysis for microarray data.
But be careful that currently (version 2.8 or earlier) doesn't
support mixed linear model, i.e. the covariance structure of the
linear model must be $\sigma^2 I_n$ if you want to use `limma`
to do analysis on microarray data.

3. `q.jabes` of Nettleton's code is based on the method that
Nettleton published in JABES (2006). It is optim... bh.. is
relatively conservative. Benjamini H..

22. Important Packages and Functions in R

(1) About Optimization  
Since we often use maximum likelihood method to solve problems,
we have to do optimization very often. There are some functions
in R which can help us:

(i) `optimize/optimise{stats}`

- used for 1-dimensional optimization only.

- a interval where the maximum/minimum is expected should
    be specified.

(ii) `optim{stats}`

- can be applied to multiply dimensions.

- includes many advanced algorithms.

- initial values of the parameters are needed.

- a hessian matrix can be returned if needed.

(iii) `nlm{stats}`

- can be applied to multiply dimensions.

- uses Newton-type algorithm, which means that smoothness is required.

- initial values of the parameters are needed.

(iv) `constrOptim{stats}`
This function is similar to the function `optim` except that it can handles linear constraints on parameters. 
Actually this function add a logarithmic barrier and calls function `optim`. 
So it has the following features:

- can be applied to multiply dimensions.

- can do optimization with linear constraints.

- uses an adaptive barrier algorithm.

- similar output as function `optim`.

(v) `nlminb{stats}`
This function can do both unconstrained and constrained optimizations using PORT routines.

Comment: generally speaking, I think function `optim` in R is
more useful for statisticians. However, for 1-dimensional
optimization problem, function `optimize/optimise` is
recommended because it is written specially for 1-dimensional
problems and thus can give us more precise results. For
constrained optimizations, function `constrOptim` and `nlminb`
are recommended.

(2) About Linear Models

(i) `lm{stats}`

- fits linear models including linear regression and
    analysis of variance.

- can also fits general linear models for given
    transformations.

- returns an object of class `lm` or for multiple
    responses of class c(`mlm`,`lm`).

(ii) `nls{stats}`

- fits non-linear models.

- returns an object of class `nls`.

(iii) `lme{nlme}`

- fits linear mix-effect models.

- returns an object of class `lme`.

- can fit unequal variance model, use option 
    {weights=varIdent(...)`

(iv) `lmer{lme4}`

- fits linear mix-effect models.

- returns an object of class `mer`.

(v) `gls{nlme}`

- fits linear models using generalized least squares.

- returns an object of class `gls`.

(vi) `glm{stats}`

- fits generalized linear models.

- returns an object of class inheriting from `glm` which
    inherits from class `lm`.

(vii) `aov{stats}`

(viii)  `anova{stats}`

(ixiv)  Other Miscellaneous Functions

## Unit Test

1. testthat

## Visualization

1. ggplot2

2. tableplot

1. rgl (3-D plot using OpenGL)

2. When you install a package, 
you might get a dependency error or error 
which says that a package does not exists (for your version of R). 
This typicially means that the R you installed is too old to use the package. 
Upgrade your R to the new version can usually solve the problem. 
Get clear about this problem ... 

1. options(repos = c(CRAN = "http://cran.rstudio.com"))

[Tools for Better Cran Experience](https://github.com/metacran)

