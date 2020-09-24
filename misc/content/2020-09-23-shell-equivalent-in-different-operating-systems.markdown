Status: published
Date: 2020-09-23 23:27:31
Author: Benjamin Du
Slug: shell-equivalent-in-different-operating-systems
Title: Shell Equivalent in Different Operating Systems
Category: Computer Science
Tags: Computer Science, OS, Linux, macOS, Windows, Shell, PowerShell

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


<div style="overflow-x:auto;">
<style>
    tr:nth-child(even) {background-color: #f2f2f2}
</style>
<table style="width:100%">
  <tr>
    <th> </th>
    <th> OS </th>
    <th> Command </th>
  </tr>

  <tr>
    <td rowspan="3"> Add user <br> to group </td>
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
    
</table>
</div>