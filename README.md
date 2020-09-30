## List All Environments

```
conda info --envs
```

comes out to be

```
base                  *  /Users/brock/opt/anaconda3
MyDjangoEnv              /Users/brock/opt/anaconda3/envs/MyDjangoEnv
```

## Create Virtual Environment

```
 conda create --name MyDjangoEnv django
 # python > 3.5
```

## Activate Environment

```
conda activate MyDjangoEnv
```

## Deactive Environment

```
conda deactivate MyDjangoEnv
```

## Remove Env

```
conda env remove --name MyDjangoEnv
```

# Django CLI

```
django-admin startproject first_project2
```

# Creat Project

```
django-admin startproject first_project
```

## Run Server

```
cd first_project
python manage.py runserver

# OR

python3 manage.py startapp <yourApp name>
```

# Error

```
Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 13, in main
    raise ImportError(
ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
```

## Solution

```
 python3 -m pip install django
 # then
 python3 manage.py runserver
 # then to url bar
 http://127.0.0.1:8000/
```

## Create DJANGO APP

```
# within first_project2
python3 manage.py startapp first_app
```

- first_project2 should be on the same level as first_app

# Import first_app to first_project/settings

scroll down to INSTALLED_APPS and import 'first_app'

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
==> 'first_app'
]
```

# django Views

in first_app/views.py add ===>

```
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('Hello World')

```

## add this route to first_project2/urls.py

```
from django.contrib import admin
from django.urls import path

............................
from first_app import views
^^^^^^^^^^^^^^^^^^^^^^^^^

urlpatterns = [
>>> path('', views.index, name='index'), <<<<
    path('admin/', admin.site.urls),
]


```
