import os
import json
import urllib
from urllib.parse import urlencode
from urllib.request import Request
from urllib.error import HTTPError
from readability import Document
from html2text import HTML2Text
from multiprocessing.dummy import Pool as ThreadPool

h2t = HTML2Text()
h2t.ignore_emphasis = True
h2t.ignore_images = True
h2t.ignore_links = True
h2t.ignore_tables = True
h2t.body_width = 0


def extract_file(filename):
    paragraphs = [paragraph for paragraph in open(filename + '.txt', 'r').readlines() if len(paragraph) > 0]

    documents = []
    for i in range(len(paragraphs)):
        documents.append({
            'language': 'en',
            'id': str(i),
            'text': paragraphs[i]})


def extract_article_content(url):
    request = urllib.request.Request(url)
    body = urllib.request.urlopen(request).read()

    doc = Document(body)
    article_html = doc.summary()
    article_text = h2t.handle(article_html).split("\n")

    return [line for line in article_text if len(line.strip()) > 0 and line.count(" ") > 5]  # Not blank and contains at least 6 words


def get_article(url):
    try:
        lines = extract_article_content(url)
        if len(lines) == 0:
            return None
        return {'url': url, 'paragraphs': [{'text': line} for line in lines]}
    except urllib.error.HTTPError as e:
        print("Error retrieving article from: " + url)
        return None  # Just chug right along...


def get_related(keywords):
    params = urllib.parse.urlencode({
        'q': " ".join(keywords),
        'mkt': 'en-us',
    })

    request = urllib.request.Request("https://api.cognitive.microsoft.com/bing/v7.0/news/search?" + params)
    request.add_header('Content-Type', 'application/json')
    request.add_header('Ocp-Apim-Subscription-Key', os.environ['SEARCH_API_KEY'])
    response = urllib.request.urlopen(request)
    data = json.loads(response.read())

    pool = ThreadPool(16)
    articles = pool.map(get_article, [article['url'] for article in data['value']])
    pool.close()
    pool.join()

    return [article for article in articles if article is not None]
