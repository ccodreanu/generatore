import sys
import http.server
import socketserver
import os

from generatore.SiteBuilder import SiteBuilder

def usage():
    print('usage: {} <command>\n'.format(sys.argv[0]))
    print('Generatore creates static websites.\n')
    print('Available commands:')
    print('{:>10}\t{}'.format('build', 'build the site inside the output directory'))
    print('{:>10}\t{}'.format('serve', 'generate content and start a webserver'))

site = SiteBuilder()

if (len(sys.argv) > 1):
    if (sys.argv[1] == 'build'):
        site.build_site()
    elif (sys.argv[1] == 'serve'):
        site.build_site()

        web_dir = os.path.join(os.path.dirname(__file__), 'output')
        os.chdir(web_dir)
        with socketserver.TCPServer(("", 9999), http.server.SimpleHTTPRequestHandler) as httpd:
            print("serving at port", 9999)
            httpd.serve_forever()
    else:
        usage()
else:
    usage()
