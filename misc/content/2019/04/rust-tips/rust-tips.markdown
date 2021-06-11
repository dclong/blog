Status: published
Date: 2021-06-10 12:17:46
Modified: 2021-06-11 00:00:44
Author: Benjamin Du
Slug: rust-tips
Title: Tips on Rust
Category: Computer Science
Tags: programming, Rust, tips, Cargo, rustup

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Installation 

### Using rustup

Please refer to
[Tips on rustup](http://www.legendu.net/misc/blog/tips-on-rustup)
for instructions.

### Using xinstall

xinstall rustup -ic

### Install a Newer Version of Rust via PPA on Ubuntu

    :::bash
    sudo apt-add-repository ppa:ubuntu-mozilla-security/rust-updates
    sudo apt-get update
    sudo apt-get install rustc

For details of the PPA ubuntu-mozilla-security/rust-updates,
please refer to
[PPA for preparing rust toolchain updates for Firefox](https://launchpad.net/~ubuntu-mozilla-security/+archive/ubuntu/rust-updates)
.

### Install Rust for Multiple Users

[Installing rustup for all linux users](https://github.com/rust-lang/rustup/issues/1085)

[Does rustup.rs support shared .multirust (or whatever) directory?](https://github.com/rust-lang/rustup/issues/313)

[Add Document of "How to Install Rust Environment for Multiple Users on Linux?"](https://github.com/rust-lang/rustup/issues/2383)

## Rust Toolchains

- [cargo](http://www.legendu.net/misc/blog/tips-on-cargo): package manager for Rust

- rustup: version manager for Rust

- [rustc](http://www.legendu.net/misc/blog/tips-on-rustc): compiler for Rust

## IDE for Rust

Please refer to 
[IDE for Rust](http://www.legendu.net/misc/blog/IDE-for-Rust)
for more details.

## General Tips and Traps

1. do not use `..=` which has performance issues. 
    use `..` instead.


## Pattern Matching
Pattern matching 

https://doc.rust-lang.org/book/ch18-03-pattern-syntax.html#matching-named-variables

## Popular Rust Libraries

Please refer to 
[Useful Rust Crates](http://www.legendu.net/misc/blog/useful-rust-crates)
for detailed discussions.

## Machine Learning

Please refer to
[Rust for Machine Learning](http://www.legendu.net/misc/blog/rust-for-machine-learning)
for detailed discussions.

## Parallel, Multithreading and Concurrency in Rust

### [loom](https://github.com/tokio-rs/loom)
is a concurrency permutation testing tool for Rust.

### [sanitizers](https://github.com/google/sanitizers)
This project is the home for Sanitizers: AddressSanitizer, MemorySanitizer, ThreadSanitizer, LeakSanitizer, 
and more The actual code resides in the LLVM repository. Here we keep extended documentation, bugfixes and some helper code.



[rayon](https://github.com/rayon-rs/rayon)
A data parallelism library for Rust.

http://worthe-it.co.za/programming/2018/10/03/going-four-times-faster-with-multithreading.html

https://skipworth.io/posts/rust-wc-threads/

https://crates.io/crates/scoped-threadpool

## [Rust GUI](http://www.legendu.net/misc/blog/develop-a-gui-application-in-rust)

## Cool Rust Projects

https://github.com/rajasekarv/native_spark

https://github.com/andygrove/ballista

https://github.com/weld-project/weld

https://github.com/rbatis/rbatis

https://github.com/dclong?language=rust&tab=stars

https://github.com/rust-unofficial/awesome-rust

https://github.com/yewstack/yew

https://github.com/valeriansaliou/sonic

## Tutorials

[Jon Gjengset's Video Tutorials (Medium to Advanced)](https://www.youtube.com/channel/UC_iD0xppBwwsrM9DegC5cQQ)

[Rust on YouTube](https://www.youtube.com/channel/UCaYhcUwRBNscFNUKTjgPFiA)

[The Rust Programming Language](https://doc.rust-lang.org/book/title-page.html)

[Rust Crash Course | Rustlang](https://www.youtube.com/watch?v=zF34dRivLOw)

https://github.com/rust-unofficial/awesome-rust

## References

- [Rust Blog](https://blog.rust-lang.org/)

- [Rust Compiler Explorer](https://rust.godbolt.org/)

- https://users.rust-lang.org/

- https://internals.rust-lang.org/

- https://play.rust-lang.org/

- https://docs.rs/

- [The Rust Standard Library](https://doc.rust-lang.org/stable/std/)

- [Are We Web Yet](http://www.arewewebyet.org/)

- [Are we game yet?](https://arewegameyet.rss)

- [The Best Rust Frameworks to Check out in 2019](https://blog.logrocket.com/the-best-rust-frameworks-to-check-out-in-2019/)
