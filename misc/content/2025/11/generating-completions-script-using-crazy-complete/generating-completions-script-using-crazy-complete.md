Status: published
Date: 2025-11-16 16:02:18
Modified: 2025-11-16 23:44:57
Author: Benjamin Du
Slug: generating-completions-script-using-crazy-complete
Title: Generating Completions Script Using crazy-complete
Category: Computer Science
Tags: Computer Science, programming, shell, bash, zsh, fish, completion, generator, generating

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

There are many tools for generating completion scripts for shell languages (bash, zsh, fish, etc),
[crazy-complete](https://github.com/crazy-complete/crazy-complete)
is one of the best among such tools.

```
ldc -h | crazy-complete --input-type=help yaml /dev/stdin > ldc.yaml
crazy-complete --input-type=yaml fish ldc.yaml > ldc.fish
```

## References

- [crazy-complete @ GitHub](https://github.com/crazy-complete/crazy-complete)

