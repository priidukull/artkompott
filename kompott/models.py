from django.db import models


class Artist(models.Model):
    prefix = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    location = models.CharField(max_length=256)