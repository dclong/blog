Status: published
Date: 2020-02-29 22:26:41
Author: Ben Chuanlong Du
Slug: ansible-tips
Title: Cluster Management Made Easy with Ansible
Category: Software
Tags: Software, Ansible, Python, cluster management, server management
Modified: 2020-02-29 22:26:41

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Installation

    :::bash
    sudo pip3 install ansible

## Configuration

Ansible looks for configuration file in the following order.

1. `ansible.cfg` in the current directory.

2. `~/.ansible.cfg`

3. `/etc/ansible.cfg`

## Examples

Copy a file to each machine in the cluster.

    :::bash
    proxychains ansible all \
        -i hosts \
        --user=stack \
        --private-key=~/.ssh/rsa \
        -m copy \
        -a "src=../pkg.tar.gz dest=~/"

Install an R package on each machine in the cluster.

    :::bash
    proxychains ansible all \
        -i hosts \
        --user=stack \
        --private-key=~/.ssh/spot_rsa \
        -a 'Rscript -e "install.packages(\"../pkg.tar.gz\")"'

## Host Key Checking

Ansible 1.2.1 and later have host key checking enabled by default.
If a machine in the cluster is reimaged, 
it will result in an error message (host fingerprint changed).
This can be fixed by removing keys from `~/.ssh/known_hosts`.
If a machine in the cluster is not in `~/.ssh/known_hosts`,
it will prompt for confirmation of adding the host as a known one. 
To avoid those interuptions,
you can add the following into your Ansible configuration file.

    :::text
    [defaults]
    host_key_checking = False

Alternatively this can be set by an environment variable:

    :::bash
    export ANSIBLE_HOST_KEY_CHECKING=False

Also note that host key checking in paramiko mode is slow, 
therefore switching to `ssh` is recommended 
when you have host key checking enabled in Ansible.

## References

http://www.legendu.net/misc/blog/run-commands-on-remote-machines/

https://github.com/ansible/ansible

https://serversforhackers.com/running-ansible-programmatically

