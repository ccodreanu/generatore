# Generatore

This is a static website generator written in Python based on Markdown and Jinja2

Install with `pip3 install -r requirements.txt`.

Usage:

```
usage: main.py <command>

Generatore creates static websites.

Available commands:
        build           build the site inside the output directory
        listen          auto-build the site inside the output directory
        serve           generate content and start a webserver
        post "..."       create a new post with metadata
```