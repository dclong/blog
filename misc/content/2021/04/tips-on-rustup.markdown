Status: published
Date: 2021-04-19 16:34:59
Author: Benjamin Du
Slug: tips-on-rustup
Title: Tips on rustup
Category: Computer Science
Tags: Computer Science, programming, rust, rustup

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



## Installing rust-src Using rustup

rustup component add rust-src

## References 

https://rust-lang.github.io/rustup/index.html

https://github.com/rust-lang/rustup