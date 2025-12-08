Status: published
Date: 2020-09-02 09:22:34
Modified: 2021-09-17 11:35:17
Author: Benjamin Du
Slug: shell-equivalent-in-different-operating-systems
Title: Shell Equivalent in Different Operating Systems
Category: Computer Science
Tags: Computer Science, OS, Linux, macOS, Windows, Shell, PowerShell

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

[Fish Shell]( https://www.legendu.net/misc/blog/tips-on-the-fish-shell ) 
is preferred to Bash/Zsh.
The following content is for Bash/Zsh only.

It suggested that you use IPython shell instead of Bash/Zsh shells.
Please refer to 
[IPython Is the Best Shell](http://www.legendu.net/en/blog/ipython-is-the-best-shell/)
for detailed discussions.
If you have to use shell commands,
it is suggested that you use Linux commands when possible 
as Linux command are more universal and useful.
You can achieve this by using WSL 2 on Windows 
and by using Docker or virtual machine on macOS.

<div style="overflow-x:auto;">
<style>
    tr:nth-child(even) {background-color: #A3E4D7}
</style>
<table style="width:100%">
  <tr>
    <th> </th>
    <th> OS </th>
    <th> Command </th>
  </tr>

  <tr>
    <td rowspan="2"> Set PATH </td>
    <td> Linux/Unix </td>
    <td> <code> 
    export PATH=/new/path:$PATH
    </code> </td>
  </tr>
  <tr>
    <td> Windows PowerShell </td>
    <td> <code> 
    $env:Path += ";.\swigwin-4.0.1";
    </code> </td>
  </tr>

  <tr>
    <td rowspan="3"> Get location <br> of a command </td>
    <td> Linux/Unix </td>
    <td> <code> 
    which command_name
    </code> </td>
  </tr>
  <tr>
    <td> Windows PowerShell </td>
    <td> <code> 
    Get-command command_name
    </code> </td>
  </tr>
  <tr>
    <td> Windows CMD[1] </td>
    <td> <code> 
    where command_name
    </code> </td>
  </tr>

  <tr>
    <td rowspan="3"> Add user <br> to a group </td>
    <td> Linux </td>
    <td> <code> 
    sudo gpasswd -a user_name group_name
    </code> </td>
  </tr>
  <tr>
    <td> macOS </td>
    <td> <code> 
    sudo dseditgroup -o edit -a $username_to_add -t user admin
    </code> </td>
  </tr>
  <tr>
    <td> Windows </td>
    <td> <code> 
    NA
    </code> </td>
  </tr>

  <tr>
    <td rowspan="2"> Compress/Decompress Archives </td>
    <td> Linux/Unix </td>
    <td> <code> 
    <a href="http://www.legendu.net/en/blog/compress-and-decompress-in-linux/">
    Compress and Decompressing Archives in Linux
    </a>
    </code> </td>
  </tr>
  <tr>
    <td> Windows PowerShell </td>
    <td> <code> 
    Expand-Archive .\swigwin-4.0.1.zip .;
    </code> </td>
  </tr>

  <tr>
    <td rowspan="3"> Download a file </td>
    <td rowspan="2"> Linux/Unix </td>
    <td> <code> 
    curl -sSL http://file.example.com -o output
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
    wget http://file.example.com -O output
    </code> </td>
  </tr>
  <tr>
    <td> Windows PowerShell </td>
    <td> <code> 
    (New-Object System.Net.WebClient).DownloadFile("http://prdownloads.sourceforge.net/swig/swigwin-4.0.1.zip","swigwin-4.0.1.zip");
    </code> </td>
  </tr>

  <tr>
    <td rowspan="2"> Watch a command </td>
    <td rowspan="1"> Linux/Unix </td>
    <td> <code> 
    watch command_to_watch
    </code> </td>
  </tr>
  <tr>
    <td> Windows </td>
    <td> 
    <a href="http://wragg.io/watch-for-changes-with-powershell/"> 
    Watch for changes with PowerShell
    </a>
    </td>
  </tr>

  <tr>
    <td rowspan="3"> Manage partitions of a disk </td>
    <td rowspan="1"> Linux </td>
    <td> <code> 
    fdisk
    </code> </td>
  </tr>
  <tr>
    <td> macOS </td>
    <td> 
    fdisk 
    <a href="#footnote1">[2]</a>
    </a>
    </td>
  </tr>
  <tr>
    <td> Windows </td>
    <td> 
    fdisk (via WSL 2 or virtual machine)
    </a>
    </td>
  </tr>

</table>
</div>

[1] Windows CMD command might not work well in Windows PowerShell. 
    For example,
    the `where` command sometimes works but sometimes doesn't work in a PowerShell.
    Since PowerShell becomes more popular than Windows CMD,
    `Get-command` is recommended over `where`.

[2] The macOS version of fdisk does not function similar to the Linux version of fdisk. 
It is not as intuitive and easy to use as the Linux version.
It is suggested that you use the Linux version of fdisk instead.
