Status: published
Author: Ben Chuanlong Du
Date: 2020-05-22 15:47:51
Title: Tips on "sed"
Slug: sed-tips
Category: Software
Tags: tips, software, text manipulation, shell, Linux, sed

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**

It is suggested that you use Python script as an alternative to `sed` 
for manipulating text files 
unless you have to stick to shell script.
 
1. Add `#!/bin/bash` to the first line of all `.txt` files.  

        :::bash
        sed -i '1 s_^_#!/bin/bash\n_' *.txt

2. Add `#!/bin/bash` to the last line of all `.txt` files.  

        :::bash
        sed -i '$ s_$_\n#!/bin/bash_' *.txt

3. Add `https://www.quandl.com/api/v1/datasets/CME/` to the beginning of each line in a file.

        :::bash
        sed -i 's_^_https://www.quandl.com/api/v1/datasets/CME/_g' done.txt 

4. Get rid of all spaces (helpful for comparing not well formatted code)
对于格式问题 可以直接先删除空格等 然后再比较文件！！！very briliant idea!!! 

        :::bash
        sed -i 's/ //g' *.r

## Examples of Cleaning CSV Data

1. Replace all ` + ` with `_` in the first (header) line.

        :::bash
        sed -i '1 s/ + /_/g' *.csv

2. Replace all ` ` with `_` in the first (header) line.

        :::bash
        sed -i '1 s/ /_/g' *.csv

3. Replace all `-` with `_` in the first (header) line.

        :::bash
        sed -i '1 s/-/_/g' *.csv

4. Replace all `.` with `_` in the first (header) line.

        :::bash
        sed -i '1 s/\./_/g' *.csv

5. Print the first (header) line of all CSV documents seprated by dash lines.

        :::bash
        echo "--------------------------------------------------";
        for f in *.csv; do
            head $f -n 1;
            echo "--------------------------------------------------";
        done

6. More examples.

        :::bash
        sed -i 'd/^layout: page/' *.md
        sed -i '/^layout: page/d' *.md
        sed -i '/^comments: yes/d' *.md
        sed -i '/^---$/d' *.md
        sed -i '/^title: /Title: /s' *.md
        sed -i 's/^title: /Title: /' *.md
        sed -i "2 s/^/Date: 2013-10-20 00:00:00\n/" *.md
        sed -i 's/\([0-9]\+\)\.  /\1\. /g' *

1. insert "Author: Ben Chuanlong Du" as the 2 line into a text file. 
Notice the `\` delimiter. You cannot use `/`.

        :::bash
        sed -i '2 i\Author: Ben Chuanlong Du' path_to_file

However, 
if text file contains only 1 line, 
the above command does not do anything!

2. Add a blank line at the beginning of file.

        :::bash
        sed '1 i\\' file.txt

### sed

4. Code for rick's problem (splitting a column into 2)

        :::bash
        sed 's/\(s[0-9]\{1,2\}\)" "\(t[0-9]\{1,2\}\)/\1-\2/g' testing.txt

16. Insert `#!/bin/bash` as the first line into file with the extension `.txt`. 

        :::bash
        sed -i '1 s_^_#!/bin/bash\n_' *.txt


1. Get rid of lines matching `^user_id,.*` with the 1st line skipped.
    This is helpful when you merge multiple text files with headers 
    (e.g., output of Spark with headers).
    This commands help you get rid of duplicated header lines. 
    Of course, 
    you have replace the regular expression `^user_id,.*` with an appropriate one.

        :::bash
        sed -i '2,$ s/^user_id,.*$//g' data.csv 

2. Get rid of escaped double quotes (`\"`).

        :::bash
        sed -i 's/\\"//g' data.csv

3. Replace `## Usage` with `## Usage in Linux/Unix`

        :::bash
        sed -i 's_^## Usage.*$_## Usage in Linux/Unix_' *.ipynb

4. Replace `valid users = ${DOCKER_USER}` with `valid users = dclong`.

        :::bash
        sed "s/^valid users\s*=\s*\${DOCKER_USER}/valid users = dclong/g" smb.conf 

5. Remove the lines containing Python 2.7 versions (e.g., `2.7.16`).

        :::bash
        sed -z 's/2\.7\.[[:digit:]]*\n//' .pyenv/version

## Questions

1. sed recursively ... aaaa aa -> a?

