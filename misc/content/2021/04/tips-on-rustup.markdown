Status: published
Date: 2021-04-24 08:36:28
Author: Benjamin Du
Slug: tips-on-rustup
Title: Tips on rustup
Category: Computer Science
Tags: Computer Science, programming, Rust, rustup, rustfmt, toochain, stable, beta, nightly

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Install rustup
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | bash -s -- -y

The `cargo`, `rustc`, `rustup` and other commands 
will be added to Cargo's bin directory, located at `$HOME/.cargo/bin`.

## Install stable/nightly Versions of Rust

rustup toolchain install stable
rustup toolchain install beta
rustup toolchain install nightly
rustup default stable



## Install rust-src

rustup component add rust-src

## Install rustfmt

rustup component add rustfmt


## References 

https://rust-lang.github.io/rustup/index.html

https://github.com/rust-lang/rustup