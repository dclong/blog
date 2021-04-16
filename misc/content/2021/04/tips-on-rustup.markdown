Status: published
Date: 2021-04-16 14:38:47
Author: Benjamin Du
Slug: tips-on-rustup
Title: Tips on rustup
Category: Computer Science
Tags: Computer Science, programming, rust, rustup

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | bash -s -- -y
rustup install stable
rustup default stable

The `cargo`, `rustc`, `rustup` and other commands 
will be added to Cargo's bin directory, located at `$HOME/.cargo/bin`.

## References 

https://rust-lang.github.io/rustup/index.html

https://github.com/rust-lang/rustup