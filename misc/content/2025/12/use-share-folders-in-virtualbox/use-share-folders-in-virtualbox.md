Status: published
Date: 2025-12-07 18:37:30
Modified: 2025-12-09 00:21:43
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
  Do check the following option(s).
    - Make Machine-permanent
        - The shared folder will survive VM reboots.
    - Make Global
        - The shared folder will be available to all VMs even after reboots.

    <img width="602" height="558" alt="Image" src="https://github.com/user-attachments/assets/94eaeb60-fbba-4d2e-86a3-961ed473b342" />

2. It is suggested that you mount a shared folder manually.

        sudo mount -t vboxsf -o uid=$(id -u),gid=$(id -u),fmask=177,dmask=077 \
            name_of_shared_folder mount_point
        
3. As alternatives to shared folders, 
    you can
    - SSH into the host machine
    - use sshfs
    - start JupyterLab, VSCode Servers on the host and work in the guest VM
