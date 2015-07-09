from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.model_util import ModelTimestamp


class Place(ModelTimestamp):
    name = models.CharField(_("Place Name"), max_length=30, unique=True)
    address = models.TextField(_("Place Address"), max_length=300)

    def __str__(self):
        return "{}: {}".format(self.id, self.name)


class Stall(ModelTimestamp):
    place = models.ForeignKey(Place)
    name = models.CharField(_("Stall Name"), max_length=30, unique=True, blank=True, default="")
    remarks = models.CharField(_("Remarks"), max_length=60, blank=True, default="")
    head_count = models.IntegerField(_("Head count"), null=True)

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.place, self.name)

    def save(self, *args, **kwargs):
        self.head_count = int(self.head_count)
        super(Stall, self).save(*args, **kwargs)