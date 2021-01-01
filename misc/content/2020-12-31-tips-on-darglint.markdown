Status: published
Date: 2020-12-31 18:23:21
Author: Benjamin Du
Slug: tips-on-darglint
Title: Tips on Darglint
Category: Computer Science
Tags: Computer Science, darglint, docstring, documentation, Python, doc, lint, linter

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Configuration 

It is suggested that you place configuration into a file named `.darglint` 
under the root directory of your project.
When darglint supports `pyproject.toml`, 
the configuration should be moved into `pyproject.toml`.
Below is an example of configuration.

    :::text
    [darglint]
    docstring_style=sphinx
    message_template={path}:{line}: {msg_id}: {msg}
