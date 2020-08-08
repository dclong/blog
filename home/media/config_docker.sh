#!/bin/bash

if [ -d /home_host/$(id -un)/archives/ ]; then
    ln -svf /home_host/$(id -un)/archives $HOME/
fi
if [ -f /workdir/user/$(id -un) ]; then
    ln -svfT /workdir/user/$(id -un) $HOME/projects
fi

xinstall sshc -c
xinstall --sudo git -ic
xinstall svim -ic
xinstall ipy -c
xinstall dsutil -ic
