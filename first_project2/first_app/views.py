from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from . import forms
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

def home(request):
    return render(request, 'first_app/home.html')

# def form(request):
#     return render(request, 'first_app/form_page.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])


    return render(request, 'first_app/form_page.html', {'form': form})