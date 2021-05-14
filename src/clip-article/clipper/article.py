# -*- coding: utf-8 -*-

import subprocess
import tempfile

from datetime import datetime
from datetime import timezone
from pathlib import Path

import goose3
import nanoid
import requests
import readability
import nltk
import newspaper


def _get_paper_meta(url, html_raw):
    nltk.download('punkt')

    article = newspaper.Article(url)
    article.download(input_html=html_raw)
    article.parse()
    article.nlp()

    keys = ('source_url', 'url', 'title', 'top_img', 'imgs', 'movies', 'keywords',
            'meta_keywords', 'tags', 'authors', 'publish_date', 'summary', 'meta_description',
            'canonical_link'
            )
    values = [getattr(article, key) for key in keys ]

    retval = dict(zip(keys, values))
    retval['imgs'] = list(retval['imgs'])
    retval['tags'] = list(retval['tags'])
    retval['publish_date'] = retval['publish_date'].isoformat()

    return retval


def _html_to_markdown(html):
    args = ['/usr/bin/pandoc', '-f', 'html', '-t', 'markdown']
    result = subprocess.run(args, input=html.encode(), stdout=subprocess.PIPE,
         stderr=subprocess.PIPE)

    return result.stdout


def _html_to_pdf(header, markdown, before_body, file_name):

    args = ['/usr/bin/pandoc', header.as_posix(), before_body.as_posix(), markdown.as_posix(),
            '-t', 'latex', '-o', file_name.as_posix()]
    subprocess.run(args)


def clip(html, header, before_body, attachments, file_name):

     with tempfile.TemporaryDirectory() as work_dir:
        tmp_pdf = Path(work_dir) / 'tmp_pdf.pdf'
        markdown = Path(work_dir) / 'article.md'

        with markdown.open('wb') as fd_out:
            fd_out.write(_html_to_markdown(html))

        _html_to_pdf(header, markdown, before_body, tmp_pdf)

        import shutil
        shutil.copyfile(tmp_pdf.as_posix(), file_name)


def fetch(url):
    html_raw = requests.get(url).text
    html_clean = html_clean = readability.Document(html_raw).summary()

    clip_meta = {
        'clip_type': 'article',
        'clip_url': url,
        'clip_id': nanoid.generate(size=12),
        'clip_ts': datetime.now(timezone.utc).isoformat(),
        }

    return (html_raw, html_clean, clip_meta)


def parse(url, html_raw):
    meta_goose = goose3.Goose().extract(raw_html=html_raw).infos
    meta_paper = _get_paper_meta(url, html_raw)

    return (meta_goose, meta_paper)
