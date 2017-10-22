from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.related_articles import *
from app.extract_keywords import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# Horrible name, please change!!
def get(request):
    highlight = request.GET.get('highlight', '')
    keywords = keywords_from_string(highlight)
    articles = get_related(keywords)
    for article in articles:
        article['keywords'] = keywords_from_article(article['text'])
    return JsonResponse({"result": articles})

