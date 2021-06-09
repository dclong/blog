Status: published
Date: 2019-05-02 02:40:46
Author: Benjamin Du
Slug: change-modified-time-of-files
Title: Change Modified Time of Files
Category: OS
Tags: Linux, modified timestamp, touch

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. Change the modifiled timestamp of a file to the specified timestamp.

        touch -m -t 201512180130.09 some_file

2. Change the modified timestamp of a file to the current time.

        touch -m some_file

3. Change the modified timestamp of all files in the current directory to the current time.

        find . -type f -print0 | xargs -0 touch -m

4. You can use the `stat` command to show the modified timestamps of files.

        stat -c '%y' some_file

## References

https://unix.stackexchange.com/questions/118577/changing-a-files-date-created-and-last-modified-attributes-to-another-file
