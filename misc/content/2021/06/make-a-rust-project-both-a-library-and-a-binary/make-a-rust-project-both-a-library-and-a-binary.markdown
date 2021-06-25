Status: published
Date: 2021-06-16 22:50:37
Modified: 2021-06-24 12:54:44
Author: Benjamin Du
Slug: make-a-rust-project-both-a-library-and-a-binary
Title: Make a Rust Project Both a Library and a Binary
Category: Computer Science
Tags: Computer Science, programming, Rust, library, binary, crate, file system, structure
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


.
├── Cargo.toml
└── src
    ├── main.rs
    │   
    └── lib.rs

```
[package]
name = "package_name"
version = "0.0.1"
authors = ["me <me@gmail.com>"]

[lib]
name = "lib_name"
path = "src/lib.rs"

[[bin]]
name = "binary_name"
path = "src/bin.rs"
```

1. It seems that you have to use relative import when using the above structure ...

2. `lib.rs` is the entrance place of the library 
    (similar to that `main.rs` is the entrance place of the binary).
    It is not a module!

## References

[Rust package with both a library and a binary?](https://stackoverflow.com/questions/26946646/rust-package-with-both-a-library-and-a-binary)

[Cargo, Crates and Basic Project Structure](https://learning-rust.github.io/docs/a4.cargo,crates_and_basic_project_structure.html)
