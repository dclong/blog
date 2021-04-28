Status: published
Date: 2021-04-28 16:21:14
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

## Build 

cargo build --release


either src/lib.rs, src/main.rs, a [lib] section, or [[bin]] section must be present


## Run 
    cargo run

## Extensions to Cargo

### Format Code

If `rustfmt` has been installed (using `rustup component add rustfmt`),
you can run the following command to format code in a Rust project.

    cargo fmt 

### [cargo-edit](https://github.com/killercup/cargo-edit)

[cargo-edit](https://github.com/killercup/cargo-edit)
is a utility for managing cargo dependencies from the command line.
It is a temporary solution before the issue
[Add cargo-add (from cargo-edit) to cargo proper](https://github.com/rust-lang/cargo/issues/5586)
is resolved.

    :::bash
    cargo install cargo-edit

### [cargo-crev](https://github.com/crev-dev/cargo-crev)
[cargo-crev](https://github.com/crev-dev/cargo-crev)
is a cryptographically verifiable code review system for the cargo (Rust) package manager.
It is an implementation of Crev as a command line tool integrated with cargo,
which helps Rust users evaluate the quality and trustworthiness of their package dependencies.

### [cargo-audit](https://github.com/RustSec/cargo-audit)
[cargo-audit](https://github.com/RustSec/cargo-audit)
is a Cargo subcommand
which audits Cargo.lock files for crates with security vulnerabilities.
It also supports CICD tools such as GitHub Actions 
(via [audit-check](https://github.com/actions-rs/audit-check))
and Travis CI.


