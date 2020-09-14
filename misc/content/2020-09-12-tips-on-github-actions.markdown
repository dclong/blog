Status: published
Date: 2020-09-13 20:40:53
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

## References

https://www.youtube.com/watch?v=Ll50l3fsoYs&feature=emb_logo

https://www.youtube.com/watch?v=0ahRkhrOePo

https://docs.github.com/en/actions/reference/virtual-environments-for-github-hosted-runners#about-virtual-environments

https://stackoverflow.com/questions/57830375/github-actions-workflow-error-permission-denied