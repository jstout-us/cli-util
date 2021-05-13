# -*- coding: utf-8 -*-

from . import article
from . import util


def main(app):

    html_raw, html_clean, meta_clipper = article.fetch(app['args']['url'])
    meta_goose, meta_newspaper = article.parse(app['args']['url'], html_raw)

    names = ('html_raw.html', 'meta_clipper.json', 'meta_goose.json', 'meta_newspaper.json')
    values = (html_raw, meta_clipper, meta_goose, meta_newspaper)

    attachments=[util.write_attach(app['work_dir'], name, value) for (name, value) in
        zip(names, values)]

    article.clip(
        html=html_clean,
        header=util.get_resource_path('article-header.yaml'),
        attachments=attachments,
        file_name=app['args']['file_name']
        )
