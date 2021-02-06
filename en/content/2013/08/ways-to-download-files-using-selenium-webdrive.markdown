Status: published
Date: 2019-02-10 17:14:12
Slug: ways-to-download-files-using-selenium-webdrive
Author: Ben Chuanlong Du
Title: Ways to Download Files Using Selenium Webdrive
Category: Software
Tags: Web, WebDrive, automation, Selenium, software

Selenium WebDrive cannot have no control of system Dialog, 
so you have to avoid the Dialog when downloading files using WebDrive.

The first way is to enable automatical download in the browser
that you use with Seleniu WebDrive. 
So when click a file link, 
the file is automatically downloaded to the directory that you set.
The second (and better way) is to export the cookie of the browser,
extract the download link and then use the command `wget` or `curl` to download it. 
Surely you have to use the cookie with `wget` or `curl` if authentication is required on the web.
