from newspaper import Article
import requests
import nltk

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

print(article.authors)
print("\n==============================\n")

print(article.publish_date)
print("\n==============================\n")

print(article.top_image)
print("\n==============================\n")

print(article.movies)
print("\n==============================\n")

print(article.keywords)
print("\n==============================\n")

print(article.summary)
print("\n==============================\n")

"""
'https://www.alternet.org/2021/05/captiol-riot/'

['Alex Henderson']

==============================

2021-05-12 15:22:47+00:00

==============================

https://www.alternet.org/media-library/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpbWFnZSI6Imh0dHBzOi8vYXNzZXRzLnJibC5tcy8yNjM4NDI0Ni9vcmlnaW4uanBnIiwiZXhwaXJlc19hdCI6MTY0MTg3NjU2MX0.NSfydeEWgzBpInJSXDX-bpiiZOLGe54fIpCQ3GDbVPw/image.jpg?width=1200&coordinates=0%2C319%2C0%2C1&height=600

==============================

[]

==============================

['capitol', 'security', 'actions', 'raises', 'damning', 'brannen', 'answers', 'dc', 'department', 'dod', 'defense', 'timeline', 'question', 'riot', 'request', 'goodman', 'details', 'guard']

==============================

Just Security reporters Kate Brannen and Ryan Goodman, in an article published on May 11, offer a timeline of U.S. Department of Defense actions on and before January 6.
The Just Security timeline is based, in part, on the DoD timeline released on January 8.
According to the Just Security reporters, "During the phone call, U.S. Capitol Police Chief Steven Sund pleaded with senior Army leaders for help.
The timeline that Brannen and Goodman provide starts on December 31, 2020 and ends on January 7, 2021.
And on January 4, according to Brannen and Goodman, the Defense Department confirmed "with U.S. Capitol Police that there" was "no request for DoD support."

==============================

"""

"""
https://www.rawstory.com/tomi-lahren-nazi-barbie/

['Travis Gettys', 'David Edwards', 'Agence France-Presse', 'Brad Reed']

==============================

2021-05-12 11:16:14+00:00

==============================

https://www.rawstory.com/media-library/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpbWFnZSI6Imh0dHBzOi8vYXNzZXRzLnJibC5tcy8yNDcwNDc2MS9vcmlnaW4ucG5nIiwiZXhwaXJlc19hdCI6MTY2NTM2NDA5OH0.5UThrWGeO5pYhIA-hzOi9XB7Flwo1xPxMmLEAYYosSo/image.png?width=1200&coordinates=0%2C41%2C0%2C41&height=600

==============================

[]

==============================

['knows', 'exactly', 'theyre', 'nazi', 'social', 'lahren', 'eggs', 'throw', 'barbie', 'trending', 'telling', 'media']

==============================

"Nazi Barbie" was trending Wednesday morning on Twitter, and everyone seemed to know exactly who that was about.
"I had a girl from the sixth floor of an apartment complex try to throw eggs at me.
But yes, she tried to throw eggs at me.
Yesterday, I had a grown man with a cigarette in hand and a mask on his face telling me I'm 'Nazi Barbie' and telling me that I dance on the graves of Native Americans.
Her anecdote was widely shared on social media, and the insult entered Twitter's trending topics -- surprising no one who looked into the reference.

==============================

"""
