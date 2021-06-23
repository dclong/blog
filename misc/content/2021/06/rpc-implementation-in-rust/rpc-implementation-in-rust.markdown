Status: published
Date: 2021-06-20 12:01:24
Modified: 2021-06-23 11:14:17
Author: Benjamin Du
Slug: rpc-implementation-in-rust
Title: RPC Implementation in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, RPC, gRPC, tonic
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [tonic](https://github.com/hyperium/tonic)
[tonic](https://github.com/hyperium/tonic)
is a gRPC over HTTP/2 implementation focused on high performance, interoperability, and flexibility. 
This library was created to have first class support of async/await 
and to act as a core building block for production systems written in Rust.

## [grpc-rust](https://github.com/stepancheg/grpc-rust)
[grpc-rust](https://github.com/stepancheg/grpc-rust)
is a Rust implementation of gRPC protocol, under development.

[tarpc](https://github.com/google/tarpc)
[tarpc](https://github.com/google/tarpc)
is an RPC framework for rust with a focus on ease of use. 
Defining a service can be done in just a few lines of code, 
and most of the boilerplate of writing a server is taken care of for you.



