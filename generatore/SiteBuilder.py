import os
from generatore.ArticleCreator import ArticleCreator

class SiteBuilder:
    def __init__(self, content_dir="content", output_dir="output"):
        self.content_dir = content_dir
        self.posts_output_dir = os.path.join(output_dir, 'posts/')
        self.pages_output_dir = os.path.join(output_dir, 'pages/')

        self.__create_site_structure__()

    def build_site(self):
        # build all posts first
        path_to_posts = os.path.join(os.getcwd(), self.content_dir, 'posts')
        path_to_pages = os.path.join(os.getcwd(), self.content_dir, 'pages')

        posts = []
        for file in os.listdir(path_to_posts):
            if file.endswith('.md'):
                path_to_post = os.path.join(path_to_posts, file)
                posts.append(ArticleCreator(path_to_post, self.posts_output_dir))

        # now pages
        pages = []
        for file in os.listdir(path_to_pages):
            if file.endswith('.md'):
                path_to_page = os.path.join(path_to_pages, file)
                pages.append(ArticleCreator(path_to_page, self.pages_output_dir))
        
        # sort for sitemap
        posts.sort(key=lambda post: post.article.metadata['date'], reverse=True)
        pages.sort(key=lambda post: post.article.metadata['date'], reverse=True)

    def __create_site_structure__(self):
        if not os.path.exists(self.posts_output_dir):
            os.makedirs(self.posts_output_dir)

        if not os.path.exists(self.pages_output_dir):
            os.makedirs(self.pages_output_dir)