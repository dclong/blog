UUID: 7777a516-ccea-454d-847a-b26589d53623
Status: published
Date: 2017-08-22 12:37:19
Author: Ben Chuanlong Du
Slug: get-group-names-on-linux-unix
Title: Get Group Names on Linux/Unix
Category: OS
Tags: Linux, Mac OSX, group, python, getent, dscl
Modified: 2017-10-22 12:37:19

## Linux

1. Get information of the `staff` group.

        $ getent group staff
        staff:x:20:

2. Get group ID of the `staff` group.

        $ getent group staff | cut -d: -f3
        20

## Mac

1. Get information of the `staff` group.

        $ dscl . -read /Groups/staff 

2. Get group ID of the `staff` group.

        $ dscl . -read /Groups/staff | awk '($1 == "PrimaryGroupID:") { print $2 }'
        20

As a matter of fact, 
`dscl` in Mac is the equivalence of `getent` in Linux.
Both of them can be used to query user information as well. 

1. Querying user information using `getent`.

        getent passwd <uid>

2. Querying user information using `dscl`.

        dscl . -search /Users UniqueID <uid>

In both cases, 
you then need to parse the output to get the username. 
The output of `getent` is standard /etc/passwd format, something like this:

    zamboni:x:1005:1005:Diego Zamboni,,,:/home/zamboni:/bin/bash

This is very easy to parse (using awk, for example) and gives you the full record at once.
`dscl` only provides the field you searched for, something like this:

    zamboni              UniqueID = (
        501
    )

So if you want to get the full record, you would need to get the username and then query for it, like this:

    dscl . -read /Users/zamboni

The output is harder to parse, 
in "keyword: value" form, 
but with many multiline values. 
You can also use the -plist option to get it in Apple's plist format, which could be easier to parse.

## Cross-platform Ways

You can also get group information using the `grp` module in Python.

    import grp
    print(grp.getgrnam("staff").gr_gid)

