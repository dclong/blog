Status: published
Date: 2022-07-28 14:39:20
Modified: 2022-07-31 17:53:03
Author: Benjamin Du
Slug: bash-equivalent-of-the-ifmain-pattern-in-python
Title: Bash Equivalent of the ifmain Pattern in Python
Category: Computer Science
Tags: Computer Science, programming, Shell, Bash, ifmain, Python, module, script, function, import, source

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**


[Fish Shell]( https://www.legendu.net/misc/blog/tips-on-the-fish-shell ) 
is preferred to Bash/Zsh.
The following content is for Bash/Zsh only.

    :::bash
    #!/usr/bin/env bash

    function install_icon.usage() {
        cat << EOF
    NAME
        /scripts/sys/install_icon.sh - Download and install icon to /usr/local/bin/.
    SYNTAX 
        /scripts/sys/install_icon.sh [-h]
    EOF
    }

    function install_icon() {
        if [[ $1 == "-h" ]]; then
            install_icon.usage
            return 0
        fi
        if [[ $# == 1 && "$1" != "-h" || $# > 1 ]]; then
            install_icon.usage
            return 1
        fi
        local URL=https://github.com/legendu-net/icon/releases
        local VERSION=$(basename $(curl -sL -o /dev/null -w %{url_effective} $URL/latest))
        local ARCH="$(uname -m)"
        case "$ARCH" in
            x86_64 )
                ARCH=amd64
                ;;
            arm64 )
                ARCH=arm64
                ;;
            *)
                echo "The architecture $ARCH is not supported!"
                return 2
                ;;
        esac
        curl -sSL $URL/download/$VERSION/icon-$VERSION-$(uname)-${ARCH}.tar.gz -o /tmp/icon.tar.gz
        tar zxf /tmp/icon.tar.gz -C /usr/local/bin/
        chmod +x /usr/local/bin/icon
    }

    if [[ "${BASH_SOURCE[0]}" == "" || "${BASH_SOURCE[0]}" == "$0" ]]; then
        install_icon $@
    fi
