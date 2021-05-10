# -*- coding: utf-8 -*-
import requests
from readability import Document


def main(app):
    response = requests.get(app['args']['url'])
    doc = Document(response.text)

    print(doc.title())
    print(doc.summary())
