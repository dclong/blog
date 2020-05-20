Status: published
Date: 2020-05-20 14:04:56
Author: Ben Chuanlong Du
Slug: macports-tips
Title: Tips on MacPorts
Category: OS
Tags: macOS, MacPorts, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

    :::bash
    sudo port selfupdate
    port search pkg
    sudo port install pkg

## MacPorts behind Firewall

1. Use http instead of rsync. 
    Open the file `/opt/local/etc/macports/sources.conf`
    and replace the line 

        :::bash
        rsync://rsync.macports.org/release/tarballs/ports.tar [default]

    with

        :::bash
        http://www.macports.org/files/ports.tar.gz [default]

2. Configure proxy.

        :::bash
        export http_proxy=http://username:password@proxyURL:portNumber
        export HTTP_PROXY=http://username:password@proxyURL:portNumberexport 
        export ftp_proxy=ftp://username:password@proxyURL:portNumber
        export FTP_PROXY=ftp://username:password@proxyURL:portNumber
        export rsync_proxy=username:password@proxyURL:portNumber
        export RSYNC_PROXY=username:password@proxyURL:portNumber

3. Use `sudo port -d sync` instead of `sudo port selfupdate` to print debugging information while updating.

## References

https://destefano.wordpress.com/2011/03/18/macports-behind-a-proxy/

https://samkhan13.wordpress.com/2012/06/15/make-macports-work-behind-proxy/
