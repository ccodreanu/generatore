---
title: Delete remote branches with Git
date: 2019-08-29 12:02:00
tags: code
---
When trying to implement some new feature, _most_ of the times I create a new branch. This usually results in a huge pile of old branches that might or might have not been synced to Github.

If you need to clean these branches out, the easiest way to do it is to delete them from Github through Git on the CLI.

Run this:

```
git push origin --delete stuff-merged-to-master
```

Note that the local branch will not get deleted. In order to delete the local branch you'll have to issue:

```
git branch -d stuff-merged-to-master
```

That's it!