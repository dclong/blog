Status: published
Date: 2020-05-22 13:20:50
Author: Ben Chuanlong Du
Title: Install Firefox and Thunderbird Automatically on Debian
Slug: install-firefox-and-thunderbird-automatically
Category: Software
Tags: software, installation, Thunderbird, Firefox, todo, Debian

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


    #!/usr/bin/env bash

    # download latest thunderbird
    path=ftp.mozilla.org/pub/mozilla.org/thunderbird/releases/latest/linux-$(uname -m)/en-US/
    dir=$(mktemp -d)
    echo "Temporary directory \"$dir\" is created."
    cd $dir
    echo "Downloading thunderbird into \"$dir\" ..."
    wget -r --no-parent -e robots=off http://$path
    path=$(ls $path/thunderbird-*)
    filename=$(basename $path)
    cp $path $filename
    # decompress thunderbird installation files
    echo "Decompressing thunderbird installation file ..."
    if [ "$filename" == *.tar.bz2 ]; then
        option=-jxvf
    elif [ "$filename" == *.tar.gz ]; then
        option=-zxvf
    else
        echo "Unrecognized installation file!"
        return 1
    fi
    tar $option $filename
    # copy to /opt
    echo "Copying thunderbird to /opt ..."
    sudo rm -rf /opt/thunderbird
    sudo cp -r thunderbird /opt/
    # uninstall icedove
    if [ "$(wajig list | grep -i icedove)" != "" ]; then
        # wajig purge -y icedove
        echo "Please uninstall icedove."
    fi
