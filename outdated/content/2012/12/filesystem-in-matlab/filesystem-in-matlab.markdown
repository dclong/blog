UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Filesystem in MATLAB
Date: 2012-12-14 22:02:00
Tags: filesystem, programming, MATLAB, file system
Category: Computer Science
Slug: filesystem-in-matlab
Author: Ben Chuanlong Du
Modified: 2015-05-14 22:02:00


1. Function `path` can be used to either display or modify the search path of MATLAB. 
Its functionality in MATLAB is similar to the functionality of environment variable `PATH` 
for DOS shell in Windows systems, 
and the use of them is also similar. 
`addpath` can be used to add new folders to the search path. 
It is a more friendly and convenient way to modify the search path than `path`. 
To add a folder and all its subfolders to the search path, 
you can use `addpath` together with `genpath` 
which can generate path strings for a folder and all its subfolders. 
To remove an existing path from the search path, 
you can use `rmpath`.

2. Function `what` can list the path for the current folder, 
and also files and folders relevant to MATLAB.

3. Function `dlmread` is helpful to read delimited files (e.g. Excel files), 
and `dlmwrite` is helpful to write delimited files. 
However,
be careful with `dlmwrite` when you want to write high accuracy data into a file, 
because by default `dlmwrite` keeps only a few digits.

4. To read data from or write data into a file, 
you must first use function `fopen` to open it to get a file pointer, 
and then you can use all different kinds of ways to read from 
(e.g. `fread`, `dlmread`, `fscanf` and `textread`) 
or write into a file (e.g.  `fwrite`, `dlmwrite`, `fprintf`). 
If you want to access a file randomly, 
you can use `fseek` to move the file point to a specific position. 
Never forget to close the file pointer using function `fclose` after you have done reading or writing. 
Usually it is much faster to read from or write into a binary file 
than to read from or write into a text file, 
and typically a binary file is smaller than a text file that contains the same data.

5. There are serveral ways to test the speed of code in MATLAB. 
The first way is to use the `Profile` button under `Desktop` menu. 
It is also the recommended way if you work in MATLAB IDE
as it tells you which part of your code is the bottle neck of performance.
The second way is to surround the code that you want to test with `tic` and `toc`.
For example, `tic; f(); toc` measures the time of running the code `f();`. 
The third way is to record the time manually using the function `now` 
and then use the function `etime` to calculate the elapsed time. 
The last ways is similar to the third way, 
but you record the cpu time using function `cputime` instead of the system time.

6. `pwd` can print out the current work directory of MATLAB, 
which is similar to the `pwd` command in Linux shell.
Though it is mutable, 
you'd better not change it. 
Because even if you change it, 
the current working directory will not change. 
To change the current working directory to a new one, 
you can use function `cd`. 
Whenever the working directory is changed, 
`pwd` be change to the current working directory. 
Note that the current working directory is always in the search path of MATLAB.

7. You can use `save` to save MATLAB workspace 
or selected variables into a file 
and `load` to load data from a MAT file to MATLAB workspace. 
To display variables in the workspace, 
you can use `whos`; 
to remove some variables from the workspace, 
you can use `clear`.

8. To display files and sub-folders of a folder, 
you can use `ls` or `dir`, 
which is same to Linux terminal command.

9. You can use `exit` or `quit` to terminate current session of MATLAB,
but you'd better save the MATLAB workspace first if necessary. 
If you want MATLAB to do some tasks before quitting, 
you can put put the corresponding code into file `finish.m` 
and place the file into the search path of MATLAB or into the current folder.

10. To remove files or graphics objects, 
you can use `delete`.

11. `fileattrib` can get and set attributes of files and folders in MATLAB.

