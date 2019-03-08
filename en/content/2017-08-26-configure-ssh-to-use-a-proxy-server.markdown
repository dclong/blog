Status: published
Date: 2019-03-07 23:42:48
Author: Ben Chuanlong Du
Slug: configure-ssh-to-use-a-proxy-server
Title: Configure SSH to Use a Proxy Server
Category: Linux
Tags: Linux, SSH, proxy server

Suppose you have a production server that you want to visit via SSH,
however,
it is not accessible directly.
Instead,
you have to visit it from a bastion/proxy server.
You can configure SSH to use the bastion/proxy server when visiting the production server.
```
Host <production_server>
ProxyCommand ssh <proxy_server> -W %h:%p

Host *

SendEnv LANG LC_*
HashKnownHosts yes
GSSAPIAuthentication yes
GSSAPIDelegateCredentials no
# make connection alive
ServerAliveInterval 90
ServerAliveCountMax 3
```

Wildcards and NOT operators are supported.

        Host *.xxx.xxx.com !*.exclude.com
        ProxyCommand ssh proxy_server_address -W %h:%p
        Host *

Notice that you can also specify the proxy to use directly
via the option `-o ProxyCommand="ssh proxy_server -W %h:%p"`.
For example,

        ssh -o ProxyCommand="ssh proxy_server -W %h:%p" target_server
