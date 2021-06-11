Status: published
Author: Ben Chuanlong Du
Date: 2012-08-17 11:42:15
Slug: useful-tools-linux
Title: Useful Tools in Linux
Category: OS
Tags: shell, remote, PDF, software, tools, terminal, application, Linux
Modified: 2020-02-17 11:42:15

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

<img src="http://dclong.github.io/media/linux/linux.png" height="200" width="240" align="right"/>

[IceWalkers](http://www.icewalkers.com/) is a great place
to find software/tools for all kinds of purposes.

## [Project](http://www.legendu.net/misc/blog/project-tips/)

## Server/Desktop Management

### [Linux Desktop Environment](http://www.legendu.net/misc/blog/desktop-environments-for-linux/)

### [Linux Package Management](http://www.legendu.net/misc/blog/package-management-in-linux/)

### [Terminal Tools](http://www.legendu.net/misc/blog/linux-terminal-tips/)

### [Administer](http://www.legendu.net/misc/blog/linux-administrator-tools/)

### [Disk Maintenance](http://www.legendu.net/misc/blog/command-line-tools-for-linux-file-system/)

### [Admin Tools](http://www.legendu.net/misc/blog/linux-administrator-tools/)

### Security
1. fail2ban
2. Tor (on-line anonymity)

### Encryption

1. gpg

### Time Synchronization

1. ntp (sync-debian)

### [Task Scheduling](http://www.legendu.net/misc/blog/workflow-managing-tools)

## Backup

### Cloud Backup Tools

1. Network Attach Storage (NAS)

2. Storage Made Simple (SME)

#### Centralized

0. Amazon S3
    - AeroFS can backup to Amazon S3
    - s3cmd is a command line client for Linux

1. Dropbox

2. TeamDrive (secure, fast)

3. Bitcasa (security, infinite storage)

2. Google Drive

#### Decentralized (private, security)

2. BitTorrent Sync (BTSync)

##### Pros

1. secure

2. free

3. no limit on files except the limit of your own disk

##### Cons

1. beta version, not stable enough

2. versioning is a little bit tricky

3. no GUI version for Linux

5. AeroFS (can use Amazon S3 as the central repository)

3. Syncthing

### Non-cloud Backup Tools

1. rsync (1-way synchronization)

3. rsnapshot (incremental backup)

4. duplicity (incremental backup with encryption and compression)

5. borg

6. Back In Time

5. unison (2-way synchronization, not a good solution compared to cloud backup tools)

7. Bacula (comprehensive backup tool)

8. BackupPC

1. FreeFileSync (a very good synchronization software written in C++, but bundled with malware now)


### File Transfer

0. infinit (fast, secure)

1. BitTorrent

2. BiTorrent Sync

### File Cleaning

1. BleachBit

### File Hosting

1. Mega

#### Pros

1. 50 GB free

2. secure (encrypted before upload)

3. 10 GB every 30 minutes free (essentially free consider currently network speed)

4. maximum file size is only restricted by browser memory capability

5. never expire

6. cross-platform and command line tools available for Linux

7. able to follow symbolic link

#### Cons
    1. one file at a time for free account

1. File Dropper

#### Pros

1. unlimited space

2. no bandwith limit

#### Cons

1. uploaded files will be removed if they are not downloaded even once
    within 30 days consecutively (files belong to premium account are never removed)

2. upload file can be at most 5 GB

3. the cheapest plan is $1/month.
    really no free account, but rather just upload and keep link
    so not convenient for people without an premium account

    Good for people who would like to share large files and do not need uploaded files to be persistent.
    Or for backing up frequently changed files so that before an uploaded file is removed,
    another updated version is uploaded.

2. Baidu Yun

3. Tencent Weiyun

## [Network](http://www.legendu.net/misc/blog/linux-network-tools/)

## [Compress and Uncompress](http://www.legendu.net/en/blog/compress-and-decompress-in-linux/)

## Virtual Machine
1. VirtualBox
2. VMWare
3. Xen
4. KVM (requires hardware support, e.g., Intel VT-x or AMD-V)
5. QEMU-KVM (requires hardware support, e.g., Intel VT-x or AMD-V)

## Database Management System (DBMS)

### Relational DBMS

1. MySQL

2. SQLite (embedded database)

### Object/Document-oriented DBMS

1. MongoDB
4. CouchDB
3. OrientDB (written in Java)
2. UnQLite (embedded database, sounds like a good replace for SQLite)
3. MooDB (embedded database)
4. Kyoto Cabinet (embedded, for simple key-value data)
5. LevelDB (embedded, for simple key-value data)

## Daily Work Tools (Office Tools, etc.)

### Well Supported Printers

1. HP
2. Brother

### Pinyin Input Method
1. Sogou Pinyin
2. Google Pinyin
3. Sun Pinyin

### Web Browser
0. Tor (on-line anonymity)
1. Google Chrome
2. Firefox/Iceweasel
3. w3m (a powerful text-based web browser)
4. lynx (another text-based web browser)

### On-line Tools

1. Doodle
2. Survata (for custom surveys)
3. Google Docs (Google Form can a simple solution to custom surveys)

### Finance
1. gnucash
2. DocumentBurst

### [Password Management](http://www.legendu.net/misc/blog/password-management/)

### Data Manipulation
0. grep/sed/awk/cut/sort/uniq/comm
1. pdfgrep

Search in pdf files for strings matching a regular expression.
It only works on PDF files but even not text files.

2. taggrepper - search and match tags of audio files against regular expressions

3. crgrep - common resource grep

4. sgrep - tool to search a file for structured pattern

2. recoll

Personal full text search package with a Qt GUI

1. catdoc/xls2csv/catppt

### Text Editor

1. Vim (general purpose text editor)
2. Visual Studio Code

## MS Office Alternative

2. LibreOffice

3. [OnlyOffice](http://www.onlyoffice.com/)

3. Calligra Suite (KDE dependent)

2. AbiWord (Word)

1. gnumeric (Excel)

3. WPS Office

### Publishing Tools

1. LaTex

#### [Scribus](https://www.scribus.net/magazine-production/)

Opensource Desktop Publishing



### Dictionary

1. goldendict

1. dict

### Email Client

1. Thunderbird (called IceDove in Debian)

2. Evolution

3. Claws Mail

4. Sieve (mail filtering language)

### PDF Tools

#### Reader/Viewer

1. evince

2. xpdf

2. okular

#### Manipulation

2. pdftk

### Scientific Reference Management

3. Zotero (open source, a very good one)

1. Mendeley (2G free, social network based, good for small usage, better to use together with Zotero)

2. ReadCube

2. JabRef (OK but not good)

### E-book library management

1. calibre

### Notes Taking

<http://www.legendu.net/misc/blog/software-for-taking-notes/>


### Task Management

0. XMind

0. WorkFlowy

1. Todoist

2. Wunderlist

3. Taskwarrior

### [Auto Typing Tools](http://www.legendu.net/misc/blog/auto-typing-tools/)

## Programming Tools

### Compiler

1. GCC

2. Clang

### Debugging Tools

0. GDB

1. Valgrind

2. CUDA-Memcheck

### Version Control

1. git

## Multimedia Tools

### Music Player

1. [Clementine](https://www.clementine-player.org/)

### Screenshot

[Shutter](http://shutter-project.org/)
is the best screenshot application for Linux (only).
You can install it on Ubuntu using the following command.
```
wajig install libgoo-canvas-perl shutter shutter
```

### CD/DVD burning

#### GUI Tools  

1. k3b  

2. gnome baker

3. brasero

#### Command line Tools

0. xvidenc (shell script to encode DVDs to Xvid)

1. isoinfo

2. genisoimage (Debian) or mkisofs (other Linux)

3. dd or cat

### Video/Audio Player

1. vlc

2. [IINA](https://github.com/iina/iina)

4. HandBrake

5. exiftool (command line multimedia meta data editor)

6. Exiv2 (image meta data library and tools written in C++)

### [Software for Editing Videos](http://www.legendu.net/misc/blog/software-for-editing-videos/)

### [Audio Tools](http://www.legendu.net/misc/blog/Audio-Tools/)

Please refer to
[Audio Tools](http://www.legendu.net/misc/blog/Audio-Tools/)
for more details.

### Screencast

1. comstudio (Windows only)

### Voice Control

1. Blather

2. Voxforge

3. Simon



### Image

1. ImageMagic

2. GwenView (KDE)

3. digiKam (KDE)

1. PIL (python image library)

4. exiftool

### Scan/OCR

0. VueScan

1. tesseract

2. gocr

### [Charts](http://www.legendu.net/misc/blog/software-for-charts/)

### 3-D Modelling

1. blender

1. freeCAD

2. OpenSCAD

1. Google Sketchup

2. EQUINOX-3D

## Social Tools

### Teleconference

0. Blink

1. Skype

2. Wire

2. Jitsi

3. ekiga

4. QQ (webqq, wineqq)

## Web Hosting

### Server Side Scripting Language

1. PHP

2. JSP

### Client Side Scripting Language

1. JavaScript

### Integrated Package for Web Hosting

1. XAMPP (originaly called LAMPP)

### Math Formulas in Web Pages

1. MathJax (a successor to jsMath)

## Performance Tools

## Boot Performance

1. bootchart

2. readahead-fedora

## Runtime Performance

1. preload

2. localepurge

## Other Suggestions

1. remove old kernels

2. package clean-up

## Web Tools

1. 1. JustInMind Prototyper

4. Django

3. Node.JS

4. ActiveJDBC

5. web2py

## Software Host

1. GitHub
    - no private repository for free account

2. Bitbucket
    - unlimited private repositories for free account

3. SourceForge

## Repository Hosting Tools

1. gitolite

2. gitlab

## Websites

1. MileWise

2. BTGuard

3. http://dedalvs.tumblr.com/post/48998678919/99-life-hacks-to-make-your-life-easier

## Translation

https://www.apertium.org/index.eng.html?dir=eng-cat#translation

## Misc

1. KeyMon: displays the mouse button or key being clicked/pressed,
    useful when you video tape your screen
