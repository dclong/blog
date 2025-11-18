Status: published
Date: 2020-09-01 12:42:15
Author: Benjamin Du
Slug: tips-on-github-actions
Title: Tips on GitHub Actions
Category: Computer Science
Tags: Computer Science, GitHub Actions, CICD
Modified: 2025-11-17 19:55:48

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Tips and Traps

1. You can use `sudo` without password in Linux and macOS when running GitHub Actions.

2. GitHub Actions supports [manual triggers with workflow_dispatch](https://github.blog/changelog/2020-07-06-github-actions-manual-triggers-with-workflow_dispatch/).
    Workflow parameters are supported in manually triggers.

2. `GITHUB_TOKEN` is an automatically generated secret 
    that lets you make authenticated calls to the GitHub API in your workflow runs. 
    Actions generates a new token for each job and expires the token when a job completes.
    `GITHUB_TOKEN` can also be used for the GitHub Action `peter-evans/create-pull-request` to create PRs automatically.
    However,
    GitHub bot is the owner of a PR created by the GitHub action 
    [create-pull-request](https://github.com/peter-evans/create-pull-request) with `GITHUB_TOKEN` 
    which might have issues triggering other pipelines listening to PR events.
    A simple solution to this problem is to manually create a repository secret (e.g., `GITHUBACTIONS`)
    and use it to autenticate the GitHub Action 
    [create-pull-request](https://github.com/peter-evans/create-pull-request) with `GITHUB_TOKEN` 
    .

3. Rust cannot be installed into a global location 
    following instructions at 
    [Install Rust Globally in Linux](https://www.legendu.net/en/blog/install-rust-globally/)
    .
    This might because GitHub Actions VMs have restrictions on environemnt variables.
    You can still install Rust using root (via sudo)
    but this doesn't give you much priviledge
    as the root account in a GitHub Actions VM is restricted too.

4. The `runner` account (even with `sudo`) in GitHub Actions VMs 
    have restricted priviledges.
    For example, 
    the Linux perf (and equivalent) tools cannot be run in GitHub Actions VMs
    even if `sudo` is used.
    Docker containers running in GitHub Actions VMs are restricted too.
    For more details,
    please refer to
    [Supported Linux capabilities](https://docs.github.com/en/actions/creating-actions/dockerfile-support-for-github-actions#supported-linux-capabilities)
    .

3. OS: ubuntu-latest, windows-latest, macOS-latest

4. Docker container is available in Ubuntu and Windows but not macOS in GitHub Actions due to license issues.
    To use Docker in macOS in GitHub Actions,
    you have to install it manually.
    Please refer to 
    [Is it possible to install and configure Docker on MacOS runner?](https://github.community/t/is-it-possible-to-install-and-configure-docker-on-macos-runner/16981)
    for more details.
    
5. Good practices for GitHub repository with GitHub Actions workflows:
    - Have 2 protected branches `main` and `dev`,
        where `main` is reserved for releasing 
        and `dev` is reserved for development.
    - Fork the `dev` branch for development.
    - A PR from `dev` to `main` should be made 
        when it is ready to release a new version.

## Issues and Solutions

### Error: The process '/usr/bin/git' failed with exit code 1

Sympton: A GitHub Actions workflow fail to checkout a branch of a repository 
and throws the following error message.

> Error: The process '/usr/bin/git' failed with exit code 1

Possible Causes and Solutions: It's possible that you use a branch name 
(e.g., used `main` while the repo does not have a `main` branch) which does not exist. 
If so, 
use the correct branch name might fix the issue.

## Branch Matching

    on:
    push:
        branches:    
        - '*'         # matches every branch that doesn't contain a '/'
        - '*/*'       # matches every branch containing a single '/'
        - '**'        # matches every branch
        - '!master'   # excludes master

For more discussions,
please refer to
[GitHub Actions: how to target all branches EXCEPT master?](https://stackoverflow.com/questions/57699839/github-actions-how-to-target-all-branches-except-master)
and
[Workflow syntax for GitHub Actions](https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions)
.


## PowerShell on Windows

### Set PATH 

echo "::add-path::./swigwin-4.0.1"

echo %programfiles%
echo ::set-env name=ProgramFilesPath::%programfiles%

https://stackoverflow.com/questions/60169752/how-to-update-the-path-in-a-github-action-workflow-file-for-a-windows-latest-hos

https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-commands-for-github-actions#adding-a-system-path

Prepends a directory to the system PATH variable for all subsequent actions in the current job. The currently running action cannot access the new path variable.


## Good Github Actions

### checkout

### [ssh-agent](https://github.com/webfactory/ssh-agent)
[ssh-agent](https://github.com/webfactory/ssh-agent)
is a GitHub Action to setup `ssh-agent` with a private key.

### [bencher](https://github.com/bencherdev/bencher)
[Bencher](https://github.com/bencherdev/bencher)
is a suite of continuous benchmarking tools.

### GitHub Actions for Python

https://hynek.me/articles/python-github-actions/

https://github.com/actions/setup-python

### Pull Request 

https://github.com/peter-evans/create-pull-request

[Create PR from push on a given branch](https://github.com/peter-evans/create-pull-request/issues/544)

### Examples

[Using semantic-release with GitHub Actions](https://www.youtube.com/watch?v=rCXq86FOlzQ)

[automerge-action](https://github.com/pascalgn/automerge-action)

[Automatic Deployment With Github Actions](https://www.youtube.com/watch?v=X3F3El_yvFg)

[Zip Code Base with Github Actions for Releases](https://www.youtube.com/watch?v=yAkMgcfdok0)

[GitHub Automatic Releases](https://github.com/marketplace/actions/automatic-releases)

[Introducing GitHub Package Registry](https://www.youtube.com/watch?v=N_-Cu9_2YAA)

## Self-hosted Runners

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

### Idle Organization Runners Which Don't Pick up Jobs 

![](https://github.com/user-attachments/assets/5b494a23-7ecd-40da-8d1f-47d373d14c3c)

![](https://github.com/user-attachments/assets/5b494a23-7ecd-40da-8d1f-47d373d14c3c)

https://github.com/orgs/community/discussions/26823
Self-hosted runner registered as idle but not picking up jobs #26823

https://github.com/orgs/community/discussions/120813
Self-hosted runners is idle but not picking up jobs #120813


## References

https://www.youtube.com/watch?v=Ll50l3fsoYs&feature=emb_logo

https://www.youtube.com/watch?v=0ahRkhrOePo

https://docs.github.com/en/actions/reference/virtual-environments-for-github-hosted-runners#about-virtual-environments

https://stackoverflow.com/questions/57830375/github-actions-workflow-error-permission-denied

[GitHub’s Actions v2 — Tips and Tricks](https://medium.com/inexdigital-fr/githubs-actions-v2-tips-and-tricks-c083ec6cfae0)

[Questions about PR workflows and actions/checkout@v2](https://github.community/t/questions-about-pr-workflows-and-actions-checkout-v2/122347)
