Status: published
Date: 2023-04-01 18:21:35
Modified: 2025-06-13 23:35:33
Author: Benjamin Du
Slug: ruff-is-an-extremely-fast-python-linter-written-in-rust
Title: Ruff Is An Extremely Fast Python Linter Written in Rust
Category: Computer Science
Tags: Computer Science, programming, Python, Ruff, lint, linter

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Use ruff In a uv Managed Python Project

    uv run ruff check 
    uv run ruff format . 

## Use ruff Standalone 

The most convenient way to use run ruff standalone is via `uvx`.

    uvx ruff check /some/path
    uvx ruff format /some/path
    
## Format Python Scripts with Indention Width = 2

    ruff format --config indent-width=2 path/to/file.py

## References

- [ruff @ GitHub](https://github.com/astral-sh/ruff)

- [ruff config - pylint](https://github.com/pylint-dev/pylint/blob/47cb11f4cb01a61f83d915d88e828f103a479980/pyproject.toml)
