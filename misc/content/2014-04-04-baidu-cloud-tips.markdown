Status: published
Author: Ben Chuanlong Du
Date: 2020-02-13 11:27:14
Slug: baidu-cloud-tips
Title: Baidu Yun Tips
Category: Internet
Tags: internet, web, Baidu Yun, cloud, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 
1. Baidu cloud is a good backup solution but not a good synchronization solution.
    Do not try to synchronize your devices via Baidu cloud.

2. `bypy -v upload` 

3. There is a unofficial client for Baidu Cloud 
    at <https://github.com/LiuLang/bcloud>.
    This client support fast upload (comparing hash before uploading).
    However, it is not compatible with Baidu's official client. 
    Suppose a file is uploaded using this unoffical client,
    the offical client won't use fast upload if you upload it again.
    So the suggestion is to stick with one of them.

## Alternatives

https://github.com/Kyle-Kyle/baidudl

https://github.com/iikira/BaiduPCS-Go

https://github.com/liuzhuoling2011/baidupcs-web

https://hub.docker.com/r/auska/docker-baidupcs

https://hub.docker.com/r/oldiy/baidupcs

wine + baidu pan 

Use BaiduExporter (Chrome plugin) to get the link 

Tampermonkey (Chrome plugin) + Greasy Fork (website)

WinTPC VM
