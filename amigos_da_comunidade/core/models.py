import re
import uuid
from django.db import models
from django.urls import reverse
from django.core import validators
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Location(models.Model):

    name = models.CharField('Nome', max_length=100, blank=False)
    description = models.CharField('Descrição', max_length=100, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:location_list')

    class Meta:
        verbose_name = 'Localização'
        verbose_name_plural = 'Localizações'
        ordering = ['name']
