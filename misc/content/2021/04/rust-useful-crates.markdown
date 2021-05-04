Status: published
Date: 2021-05-03 10:02:06
Author: Benjamin Du
Slug: useful-rust-crates
Title: Useful Rust Crates
Category: Computer Science
Tags: Computer Science, programming, Rust, crate, useful
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

https://crates.io/crates?sort=downloads

## Databases

### [serde](https://crates.io/crates/serde)
[serde](https://crates.io/crates/serde)
is a framework for serializing and deserializing Rust data structures efficiently and generically.

### [sled](https://github.com/spacejam/sled)
[sled](https://github.com/spacejam/sled)
is an embedded key-value pair databases written in Rust.

## Other
### [rayon](https://crates.io/crates/rayon)
[rayon](https://crates.io/crates/rayon)
is a data-parallelism library for Rust. 
It is extremely lightweight and makes it easy to convert a sequential computation into a parallel one. 
It also guarantees data-race freedom. 

### [num-derive](https://crates.io/crates/num-derive)
[num-derive](https://crates.io/crates/num-derive)
providess procedural macros to derive numeric traits in Rust.

### [num-traits](https://crates.io/crates/num-traits)
[num-traits](https://crates.io/crates/num-traits)
provides numeric traits for generic mathematics in Rust.

### [itertools](https://crates.io/crates/itertools)
[itertools](https://crates.io/crates/itertools)
provides extra iterator adaptors, iterator methods, free functions, and macros.

### [lazy_static](https://crates.io/crates/lazy_static)
[lazy_static](https://crates.io/crates/lazy_static)
is a macro for declaring lazily evaluated statics in Rust.
Using this macro, 
it is possible to have statics that require code to be executed at runtime in order to be initialized. 
This includes anything requiring heap allocations, 
like vectors or hash maps, 
as well as anything that requires non-const function calls to be computed.

### [bitflags](https://crates.io/crates/bitflags)
[bitflags](https://crates.io/crates/bitflags)
is a Rust macro to generate structures which behave like a set of bitflags.

### [futures](https://crates.io/crates/futures)
[futures](https://crates.io/crates/futures)
is an implementation of futures and streams featuring zero allocations, 
composability, and iterator-like interfaces.
It is a library providing the foundations for asynchronous programming in Rust. 
It includes key trait definitions like Stream, 
as well as utilities like `join!`, `select!`, 
and various futures combinator methods which enable expressive asynchronous control flow.

### [tokio](https://crates.io/crates/tokio)
[tokio](https://crates.io/crates/tokio)
is an event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications.

### [enum_primitive](https://crates.io/crates/enum_primitive)
[enum_primitive](https://crates.io/crates/enum_primitive)
is a macro to generate `num::FromPrimitive` instances for enum that works in Rust 1.0+.

## References

https://crates.io/


