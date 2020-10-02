from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
# Create your views here.


def index(request):
    # html = "<em> Hello World </em>"
    # return HttpResponse(html)
    # return JsonResponse('Hello World')
    # my_dictionary = {'insert_me': 'Hello, I am from first_app/index.html'}
    # return render(request, 'first_app/index.html', context=my_dictionary)

    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)


def hello(request):
    return HttpResponse('Whats going on')
