# -*- coding: utf-8 -*-
"""Clipper application entry point."""
from . import article
from . import util


def main(app):
    """Application entry point."""
    html_raw, html_clean, meta_clipper = article.fetch(app['args']['url'])
    meta_goose, meta_newspaper = article.parse(app['args']['url'], html_raw)

    names = ('html_raw.html', 'meta_clipper.json', 'meta_goose.json', 'meta_newspaper.json')
    values = (html_raw, meta_clipper, meta_goose, meta_newspaper)

    attachments = [util.write_attach(app['work_dir'], name, value) for (name, value) in
                   zip(names, values)]

    title_block = app['work_dir'] / 'title_block.md'

    with title_block.open('w') as fd_out:
        fd_out.write(f"# {meta_goose['title']}")

    article.clip(
        html=html_clean,
        header=util.get_resource_path('article-header.yaml'),
        before_body=title_block,
        attachments=attachments,
        file_name=app['args']['file_name']
        )
