from factory.django import DjangoModelFactory
from .models import Entry


class EntryFactory(DjangoModelFactory):
    class Meta:
        model = Entry

    site_name = 'google'
    site_url = 'https://www.google.com/login/'
    login = 'admin'
    password = 'test12345'
