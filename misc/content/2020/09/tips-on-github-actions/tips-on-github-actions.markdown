Status: published
Date: 2020-09-01 12:42:15
Author: Benjamin Du
Slug: tips-on-github-actions
Title: Tips on GitHub Actions
Category: Computer Science
Tags: Computer Science, GitHub Actions, CICD
Modified: 2021-06-01 12:42:15

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Tips and Traps

1. You can use `sudo` without password in Linux and macOS when running GitHub Actions.

2. `GITHUB_TOKEN` is an automatically generated secret 
    that lets you make authenticated calls to the GitHub API in your workflow runs. 
    Actions generates a new token for each job and expires the token when a job completes.

2. OS: ubuntu-latest, windows-latest, macOS-latest

3. Docker container is available in Ubuntu and Windows but not macOS in GitHub Actions due to license issues.
    To use Docker in macOS in GitHub Actions,
    you have to install it manually.
    Please refer to 
    [Is it possible to install and configure Docker on MacOS runner?](https://github.community/t/is-it-possible-to-install-and-configure-docker-on-macos-runner/16981)
    for more details.

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


## GitHub Actions for Python

https://hynek.me/articles/python-github-actions/

https://github.com/actions/setup-python

## Pull Request 

https://github.com/peter-evans/create-pull-request

[Create PR from push on a given branch](https://github.com/peter-evans/create-pull-request/issues/544)

## Examples

[Using semantic-release with GitHub Actions](https://www.youtube.com/watch?v=rCXq86FOlzQ)

[automerge-action](https://github.com/pascalgn/automerge-action)

[Automatic Deployment With Github Actions](https://www.youtube.com/watch?v=X3F3El_yvFg)

[Zip Code Base with Github Actions for Releases](https://www.youtube.com/watch?v=yAkMgcfdok0)

[GitHub Automatic Releases](https://github.com/marketplace/actions/automatic-releases)

[Introducing GitHub Package Registry](https://www.youtube.com/watch?v=N_-Cu9_2YAA)

## References

https://www.youtube.com/watch?v=Ll50l3fsoYs&feature=emb_logo

https://www.youtube.com/watch?v=0ahRkhrOePo

https://docs.github.com/en/actions/reference/virtual-environments-for-github-hosted-runners#about-virtual-environments

https://stackoverflow.com/questions/57830375/github-actions-workflow-error-permission-denied

[GitHub’s Actions v2 — Tips and Tricks](https://medium.com/inexdigital-fr/githubs-actions-v2-tips-and-tricks-c083ec6cfae0)

[Questions about PR workflows and actions/checkout@v2](https://github.community/t/questions-about-pr-workflows-and-actions-checkout-v2/122347)