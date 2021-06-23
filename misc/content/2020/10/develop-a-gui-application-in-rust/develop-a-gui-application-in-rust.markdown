Status: published
Date: 2020-10-03 21:36:53
Author: Benjamin Du
Slug: develop-a-gui-application-in-rust
Title: Develop a GUI Application in Rust
Category: Computer Science
Tags: Computer Science, Rust, GUI
Modified: 2021-06-23 08:50:23

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

The article
[Rust GUI: Introduction, a.k.a. the state of Rust GUI libraries (As of January 2021)](https://dev.to/davidedelpapa/rust-gui-introduction-a-k-a-the-state-of-rust-gui-libraries-as-of-january-2021-40gl)
has a good review of different GUI libraries in Rust.
According to the article and based on star and activities of the corresponding GitHub repos of the libraries,
iced, druid and azul are the 3 good ones.

## [tauri](http://www.legendu.net/misc/blog/use-tauri-to-build-a-desktop-application)
Please refer to 
[tauri](http://www.legendu.net/misc/blog/use-tauri-to-build-a-desktop-application)
for more discussions.

## [fltk-rs](https://github.com/fltk-rs/fltk-rs)
[fltk-rs](https://github.com/fltk-rs/fltk-rs)
is a rust binding for the FLTK Graphical User Interface library.
The 
[fltk-rs](https://github.com/fltk-rs/fltk-rs)
crate is a crossplatform lightweight gui library 
which can be statically linked to produce small, 
self-contained and fast gui applications.

## [iced](https://github.com/hecrj/iced)
A cross-platform GUI library for Rust focused on simplicity and type-safety. Inspired by Elm.

## [gtk-rs](https://github.com/gtk-rs/gtk-rs)
Works well on Linux but not as well on macOS and Windows.

## [druid](https://github.com/linebender/druid)
Druid is an experimental Rust-native UI toolkit. 
Its main goal is to offer a polished user experience. 
There are many factors to this goal, including performance, 
a rich palette of interactions (hence a widget library to support them), and playing well with the native platform. 
See the goals section for more details.

## [azul](https://github.com/fschutt/azul)

Azul is a free, functional, reactive GUI framework for Rust and C++, 
built using the WebRender rendering engine and a CSS / HTML-like document object model for rapid development of beautiful, native desktop applications


## [orbtk](https://github.com/redox-os/orbtk)
[orbtk](https://github.com/redox-os/orbtk)
is a cross-platform (G)UI toolkit for building scalable user interfaces 
with the programming language Rust. 
It's based on the Entity Component System Pattern and provides a functional Reactive-like API.

https://crates.io/crates/OrbTk

## [conrod](https://github.com/PistonDevelopers/conrod)
[conrod](https://github.com/PistonDevelopers/conrod)
is an easy-to-use, 2D GUI library written entirely in Rust.

## [imgui-rs](https://github.com/Gekkio/imgui-rs)
[imgui-rs](https://github.com/Gekkio/imgui-rs)
is a Rust bindings for Dear ImGui. 

## References

- [Rust GUI: Introduction, a.k.a. the state of Rust GUI libraries (As of January 2021)](https://dev.to/davidedelpapa/rust-gui-introduction-a-k-a-the-state-of-rust-gui-libraries-as-of-january-2021-40gl)

- [Rust语言有那些好的GUI库?](https://www.zhihu.com/question/312815643/answer/1846050229)

- https://www.areweguiyet.com/

- https://github.com/webview/webview_rust

- https://github.com/webview/webview

- [Best way to create a front end (in any language) that calls a Rust library?](https://users.rust-lang.org/t/best-way-to-create-a-front-end-in-any-language-that-calls-a-rust-library/38008)

- [Tauri + Svelte = cross-platform native GUI apps compiled to WASM](https://forum.safedev.org/t/tauri-svelte-cross-platform-native-gui-apps-compiled-to-wasm/2870)

- [Is There a Demand for UI Framework?](https://users.rust-lang.org/t/is-there-a-demand-for-ui-framework/47689)