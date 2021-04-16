Status: published
Date: 2021-04-16 11:33:39
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


## Syntax

!, ?, 

do not use `..=` which has performance issues. 
use `..` instead.

## Result
`Result.unwrap()` unwrap a result object. 
You can also unwrap it using pattern matching.

Ok, 
Result, 


## Pattern Matching
Pattern matching 

https://doc.rust-lang.org/book/ch18-03-pattern-syntax.html#matching-named-variables

## Functionall Programming 

Rust operations are generic 
so that a `map` can only be done on iterators 
instead of the raw collection type. 

use collect to convert a map to a collection

https://doc.rust-lang.org/stable/std/iter/struct.Map.html

## Deducted Types 

It doesn't seem to be as powerful/smart as Scala. 
It is suggested that you write types as much as possible at this time.

## Types

Rust is very picky about data types.
For example, 
the modulus operation `%` is only defined for integers with the same type.
For more discussion,
please refer to
[RFC: implement Rem for all equally signed integers where RHS < LHS](https://github.com/rust-lang/rfcs/pull/2643)
.

## Misc

[Programming in Rust: the good, the bad, the ugly.](https://hackernoon.com/programming-in-rust-the-good-the-bad-the-ugly-d06f8d8b7738)
summarizes good/bad/ugly things about Rust.

- [cargo](http://www.legendu.net/misc/blog/tips-on-cargo): package manager for Rust

- rustup: version manager for Rust

- [rustc](http://www.legendu.net/misc/blog/tips-on-rustc): compiler for Rust

1. Rust uses the underscore name convention.

2. A variable is immutable by default.
    You can make it mutable using the keyword `mut`.

    let mut x = 1;

    There is also a keyword `cconst` in rust. 
    The difference between `const` and `let` is that 
    you must explicitly specify the type of the variable when defining it using `const`.
    `const` is seldom used in Rust.

3. Use `::` to access members in a module and enum object.

4. Use the keyword `use` to import a library.
    use the keyword `mod` to import local modules.

5. '&' vs `&mut`

6. `assert_eq!`

## Rust IDE

VSCode with the [Rust extenstion (rust-lang.rust)](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust) seems to be a good option.

IntelliJ based IDE is another good option.

https://medium.com/cloud-native-the-gathering/whats-the-best-ide-for-developing-in-rust-5087d46006f5

[Are We IDE Yet](https://areweideyet.com/)

## Popular Rust Libraries

[12 Killer Rust Libraries You Should Know](https://jondot.medium.com/12-killer-rust-libraries-you-should-know-c60bab07624f)

[Awesome Rust](https://github.com/rust-unofficial/awesome-rust)

## Machine Learning

[Are We Learning Yes](http://www.arewelearningyet.com/)

## Parallel, Multithreading and Concurrency in Rust

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

[Rust on YouTube](https://www.youtube.com/channel/UCaYhcUwRBNscFNUKTjgPFiA)

[The Rust Programming Language](https://doc.rust-lang.org/book/title-page.html)

[Rust Crash Course | Rustlang](https://www.youtube.com/watch?v=zF34dRivLOw)

https://github.com/rust-unofficial/awesome-rust

## References

- [Rust Compiler Explorer](https://rust.godbolt.org/)

- https://users.rust-lang.org/

- https://internals.rust-lang.org/

- https://play.rust-lang.org/

- https://docs.rs/

- [The Rust Standard Library](https://doc.rust-lang.org/stable/std/)

- [Are We Web Yet](http://www.arewewebyet.org/)

- [Are we game yet?](https://arewegameyet.rss)

- [The Best Rust Frameworks to Check out in 2019](https://blog.logrocket.com/the-best-rust-frameworks-to-check-out-in-2019/)