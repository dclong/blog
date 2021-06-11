UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-02-03 19:30:50
Author: Ben Chuanlong Du
Slug: add-an-entry-into-the-right-click-menu-in-windows
Title: Add an Entry into the Right-click Menu in Windows
Category: OS
Tags: Windows, right-click menu, registry, regedit
Modified: 2015-02-03 19:30:50

To add an entry into the right-click menu in Windows, 
edit the registry following the steps below.

0. Open the registry.
You can search for `regedit` in Windows Start menu and run it.

1. Navigate to the key
`HKEY_CLASSES_ROOT\Directory\Background\shell`
in the registry.

2. Create another key with any name (e.g., rstudio) under 
`HKEY_CLASSES_ROOT\Directory\Background\shell`. 

3. Set a value (e.g., Rstudio) for the newly created key (rstudio)
in the right-side pane of the registry.
This value (Rstudio) shows up in the right-click menu whenever you right click.

4. Create another key named `command` under the newly created key (rstudio).

5. Set the value of the newly created key `command` 
to be the full path of the application
(e.g., `C:\Program Files\RStudio\bin\rstudio.exe`)
that you want to launch.
