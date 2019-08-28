import re
import markdown

class Content:
    def __init__(self, filename):
        self.__filename = filename
        self.metadata = {}

        self.__parse_content()

    def __parse_content(self):
        with open(self.__filename, 'r') as file_with_content:
            content = file_with_content.read()
            parsed_content = re.split(r'---', content, flags=re.MULTILINE)
        
        metadata = parsed_content[1:2][0].split(sep='\n')[1:-1]
        self.body = markdown.markdown(parsed_content[2:][0])

        for m in metadata:
            self.metadata[m.split(sep=': ')[0]] = m.split(sep=': ')[1]
