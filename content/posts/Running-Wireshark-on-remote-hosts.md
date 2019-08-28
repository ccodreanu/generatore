---
title: Running Wireshark on remote hosts
date: 2019-02-28 10:39:36
tags: devops
---
You might need to run Wireshark on remote hosts and that's usually a pain to deal with. What I prefer to do, in order to also have the traffic displayed on my machine in real time is to run `tcpdump` remotely and stream its output to `stdout` over SSH and finally pipe that to my local installation of Wireshark.

Run this on your local machine:

```
ssh user@host "/usr/sbin/tcpdump -s0 -w -" | wireshark -k -i -
```

When Wireshark starts on your machine, you should select the interface named `-` and you should be able to see the hosts traffic.

Note that if you stop the capture, you'll have to restart the remote `tcpdump` process. That's pretty much it.