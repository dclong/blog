Status: published
Date: 2020-10-18 15:12:07
Author: Benjamin Du
Slug: tips-on-github-actions
Title: Tips on GitHub Actions
Category: Computer Science
Tags: Computer Science, GitHub Actions, CICD

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Tips and Traps

1. You can use `sudo` without password in Linux and macOS when running GitHub Actions.

2. OS: ubuntu-latest, windows-latest, macOS-latest

3. Docker container is available in Ubuntu and Windows but not macOS in GitHub Actions due to license issues.
    To use Docker in macOS in GitHub Actions,
    you have to install it manually.
    Please refer to 
    [Is it possible to install and configure Docker on MacOS runner?](https://github.community/t/is-it-possible-to-install-and-configure-docker-on-macos-runner/16981)
    for more details.

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

## Examples

[Using semantic-release with GitHub Actions](https://www.youtube.com/watch?v=rCXq86FOlzQ)

[automerge-action](https://github.com/pascalgn/automerge-action)

(https://www.youtube.com/watch?v=X3F3El_yvFg)[Automatic Deployment With Github Actions]

## References

https://www.youtube.com/watch?v=Ll50l3fsoYs&feature=emb_logo

https://www.youtube.com/watch?v=0ahRkhrOePo

https://docs.github.com/en/actions/reference/virtual-environments-for-github-hosted-runners#about-virtual-environments

https://stackoverflow.com/questions/57830375/github-actions-workflow-error-permission-denied