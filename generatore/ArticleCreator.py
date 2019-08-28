import os

from jinja2 import Environment, FileSystemLoader

from generatore.Content import Content

class ArticleCreator(Content):
    def __init__(self, filename, destination):
        super().__init__(filename)

        self.destination = destination

    def write(self, pages):
        output_dir = self.destination

        file_loader = FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
        env = Environment(loader=file_loader)

        template = env.get_template('article.html')
        output = template.render(title=self.metadata['title'], date=self.metadata['date'], content=self.body, pages=pages)
        
        with open(os.path.join(output_dir, self.document_url), 'w') as writer:
            writer.write(output)
