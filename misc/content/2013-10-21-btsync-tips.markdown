UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Title: Tips for BTSync
Date: 2016-07-09 22:47:36
Slug: btsync-tips
Category: Software
Tags: tips, BitTorrent Sync, BTSync, cloud, synchronization

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 
1. BitTorrent Sync does not synchronize files that you do not have the right permissions.

2. Do not modify the same file in a short time on different computers,
as this potentially causes version conflictions.
And you should event avoid changing the same file too frequently on the same computer!
not sure whether this has been improved ...

3. BTSync syncs .swp files which results in warnings when you edit file on the other computer
fortunately this is not a big problem, as even if you try to recover it will not work
possible solution: let BTSync ignores .swp files, not sure how to do that
auto delete swap files from vim using autocmd
move all swp files into a center directory that is not synchronized

4. BTSync is fast (average speed) when synchronizing big files,
but the overhead is also kind of big.
It takes a relative long time (compared to Dropbox) for BTSync to sync small files.
Not sure whether there is a way to improve the performance of BTSync on small files
Dropbox sync small files almost immediately


5. It is not a good idea to backup big files that are frequently changed.
One such example is the profile of thunderbird/firefox.
It is not surprising for a user to have large number of emails resulting large files 
in the profile directory of thunderbird. 
However, everytime a single change in the emails (marking read, unread, deteling, etc.) 
causes the profile to change. 
This soon accumulate large amount of backup files on your computer.

6. Prefer multiple smaller directories than one big directory.
This allows you to control which directory to sync after installing a new system 

7. BTSync fails to sync +x permission of files, not cool
it is probably that BTSync do not sync just because the change of permissions ...

4. it seems that .!sync file prevent files to be synced ..., check what happens

5. no warnings of version confliction which is not cool!
Fortunately, BitTorrent Sync keeps old version of files, so you can manually merge files ...

6. http://www.usesync.com/ always online BTSync
smart phone is probably just a better alternative

7. Incloudibly for central BTSync repository

## Possible Bugs

1. BTSync bug: sometimes symbolic link b.sh is gone

2. BTSync bug: false copy of some empty dirs

3. BTSync sometimes have folders left, when it is moved to a different place

## Share Keys

1. find websites or platforms that offering shared keys
you can actually start a business on this (using Vole or related technologies)

7. People say BTSync is faster (especially for large files).
I guess this measures the transfer process. 
According to my experience, BTSync and Software:AeroFS is not fast when detecting changes and finding peers.
This is easy to understand.
Sync solutions based on Software:BitTorrent is not good for real time usages!!!
They are good for syncing larges files but no need for them to start syncing immediately. 

## Cloud

7. Incloudibly seems to be a very good center server for Bittorrent Sync.

