Status: published
Date: 2025-11-11 18:13:06
Modified: 2025-11-16 14:45:10
Author: Benjamin Du
Slug: tips-on-the-fish-shell
Title: Tips on the Fish Shell
Category: Computer Science
Tags: Computer Science, programming, shell, fish

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Configuration

~/.config/fish

## Key Bindings

<table class="tg"><thead>
  <tr>
    <th class="tg-0pky">Shortcuts</th>
    <th class="tg-0pky">Description</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0pky">Alt-.</td>
    <td class="tg-0pky">Get parameter of previous commands.</td>
  </tr>
  <tr>
    <td class="tg-0pky">Alt-e</td>
    <td class="tg-0pky">Edit the current command line in an external editor.</td>
  </tr>
</tbody>
</table>

Please refer to 
[Interactive use](https://fishshell.com/docs/current/interactive.html)
for a more comprehensive list of key bindings.

## Completions

1. The built-in fish function
    [fish_update_completions](https://fishshell.com/docs/current/cmds/fish_update_completions.html)
    updates completions using manual pages.

2. Instead of writing completion scripts manually,
    lots of tools support exporting completion scripts for bash, zsh, fish, etc.

3. [crazy-complete](https://github.com/crazy-complete/crazy-complete)
    helps generate completion scripts based on YAML defined completion rules.

