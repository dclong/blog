Status: published
Date: 2020-09-01 12:42:15
Author: Benjamin Du
Slug: tips-on-github-actions
Title: Tips on GitHub Actions
Category: Computer Science
Tags: Computer Science, GitHub Actions, CICD
Modified: 2026-01-08 11:31:40

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
    [create-pull-request](https://github.com/peter-evans/create-pull-request)
    .

3. Rust cannot be installed into a global location 
    following instructions at 
    [Install Rust Globally in Linux](https://www.legendu.net/en/blog/install-rust-globally/)
    .
    This might because GitHub Actions VMs have restrictions on environemnt variables.
    You can still install Rust using root (via sudo)
    but this doesn't give you much priviledge
    as the root account in a GitHub Actions VM is restricted too.

5. Good practices for GitHub repository with GitHub Actions workflows:
    - Have 2 protected branches `main` and `dev`,
        where `main` is reserved for releasing 
        and `dev` is reserved for development.
    - Fork the `dev` branch for development.
    - A PR from `dev` to `main` should be made 
        when it is ready to release a new version.

## Runner Images

1. OS: ubuntu-latest, windows-latest, macOS-latest

Please refer to
[runner-images](https://github.com/actions/runner-images)
for support OS images for VMs.

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

## References

- [Common Issues and Solutions for GitHub Actions]( https://www.legendu.net/misc/blog/common-issues-and-solutions-for-github-actions ) 

- [Self-hosted Runners for GitHub Actions]( https://www.legendu.net/misc/blog/self-hosted-runners-for-github-actions ) 

- [Use Docker Containers for GitHub Actions]( https://www.legendu.net/misc/blog/use-docker-containers-for-github-actions ) 

- [Machine learning operations with GitHub Actions and Kubernetes - GitHub Universe 2019](https://www.youtube.com/watch?v=Ll50l3fsoYs&feature=emb_logo)

- [Advanced GitHub Actions: workflows for production grade CI/CD - GitHub Universe 2019](https://www.youtube.com/watch?v=0ahRkhrOePo)

- [Virtual Environments for Github Hosted Runners](https://docs.github.com/en/actions/reference/virtual-environments-for-github-hosted-runners#about-virtual-environments)

- [Github Actions Workflow Error Permission Denied](https://stackoverflow.com/questions/57830375/github-actions-workflow-error-permission-denied)

- [GitHub’s Actions v2 — Tips and Tricks](https://medium.com/inexdigital-fr/githubs-actions-v2-tips-and-tricks-c083ec6cfae0)

- [Questions about PR workflows and actions/checkout@v2](https://github.community/t/questions-about-pr-workflows-and-actions-checkout-v2/122347)

- [Powershell on Windows for GitHub Actions]( https://www.legendu.net/misc/blog/powershell-on-windows-for-github-actions ) 
