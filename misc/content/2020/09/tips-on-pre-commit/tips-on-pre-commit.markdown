Status: published
Date: 2020-09-09 12:03:21
Author: Benjamin Du
Slug: tips-on-pre-commit
Title: Tips on pre-commit
Category: Computer Science
Tags: Computer Science, Git hooks, pre-commit, CICD, GitHub Actions
Modified: 2021-03-09 12:03:21

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


It is suggested that you leverage CICD tools (e.g., GitHub Actions)
instead of Git Hooks which happens locally.
However, 
Git hooks can be useful for simple and fast local code formatting.

## Quick Start

1. Install pre-commit.

        :::bash
        pip3 install pre-commit

2. Edit `.pre-commit-config.yaml`.
    Below is an example of of leveraging pre-commit 
    to automate local linting and formatting for Python projects.

        :::yaml
        fail_fast: true
        repos:
        - repo: local
            hooks:
            - id: system
                name: pylint
                entry: poetry run pylint template_python
                pass_filenames: false
                language: system
        - repo: local
            hooks:
            - id: system
                name: pytype
                entry: poetry run pytype template_python
                pass_filenames: false
                language: system
        - repo: local
            hooks:
            - id: system
                name: yapf
                entry: poetry run yapf -r template_python
                pass_filenames: false
                language: system

3. Install the git hook scripts.

        :::bash
        pre-commit install

## References

https://pre-commit.com/

https://github.com/pre-commit/pre-commit

misc/content/2020-09-11-tips-on-pre-commit.markdown

https://about.gitlab.com/blog/2019/01/31/pre-commit-post-deploy-is-dead/
