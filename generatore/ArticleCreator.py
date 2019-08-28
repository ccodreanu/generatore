import os

from jinja2 import Environment, FileSystemLoader

from generatore.Content import Content

class ArticleCreator():
    def __init__(self, filename, destination, pages):
        self.article = Content(filename)
        output_dir = destination

        file_loader = FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
        env = Environment(loader=file_loader)

        template = env.get_template('article.html')
        output = template.render(title=self.article.metadata['title'], content=self.article, pages=pages)
        
        with open(os.path.join(output_dir, self.article.document_url), 'w') as writer:
            writer.write(output)
