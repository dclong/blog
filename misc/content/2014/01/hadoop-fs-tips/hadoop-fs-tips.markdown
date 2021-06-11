Status: published
Author: Ben Chuanlong Du
Date: 2014-01-21 23:37:52
Slug: hadoop-fs-tips
Title: Hadoop Filesystem Tips
Category: Software
Tags: big data, Hadoop, filesystem, file system, tips
Modified: 2021-02-21 23:37:52

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**


## hadoop fs vs hadoop dfs vs hdfs dfs

1. `hadoop fs` supports generic file systems.
    It can be used when you are dealing with different file systems 
    such as Local FS, HFTP FS, S3 FS, and others.
    `hadoop fs` is recommended when you work with differnt file systems at the same time.

2. Both `hdfs dfs` and `hadoop dfs` are very specific to HDFS. 
    They work for operation relates to HDFS. 
    `hadoop dfs` has been deprecated in favor of `hdfs dfs`.
    `hdfs dfs` is recommended when you work with HDFS only.


## General Tips 

1. `*` represents all files/directories 
    including hidden ones (which is different from Linux/Unix shell).

2. The success file `_SUCCESS` is generated when a Spark/Hadoop application succeed.
    It can be used to check whether the data produced by a Spark application is ready.
    The success file `_HIVESUCCESS` is generated when a Hive table is refreshed successfully.
    It can be used to check whether a Hive table is ready for consumption.

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

## count (for Quota)

    :::bash
    hdfs dfs -count -q -v -h /user/username
    QUOTA       REM_QUOTA     SPACE_QUOTA REM_SPACE_QUOTA    DIR_COUNT   FILE_COUNT       CONTENT_SIZE  PATHNAME  
    16 K           7.9 K             3 T           3.0 T           27        8.1 K            573.8 M  /user/username

`QUOTA` is namespace quota, 
i.e., the number of files you can store. 
The directory /tmp has no quota limit. You can use it for storing files temporarily.


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
        hdfs dfs -rm -r -skipTrash /tmp/item_desc


## checksum

    :::bash
    hdfs dfs -checksum URL

Notice that the checksum command on HDFS returns different result from the md5sum command on Linux.


## Merge Multiple Files¶

Use hadoop-streaming job (with single reducer) 
to merge all part files data to single hdfs file on cluster itself 
and then use hdfs get to fetch single file to local system.

    :::bash
    hadoop jar /usr/hdp/2.3.2.0-2950/hadoop-mapreduce/hadoop-streaming-2.7.1.2.3.2.0-2950.jar \
        -Dmapred.reduce.tasks=1 \
        -input "/hdfs/input/dir" \
        -output "/hdfs/output/dir" \
        -mapper cat \
        -reducer cat

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

https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html

https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/FileSystemShell.html

https://stackoverflow.com/questions/6504107/the-way-to-check-a-hdfs-directorys-size

https://dzone.com/articles/top-10-hadoop-shell-commands

https://stackoverflow.com/questions/18142960/whats-the-difference-between-hadoop-fs-shell-commands-and-hdfs-dfs-shell-co