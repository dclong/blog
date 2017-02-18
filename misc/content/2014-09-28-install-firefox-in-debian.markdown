UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2016-07-13 22:21:27
Author: Ben Chuanlong Du
Slug: install firefox in debian
Title: Install Firefox in Debian
Category: Linux
Tags: Linux, Firefox, Debian, web browser

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

you have to update your script based on the DE being used.
but first check whether a desktop file created in GNOME can be used in Xfce or not.

    # download latest firefox
    path=ftp.mozilla.org/pub/mozilla.org/firefox/releases/latest/linux-$(uname -m)/en-US/
    dir=$(mktemp -d)
    echo "Temporary directory \"$dir\" is created."
    cd $dir
    echo "Downloading firefox into \"$dir\" ..."
    wget -r --no-parent -e robots=off http://$path
    path=$(ls $path/firefox-*)
    filename=$(basename $path)
    cp $path $filename
    # decompress firefox installation files
    echo "Decompressing firefox installation file ..."
    if [[ "$filename" == *.tar.bz2 ]]; then
        option=-jxvf
    elif [[ "$extension" == *.tar.gz ]]; then
        option=-zxvf
    else
        echo "Unrecognized installation file!"
        return 1
    fi
    tar $option $filename
    # copy to /opt
    echo "Copying firefox files to /opt ..."
    sudo rm -rf /opt/firefox
    sudo cp -r firefox /opt/
    # install flashplugin-nonfree to make firefox more usable
    echo "Installing flashplugin-nonfree ..."
    wajig install -y flashplugin-nonfree
    # uninstall iceweasel
    if [ "$(wajig list | grep -i iceweasel)" != "" ]; then 
        # wajig purge -y iceweasel
        echo "Please uninstall iceweasel manually!"
    fi
