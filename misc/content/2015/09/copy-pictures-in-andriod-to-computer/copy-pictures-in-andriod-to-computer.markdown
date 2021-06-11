Status: published
Date: 2015-09-12 23:41:58
Author: Ben Chuanlong Du
Slug: copy-pictures-in-android-to-computer
Title: Copy Pictures from an Android Phone to a Computer
Category: OS
Tags: Linux, scp, rsync, pictures, image, photo, media, Android
Modified: 2021-04-12 23:41:58

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

You have to have a SSH server installed on the Android phone.
```bash
scp -r -P port user_name@192.168.1.105:/sdcard/DCIM . 
scp -r -P port user_name@192.168.1.105:/sdcard/DCIM/Camera .
scp -r -P port user_name@192.168.1.105:/sdcard/Download .
scp -r -P port user_name@192.168.1.105:/sdcard/Tencent/MicroMsg/WeChat .
scp -r -P port user_name@192.168.1.105:/sdcard/Tencent/MicroMsg/WeiXin .
```

`/sdcard/DCIM`
`/sdcard/Download`
`/sdcard/MicroMsg`

Notice that `rsync` does not work on an Android phone.