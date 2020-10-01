import django
from faker import Faker
from first_app.models import AccessRecord, Webpage, Topic
import random
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project2.settings')
django.setup()
# Fake Pop Script
###############################


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
