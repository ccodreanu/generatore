import os

from jinja2 import Environment, FileSystemLoader

from generatore.Content import Content
from generatore.Utils import slug_creator

class ArticleCreator():
    def __init__(self, filename):
        article = Content(filename)

        file_loader = FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
        env = Environment(loader=file_loader)

        template = env.get_template('article.html')
        output = template.render(content=article)
        
        with open('output/' + slug_creator(article.metadata['title']) + '.html', 'w') as writer:
            writer.write(output)
