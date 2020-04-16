Status: published
Author: Ben Chuanlong Du
Date: 2019-12-19 18:43:44
Slug: hadoop-fs-tips
Title: Hadoop Filesystem Tips
Category: Software
Tags: big data, Hadoop, filesystem, file system, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 

## cat - Print a File

    :::bash
    hdfs dfs -cat

## chmod - Change Permission of Files/Directories

    :::bash
    hdfs dfs -chmod -R 777 /hdfs/path

## chown - Change the Owner of Files/Directories

    :::bash
    hdfs dfs -chown new_owner /hdfs/path

Notice that a HDFS path (file or directory)
can only be removed by its owner.
Other users cannot remove the path even if the file permission of the path is set 777.
If a HDFS path under user A's home (`/user/A/`) is changed to be owned by user B,
then neither A nor B can remove the path.
You have to change the owner of the path back to user A
and then use user A to remove the path.

## cp - Copy Files/Directories

    :::bash
    hdfs dfs -cp /user/saurzcode/dir1/abc.txt /user/saurzcode/dir2


## get - Download a File/Directory

    :::bash
    hdfs dfs -get

## getmerge 

    :::bash
    hdfs dfs -getmerge /hdfs/path /path/in/linux

## mkdir

    :::bash
    hdfs dfs -mkdir [-p] /path/to/create

## mv - Move/Rename Files/Directories

Move/rename the source file/directory `/path/to/source` TO `/path/to/des`.

    :::bash
    hdfs dfs -mv /path/to/source /path/to/des

Move the source file/directory `/path/to/source` INTO the directory `/path/to/des`.
That is,
move/rename the file/directory `/path/to/source` to `/path/to/des/source`.

    :::bash
    hdfs dfs -mv /path/to/source /path/to/des/

## put/copyFromLocal - Upload a file/directory to HDFS.

    :::bash
    hdfs dfs -put [-f]

The option `-f` overwrite existing files on HDFS. 
However, 
a tricky misunderstanding might happend when you upload a directory using the following command.

    :::bash
    hdfs dfs -put -f /local/path/to/some_directory /hdfs/path/to/some_directory

Supppose `/hdfs/path/to/some_directory` already exists,
it is not the directory `/hdfs/path/to/some_directory` itself get overwritten 
but rather files in it get overwritten.
If files in `/local/path/to/some_directory` have diffrent names than files in `/hdfs/path/to/some_directory`
then nothing is overwritten.
This might not what you want and can get you bitten. 
It is suggested that you always remove a directory manually using the command `hdfs dfs -rm -r /hdfs/path/to/some_directory`
if you intend to overwrite the whole directory.

## tail - Show Last Lines of a File

    :::bash
    hdfs dfs -tail /user/saurzcode/dir1/abc.txt


2. The command `hdfs dfs -mkdir` supports the `-p` option similar to that of the `mkdir` command in Linux/Unix.

3. Check size of a directory.
    However, the depth option is not supported currently.

        :::bash
        hdfs dfs -du [-s] [-h] URI [URI …] 

4. Remove a directory in HDFS without making a backup in trash.
    This is a dangerous operation 
    but it is useful when the directory that you want to remove 
    is too big to place into the trash directory.

        :::bash
        hdfs dfs -rm -r -skipTrash /tmp/chdu_item_desc

## Parquet Format

Hadoop commands do not support merging Parquet files. 
You can use [apache/parquet-mr](https://github.com/apache/parquet-mr) to merge Parquet files.

## Hadoop FS compress 

http://stackoverflow.com/questions/5571156/hadoop-how-to-compress-mapper-output-but-not-the-reducer-output

http://www.ericlin.me/disable-hive-output-compression



1. no update, have to update locally and upload to hadoop

3. by default 3 reps of each block of data, 3 reps is the best according to many discussions

4. hadoop is for large data of course

5. because of false tolorence/replication of data, you acutally use more space on Hadoop

6. master node (name node): data about data, primary and secondary master node, for reliable

7. data nodes (slave nodes), edge node, access point for the external applications, tools, and users that need to utilize the hadoop environment

11. edge nodes (gate to hadoop), name nodes, data nodes

## References

https://stackoverflow.com/questions/6504107/the-way-to-check-a-hdfs-directorys-size

https://dzone.com/articles/top-10-hadoop-shell-commands
