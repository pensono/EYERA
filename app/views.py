from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.related_articles import *
from app.extract_keywords import *
from app.deduplicate import *
from django.views.decorators.csrf import csrf_exempt
from app.extract_polarization import *
from app.SourceDatabase import *

# Create your views here.
@csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# Horrible name, please change!!
@csrf_exempt
def get(request):
    if request.method == 'GET':
        highlight = request.GET.get('highlight', '')
    elif request.method == 'POST':
        highlight = request.POST.get('highlight', '')

    if highlight == '':
        return JsonResponse({"error": "Please provide a highlight url param"})

    keywords = keywords_from_string(highlight)

    articles = get_related(keywords)

    for article in articles:
        keywords = keywords_from_article(article)

        for z in zip(keywords, article['paragraphs']):
            z[1]['keywords'] = z[0]  # Just think about it a little

    reccomended_articles = articles[:2]

    franken_article = frankenarticle(articles)
    return JsonResponse({"article": franken_article, 'recommended': reccomended_articles})

