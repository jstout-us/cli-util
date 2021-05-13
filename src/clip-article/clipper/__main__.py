# -*- coding: utf-8 -*-
import json
import os
import shutil
import tempfile

from datetime import datetime
from datetime import timezone
from io import StringIO
from string import Template
from subprocess import PIPE
from subprocess import Popen

import nanoid
import nltk
import requests

from goose3 import Goose
from newspaper import Article
from PyPDF4.pdf import PdfFileReader
from PyPDF4.pdf import PdfFileWriter
from PyPDF4.generic import ArrayObject
from PyPDF4.generic import DecodedStreamObject
from PyPDF4.generic import DictionaryObject
from PyPDF4.generic import NameObject
from PyPDF4.generic import createStringObject

from readability import Document

pdf_header = Template("""
fontsize: 12pt
geometry: margin=0.8in
title-meta: $title
""")


class PatchedPdfFileWriter(PdfFileWriter):
    """Include add multiple attachments method from head"""

    def attachFiles(self, files, cut_paths=True):
        """
        Embed multiple files inside the PDF.
        Similar to addAttachment but receives a file path or a list of file paths.
        Allows attaching more than one file.
        :param files: Single file path (string) or multiple file paths (list of strings).
        :param cut_paths: Display file name only in PDF if True,
                        else display full parameter string or list entry.
        """
        if not isinstance(files, list):
            files = [files]
        files_array = ArrayObject()

        for file in files:
            fname = file
            if cut_paths:
                fname = os.path.basename(fname)
            fdata = open(file, "rb").read()

            # The entry for the file
            file_entry = DecodedStreamObject()
            file_entry.setData(fdata)
            file_entry.update({NameObject("/Type"): NameObject("/EmbeddedFile")})

            # The Filespec entry
            efEntry = DictionaryObject()
            efEntry.update({NameObject("/F"): file_entry})

            filespec = DictionaryObject()
            filespec.update(
                {
                    NameObject("/Type"): NameObject("/Filespec"),
                    NameObject("/F"): createStringObject(fname),
                    NameObject("/EF"): efEntry,
                }
            )

            files_array.extend([createStringObject(fname), filespec])

        # The entry for the root
        embeddedFilesNamesDictionary = DictionaryObject()
        embeddedFilesNamesDictionary.update({NameObject("/Names"): files_array})

        embeddedFilesDictionary = DictionaryObject()
        embeddedFilesDictionary.update(
            {NameObject("/EmbeddedFiles"): embeddedFilesNamesDictionary}
        )

        # Update the root
        self._root_object.update({NameObject("/Names"): embeddedFilesDictionary})


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
        PDF_HEADER = work_dir + '/' + 'header.yaml'

        html_raw = requests.get(app['args']['url']).text
        html_clean = Document(html_raw).summary()

        meta_clip = _get_clipper_meta()
        meta_goose = Goose().extract(raw_html=html_raw).infos
        meta_paper = _get_paper_meta(app['args']['url'], html_raw)


        with open(PDF_HEADER, 'w') as fd_out:
            fd_out.write(pdf_header.substitute(title=meta_goose['title']))

        opts = ['/usr/bin/pandoc', '--metadata-file', PDF_HEADER, '-f', 'html', '-t', 'latex', '-o', TMP_PDF]

        proc = Popen(opts, stdin=PIPE)
        out, errs = proc.communicate(input=html_clean.encode())
        proc.wait()

        attach_names = ['meta_clip.json', 'meta_goose.json', 'meta_paper.json', 'raw.html']
        attach_paths = [work_dir + '/' + x for x in attach_names]

        for data, path in zip([meta_clip, meta_goose, meta_paper, html_raw], attach_paths):
            with open(path, 'w') as fd_out:
                if type(data) is dict:
                    json.dump(data, fd_out, indent=4, sort_keys=True)

                else:
                    fd_out.write(data)

        with open(TMP_PDF, 'rb') as pdf_in:
            reader = PdfFileReader(pdf_in)
            writer = PatchedPdfFileWriter()

            writer.appendPagesFromReader(reader)
            writer.attachFiles(attach_paths)

            with open(app['args']['file_name'], 'wb') as pdf_out:
                writer.write(pdf_out)
