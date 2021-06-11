UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2016-12-10 01:57:25
Author: Ben Chuanlong Du
Slug: install-r-packages-on-windows-behind-proxy
Title: Install R Packages Behind Proxy on Windows 
Category: Computer Science
Tags: programming, R, Windows, install package, proxy
Modified: 2016-12-10 01:57:25


There are 3 ways to install R packages behind a proxy on Windows.

1. Download packages and install them locally.
This is generally speaking not recommended 
as it is a hassle to resolve dependencies.
When the package you want to install has no (or very few) dependencies,
you can use this way to install it.

2. Run `setInternet2(use=True)` and then install packages as usual.
This is the recommended way to install R packages behind a proxy on Windows.

3. Select "Internet2" when you are asked to specify standard or Internet2 
during installation of R.
If you have done this during the installation of R,
you can install packages as usually with no need to run `setInternet2(use=True)`.

4.  If you have a proxy server to use, 
you can first setup proxy environment variables 
and then install R packages.
Proxy environment variables can be set using the following code. 

        Sys.setenv(http_proxy = 'proxy_server:port')
        Sys.setenv(https_proxy = 'proxy_server:port')

    This is a more general way and is recommended if you have a proxy serve to use.

Note that working in a Linux virtual machine on your office laptop with Windows OS
can possibly help you circumvent the proxy issue.
