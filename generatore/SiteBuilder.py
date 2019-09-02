import os

from distutils.dir_util import copy_tree
from jinja2 import Environment, FileSystemLoader

from generatore.ArticleBuilder import ArticleBuilder
from generatore.ConfigManager import ConfigManager

class SiteBuilder:
    def __init__(self, dir=os.getcwd(), content_dir="content", output_dir="output"):
        self.dir = os.path.abspath(dir)

        self.config = ConfigManager(dir).read()

        print(self.config)

        self.content_dir = os.path.join(dir, content_dir)
        self.output_dir = os.path.join(dir, output_dir)

        self.posts_content_dir = os.path.join(self.content_dir, 'posts')
        self.pages_content_dir = os.path.join(self.content_dir, 'pages')

        self.posts_output_dir = os.path.join(self.output_dir, 'posts')
        self.pages_output_dir = os.path.join(self.output_dir, 'pages')

        self.static_output_dir = os.path.join(self.output_dir, 'static')

        self.__create_site_structure__()

    def build_site(self):
        self.pages = []
        self.pages = self.__generate_content__(self.pages_content_dir, self.pages_output_dir)
        self.pages.sort(key=lambda post: post.metadata['date'], reverse=True)

        self.posts = self.__generate_content__(self.posts_content_dir, self.posts_output_dir)
        
        # sort for sitemap
        self.posts.sort(key=lambda post: post.metadata['date'], reverse=True)
        
        [post.write(self.pages) for post in self.posts]
        [page.write(self.pages) for page in self.pages]

        self.__generate_index__()

        # Copy over static files
        copy_tree(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates', 'static'), self.static_output_dir)

    def __create_site_structure__(self):
        if not os.path.exists(self.posts_content_dir):
            os.makedirs(self.posts_content_dir)

        if not os.path.exists(self.pages_content_dir):
            os.makedirs(self.pages_content_dir)

        if not os.path.exists(self.posts_output_dir):
            os.makedirs(self.posts_output_dir)

        if not os.path.exists(self.pages_output_dir):
            os.makedirs(self.pages_output_dir)

    def __generate_content__(self, content_path, output_dir):
        contents = []
        for file in os.listdir(content_path):
            if file.endswith('.md'):
                path_to_post = os.path.join(content_path, file)
                content = ArticleBuilder(path_to_post, output_dir, self.config)
                contents.append(content)

        return contents

    def __generate_index__(self):
        file_loader = FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
        env = Environment(loader=file_loader)

        template = env.get_template('index.html')
        output = template.render(site_name=self.config['site_name'], google_analytics=self.config['google_analytics'], title='Home', posts=self.posts, pages=self.pages)

        with open(os.path.join(self.output_dir, 'index.html'), 'w') as writer:
            writer.write(output)