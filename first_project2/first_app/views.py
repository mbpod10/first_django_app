from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    html = "<em> Hello World </em>"
    return HttpResponse(html)
    # return JsonResponse('Hello World')


def hello(request):
    return HttpResponse('Whats going on')
