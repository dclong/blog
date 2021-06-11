UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2016-07-13 22:53:29
Author: Ben Chuanlong Du
Slug: useful-add-ons-for-thunderbird
Title: Useful Add-ons for Thunderbird
Category: software
Tags: software, thunderbird, add-on, plugin
Modified: 2016-07-13 22:53:29

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**


### Addons

#### Contacts

- Contact Tabs
- Display Contact Photo
- Google Contacts (for syncing contacts with Gmail)
- gContactSync

#### Calendar

- Lightning (comes with Task managing)
- Provider for Google Calendar (use with Lightning to sync Google Calendars)
- Zindus

#### Task Managing/Todo List/Notes Taking/Reminder

- Lightning (Task managing is one of the functionalities)
- Google Tasks Sync (integrate with Lightning well)
- Notepad (QuickFox)
- ReminderFox
- Todoist 
- StormCows

#### Email Operation Related

- Muttator (Vim key bindings)
- FiltaQuilla (message filtering)
- TaQuilla
Automatic tagging using Bayesian statistics
- Send Later (schedules email sending)
- ThunderBrowse (open web page in Thunderbird)
- SmartTemplate4
- QuickText (email templates)
- Macro Template
- Expression Search/Google Mail UI
- quickFilters

#### Miscellanea

- ImportExportTools (great for importing and exporting things)
- Tag Toolbar 
Add toolbar for toggling tags.
- Mail Merge (mass mails and person mails)
- Quick Translator 1.0 
- gTranslate
- ProfileSwitcher
- Signature Switch
- Quick Locale Switcher
- Simple Locale Switcher
- Adblock Plus (good for firefox but seems unnecessary for Thunderbird)
- Duplicate Contact Manager
- ThunderPlunger
- Signature Switch
- Dropbox for Filelink
- TorBirdy
- Enigmail
- Google Docs Viewer (PDF, DOCX, PPTX, XLSX, etc...)
- Remove Duplicate Messages (Alternate)
- G-Hub Lite 
- More Snooze
- LaTeX It!
This addons allows you to write LaTeX expressions 
such as `$x^2$` or `$$\sum_{x=0}\infty$$` in your emails 
and have them all replaced by a PNG image with the corresponding formula inside.



## FiltaQuilla

Header Regex Match

This matches any available property of the message header database with a regular expression. 
(Once again, if you don’t know what a regular expression is, this is not for you.) 
The format of the text in the search is PROPERTY:REGEX (that is, delimited with a ‘:’ character). 
The property is one of the available properties 
that are set on the nsIMsgDBHdr object associated with the message. 
OK, you probably don't know what those are, but some common values are:

"subject",  "sender",  "message-id",  "references", "recipients", "date",  "size", "flags", "priority",
"label" (obsolete TB 1.5 term),  "statusOfset" (yes it is really spelled that way),  "ccList", "bccList",
"msgThreadId",  "threadFlags",  "threadId", "threadSubject", "msgCharSet",  "threadParent",
"junkscore" (either null, 0, or 100), "junkpercent", "junkscoreorigin",  "threadNewestMsgDate",
"msgOffset",  "offlineMsgSize".

