import markdown
import re

from generatore.Content import Content

filename = 'content/posts/Running-Wireshark-on-remote-hosts.md'

c = Content(filename)

print(c.body)
print(c.metadata)