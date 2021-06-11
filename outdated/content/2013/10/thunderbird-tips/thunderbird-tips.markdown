UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2017-03-04 14:29:35
Slug: thunderbird-tips
Title: Random Tips About Thunderbird
Category: Software
Tags: tips, software, thunderbird, email client
Modified: 2017-03-04 14:29:35

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**
 
## Backup

0. Regularly backup your whole thunderbird profile!
When your thunderbird encounters problems, 
you can recover it easily using your backup profiles.

1. copy the entire folder of tunderbird to move configuration to another computer

## General Tips

2. it seems that Thunderbird can handles multiple profiles itslef, 
see how thunderbird switches profiles itself, 
this is great!

2. External Editor Plugin

7. not good way to use thunderbird as RSS reader,
too big very soon,
cannot sync, just use a web RSS, e.g., feedly

8. archive your important emails!!!

9. Do not use display attachment inline. 
It makes Thunderbird slow when reading emails with large attachments.
You can turn it off by uncheck "View -> Display attachment inline".  

10. To show pictures in the email:
Menu: Edit -> Preference -> Privacy -> Allow remote content in messages

11. to disable message sync (can be useful if you want to keep an expired email account but don't want to get bother by login failure message)
right click on an account -> Settings -> Server Settings
uncheck "Check for new messages at startup" and 'Check for new messages every X minutes" in Server Settings.

## Tags

1. Thunderbird does not have built-in support for wildcard or regular expression.
However, you can use the plugin "FiltaQuilla".

## Sync Lightning with Google Calendar

You need the addons `Lightning` and `Google Calendar Provider`.

New calendar -> Calendar on network -> paste carlendar private link
-> Google calendar -> type in and save password.

12. thunderbird works well with Outlook calendar invitation

## Sync

0. sync apps files such as thunderbird might not be a good idea!!!
The files are the same, so it's easy to get conficts, corruption, etc.
Use your way, copy from one to the other directly!!

1. it is not a good idea to sync thunderbird profile.
A much better way is to makes changes (such as adding/deleting accounts, installing/removing add-ons, tags, etc.) 
only on a main computer. 
You can still read, write, archive, deleting emails on multiple computers using thunderbird.
Backup the thunderbird profile on the main computer you use. 
Whenever you want use thunderbird on a new computer, 
just copy the thundbird profile from the main computer or from a backup over.

10. It seems more and more to me that sync thunderbird is not a good idea ...
At least, you should not use btsync because it causes problems frequently ...

3. You should think about how to sync address book,
I think you can use a central address book and link ...
or think about sync with Google contacts (not recommend as Google is evil)

0. You can move an old `msgFilterRules.dat` file 
into a new Thunderbird profile.
Those filters involing non-existing tags won't work.
They automatically delegate to the tag `Important`.
However, 
if you add the missing tags, then most of the filters works like a charm.
You can manually correct these filters that still delegat to the tag `Important`.
This a good way to migrate filters in Thunderbird.

## change default account

1. select the account that you want to set as default
2. right click on the acount and choose settings
3. click Account Action at the bottom and then choose Set as Default in the drop-down menu.

## Questions

1. thunderbird: is there an easy way to convert a message filter on one account to another account?

2. thunderbird hangs at "attaching ..." -> reply contains image that are not available or after compact folders ...
