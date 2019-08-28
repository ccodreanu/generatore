import re
import markdown

from datetime import datetime

from generatore.Utils import slug_creator

class Content:
    def __init__(self, filename):
        self.__filename = filename

        self.__parse_content()

    def __parse_content(self):
        with open(self.__filename, 'r') as file_with_content:
            content = file_with_content.read()
            parsed_content = re.split(r'---', content, flags=re.MULTILINE)
        
        metadata = parsed_content[1:2][0].split(sep='\n')[1:-1]
        self.body = markdown.markdown(text=parsed_content[2:][0], output_format='html5')
        
        self.metadata = {}
        for m in metadata:
            self.metadata[m.split(sep=': ')[0]] = m.split(sep=': ')[1]

        self.slug = slug_creator(self.metadata['title'])
        self.document_url = self.slug + '.html'
        self.metadata['date'] = datetime.strptime(self.metadata['date'], '%Y-%m-%d %H:%M:%S')

        try:
            self.metadata['tags'] = self.metadata['tags'].split(', ')
        except KeyError:
            pass
