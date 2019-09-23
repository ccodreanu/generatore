import re
import markdown2

from datetime import datetime

from generatore.Utils import slug_creator


class Content:

    def __init__(self, filename):
        self.__filename = filename

        self.__parse_content()

    def __parse_content(self):
        with open(self.__filename, 'r') as file_with_content:
            content = file_with_content.read()
            h = markdown2.markdown(
                content, extras=['metadata', 'fenced-code-blocks'])

        self.metadata = h.metadata
        self.body = h
        self.slug = slug_creator(self.metadata['title'])
        self.document_url = self.slug + '.html'

        try:
            self.metadata['date'] = datetime.strptime(self.metadata['date'],
                                                      '%Y-%m-%d %H:%M:%S')
        except KeyError:
            raise ValidationError(self.__filename + ': Date is missing.')

        try:
            self.metadata['tags'] = self.metadata['tags'].split(', ')
        except KeyError:
            pass


class ValidationError(Exception):

    def __init__(self, message):

        super().__init__(message)
