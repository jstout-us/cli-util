import json

from newspaper import Article
import requests
import nltk

from pprint import pprint as pp

nltk.download('punkt')
# response = requests.get(app['args']['url'])
#     doc = Document(response.text)

URL='https://www.rawstory.com/tomi-lahren-nazi-barbie/'
# URL = 'https://www.alternet.org/2021/05/captiol-riot/'
article = Article(URL)
article.download()
# article.download(input_html=requests.get(URL).text)

article.parse()
article.nlp()

keys = ('source_url', 'url', 'title', 'top_img', 'imgs', 'movies', 'keywords', 'meta_keywords',
        'tags', 'authors', 'publish_date', 'summary', 'meta_description', 'canonical_link'
    )


values = [getattr(article, key) for key in keys ]

paper_meta = dict(zip(keys, values))
paper_meta['imgs'] = list(paper_meta['imgs'])
paper_meta['tags'] = list(paper_meta['tags'])
paper_meta['publish_date'] = paper_meta['publish_date'].isoformat()

for key, value in paper_meta.items():
    print(f"key: {key} type: {type(paper_meta[key])}")

json.dumps(paper_meta)

pp(paper_meta)
