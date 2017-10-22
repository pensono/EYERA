from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.related_articles import *
from app.extract_keywords import *
from app.deduplicate import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# Horrible name, please change!!
def get(request):
    highlight = request.GET.get('highlight', '')
    keywords = keywords_from_string(highlight)
    articles = get_related(keywords)
    for article in articles:
        keywords = keywords_from_article(article)

        for z in zip(keywords, article['paragraphs']):
            z[1]['keywords'] = z[0]  # Just think about it a little

    franken_article = frankenarticle(articles)
    return JsonResponse({"article": franken_article})

