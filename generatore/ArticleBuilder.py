import os

from datetime import datetime

from jinja2 import Environment, FileSystemLoader

from generatore.Content import Content
from generatore.Utils import slug_creator


class ArticleBuilder(Content):
    def __init__(self, filename, destination, config):
        super().__init__(filename)

        self.config = config

        self.destination = destination

    def write(self, pages):
        output_dir = self.destination

        file_loader = FileSystemLoader(os.path.join(os.path.dirname(
                        os.path.abspath(__file__)), 'templates'))
        env = Environment(loader=file_loader)

        template = env.get_template('article.html')
        o = template.render(config=self.config,
                            title=self.metadata['title'],
                            date=self.metadata['date'],
                            content=self.body,
                            pages=pages)

        with open(os.path.join(output_dir, self.document_url), 'w') as writer:
            writer.write(o)

    @staticmethod
    def new_skeleton(title):
        with open(os.path.join(
                os.getcwd(),
                'content',
                'posts',
                slug_creator(title) + '.md'), 'w+') as writer:
            writer.write('---\ntitle: {}\ndate: {}\n---\n'.format(
                    title,
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
