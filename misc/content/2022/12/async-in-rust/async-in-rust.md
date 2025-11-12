Status: published
Date: 2022-12-04 10:38:16
Modified: 2025-11-11 18:42:02
Author: Benjamin Du
Slug: async-in-rust
Title: Async in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, async

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Combining asynchronous code with synchronous code that can cause blocking is never a wise choice.
    When calling asynchronous code from a synchronous context, 
    use `futures::executor::block_on` and spawn the async code to a dedicated runtime, 
    because the former will block the current thread.
    On the other hand, 
    if you have to call blocking synchronous code from an asynchronous context, 
    it is recommended to use `tokio::task::spawn_blocking` 
    to execute the code on a dedicated executor that handles blocking operations.


## Issues in Async Rust

- [Rain: "Cancelling Async Rust" | RustConf 2025](https://www.youtube.com/watch?v=zrv5Cy1R7r4&list=PL2b0df3jKKiRFEuVNk76ufXagOgEJ9sBZ&index=32)

## Tutorials

[Basics of Rust Concurrency (Atomics and Locks Chapter 1)](https://www.youtube.com/watch?v=99Qzpv325yI)

## References

- [Improving async Rust codegen](https://swatinem.de/blog/improving-async-codegen/)

- [Implementation Details of async Rust](https://swatinem.de/blog/async-codegen/)

- [how I finally understood async/await in Rust (part 1)](https://hegdenu.net/posts/understanding-async-await-1/)

- [How Much Memory Do You Need to Run 1 Million Concurrent Tasks?](https://pkolaczk.github.io/memory-consumption-of-async/)

- [Bridging Async and Sync Rust Code - A lesson learned while working with Tokio](https://rustmagazine.org/issue-3/bridging-async-and-sync-in-rust/)
