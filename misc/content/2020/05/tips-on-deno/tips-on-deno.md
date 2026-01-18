Status: published
Date: 2020-05-09 17:27:49
Author: Benjamin Du
Slug: tips-on-deno
Title: Tips on Deno
Category: Computer Science
Tags: Computer Science, JavaScript, JS, TypeScript, TS, deno, jupyter, notebook
Modified: 2026-01-17 18:41:35

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


[VS Code Plugin for Deno](https://marketplace.visualstudio.com/items?itemName=axetroy.vscode-deno)

Add the following into the file `.vscode/settings.json` under the root directory of your project.

    :::json
    {
    "deno.enable": true,
    }

## Jupyter Kernel

Deno ships with a built-in Jupyter kernel that allows you to write JavaScript and TypeScript.
For more details,
please refer to
[Jupyter Kernel for Deno](https://docs.deno.com/runtime/reference/cli/jupyter/)
and
[Bringing Modern JavaScript to the Jupyter Notebook](https://blog.jupyter.org/bringing-modern-javascript-to-the-jupyter-notebook-fc998095081e)
.

