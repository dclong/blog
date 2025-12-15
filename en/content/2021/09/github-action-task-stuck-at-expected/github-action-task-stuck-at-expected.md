Status: published
Date: 2021-09-15 01:11:06
Modified: 2025-12-14 16:57:11
Author: Benjamin Du
Slug: github-action-task-stuck-at-expected
Title: GitHub Action Task Stuck At Expected
Category: Computer Science
Tags: Computer Science, programming, GitHub, Actions, task, check, stuck, expected



Github pull request - Waiting for status to be reported

<img width="812" height="426" alt="Image" src="https://github.com/user-attachments/assets/671e80e7-94b0-4738-a1a1-83c36b9a3abf" />

1. The simplest manually solution is to close the PR and reopen it.

2. In my case, 
    the issue was due to `GITHUB_TOKEN` was used for the GitHub Action
    [create-pull-request](https://github.com/peter-evans/create-pull-request)
    .
    Creating a repository secret 
    and use it to authenticate the GitHub Action
    [create-pull-request](https://github.com/peter-evans/create-pull-request)
    resolved the issue.
