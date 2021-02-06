Status: published
Date: 2021-01-10 10:24:23
Author: Ben Chuanlong Du
Slug: linux-network-tools
Title: Linux Network Tools
Category: Software
Tags: Software, Linux, network, tool, download, VPN

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Monitor Network
[WireShark](https://www.wireshark.org/)
[iStatMenus](https://bjango.com/mac/istatmenus/)
tcpdump


[9 Best Bandwidth Monitor and Network Usage Monitoring Tools](https://www.dnsstuff.com/bandwidth-monitor)

[Best Bandwidth Monitoring Software for Tracking Network Traffic Usage](https://www.netadmintools.com/bandwidth-monitor/)


## Network Admin  

1. [arp-scan](http://www.legendu.net/misc/blog/tips-on-arp-scan)
2. ping
3. netstat
4. proxychains
5. sshuttle
4. ip addr

        ip addr show dev eth0
        ip addr show dev eth0 | grep -i --color=auto inet | cut -d / -f 1 | cut -d ' ' -f 6

5. nslookup

        nslookup ip_address


## Remote Tools

1. OpenSSH, keychain (keyring for OpenSSH)
0. Teamviewer
5. NoMachine, FreeNX
2. VNC
3. SSHFS
4. Remmina
6. YuuGuu (Web Conference)
7. LogMeIn (Windows and Mac only)

## VPN

1. [WireGuard](https://www.wireguard.com/) is a better alternative to OpenVPN.
0. ExpressVPN
1. PrivateInternetAccess
2. LogMeIn Hamachi


## Anonymous Tools
1. VPN
2. Proxy
3. Anomos
4. Tor
5. proxychains 

## [Downloading Tools](http://www.legendu.net/misc/blog/downloading-tools/)
