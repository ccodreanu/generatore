---
title: Installing NodeJS on WSL
date: 2019-08-21 16:26:17
tags: devops
---
After installing your WSL, if you want to install NodeJS on the Ubuntu 18.04 from Windows Store just run:

```
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
```

This will add the 12.x NodeJS repository to your system. Installing Node is a matter of:

```
sudo apt install nodejs
```

That's it!