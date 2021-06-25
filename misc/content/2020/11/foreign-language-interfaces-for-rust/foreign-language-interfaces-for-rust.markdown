Status: published
Date: 2020-11-28 11:37:35
Author: Benjamin Du
Slug: foreign-language-interfaces-for-rust
Title: Foreign Language Interfaces for Rust
Category: Computer Science
Tags: Computer Science, inline-python, interface, foreign, language, interface, Rust, bindgen, ffi
Modified: 2021-06-25 15:55:19

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**
## [libc](https://crates.io/crates/libc)
[libc](https://crates.io/crates/libc)
Raw FFI bindings to platform libraries like libc.
[libc](https://crates.io/crates/libc)
provides all of the definitions necessary 
to easily interoperate with C code (or "C-like" code) 
on each of the platforms that Rust supports. 
This includes type definitions (e.g. c_int), constants (e.g. EINVAL) as well as function headers (e.g. malloc).

## [rust-bindgen](https://github.com/rust-lang/rust-bindgen)
[rust-bindgen](https://github.com/rust-lang/rust-bindgen)
automatically generates Rust FFI bindings to C (and some C++) libraries.

## [ritual](https://github.com/rust-qt/ritual)
[Ritual](https://github.com/rust-qt/ritual)
allows to use C++ libraries from Rust. 
It analyzes the C++ API of a library and generates a fully-featured crate 
that provides convenient (but still unsafe) access to this API.

## [rust-cpp](https://github.com/mystor/rust-cpp)
[rust-cpp](https://github.com/mystor/rust-cpp)
is a build tool & macro which enables you to write C++ code inline in your rust code.

## [inline-python](https://github.com/fusion-engineering/inline-python)
[inline-python](https://github.com/fusion-engineering/inline-python)
inlines Python code directly in your Rust code.

## [rust-cpython](https://github.com/dgrunwald/rust-cpython)

## References 

- [Foreign Function Interface](https://doc.rust-lang.org/nomicon/ffi.html)
- [How to call a C++ dynamic library from Rust?](https://stackoverflow.com/questions/52923460/how-to-call-a-c-dynamic-library-from-rust)
