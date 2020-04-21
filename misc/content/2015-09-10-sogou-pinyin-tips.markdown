UUID: a3dd9255-1a1c-4089-85d7-cd48e2e90fab
Status: published
Date: 2017-10-22 10:09:59
Author: Ben Chuanlong Du
Slug: sogou-pinyin-tips
Title: Sogou Pinyin Tips
Category: Software
Tags: software, tips, sogou, pinyin, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Settings

0. 常用 -> 隐藏状态栏
1. use half width punctuation
2. 按键 -> 切换英文状态时，保留输入框中已存在的字符并上屏
3. 细胞词库 -> uncheck 启用细胞词库自动跟新 to avoid notification of auto updating of sogou pinyin.
Currently there is no way to disable the notification.
you can close auto update to avoid distraction


4. it seems that you cannot turn off sogou pinyin on Linux Mint? ctrl + space does not work ...
you can use the command kill of course ...


## Issues

1. candidate window does not show up, might due to missing driver

2. sometimes fail to start, 
you can manually run 

        fcitx -d 

if the input method application doesn't start correctly

3. fcitx sogou拼音输入法 导致fcitx无法显示退出按钮 目前唯一的解决办法是隐藏搜狗拼音输入法的状态栏　

4. web WeChat: if sogou pinyin does not wok, just refresh web wechat, this can fix the issue usually

5. 搜狗拼音 it take a while after booting for sogou to work ... not sure how to speed it up or ...
sogou is really slow to boot
sogou related process: sogou-*

