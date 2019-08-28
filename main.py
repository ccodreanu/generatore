import markdown
import re

from generatore.Content import Content

def get_content_metadata(file):
    content = ''
    with open(filename, 'r') as file_with_content:
        content = file_with_content.read()
        content2 = re.split(r'---', content, flags=re.MULTILINE)

    return content2[1:]

filename = 'content/posts/Running-Wireshark-on-remote-hosts.md'

# print(get_content_metadata(filename)[1])

# markdown.markdownFromFile(input=filename)
# print(markdown.markdown(get_content_metadata(filename)[1]))

c = Content(filename)

print(c.body)
print(c.metadata)