# -- coding: utf-8 --
from django.db import models
from django.utils.translation import ugettext_lazy as _
__author__ = 'amryfitra'

class ModelTimestamp(models.Model):
    date_created = models.DateTimeField(_("date_created"), auto_now_add=True)
    date_modified = models.DateTimeField(_("date_modified"), auto_now=True)

    class Meta:
        abstract = True