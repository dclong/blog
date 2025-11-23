Status: published
Date: 2025-11-23 10:49:01
Modified: 2025-11-23 10:49:01
Author: Benjamin Du
Slug: self-hosted-runners-for-github-actions
Title: Self-hosted Runners for GitHub Actions
Category: Computer Science
Tags: Computer Science, programming, GitHub Actions, CICD, development, self-hosted, runner

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. straight forward to set up self-hosted runners following instructions

2. No need for the machine to be publicly accessible

3. Currently, 
    a runner can be configured to accept only 1 repo in a personal account 
    (which is inconveneint)
    or multiple repositories in a GitHub organization.

4. A self-hosted runner is able to use SSH keys on the host.
    However, 
    if a Docker container is used with a self-hosted runner,
    you have to properly expose SSH keys on the host to the Docker container.
    A feasible way is to 

        1. Configure the GitHub Action workflow to mount `$HOME/.ssh` to `/ssh`.
        2. Copy `/ssh` to `/root/.ssh` in the Docker container. 
        3. Run `chmod 600 /root/.ssh/*` to ensure right permissions of SSH keys and configuration files.

## Idle Organization Runners Which Don't Pick up Jobs 

![](https://github.com/user-attachments/assets/5b494a23-7ecd-40da-8d1f-47d373d14c3c)

![](https://github.com/user-attachments/assets/5b494a23-7ecd-40da-8d1f-47d373d14c3c)

[Self-hosted runner registered as idle but not picking up jobs #26823](https://github.com/orgs/community/discussions/26823)

[Self-hosted runners is idle but not picking up jobs #120813](https://github.com/orgs/community/discussions/120813)

