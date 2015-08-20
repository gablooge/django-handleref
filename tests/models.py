
from django.db import models
from django_handleref.models import HandleRefModel


class Org(HandleRefModel):
    name = models.CharField(max_length=255, unique=True)
    website = models.URLField(blank=True)
    notes = models.TextField(blank=True)

    class HandleRef:
        #delete_cascade = ["widget_set",]
        tag = 'org'

    def __unicode__(self):
        return self.name


class Widget(HandleRefModel):
    name = models.CharField(max_length=255, unique=True)

