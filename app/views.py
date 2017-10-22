from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.related_articles import *
from app.extract_keywords import *
from app.deduplicate import *

from datetime import datetime

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# Horrible name, please change!!
def get(request):
    print(datetime.now())
    highlight = request.GET.get('highlight', '')
    if highlight == '':
        return JsonResponse({"error": "please provide a highlight url param"})

    keywords = keywords_from_string(highlight)

    print(datetime.now())
    articles = get_related(keywords)

    print(datetime.now())
    for article in articles:
        keywords = keywords_from_article(article)

        for z in zip(keywords, article['paragraphs']):
            z[1]['keywords'] = z[0]  # Just think about it a little
    print(datetime.now())
    franken_article = frankenarticle(articles)
    print(datetime.now())
    return JsonResponse({"article": franken_article})

