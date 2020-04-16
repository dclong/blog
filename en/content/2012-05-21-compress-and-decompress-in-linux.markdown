Status: published
Title: Compress and Decompressing Archives in Linux
Date: 2016-06-19 12:17:21
Slug: compress-and-decompress-in-linux
Author: Ben Chuanlong Du
Category: OS
Tags: Linux, decompress, compress, archive, split, multiple, zip, tar, gz, bz2, dtrx, rar, 7zip


## Tips and Traps

1. Always test integrity of the compressed file
    before you throw away the original archives.
    I've seen a case before that a large zip file generated in Windows
    cannot be unzipped correctly in Linux.
    Not sure what happend though. 

## Universal Way

```bash
# decompress
dtrx file_name
```

## tar.gz or tgz

1. List the content of an archive.

        :::bash
        tar -ztvf archive_name.tag.gz

2. Extract the content of an archive to the current directory.

        :::bash
        tar -zxvf archive_name.tag.gz

3. Extract the content of an archive to a directory named "exdir".

        :::bash
        tar -zxvf archive_name.tag.gz -C exdir

4. Create an archive.

        :::bash
        tar -zcvf archive_name.tar.gz /path/to/file_or_dir

5. Create an archive with some files excluded.

        :::bash
        tar -zcvf archive_name.tar.gz --exclude='abc' --exclude='xyz' /path/to/file_or_dir

## .gz

```bash
# decompress
gunzip -c archive_name.gz > decompressed_file_name
# or
gzip -cd archive_name.gz > decompressed_file_name
# or
zcat archive_name.gz > decompressed_file_name
```
Notice that you have to use the `-c` option,
otherwise,
the original compressed file is removed.

## tar.bz2

```bash
# list the archive contents
tar -jtvf archive_name.tar.bz2
# extract the archive contents to the current directory
tar -jxvf archive_name.tar.bz2
# extract the archive contents to a directory named "exdir"
tar -jxvf archive_name.tar.bz2 -C exdir
```

## zip

1. List the content of an archive.

        :::bash
        unzip -l archive_name.zip

2. Test the integrity of an archive.

        :::bash
        unzip -t archive_name.zip

3. Extract the archive contents into the current directory.

        ::bash
        unzip archive_name.zip

4. Extract the archive contents into the directory "exdir".

        :::bash
        unzip archive_name.zip -d exdir

5. Create a zip archive. 

        :::bash
        zip -r archive_name.zip .

6. Create a zip archive with some files excluded.

        :::bash
        zip -r -x "Nothanks.jpg" archive.zip images/ 

## rar

```bash
# list the archive contents
unrar l file_name
# test integrity of the archive
unrar t file_name
# extract the archive with full names
unrar x file_name
```

## Jar 

```
# extract the archive
jar xf jar-file [archived-file(s)]
```

## 7zip

```bash
# list the archive contents
7za l file_name
# test the archive contents
7za t file_name
# extract the archive contents with full names
7za x file_name
# extract a file/folder from the archive
7za x archive_name path_to_file_to_be_extracted
```
If the compressed archive is splitted into several smaller files,
just replace `file_name` in the above commands
with the name of the first file of the compressed archive.

For `rar` and `7za`,
I'm not sure whether there are options for creating a new directory
to uncompress the archive into.
However, you can always first create an empty directory,
move the archive into it and then uncompress it.

## Multiple Archives

The archive related commands (e.g., `tar`, `zip`, `unzip`, etc.) in Linux
does not support decompressing from multiple archives
or compressing files into multiple archives directly.
To extract content from multiple archives,
you need to first concatenate them into a single one.
For example,
you can use the following command to unzip archives
`BigDataLite-3.0.zip.001`, `BigDataLite-3.0.zip.002`, `BigDataLite-3.0.zip.003`,
`BigDataLite-3.0.zip.004`, `BigDataLite-3.0.zip.005` and `BigDataLite-3.0.zip.006`.
```bash
# concatenate zipped archives into a single one
cat BigDataLite-3.0.zip.00? > BigDataLite-3.0.zip
# unzip the combined archive
unzip BigDataLite-3.0.zip
```
To compress files into multiple archives,
you have to first compress them into a single archive
using one of the commands introduced before
and then split the single archive into multiple ones
using the command `split`.
For example,
the following command split the archive `WinTPC_1.tar.gz`
into smaller ones named `WinTPC_1.tar.gz_part??` with size around 2.7G.
```bash
split -b 2700M -d WinTPC_1.tar.gz WinTPC_1.tar.gz_part
```
An alternative way (and better in my opinion)
is to specify the number of archives (with about equal size) to split into.
```bash
split -n 5 -d xp_2.tar.gz xp_2.tar.gz_part
```

## References

[18 Tar Command Examples in Linux](https://www.tecmint.com/18-tar-command-examples-in-linux/)

[Exclude Certain Files When Creating A Tarball Using Tar Command](https://www.cyberciti.biz/faq/exclude-certain-files-when-creating-a-tarball-using-tar-command/)

[6.4 Excluding Some Files](https://www.gnu.org/software/tar/manual/html_node/exclude.html)

[How to Exclude Files from a Zip Archive](https://osxdaily.com/2013/04/30/how-to-exclude-files-from-a-zip-archive/)