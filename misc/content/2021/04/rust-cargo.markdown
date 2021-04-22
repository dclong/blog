Status: published
Date: 2021-04-17 10:39:55
Author: Benjamin Du
Slug: tips-on-cargo
Title: Tips on Cargo
Category: Computer Science
Tags: Computer Science, programming, rust, cargo

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Create a Project

    cargo init
    cargo new project_name

Install a package from GitHub (the default branch).

    cargo install --git https://github com/RustPython/RustPython
    
Use the option `--version` to install a specific version of a package.

    cargo install --version 0.8.1 evcxr_jupyter

## Build 

cargo build --release


either src/lib.rs, src/main.rs, a [lib] section, or [[bin]] section must be present


## Run 
    cargo run