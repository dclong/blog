Status: published
Author: Ben Chuanlong Du
Date: 2020-01-26 13:02:55
Slug: curl-tips
Title: Tips on cURL and Wget
Category: Software
Tags: tips, cURL, downloading, web, wget
Modified: 2020-01-26 13:02:55

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## cURL vs Wget

[curl vs wget](https://daniel.haxx.se/docs/curl-vs-wget.html)
has a detailed comparison between curl and wget.
In short, 
curl is more powerful and flexible and thus is preferred to wget
unless you want to download content recursively from a site 
(which curl does not support currently).

## Alternatives to `curl`

[Convert curl syntax to Python, Node.js, R, PHP, Strest, Go, JSON, Rust](https://curl.trillworks.com/)

The postman plugin for Google Chrome can also convert curl command to other programming languages.

## Proxy

A general way (works for most other command-line tools too) is set the environment variables `http_proxy` and `https_proxy`
(and `ftp_proxy`, etc. if need them).
This way is preferred if your command/script to run has dependencies which also requires proxy to work.

    :::bash
    export http_proxy=http://your.proxy.server:port
    export https_proxy=http://your.proxy.server:port

Another simple way is to use the option `--proxy` directly.
This way is preferred if your command/script does not have other dependencies which also requires proxy to work.
    
    :::bash
    curl --proxy http://your.proxy.server:port ...

## Tricks and Traps

1. Use the `-L` option to follow redirect URLs. 
    This is a really useful trick to use curl to download things from GitHub.

## cURL Examples

1. Get redirected URL.

        :::bash
        curl -sSL -o /dev/null -w %{url_effective} https://github.com/dclong/dsutil/releases/latest

2. Use browser cookie.

        :::bash
        curl -v --cookie-jar cjar \
            --output /dev/null \
            http://cos.name/cn/

        curl -v --cookie cjar --cookie-jar cjar \
            --data 'user_login={username}' \
            --data 'password={password}' \
            --data 'form_id=login' \
            --output cos.html \
            http://cos.name/cn/

        :::bash
        curl -v --cookie-jar cjar \
            --output /dev/null \
            https://www.economy.com/home/login/a_login.asp

        curl -v --cookie cjar \
            --cookie-jar cjar \
            --data 'email={user_email@some.com}' \
            --data 'password={password}' \
            --data 'form_id=frmMain' \
            --output moody.html \
            https://www.economy.com/home/login/a_login.asp

        :::bash
        curl -v --cookie-jar cjar \
            --output /dev/null \
            https://www.ncreif.org/login.aspx

        curl -v --cookie cjar \
            --cookie-jar cjar \
            --data 'username={user_name}' \
            --data 'password={password}' \
            --data 'form_id=form1' \
            --output ncreif.html \
            https://www.ncreif.org/login.aspx

        :::bash
        wget --no-check-certificate \
            --load-cookies=ff_cookies.txt \
            -p https://bitbucket.org/dclong/config/get/

The easy way: login with your browser,
and give the cookies to wget

Easiest method: in general,
you need to provide wget or `cURL` with the (logged-in) cookies
from a particular website for them to fetch pages as if you were logged in.

If you are using Firefox,
it's easy to do via the Export Cookies add-on.
Install the add-on, and:

Go to Tools...Export Cookies,
and save the cookies.txt file (you can change the filename/destination).

Open up a terminal,
and use wget with the `--load-cookies=FILENAME` option, e.g.

    :::bash
    wget --load-cookies=cookies.txt http://en.wikipedia.org/wiki/User:A

For `cURL`, it's

    :::bash
    curl --cookie cookies.txt ...


The hard way: use `cURL` (preferably) or `wget` to manage the entire session

A detailed how-to is beyond the scope of this answer,
but you use `cURL` with the --cookie-jar or `wget`
with the --save-cookies --keep-session-cookiesoptions,
along with the HTTP/S PUT method to log in to a site,
save the login cookies, and then use them to simulate a browser.
Needless to say,
this requires going through the HTML source for the login page (get input field names, etc.),
and is often difficult to get to work for sites
using anything beyond simple login/password authentication.

Tip: if you go this route,
it is often much simpler to deal with the mobile version of a website (if available),
at least for the authentication step.


## Tricks and Traps

`-q`/`--quiet`: quiet mode which turns off wget's output.
This option is helpful if you want to have the downloaded content as output only.
`curl` by default is in quiet mode.
You can force it (or overwrite other non-quiet options) using `-s`/`--silent`.

## Wget Examples

To filter for specific file extensions:

    :::bash
    wget -A pdf,jpg -m -p -E -k -K -np http://site/PATH/

This will mirror the site, but the files without jpg or pdf extension will be automatically removed.

Download all contents under the link.

    :::bash
    wget -r --no-parent -e robots=off http://site/PATH/

Download all contents except HTML files under the link.

    :::bash
    wget -r --no-parent -e robots=off -R "*.html"
    wget --no-check-certificate
    wget --random-wait -r -p -e robots=off -U mozilla

## References

https://stackoverflow.com/questions/9445489/performing-http-requests-with-curl-using-proxy