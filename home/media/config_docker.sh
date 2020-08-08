#!/bin/bash

ln -svf /home_host/$(id -un)/archives $HOME/
ln -svfT /workdir/user/$(id -un) $HOME/projects

xinstall sshc -c
xinstall --sudo git -ic
xinstall svim -ic
xinstall ipy -c
xinstall dsutil -ic
