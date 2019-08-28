import os

from distutils.dir_util import copy_tree
from jinja2 import Environment, FileSystemLoader

from generatore.ArticleCreator import ArticleCreator

class SiteBuilder:
    def __init__(self, content_dir="content", output_dir="output"):
        self.content_dir = os.path.join(os.getcwd(), content_dir)
        self.output_dir = os.path.join(os.getcwd(), output_dir)
        self.posts_output_dir = os.path.join(self.output_dir, 'posts')
        self.pages_output_dir = os.path.join(output_dir, 'pages')

        self.output_static_dir = os.path.join(self.output_dir, 'static')

        self.__create_site_structure__()

    def build_site(self):
        posts_content_path = os.path.join(os.getcwd(), self.content_dir, 'posts')
        pages_content_path = os.path.join(os.getcwd(), self.content_dir, 'pages')

        self.pages = []
        self.pages = self.__generate_content__(pages_content_path, self.pages_output_dir)
        self.pages.sort(key=lambda post: post.metadata['date'], reverse=True)

        self.posts = self.__generate_content__(posts_content_path, self.posts_output_dir)
        
        # sort for sitemap
        self.posts.sort(key=lambda post: post.metadata['date'], reverse=True)

        self.__generate_index__()

        copy_tree(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates', 'static'), self.output_static_dir)

    def __create_site_structure__(self):
        if not os.path.exists(self.posts_output_dir):
            os.makedirs(self.posts_output_dir)

        if not os.path.exists(self.pages_output_dir):
            os.makedirs(self.pages_output_dir)

    def __generate_content__(self, content_path, output_dir):
        contents = []
        for file in os.listdir(content_path):
            if file.endswith('.md'):
                path_to_post = os.path.join(content_path, file)
                contents.append(ArticleCreator(path_to_post, output_dir, self.pages).article)

        return contents

    def __generate_index__(self):
        file_loader = FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
        env = Environment(loader=file_loader)

        template = env.get_template('index.html')
        output = template.render(title='Catalin Codreanu', posts=self.posts, pages=self.pages)

        with open(os.path.join(self.output_dir, 'index.html'), 'w') as writer:
            writer.write(output)