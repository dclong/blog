Status: published
Date: 2023-01-13 16:44:56
Modified: 2023-08-03 15:43:30
Author: Benjamin Du
Slug: serialization-and-deserialization-in-rust
Title: Serialization and Deserialization in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, serialization, deserialization, binary, encoding

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


[msgpacker](https://crates.io/crates/msgpacker)

[msgpack-rust](https://github.com/3Hren/msgpack-rust)

## Protobuf

https://crates.io/crates/protobuf

https://crates.io/crates/prost

## [serde Based Serialization and Deserialization](https://www.legendu.net/en/blog/hands-on-the-Rust-library-serde/)

### [serde](https://www.legendu.net/en/blog/hands-on-the-Rust-library-serde/)
[serde](https://www.legendu.net/en/blog/hands-on-the-Rust-library-serde/)
is a generic serialization/deserialization framework
.

### [serde_with](https://crates.io/crates/serde_with)
[serde_with](https://crates.io/crates/serde_with)
provides custom de/serialization helpers 
to use in combination with serde's with-annotation and with the improved serde_as-annotation.

### [serde_yaml](https://www.legendu.net/misc/blog/handle-duplicated-keys-in-serde-yaml/)
[serde_yaml](https://www.legendu.net/misc/blog/handle-duplicated-keys-in-serde-yaml/)
is a YAML data format for Serde
.

### [serde-big-array](https://crates.io/crates/serde-big-array)
[serde-big-array](https://crates.io/crates/serde-big-array)
Big array helper for serde. The purpose of this crate is to make (de-)serializing arrays of sizes > 32 easy. This solution is needed until serde adopts const generics support.

### [serde_stacker](https://crates.io/crates/serde_stacker)
[serde_stacker](https://crates.io/crates/serde_stacker)
is a serde adapter that avoids stack overflow by dynamically growing the stack
.

## [basic-toml](https://github.com/dtolnay/basic-toml)
[basic-toml](https://github.com/dtolnay/basic-toml)
is a library for parsing and producing data in TOML format using Serde.

## [ciborium](https://crates.io/crates/ciborium)
[Ciborium](https://crates.io/crates/ciborium)
contains CBOR serialization and deserialization implementations for serde.


## [minicbor](https://crates.io/crates/minicbor)
[minicbor](https://crates.io/crates/minicbor)
is a small CBOR codec suitable for no_std environments.

## [bincode](https://github.com/bincode-org/bincode)
[bincode](https://github.com/bincode-org/bincode)
is a compact encoder / decoder pair that uses a binary zero-fluff encoding scheme. 
The size of the encoded object will be the same or smaller 
than the size that the object takes up in memory in a running Rust program.

## [serde-repr](https://github.com/dtolnay/serde-repr)

## [nanoserde](https://github.com/not-fl3/nanoserde)

## [goblin](https://github.com/m4b/goblin)

## [speedy](https://github.com/koute/speedy)

## [borsh-rs](https://github.com/near/borsh-rs)

## [rust-ini](https://github.com/zonyitoo/rust-ini)

## [xml-rs](https://github.com/netvl/xml-rs)

## Other Crates
Strictly speaking,
the following crates are not serialization/deserialization crates.
There are more like binary encoding/decoding crates. 
However,
they can be very useful when you work with primitive types in Rust.

## [parquet](https://crates.io/crates/parquet)
[parquet](https://crates.io/crates/parquet)
is an Apache Parquet implementation in Rust.

## [atoi-rs](https://github.com/pacman82/atoi-rs)
[atoi-rs](https://github.com/pacman82/atoi-rs)
parses integers directly from [u8] slices in safe code
.

## References

- [Hands on the Rust Library Serde](https://www.legendu.net/en/blog/hands-on-the-Rust-library-serde)

- [Parse TOML Files in Rust](https://www.legendu.net/misc/blog/parse-toml-files-in-rust)

- [Data Frame Implementations in Rust](https://www.legendu.net/misc/blog/data-frame-implementations-in-rust)
