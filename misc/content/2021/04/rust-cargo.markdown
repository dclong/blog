Status: published
Date: 2021-04-24 08:50:49
Author: Benjamin Du
Slug: tips-on-cargo
Title: Tips on Cargo
Category: Computer Science
Tags: Computer Science, programming, Rust, cargo, format, fmt, rustfmt

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

## Format Code

If `rustfmt` has been installed (using `rustup component add rustfmt`),
you can run the following command to format code in a Rust project.

    cargo fmt 

## Build 

cargo build --release


either src/lib.rs, src/main.rs, a [lib] section, or [[bin]] section must be present


## Run 
    cargo run