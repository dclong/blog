Status: published
Date: 2019-01-03 16:17:10
Author: Ben Chuanlong Du
Slug: shell-alternatives
Title: Python Alternatives to Shell
Category: Computer Science
Tags: programming, IPython, shell, bash, xonsh, plumbum, Python, shell alternatives
Modified: 2020-03-03 16:17:10

## Python Equivalent of Shell Commands

<table style="width:100%">
  <tr>
    <th> Shell Command </th>
    <th> Alternative </th>
    <th> Python </th>
  </tr>
  <tr>
    <td rowspan="4"> mkdir -p /path/to/file </td>
    <td bgcolor="#348017"> Path("path/to/some/file").mkdir(exist_ok=True) </td>
    <td> <a href="https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir"> pathlib </a> </td>
  </tr>
  <tr>
    <td> os.makedirs("/path/to/file", exist_ok=True) </td>
    <td> <a href="https://docs.python.org/3/library/os.html#os.makedirs"> os </a> </td>
  </tr>
  <tr>
    <td> !mkdir -p /path/to/file </td>
    <td> <a href="https://ipython.readthedocs.io/en/stable/overview.html#enhanced-interactive-python-shell"> IPython </a> </td>
  </tr>
  <tr>
    <td> mkdir -p /path/to/file </td>
    <td> <a href="https://xon.sh/"> xonsh </a> </td>
  </tr>
  <tr>
    <td rowspan="4"> cp file1 file2 </td>
    <td bgcolor="#348017"> shutil.copy2("file1", "file2") </td>
    <td> <a href="https://docs.python.org/3/library/shutil.html#shutil.copy2"> shutil </a> </td>
  </tr>
  <tr>
    <td> shutil.copyfile("file1", "file2") </td>
    <td> <a href="https://docs.python.org/3/library/shutil.html#shutil.copyfile"> shutil </a> </td>
  </tr>
  <tr>
    <td> !cp file1 file2 </td>
    <td> <a href="https://ipython.readthedocs.io/en/stable/overview.html#enhanced-interactive-python-shell"> IPython </a> </td>
  </tr>
  <tr>
    <td> cp file1 file2 </td>
    <td> <a href="https://xon.sh/"> xonsh </a> </td>
  </tr>
  <tr>
    <td rowspan="4"> ln -s file1 file2 </td>
    <td bgcolor="#348017"> Path("file1").symlink_to("file2", target_is_directory=True) </td>
    <td> <a href="https://docs.python.org/3/library/pathlib.html#pathlib.Path.symlink_to"> pathlib </a> </td>
  </tr>
  <tr>
    <td> os.symlink("file1", "file2", target_is_directory=True) </td>
    <td> <a href="https://docs.python.org/3/library/os.html#os.symlink"> os </a> </td>
  </tr>
  <tr>
    <td> !ln -s file1 file2 </td>
    <td> <a href="https://ipython.readthedocs.io/en/stable/overview.html#enhanced-interactive-python-shell"> IPython </a> </td>
  </tr>
  <tr>
    <td> ln -s file1 file2 </td>
    <td> <a href="https://xon.sh/"> xonsh </a> </td>
  </tr>
  <tr>
    <td rowspan="4"> ln -sT file1 file2 </td>
    <td bgcolor="#348017"> Path("file1").symlink_to("file2", target_is_directory=False) </td>
    <td> <a href="https://docs.python.org/3/library/pathlib.html#pathlib.Path.symlink_to"> pathlib </a> </td>
  </tr>
  <tr>
    <td> os.symlink("file1", "file2", target_is_directory=False) </td>
    <td> <a href="https://docs.python.org/3/library/os.html#os.symlink"> os </a> </td>
  </tr>
  <tr>
    <td> !ln -sT file1 file2 </td>
    <td> <a href="https://ipython.readthedocs.io/en/stable/overview.html#enhanced-interactive-python-shell"> IPython </a> </td>
  </tr>
  <tr>
    <td> ln -sT file1 file2 </td>
    <td> <a href="https://xon.sh/"> xonsh </a> </td>
  </tr>
  <tr>
    <td rowspan="4"> rm file </td>
    <td bgcolor="#348017"> Path("/path/to/file").unlink() </td>
    <td> <a href="https://docs.python.org/3/library/pathlib.html#pathlib.Path.unlink"> pathlib </a> </td>
  </tr>
  <tr>
    <td> os.remove(file) </td>
    <td> <a href="https://docs.python.org/3/library/os.html#os.remove"> os </a> </td>
  </tr>
  <tr>
    <td> !rm file </td>
    <td> <a href="https://ipython.readthedocs.io/en/stable/overview.html#enhanced-interactive-python-shell"> IPython </a> </td>
  </tr>
  <tr>
    <td> rm file </td>
    <td> <a href="https://xon.sh/"> xonsh </a> </td>
  </tr>
  <tr>
    <td> rmdir /path/to/dir </td>
    <td bgcolor="#348017"> Path("/path/to/dir").rmdir() </td>
    <td> <a href="https://docs.python.org/3/library/pathlib.html#pathlib.Path.rmdir"> pathlib </a> </td>
  </tr>
  <tr>
    <td rowspan="3"> rm -rf dir </td>
    <td> shutil.rmtree(dir) </td>
    <td> <a href="https://docs.python.org/3/library/shutil.html#shutil.rmtree"> shutil </a> </td>
  </tr>
  <tr>
    <td> !rm -rf dir </td>
    <td> <a href="https://ipython.readthedocs.io/en/stable/overview.html#enhanced-interactive-python-shell"> IPython </a> </td>
  </tr>
  <tr>
    <td> rm -rf dir </td>
    <td> <a href="https://xon.sh/"> xonsh </a> </td>
  </tr>
  <tr>
    <td rowspan="5"> mv file1 file2 </td>
    <td bgcolor="#348017"> Path("file1").rename("file2") </td>
    <td> <a href="https://docs.python.org/3/library/pathlib.html#pathlib.Path.rename"> pathlib </a> </td>
  </tr>
  <tr>
    <td> shutil.move("file1", "file2") </td>
    <td> <a href="https://docs.python.org/3/library/shutil.html#shutil.rmtree"> shutil </a> </td>
  </tr>
  <tr>
    <td> os.rename("file1", "file2") </td>
    <td> <a href="https://docs.python.org/3/library/os.html#os.rename"> os </a> </td>
  </tr>
  <tr>
    <td> !mv file1 file2 </td>
    <td> <a href="https://ipython.readthedocs.io/en/stable/overview.html#enhanced-interactive-python-shell"> IPython </a> </td>
  </tr>
  <tr>
    <td> mv file1 file2 </td>
    <td> <a href="https://xon.sh/"> xonsh </a> </td>
  </tr>
  <tr>
    <td> chmod 600 /path/to/file </td>
    <td bgcolor="#348017"> Path("/path/to/file").chmod(0o600) </td>
    <td> <a href="https://docs.python.org/3/library/pathlib.html#pathlib.Path.chmod"> pathlib </a> </td>
  </tr>
