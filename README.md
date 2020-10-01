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

# Create Project

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

## Running Setting

cd into `first_project2/first_project2`
run `python3 settings.py`
add below `BASE_DIR = Path(__file__).resolve().parent.parent`

```
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
#this gets full file path of project
==
/Users/brock/Desktop/postGA/projects/python_projects/first_django_app/first_project2
```

- Create a new folder called `templates` in base of first_project2
- Go back to `first_project2/first_project2/settings.py` and set a new variable that is the path to templates

```
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / 'templates'
print(TEMPLATE_DIR)
==
/Users/brock/Desktop/postGA/projects/python_projects/first_django_app/first_project2/templates
```

- Scroll Down to TEMPLATES in `first_project2/first_project2/settings.py` and add the new template variable TEMPLATE_DIR

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### Creat API

cd into `first_app/models.py`

create models:

```
from django.db import models

# Create your models here.


class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

```

- If error `no value for argument 'on_delete' in constructor call` put `on_delete=models.CASCADE` in foreign key

# Migrate Models

- while in `first_project2` folder command:
  `python3 manage.py migrate`
- Register Application
  `python3 manage.py makemigrations first_app`
  RETURN:

```
Migrations for 'first_app':
  first_app/migrations/0001_initial.py
    - Create model Topic
    - Create model Webpage
    - Create model AccessRecord
```
