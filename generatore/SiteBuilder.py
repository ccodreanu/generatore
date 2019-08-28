import os
from generatore.ArticleCreator import ArticleCreator

class SiteBuilder:
    def __init__(self, content_dir="content", output_dir="output"):
        self.content_dir = content_dir
        self.posts_output_dir = os.path.join(output_dir, 'posts/')
        self.pages_output_dir = os.path.join(output_dir, 'pages/')

        self.__create_site_structure__()

    def build_site(self):
        md_posts_path = os.path.join(os.getcwd(), self.content_dir, 'posts')
        md_pages_path = os.path.join(os.getcwd(), self.content_dir, 'pages')

        self.posts = self.__generate_output__(md_posts_path)
        self.pages = self.__generate_output__(md_pages_path)
        
        # sort for sitemap
        self.posts.sort(key=lambda post: post.article.metadata['date'], reverse=True)
        self.pages.sort(key=lambda post: post.article.metadata['date'], reverse=True)

    def __create_site_structure__(self):
        if not os.path.exists(self.posts_output_dir):
            os.makedirs(self.posts_output_dir)

        if not os.path.exists(self.pages_output_dir):
            os.makedirs(self.pages_output_dir)

    def __generate_output__(self, content_path):
        contents = []
        for file in os.listdir(content_path):
            if file.endswith('.md'):
                path_to_post = os.path.join(content_path, file)
                contents.append(ArticleCreator(path_to_post, self.posts_output_dir))

        return contents
