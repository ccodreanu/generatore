# Generatore - A static site generator

[![Actions Status](https://github.com/picofish/generatore/workflows/build/badge.svg)](https://github.com/picofish/generatore/actions)

This is a static website generator written in Python based on Markdown and Jinja2

Install with `pip3 install -r requirements.txt`, `make` and `make install`.

Usage:

```
usage: generatore [-h] [--build] [--listen] [--serve] [--create DIR]
                  [--post 'Post title']

optional arguments:
  -h, --help           show this help message and exit
  --build              build the site in the output directory
  --listen             auto-build the site inside the output directory
  --serve              generate content and start a webserver
  --create DIR         create a new site in DIR
  --post 'Post title'  create a new post with metadata
```
