UUID: 9ba8c173-8851-4beb-bda4-a68e1360a23f
Status: published
Date: 2015-06-19 10:30:15
Author: Ben Chuanlong Du
Slug: map-keys-in-linux
Title: Map Keys in Linux
Category: OS
Tags: Linux, keyboard, mapping, swap, setxkbmap, Cinnamon, GNOME, keys
Modified: 2017-03-19 10:30:15

Note: For Vim users, it is appealing to make the `Caps Lock` function like `Escape`.
It is suggested that you make `Caps Lock` an additonal `Escape`
rather than swap them.
This avoid inconsistent key mapping issues when you work remotely via VNC, NoMachine, etc.

## Desktop Environment

Some desktop environment (e.g., Cinnamon, GNOME, etc.) let you define behavior of keys.
For example,
you can follow the steps below to define the behavior of the `Caps Lock` key in Cinnamon.

1. Open System Settings.

2. Select Keybord.

3. Keybord layouts

4. Options (on the right-bottom corner)

5. Caps Lock key behavior

6. Choose the behavior you want.

For the Unity desktop environment,
you need to install `unity-tweak-tool`.
And if you are on the GNOME desktop,
you need `gnome-tweak-tool`.


## setxkbmap

Swap the Caps and the Escape keys.
```bash
setxkbmap -option -option caps:swapescape
```

Unfortunately,
the key mapping partially pass to virtual machines or remote desktops,
which is the worst scenario.
It is suggested that you turn off the mapping on the Linux host
when you work in a VM or a remote desktop.

### Keyboard Configuration

Keyboard in configured in by the file `/etc/default/keyboard` on Linux.
For example,
you can find the line that starts with `XKBOPTIONS`,
and add `ctrl:nocaps` to make Caps Lock an additional Control key
or `ctrl:swapcaps` to swap Caps Lock and Control.
Run the following command after updating the file `/etc/default/keyboard` to make it in effect.
```
sudo dpkg-reconfigure keyboard-configuration
```
This way is better as it will take effect on the virtual consoles as well as in the GUI DE.

## More References

- <http://askubuntu.com/questions/444714/how-do-i-swap-escape-and-caps-lock-in-14-04/446725#446725>

- <http://www.fascinatingcaptain.com/howto/remap-keyboard-keys-for-ubuntu/>

- <http://askubuntu.com/questions/885045/how-to-swap-ctrl-and-alt-keys-in-ubuntu-16-04/885047>

- <http://askubuntu.com/questions/453793/remapping-caps-lock-in-14-04-trusty-tahr>

- <http://askubuntu.com/questions/444714/how-do-i-swap-escape-and-caps-lock-in-14-04/446725#446725>
