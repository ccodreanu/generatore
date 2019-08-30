# Generatore

This is a static website generator written in Python based on Markdown and Jinja2

Install with `pip3 install -r requirements.txt`, `make` and `pip3 install` on the `whl` that was generated.

Usage:

```
usage: generatore <command>

Generatore creates static websites.

Available commands:
        create DIR      create a new site
        post "..."      create a new post with metadata
        build           build the site inside the output directory
        listen          auto-build the site inside the output directory
        serve           generate content and start a webserver
```