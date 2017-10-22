from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.related_articles import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# Horrible name, please change!!
def get(request):
    return JsonResponse({"result":get_related(["obama", "muslim"])})
    # return JsonResponse({'foo': 'bar'})

