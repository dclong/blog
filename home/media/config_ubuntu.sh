#!/bin/bash

if [[ $(id -u) == 0 ]]; then
    prefix=''
else
    prefix=sudo
fi
$prefix apt-get update -y
$prefix apt-get install -y python3 python3-setuptools python3-pip wajig
pip3 install --user loguru

mkdir -p $HOME/archives
git clone git@github.com:dclong/blog.git $HOME/archives/blog
git clone git@github.com:dclong/config.git $HOME/archives/config
git clone git@bitbucket.org:dclong/dsutil.git $HOME/archives/dsutil

xinstall sshc -y -ic
xinstall nodejs -y -ic
xinstall poetry -y -ic
xinstall ipy -y -ic
xinstall svim -y -ic
xinstall docker -y -ic
