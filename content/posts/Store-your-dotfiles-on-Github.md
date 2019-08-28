---
title: Store your dotfiles on Github
date: 2019-08-21 16:37:01
tags: devops
---
Moving to a new system is almost always painful to deal with. From time to time, when I have to reinstall my system, I end up googling for this HN [discussion](https://news.ycombinator.com/item?id=11070797).

So what I do, is saving my dotfiles from my home directory on a Github repository. This works great if you use the detached `.git` directory. Run the following:

Run `git init --bare $HOME/.myconf` to create your empty repository.
Add an alias to your `.profile` configuration:
```
alias config='/usr/bin/git --git-dir=$HOME/.myconf/ --work-tree=$HOME'
```

Finally, run: `config config status.showUntrackedFiles no` so you don't see all of your files in the working directory as untracked.

Running a `config status` will show you what dotfiles have been modified and are ready to be commited. Adding files to your git repository is done with `config add ~/path/to/file`, `config commit` and `config push`.

Restoring the files from Github is a matter of cloning and manually moving your files into place.
So you run:
```
git clone --separate-git-dir=$HOME/.myconf /path/to/repo $HOME/myconf-tmp
```
And then copy or move the files from `~/myconf-tmp` to `.vimrc`, `.gitconfig` and so on.

Done!