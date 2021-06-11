Status: published
Date: 2021-01-08 13:41:56
Author: Benjamin Du
Slug: github-tips
Title: Tips on GitHub
Category: Computer Science
Tags: programming, GitHub, tips, GitHub Actions, CICD, CI, CD
Modified: 2021-01-08 13:41:56

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Tips and Traps

1. Have at least 2 branches master and dev.
    Reserve the master branch for releasing purpose 
    and the dev banch for development.
    Protect the master branch on GitHub to require checks to pass before merging. 
    If it is only one person (yourself) developing on the project,
    do not require pull request review before merging. 
    Otherwise, if there are multiple people developing on the projects, 
    require pull request review (of at least 1 person) before merging.

2. CI workflows should be set up to make sure that the master branch is always valid.

3. A development (dev, daily, next, or whatever name) release should be made 
    when a push is made into the master branch. 
    An official tagged release should be made on creation of a new tag.
    A new tag should only be created on the lastest commit of the master branch!

## Deploy Keys

Deploy Keys are SSH keys which access restricted to a specific repository only.

https://developer.github.com/v3/guides/managing-deploy-keys/#deploy-keys

## [Creating a personal access token for the command line](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)

## [Creating a PR Template for Your Repository](https://docs.github.com/en/github/building-a-strong-community/creating-a-pull-request-template-for-your-repository)

## [Connect JIRA Cloud to GitHub](https://confluence.atlassian.com/adminjiracloud/connect-jira-cloud-to-github-814188429.html)

## Some Good Organizations and Repositories

https://github.com/Meituan-Dianping

https://github.com/xingshaocheng/architect-awesome#fork-destination-box

https://ai.googleblog.com/

https://coolshell.cn/

https://brendansterne.com/

https://www.raychase.net/

https://www.kawabangga.com/

## References

[GitHub Support Community](https://github.community/)

[GitHub Support - Feedback](https://support.github.com/contact/feedback)

https://stackoverflow.com/questions/26372417/github-oauth2-token-how-to-restrict-access-to-read-a-single-private-repo


https://github.blog/2019-06-06-generate-new-repositories-with-repository-templates/

https://mp.weixin.qq.com/s/r9dNXpoH8F5CMoHdyv6BFQ

[Tips on GitHub Actions](http://www.legendu.net/misc/blog/tips-on-github-actions)
