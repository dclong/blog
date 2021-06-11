UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: R System and Configurations
Date: 2012-11-21 00:00:00
Tags: R, configuration, programming, system
Category: Computer Science
Slug: r-system-and-configurations
Author: Ben Chuanlong Du
Modified: 2012-11-21 00:00:00

<img src="http://dclong.github.io/media/r/r.png" height="200" width="240" align="right"/>

1. To allow opening R from a directory in R in Windows system, we can
modify the registry. More specifically, we can add a command name
(to be appear in the right-click menu) under
`HKEY_CLASSES_ROOT\Directory\Backgroup\shell`, and then
add a subkey `command` under it. Last, we just need to change the
default value to be the command that we want to run each time we
click the menu item.

2. There are many ways to change configurations of R. For example, to
change the default working directory of R in Windows, you can change
the properties of the shortcut of R software, which also applies to
other softwares in Windows. Another way is to put some code which
changes the default working directory into file `Rprofile.site` 
(The code inside this file will be run on the startup of R.).
The latter way can also be used to set other configurations for R,
and it is preferred to other ways of setting configurations for R,
because it is a universal way and is guaranteed to work (If you set configurations for R in other ways and at the same
time, set configurations in file `Rprofile.site`, these
configurations in file `Rprofile.site` will be in effect.)

3. `R.Version` can display the version information of R.

4. Function `args` can show the arguments of functions in R.

5. We can use function `Sys.sleep` to suspend execution of R for given
time.

6. By default, function `ls` returns non-hidden objects 
(By default, `ls` does not return objects whose names start with a
dot. For this reason I call these objects whose name start with a
dot hidden objects.) in current
environment. For example if we use `ls()` in a function, then it
only returns these non-hidden objects defined in the function. To
get non-hidden object in the top level environment (R workspace),
you can use `ls(pos=1)`; to get non-hidden objects in a package, we
can use `ls(pos="package:pkgname")`. Sometimes, you might want to
see all objects including these hidden ones in an environment. To do
so, you can use the option `all.anmes=T`. Notice that `ls` also support
regular expression (use the option `pattern`), which enables you to find
objects in R workspace faster.

7. In order to be convenient, usually we would like to specify short
names of executables. Sometimes this could lead to failure because
some functions in R do not accept short names of executables, e.g.
`shell.exec`, which is really stupid. A good way to solve the
problem is to use function `Sys.which` to find the full name of
executables. Conversely, function `basename` can get the base name
of a path.

8. `system` calls invokes a system command, but the command passed to
it must be an executable (extensions `.exe` or `.com`) or a batch
file (extensions `.cmd` or `.bat`). Redirection, pipes, DOS internal
commands and so on cannot be used with `system`. `shell` is a more
user-friendly wrapper for `system` which is more powerful (support
redirection, pipes, DOS internal commands and so on). If you want to
make use of Windows file association, use `shell.exec`.

9. Function `search` returns search path for R, which includes loaded
packages.

10. Function `demo` is helpful to show how to use a function or package,
however, it creates many global variables which is annoying. Using
function `example` can solve this problem, but it seems that these
functions are not exactly the same. I'm a little confused about
these two functions.

11. R support partial matching on tags, which means that usually you
do not have to use full names for arguments of a R function. You can
use partial names for arguments. However, always be careful when a R
function takes `ldots` as an argument.

12. Function `Sys.setenv` and `Sys.unsetenv` can set and unset
environment variables.

13. `Sys.info` contains information about the operating system. Variable
`.Platform` contains information about R system 
(Actually information related to R system are usually stored in
variables starting with dot).

14. `Sys.time` returns the system time, i.e. the time of the computer on
which the code is run. There is another function called `system.time`
which can calculate how much time an evaluation takes.

15. `gc` collect garbage. R is infamous for extensive memory using. If
you delete some big objects in R workspace, you'd better use `gc()`
to manually trigger the garbage collection.

16. the good us of `source` with local = TRUE ...

17. `options` allows one to get and set a variety of global options
which affect the way in which R computes and displays ints results.
For example, `options(width=40)` forces R to format its output
results to have at most 40 characters (if possible). Notice that
this can be very helpful if you use Sweave. For example, if the
outputs of some R code in Sweave is too long, you can add a similar
command as above to format the R outputs.
