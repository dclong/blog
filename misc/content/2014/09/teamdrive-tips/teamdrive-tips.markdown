Status: published
Date: 2020-05-18 08:12:57
Author: Ben Chuanlong Du
Slug: teamdrive-tips
Title: Tips on TeamDrive
Category: Software
Tags: software, teamdrive, tips, synchronization, cloud, backup
Modified: 2020-05-18 08:12:57

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

0. fix a startup issue

        :::bash
        LIBGL_DRI3_DISABLE=1 /usr/bin/synqion

1. TeamDrive 4 asking users to buy a commerical license frequently,
    which is very annoying. 
    It is suggested that you stay with TeamDrive 3 as long as it is supported. 
 
0. teamdrive on phone, if you use "available offline", update might not take effect ...
    if you encounter a problem, just uncheck available offline ...

1. TeamDrive clients might show more space usage than the web dashboard. 
    It's because the clients counts everything watched locally including old versions
    while the web only shows the true space usage. 

2. TeamDrive does not sync symbolic links currently!!

3. I don't TeamDrive support the standard hierarchical configuration files. 


2. It seems that TeamDrive is slow when syncing database files.

---------------------------------------
Why can't I see my Spaces when I install a new client?

Every new TeamDrive client is empty. There is no central server which has information about a client. The new client hast to learn where its servers are, which Spaces it has access to and with whom it can share files.

There are 3 ways to teach your client:

1) Receive and accept Space invitations.
If you want to sync 2 computers you have to invite yourself from the first computer. You can do this by choosing the "Invite all my TeamDrive installations" option at one of your old installations (right-click the relevant Space).

2) Alternatively, you can import your own Space keys by choosing "Extras" --> "Settings" --> "Backup" --> "Import from Backups..." from the menu -->, provided you have previously saved these keys, select all backups --> "Open" --> select the backups and click "Import" --> afterwards, right click on the imported Spaces and select "Restore Space". Keys function only in conjunction with your username and are thus useless to other users.

3) You can always create an new Space sync it to the Cloud and share your files with others.

Once your clients have been installed, you will automatically receive invitations to new Spaces on all clients.

also restore space ...
---------------------------------------



1. It seems that TeamDrive ignores symbolic links ...
    Is possible to keep symbolic links? Just keep these files, don't copy content ...
    Similarly, to Dropbox? At least should give options ...

3. How to let TeamDrive show up in the notification aera in Ubuntu?

5. You can check in virtual machine to see whether a local config file works.
    Contact support first.

16. you should sync the filter files, let ... point to local ...

8. Check how you can link TeamDrive with Amazon S3 or use local disk 

6. Teamview mess up file permissions!!!

7. how to change a space name on iPhone/computer?

4. how to ignore files/directories in TeamDrive?