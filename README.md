(Note: All CLI may need need to start with `python3`)

# Virtual Environments

### List All Virtual Environments

```
conda info --envs
```

comes out to be:

```
base                  *  /Users/brock/opt/anaconda3

```

### Create Virtual Environment

```
 conda create --name MyDjangoEnv django
```

- View Envs Again
  conda info --envs

```
base                  *  /Users/brock/opt/anaconda3
MyDjangoEnv              /Users/brock/opt/anaconda3/envs/MyDjangoEnv
```

<b>Environment created!</b>

### Activate Environment

```
conda activate MyDjangoEnv
```

terminal should now look like:

```
(MyDjangoEnv) brock@Brocks-MBP first_django_app %
```

### Deactive Environment

- To deactive your environment:

```
conda deactivate
```

- Terminal looks like:

```
(base) brock@Brocks-MBP first_django_app %
```

### Delete Env

```
conda env remove --name MyDjangoEnv
```

# Create Django Project

```
django-admin startproject first_project
```

### Run Server

cd into `first_project`

```

python3 manage.py runserver
```

Result:

```
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
October 02, 2020 - 12:44:49
Django version 3.1.1, using settings 'django2_exercise.settings'
Starting development server at http://127.0.0.1:8000/
```

- Go to `http://127.0.0.1:8000/` to see if server is working

## Error

```
Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 13, in main
    raise ImportError(
ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
```

### Solution

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

```python
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

```python
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('Hello World')

```

## add this route to first_project2/urls.py

```python
from django.contrib import admin
from django.urls import path

#............................
from first_app import views
#^^^^^^^^^^^^^^^^^^^^^^^^^

urlpatterns = [
    path('', views.index, name='index'),
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

```python
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / 'templates'
print(TEMPLATE_DIR)
#==
#/Users/brock/Desktop/postGA/projects/python_projects/first_django_app/first_project2/templates
```

- Scroll Down to TEMPLATES in `first_project2/first_project2/settings.py` and add the new template variable TEMPLATE_DIR

```python
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

```python
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
  `python3 manage.py makemigrations first_app` <br  /> <br  />
  RETURN:

```
Migrations for 'first_app':
  first_app/migrations/0001_initial.py
    - Create model Topic
    - Create model Webpage
    - Create model AccessRecord
```

- Migrate One More Time
  `python3 manag.py migrate`

# Confirm It Worked With Python Shell

`python3 manage.py shell`

```python
from first_app.models import Topic
print(Topic.objects.all())
t = Topic(top_name="Social Network")
t.save()
```

RETURN:

```python
In [1]: print('hello')
hello

In [2]: from first_app.models import Topic

In [3]: print(Topic.objects.all())
<QuerySet []>

In [4]: t = Topic(top_name="Social Network")

In [5]: t.save()

In [6]: print(Topic.objects.all())
<QuerySet [<Topic: Social Network>]>

```

# Make Posts Via `first_app/admin.py`

- go to `first_app/admin.py`
- import models from `first_app`

```python
from django.contrib import admin
from first_app.models import AccessRecord, Topic, Webpage

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)

```

# Create Super User

`python3 manage.py createsuperuser`

- So no one can corrupt the database

```
Username (leave blank to use ''): training@gmail.com
Email address: training@gmail.com
Password: training123
Password (again): training123
```

`Superuser created successfully`

### Let's See If It Worked

`python3 manage.py runserver` <br  /> <br  />

- In brower go to `http://127.0.0.1:8000/admin`
- Enter Username and password

  ![Superuser Login](https://i.imgur.com/75qenrj.png "Successful Superuser Login")

<br  />
<b>SUCCESS!</b>

### Faker Populate Database

- Install Faker in virtual environment `MyDjangoEnv` <br  />
  `pip3 install faker`
- Create a seed data file at the top level of the project called `populate_first_app.py`

```python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project2.settings')
import django
django.setup()
#Fake Pop Script

import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker



fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):

        # get topic for entry
        top = add_topic()

        # Create fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Creaet new webpage
        webpg = Webpage.objects.get_or_create(
            topic=top, url=fake_url, name=fake_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(
            name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('population complete!')


```

<b>Prettier Will Mess Up The Import and Make It Impossible To Run The File</b>

run `python3 populate_first_app.py`

- <em>reload</em> after css update `shiftt + click refresh`
