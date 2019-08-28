from generatore.SiteBuilder import SiteBuilder

filename = 'content/posts/Running-Wireshark-on-remote-hosts.md'

# c = Content(filename)

# print(c.body)
# print(c.metadata['title'])

# file_loader = FileSystemLoader('template')
# env = Environment(loader=file_loader)

# template = env.get_template('article.html')
# output = template.render(content=c)
# print(output)

# g = ArticleCreator(filename)

s = SiteBuilder()

s.build_site()