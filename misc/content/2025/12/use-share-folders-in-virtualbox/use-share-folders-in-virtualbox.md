Status: published
Date: 2025-12-07 18:37:30
Modified: 2025-12-07 20:43:38
Author: Benjamin Du
Slug: use-share-folders-in-virtualbox
Title: Use Share Folders in VirtualBox
Category: Computer Science
Tags: Computer Science, programming, VirtualBox, shared, folder, mount

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

 
1. Do NOT check any of the following options unless you know what you are doing.
    - Read-only
        - You won't be able to write to the share directory.
    - Auto-mount
        - Auto-mount uses the root account by default.
        - Not sure whether it uses the user account if a root account is not created in the VM.
    - Make Machine-permanent
        - You won't be able to mount it manually even if you try to unmount it first.
    - Make Global
        - You won't be able to mount it manually even if you try to unmount it first.

    <img width="592" height="562" alt="Image" src="https://github.com/user-attachments/assets/ce0f62d6-5bf8-4bdc-9932-647c845cf7fb" />

2. It is suggested that you mount a shared folder manually.

        sudo mount -t vboxsf -o uid=$(id -u),gid=$(id -u),fmask=177,dmask=077 \
            name_of_shared_folder mount_point
        
3. As alternatives to shared folders, 
    you can
    - SSH into the host machine
    - use sshfs
    - start JupyterLab, VSCode Servers on the host and work in the guest VM
