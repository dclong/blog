Status: published
Date: 2022-12-21 10:14:53
Modified: 2025-05-27 23:47:28
Author: Benjamin Du
Slug: great-command-line-tools-developed-in-rust
Title: Great Command Line Tools Developed in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, alternative, command-line, rewrite

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


## [GQL](https://github.com/AmrDeveloper/GQL)
[GQL](https://github.com/AmrDeveloper/GQL)
is a query language with a syntax very similar to SQL with a tiny engine to perform queries on .git files instance of database files, 
the engine executes the query on the fly without the need to create database files or convert .git files into any other format, 
note that all Keywords in GQL are case-insensitive similar to SQL.

## [tealdeer](https://crates.io/crates/tealdeer)
[tealdeer](https://crates.io/crates/tealdeer)
is a very fast implementation of tldr in Rust: 
Simplified, example based and community-driven man pages.

## [halp](https://github.com/orhun/halp)
[halp](https://github.com/orhun/halp)
aims to help find the correct arguments for command-line tools 
by checking the predefined list of commonly used options/flags. 
Additionally, 
it provides a prompt for quick access to the manual page or cheat sheet of the given command.

## [Atuin](https://github.com/ellie/atuin)
[Atuin](https://github.com/ellie/atuin)
replaces your existing shell history with a SQLite database, 
and records additional context for your commands. 
Additionally, 
it provides optional and fully encrypted synchronisation of your history between machines, via an Atuin server.

## [see](https://github.com/guilhermeprokisch/see)

[see](https://github.com/guilhermeprokisch/see)
is a powerful file visualization tool for the terminal, 
offering advanced code viewing capabilities, Markdown rendering, and more. 
It provides syntax highlighting, emoji support, and image rendering capabilities, 
offering a visually appealing way to view various file types directly in your console.

## [bat]( https://www.legendu.net/misc/blog/bat-is-a-better-alternative-to-cat )
[bat]( https://www.legendu.net/misc/blog/bat-is-a-better-alternative-to-cat )
is a cat clone with syntax highlighting and Git integration.

## [exa](https://github.com/ogham/exa)
[exa](https://github.com/ogham/exa)
is a modern replacement for ls.

## [procs](https://github.com/dalance/procs)
[procs](https://github.com/dalance/procs)
is a modern replacement for ps written in Rust.

## [sd](https://github.com/chmln/sd)
[sd](https://github.com/chmln/sd)
is an intuitive find & replace CLI (sed alternative).

## [skim](https://github.com/skim-rs/skim)
[skim](https://github.com/skim-rs/skim)
is a fuzzy finder implemented in rust!

## Summarize a Project

### [git-cliff](https://github.com/orhun/git-cliff)
[git-cliff](https://github.com/orhun/git-cliff)
can generate changelog files from the Git history 
by utilizing conventional commits as well as regex-powered custom parsers. 
The changelog template can be customized with a configuration file to match the desired format.

### [tokei](https://github.com/XAMPPRocky/tokei)
[Tokei](https://github.com/XAMPPRocky/tokei)
is a program that displays statistics about your code. 
Tokei will show the number of files, 
total lines within those files and code, comments, and blanks grouped by language.

### [onefetch](https://github.com/o2sh/onefetch)
[OneFetch](https://github.com/o2sh/onefetch)
is a command-line Git information tool written in Rust 
that displays project information and code statistics 
for a local Git repository directly to your terminal. 
The tool is completely offline - no network access is required.

## System Monitoring

### [bottom](https://crates.io/crates/bottom)
[bottom](https://crates.io/crates/bottom)
is a customizable cross-platform graphical process/system monitor 
for the terminal. 
It supports Linux, macOS, and Windows.

### [sniffnet](https://crates.io/crates/sniffnet)
[sniffnet](https://crates.io/crates/sniffnet)
is an application to comfortably monitor your network traffic.

### [trippy](https://github.com/fujiapple852/trippy)
[Trippy](https://github.com/fujiapple852/trippy)
combines the functionality of traceroute and ping 
and is designed to assist with the analysis of networking issues.

### [gping](https://github.com/orf/gping)
[gping](https://github.com/orf/gping)
is ping with a graph.

### [bandwhich](https://crates.io/crates/bandwhich)
[bandwhich](https://crates.io/crates/bandwhich)
is a CLI utility for displaying current network utilization by process, 
connection and remote IP/hostname.

### [below](https://github.com/facebookincubator/below)
[below](https://github.com/facebookincubator/below)
is an interactive tool to view and record historical system data.

## Disk Usage
### [dust](https://github.com/bootandy/dust)
[Dust](https://github.com/bootandy/dust)
is a more intuitive version of du in rust.

### [dua-cli](https://crates.io/crates/dua-cli)
[dua-cli](https://crates.io/crates/dua-cli)

## Navigation and Searching
### [ripgrep](https://www.legendu.net/misc/blog/ripgrep-is-a-better-alternative-to-find)
[ripgrep](https://www.legendu.net/misc/blog/ripgrep-is-a-better-alternative-to-find)
recursively searches directories for a regex pattern while respecting your gitignore.

### [igrep](https://github.com/konradsz/igrep)
[igrep](https://github.com/konradsz/igrep)
runs grep (ripgrep's library) in the background, 
allows interactively pick its results and open selected match in text editor of choice (vim by default).

### [broot](https://github.com/Canop/broot)
[broot](https://github.com/Canop/broot)
provides a new better way to see and navigate directory trees.

## Git Tools

### [gitui](https://github.com/extrawurst/gitui)
[GitUI](https://github.com/extrawurst/gitui)
provides you with the comfort of a git GUI but right in your terminal
.

### [gitoxide](https://github.com/Byron/gitoxide)
[gitoxide](https://github.com/Byron/gitoxide)
is an implementation of git written in Rust 
for developing future-proof applications which strive 
for correctness and performance 
while providing a pleasant and unsurprising developer experience.

### [git-leave](https://crates.io/crates/git-leave)
[git-leave](https://crates.io/crates/git-leave)
checks for unsaved or uncommitted changes on your machine.

### [Stacked Git](https://github.com/stacked-git/stgit)
[Stacked Git](https://github.com/stacked-git/stgit)
,
StGit for short, 
is an application for managing Git commits as a stack of patches.

## [grex](https://github.com/pemistahl/grex)
[grex](https://github.com/pemistahl/grex)
is a command-line tool and Rust library 
for generating regular expressions from user-provided test cases
.

## [delta](https://github.com/dandavison/delta)
[delta](https://github.com/dandavison/delta)
is a syntax-highlighting pager for git, diff, and grep output.

## [difftastic](https://github.com/Wilfred/difftastic)
[Difftastic](https://github.com/Wilfred/difftastic)
is a structural diff tool that compares files based on their syntax.

## [ruff](https://github.com/charliermarsh/ruff)
[ruff](https://github.com/charliermarsh/ruff)
is an extremely fast Python linter, written in Rust.

## [Rome](https://github.com/rome/tools)
[Rome](https://github.com/rome/tools)
provides unified developer tools for JavaScript, TypeScript, and the web.

## [carbonyl](https://github.com/fathyb/carbonyl)
[Carbonyl](https://github.com/fathyb/carbonyl)
is a Chromium based browser built to run in a terminal.

## [speedtest-rs](https://github.com/nelsonjchen/speedtest-rs)
[speedtest-rs](https://github.com/nelsonjchen/speedtest-rs)
a tool like speedtest-cli, but in Rust
.


## [mprocs](https://github.com/pvolok/mprocs)
[mprocs](https://github.com/pvolok/mprocs)
runs multiple commands in parallel and shows output of each command separately.

## Security

## [Nosey Parker](https://github.com/praetorian-inc/noseyparker)
[Nosey Parker](https://github.com/praetorian-inc/noseyparker)
is a command-line program that finds secrets and sensitive information in textual data and Git history.


## [rtx](https://github.com/jdxcode/rtx)
[rtx](https://github.com/jdxcode/rtx)
is a version manager for multiple programming languages.

## Good Ones but Which I Won't Use



nushell

## References

- [Rewritten in Rust: Modern Alternatives of Command-Line Tools](https://zaiste.net/posts/shell-commands-rust/)

- [Awesome Alternatives in Rust](https://github.com/TaKO8Ki/awesome-alternatives-in-rust)
