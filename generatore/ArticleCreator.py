import os

from jinja2 import Environment, FileSystemLoader

from generatore.Content import Content
from generatore.Utils import slug_creator

class ArticleCreator():
    def __init__(self, filename, destination):
        self.article = Content(filename)
        output_dir = destination

        file_loader = FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
        env = Environment(loader=file_loader)

        template = env.get_template('article.html')
        output = template.render(content=self.article)
        
        with open(output_dir + slug_creator(self.article.metadata['title']) + '.html', 'w') as writer:
            writer.write(output)
