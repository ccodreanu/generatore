import sys
import http.server
import socketserver
import os
import datetime

from generatore.SiteBuilder import SiteBuilder
from generatore.Utils import slug_creator

def usage():
    print('usage: {} <command>\n'.format(sys.argv[0]))
    print('Generatore creates static websites.\n')
    print('Available commands:')
    print('\t{:10}\t{}'.format('build', 'build the site inside the output directory'))
    print('\t{:10}\t{}'.format('serve', 'generate content and start a webserver'))
    print('\t{:10}\t{}'.format('new "..."', 'create a new post with metadata'))

site = SiteBuilder()

if (len(sys.argv) > 1):
    if (sys.argv[1] == 'new'):
        try:
            title = sys.argv[2]

            with open(os.path.join(os.path.dirname(__file__), 'content', 'posts', slug_creator(title) + '.md'), 'w') as writer:
                writer.write('---\ntitle: {}\ndate: {}\n---\n'.format(title, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        except IndexError:
            usage()
    elif (sys.argv[1] == 'build'):
        site.build_site()
    elif (sys.argv[1] == 'serve'):
        site.build_site()

        web_dir = os.path.join(os.path.dirname(__file__), 'output')
        os.chdir(web_dir)
        with socketserver.TCPServer(("", 9999), http.server.SimpleHTTPRequestHandler) as httpd:
            print('Serving at http://localhost:9999')
            httpd.serve_forever()

    else:
        usage()
else:
    usage()
