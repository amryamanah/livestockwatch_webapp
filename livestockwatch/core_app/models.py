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
    device_name = models.CharField(_("Stall Device Name"), max_length=30, unique=True)
    name = models.CharField(_("Stall Name"), max_length=30, unique=True, blank=True, default="")
    remarks = models.CharField(_("remarks"), max_length=60, blank=True, default="")
    head_count = models.IntegerField(_("head_count"), null=True)

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.place, self.name)

    def save(self, *args, **kwargs):
        self.head_count = int(self.head_count)
        super(Stall, self).save(*args, **kwargs)

class NeckbandPattern(ModelTimestamp):
    pattern = models.CharField(_("pattern"), max_length=10, unique=True)

    def __str__(self):
        return "{}: {}".format(self.id, self.pattern)

class Cattle(ModelTimestamp):
    MALE = 'M'
    FEMALE = 'F'
    CASTRATED_MALE = 'CM'
    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (CASTRATED_MALE, 'Castrated Male'),
    )
    id_number = models.CharField(_("id_number"), max_length=12, unique=True)
    regist_num_father = models.CharField(_("regist_num_father"), max_length=12)
    regist_num_mother = models.CharField(_("regist_num_mother"), max_length=12)
    sex = models.CharField(_("sex"), max_length=2, choices=SEX_CHOICES, default=FEMALE)
    birthday = models.DateField(_("birthday"), null=True, blank=True)
    fat_start_date = models.DateField(_("fat_start_date"), null=True, blank=True)
    fat_finish_date = models.DateField(_("fat_finish_date"), null=True, blank=True)
    examination_number = models.CharField(_("Examination number"), max_length=10)
    stall = models.ForeignKey(Stall)

    class Meta:
        unique_together = ("id_number", "examination_number")

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.stall.name, self.id_number)


class CattleNeckband(ModelTimestamp):
    cattle = models.ForeignKey(Cattle)
    neckband_pattern = models.ForeignKey(NeckbandPattern)
    is_active = models.BooleanField(_("is_active"), default=False)
    start_date = models.DateField(_("start_date"), null=True, blank=True)
    end_date = models.DateField(_("end_date"), null=True, blank=True)

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.cattle.id_number, self.neckband_pattern.pattern)
