UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Title: Synchronization and Backup Solutions
Author: Ben Chuanlong Du
Date: 2014-03-04 22:11:05
Slug: synchronization-and-backup-solutions
Category: Software
Tags: software, synchronization, backup, Baidu Yun, Dropbox, BitTorrent Sync, TeamDrive
Modified: 2016-12-04 22:11:05

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Alway all sychronization tools have problems with symbolic links.
Most of them just ignore symbolic links.
This makes sense as following symbolic links can causes serious disk problems.
If not followed then symbolic links are likely broken on other device.
The simple suggestion is do not place symbolic links in your synchronization folders.

Dropbox, TeamDrive, Mega, Bitcasa, BitTorrent Sync, Baidu Yun, Wei Yun

1. Among non-native sync & backup apps TeamDrive, Mega Sync, OneDrive (official client) are usable in mainland of China.

## Comparison of Cloud-based Synchronization/Backup Solutions

### Dropbox

Overall speaking, it is the best one.

#### Pros
1. cross-platform
2. relatively large free space (gained via invitation, etc.)
3. very reliable (stable)

#### Cons
1. not very secure, never put high privacy files in Dropbox before you encrypt it
manual encryption solves the problem
2. startup is very slow
3. every thing is in the same folder, no way to sync a folder with higher priority over others
while you can do this with TeamDrive or BTSync

### TeamDrive

#### Pros
1. cross-platform
1. very secure, good for private documentations
3. separated spaces which is much better than dropbox

#### Cons
1. small free space
2. symbolic links are ignored!!!

### BTSync

#### Pros
1. cross-platform but no GUI version for Linux.
2. free and the only limit is the limit of your hard disk
3. secure
4. fast for large files

#### Cons
1. not good for small files
2. encountered some problems last time I tried. some files was missing. I guess it is not very stable.
I'd rather wait for a stablization version rather than using the Beta version.

## Google Drive
overdrive for google drive

## OneDrive

### Linux

1. Use the non-official client at https://github.com/skilion/onedrive

2. Use OneDrive Windows app in Wine.

3. Use OneDrive Windows app in a VM.

## Box Sync

1. Use Box Sync instead of Box Edit.

2. The default sync directory of Box can be changed.
http://community.box.com/t5/Box-Sync/Can-An-Admin-Change-the-Default-Folder-Location-for-Box-Sync/ta-p/84

3. how to resolve the symbolic link problem? Box Sync, ...

4. There is no official Box Sync client for Linux.
However, unofficial clients exist.
My suggestion is do not bother to install Box Sync client on Linux.

https://uisapp2.iu.edu/confluence-prd/display/SOICKB/Using+Box+under+Linux

https://github.com/noiselabs/box-linux-sync

https://pypi.python.org/pypi/box-linux-sync/0.1.0

https://www.maketecheasier.com/auto-mount-box-net-to-linux-desktop/

http://xmodulo.com/how-to-mount-box-com-cloud-storage-on-linux.html

https://box-linux-sync.readthedocs.org/en/latest/


### Bitcasa

#### Pros
1. cross-platform, but no GUI version for Linux
2. can be mounted as a disk, so you can treat it as a network drive, save space on your local drive
#### Cons
1. no GUI version for Linux
3. the network drive usage highly relies on network speed!!!

## Mega

## Good Practices

1. Backup large non-privacy files on Baidu Yun or Wei Yun.

2. Backup large privacy critial files on Mega or encrypt them first and then backup to Baidu Yun or Wei Yun.

3. Build a local home server (e.g., using NFS or SAMBA) for sharing files.

4. Sync/backup small privacy critical files using TeamDrive.

5. Sync/backup other important but not privacy critical files using Dropbox.

9. It seems to me that mount network disk as a local one is not a good idea.
The reason is internet speed.
Mirroring network disk (or part of it) to local disk is the way to go.

12. It seems to me (based on a few very simple tests) that TeamDrive is faster than SpiderOak.

## Comparison of non-cloud Backup Solutions

1. Rsnpashot sounds like a good one for ordinary users,
good balance between easy to use, quick access, disk-saving, etc.
no diff but rather copy on change
takes more disk than incremental backup tools but it is much simipler to use and very robust

2. Duplicity is great incremental backup tool which also support encryption.
rdiff-backup is similar to Duplicity but without support of encryption.
I prefer Duplicity to rdiff-backup.

4. backupPC
BackupPC is a high-performance, enterprise-grade system for backing up Linux, WinXX and MacOSX PCs and laptops to a server's disk. BackupPC is highly configurable and easy to install and maintain.

5. Areca Backup is an Open Source personal backup solution which is released under the General Public License (GPL) v2.
It basically allows you to select a set of files / directories to back-up, choose where and how (as a simple file copy, as a zip archive, ...) they will be stored, and configure post-backup actions (like sending backup reports by email or launching custom shell scripts)

It has been designed to ...

... Be as simple as possible to set up : No complex configuration files to edit - Your backup configuration (stored as an XML file) can be edited with Areca's graphical user interface.

... Be as versatile as possible : Areca can use advanced backup modes (like "delta backup") or simply produce a basic copy of your source files as a standard directory or zip archive (readable by WinZip or other archivers).

... Allow you to interact with your archives : Browse your archives, track and recover a specific version of a file, merge a set of archives into a single one, etc.


Bacula is an open source, enterprise level computer backup system for heterogeneous networks. It is designed to automate backup tasks that had often required intervention from a systems administrator or computer operator.

Bacula supports Linux, UNIX, Windows, and Mac OS X backup clients, and a range of professional backup devices including tape libraries. Administrators and operators can configure the system via a command line console, GUI or web interface; its back-end is a catalog of information stored by MySQL, PostgreSQL, or SQLite.

Clonezilla is a free disk cloning, disk imaging, data recovery, and deployment computer program.[2] Clonezilla is designed by Steven Shiau and developed by the NCHC Free Software Labs in Taiwan.[3] Clonezilla SE provides multicast support similar to Norton Ghost Corporate Edition.

3. http://www.netpower.fr/osync
Osync - A two way local and / or remote sync script with fault tolerance, soft-deletion, resume support and more

-----------------------------


5. one important thing is whether to have a NAS or NFS.
if so, you can first backup to NAS/NFS, and let NAS/NFS worry about backup to cloud.
The NAS/NFS must be stable enought!!!

compare the different tools ...
rsnapshot
check rdiff-backup, it is probably better ...

and duplicity ...



https://alliance.seas.upenn.edu/~bcpierce/wiki/?n=Main.UnisonFAQTips

http://xmodulo.com/synchronize-files-between-two-servers.html

http://superuser.com/questions/31512/how-to-synchronize-the-home-folder-between-multiple-computers

osync: https://github.com/deajan/osync

csync: https://www.csync.org/

http://thanhsiang.org/faqing/node/192

http://fak3r.com/2009//howto-build-your-own-open-source-dropbox-clone/ 14.09.2016

## Unison

1. how does unison handle symbolic links?
