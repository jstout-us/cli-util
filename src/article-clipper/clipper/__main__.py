# -*- coding: utf-8 -*-
import os
import shutil
import tempfile

from datetime import datetime
from datetime import timezone
from subprocess import Popen
from subprocess import PIPE

import nanoid
import nltk
import requests

from goose3 import Goose
from newspaper import Article
from readability import Document


def _get_clipper_meta():
    retval = {
        'clip_type': 'article',
        'clip_id': nanoid.generate(size=12),
        'clip_ts': datetime.now(timezone.utc).isoformat(),
        'clip_updated_ts': datetime.now(timezone.utc).isoformat()
        }

    return retval


def _get_paper_meta(url, html_raw):
    nltk.download('punkt')

    article = Article(url)
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


def main(app):


    with tempfile.TemporaryDirectory() as work_dir:
        TMP_PDF = work_dir + '/' + 'temp.pdf'

        html_raw = requests.get(app['args']['url']).text
        html_clean = Document(html_raw).summary()

        meta_clip = _get_clipper_meta()
        # meta_goose = Goose().extract(raw_html=html_raw).infos
        # meta_paper = _get_paper_meta(app['args']['url'], html_raw)

        opts = ['/usr/bin/pandoc', '-f', 'html', '-t', 'latex', '-o', TMP_PDF]
        proc = Popen(opts, stdin=PIPE)
        out, errs = proc.communicate(input=html_clean.encode())
        proc.wait()

        shutil.copyfile(TMP_PDF, app['args']['file_name'])
