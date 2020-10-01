from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # html = "<em> Hello World </em>"
    # return HttpResponse(html)
    # return JsonResponse('Hello World')
    my_dictionary = {'insert_me': 'Hello, I am from first_app/index.html'}
    return render(request, 'first_app/index.html', context=my_dictionary)


def hello(request):
    return HttpResponse('Whats going on')
