from django.db import models


class Entry(models.Model):
    site_name = models.CharField(max_length=80)
    site_url = models.CharField(max_length=150)
    login = models.CharField(max_length=40)
    password = models.CharField(max_length=128)
