UUID: d8064194-3125-4c54-a2ef-a55e5cff25a5
Status: published
Date: 2015-12-06 09:09:35
Author: Ben Chuanlong Du
Slug: copy-pictures-in-android-to-computer
Title: Copy Pictures in Android to Computer
Category: OS
Tags: Linux, scp, rsync, pictures, image, photo, media, Android

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