</table>

## [IPython](https://github.com/ipython/ipython)

IPython is the best and simpliest Python approach to replace (all part of) shell so far.

https://ipython.readthedocs.io/en/stable/interactive/magics.html

https://github.com/ivanov/vim-ipython

1. Use the IPython shell or JupyterLab notebook (preferred) 
    instead of Shell for complicated interactive operations.

2. Be careful about illegal shell commands.
    For example,
    `ls )` in Bash shell throws the error message `bash: syntax error near unexpected token )`.
    If you have a equivalent IPython command,
    it will throw the same error message.
    For example,
    suppose `file` is path of a file which contains `)`
    then `!ls {file}` in IPython will throws the same error message as above.
    However,
    this is definitely trickier to debug than the original Bash shell command `ls )`.
    There are several ways to avoid this.
    First,
    you can use Python script
    ([xonsh](https://github.com/xonsh/xonsh) is a great choice is vanilla Python script is too verbose)
    instead Shell as underlying commands.
    Second,
    you can show the underlying Shell commands for debugging.

3. You can even run Shell commands on a remote server (via `ssh` or a remote kernel) in JupyterLab notebook.
    This provide the advantage of leveraging the JupyterLab notebook UI.


## [xonsh](https://github.com/xonsh/xonsh)

`xonsh` is another great Python approach to replace shell.
Unlike IPython, 
xonsh does not require the prefix `!` to run arbitrary shell command. 
However, 
there is one flaw of xonsh.
You cannot use `$()` and friends in the middle of an argument,
which limits its usability serious for complicated shell commands.
Please refer to 
[this issue](https://github.com/xonsh/xonsh/issues/3290)
for more details.

## [plumbum](https://github.com/tomerfiliba/plumbum)

Yet another Python approach as a replacement of shell.
I personally prefer IPython and xonsh to plumbum.

## References

https://github.com/ninjaaron/replacing-bash-scripting-with-python

https://stackoverflow.com/questions/209470/how-to-implement-common-bash-idioms-in-python

https://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python

https://docs.python.org/3/library/pathlib.html#module-pathlib