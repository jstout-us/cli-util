from goose3 import Goose

URL='https://www.rawstory.com/tomi-lahren-nazi-barbie/'
URL='https://www.alternet.org/2021/05/captiol-riot/'
# goose = Goose()
article = Goose().extract(url=URL)

print(article.title)
print("\n==============================\n")
# 'Nazi Barbie' is trending on social media -- and everyone knows exactly who it's about

print(article.meta_description)
print("\n==============================\n")
# "Nazi Barbie" was trending Wednesday morning on Twitter, and everyone seemed to
# "know exactly who that was about.Fox Nation's Tomi Lahren complained about two
# "recent confrontations she purportedly had where a neighbor threw eggs at her
# "and a passerby slurred her as "Nazi Barbie," which she claimed wa...

print(article.canonical_link)
print("\n==============================\n")
# https://www.rawstory.com/tomi-lahren-nazi-barbie/

print(article.domain)
print("\n==============================\n")
# www.rawstory.com

print(article.tags)
print("\n==============================\n")
# []

print(article.opengraph)
print("\n==============================\n")
# {'type': 'article', 'url': 'https://www.rawstory.com/tomi-lahren-nazi-barbie/',
# {''site_name': 'Raw Story - Celebrating 17 Years of Independent Journalism',
# {''image':
# {''https://www.rawstory.com/media-library/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpbWFnZSI6Imh0dHBzOi8vYXNzZXRzLnJibC5tcy8yNDcwNDc2MS9vcmlnaW4ucG5nIiwiZXhwaXJlc19hdCI6MTY2NTM2NDA5OH0.5UThrWGeO5pYhIA-hzOi9XB7Flwo1xPxMmLEAYYosSo/image.png?width=1200&coordinates=0%2C41%2C0%2C41&height=600',
# {''image:width': '1200', 'image:height': '600', 'title': "'Nazi Barbie' is
# {'trending on social media -- and everyone knows exactly who it's about",
# {''description': '"Nazi Barbie" was trending Wednesday morning on Twitter, and
# {'everyone seemed to know exactly who that was about.Fox Nation\'s Tomi Lahren
# {'complained about two recent confrontations she purportedly had where a
# {'neighbor threw eggs at her and a passerby slurred her as "Nazi Barbie," which
# {'she claimed wa...', 'article:published_time': '2021-05-12T11:16:14+00:00',
# {''article:modified_time': '2021-05-12T15:24:12+00:00', 'article:author':
# {''https://www.facebook.com/20324257234'}

print(article.tweets)
print("\n==============================\n")
# [] Article does have tweets

print(article.movies)
print("\n==============================\n")
# []

print(article.links)
print("\n==============================\n")
# ['https://radio.foxnews.com/2021/05/10/tomi-lahren-a-girl-tried-to-throw-eggs-at-me-its-only-going-to-get-worse/']

print(article.authors)
print("\n==============================\n")
# [] Travis Gettys

print(article.final_url)
print("\n==============================\n")
# https://www.rawstory.com/tomi-lahren-nazi-barbie/

print(article.publish_date)
print("\n==============================\n")
# 2021-05-12T11:16:14+00:00

print(article.publish_datetime_utc)
print("\n==============================\n")
# 2021-05-12 11:16:14+00:00

print(article.infos)

"""
From https://www.alternet.org/2021/05/captiol-riot/

$ python3 test_goose.py
Damning timeline details DOD actions before and during the Capitol riot — and it raises more question than answers

==============================

Four months after a violent mob of far-right extremists attacked the U.S. Capitol Building in the hope of stopping Congress from certifying now-President Joe Biden's Electoral College victory, many Americans continue to ask: Why was this allowed to happen — and why weren't the extremists prevented f...

==============================

https://www.alternet.org/2021/05/captiol-riot/

==============================

www.alternet.org

==============================

['Religious right']

==============================

{'type': 'article', 'url': 'https://www.alternet.org/2021/05/captiol-riot/', 'site_name': 'Alternet.org', 'image': 'https://www.alternet.org/media-library/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpbWFnZSI6Imh0dHBzOi8vYXNzZXRzLnJibC5tcy8yNjM4NDI0Ni9vcmlnaW4uanBnIiwiZXhwaXJlc19hdCI6MTY0MTg3NjU2MX0.NSfydeEWgzBpInJSXDX-bpiiZOLGe54fIpCQ3GDbVPw/image.jpg?width=1200&coordinates=0%2C319%2C0%2C1&height=600', 'image:width': '1200', 'image:height': '600', 'title': 'Damning timeline details\xa0 DOD actions before and during the Capitol riot — and it raises more question than answers', 'description': "Four months after a violent mob of far-right extremists attacked the U.S. Capitol Building in the hope of stopping Congress from certifying now-President Joe Biden's Electoral College victory, many Americans continue to ask: Why was this allowed to happen — and why weren't the extremists prevented f...", 'article:published_time': '2021-05-12T15:22:47+00:00', 'article:modified_time': '2021-05-12T15:22:47+00:00'}

==============================

[]

==============================

[]

==============================

['https://www.justsecurity.org/76117/the-official-and-unofficial-timeline-of-defense-department-actions-on-january-6/', 'https://oversight.house.gov/legislation/hearings/the-capitol-insurrection-unexplained-delays-and-unanswered-questions', 'https://www.alternet.org/2021/03/as-reality-sets-in-qanon-shaman-other-capitol-riot-suspects-issue-apologies/', 'https://www.alternet.org/2021/03/parler-2651243411/', 'https://www.alternet.org/2021/04/capitol-riots/', 'https://www.usatoday.com/in-depth/news/politics/elections/2021/05/09/capitol-riot-conspiracy-charge-faces-31-suspects-including-proud-boys/7353740002/', 'https://www.businessinsider.com/capitol-riot-suspect-arrested-facebook-post-boasting-attendance-2021', 'https://www.nytimes.com/2021/04/13/us/politics/capitol-riot-police-report.html']

==============================

[]

==============================

https://www.alternet.org/2021/05/captiol-riot/

==============================

2021-05-12T15:22:47+00:00

==============================

2021-05-12 15:22:47+00:00

"""
