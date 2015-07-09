from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.model_util import ModelTimestamp
from farm_app.models import Stall

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


class BloodData1(ModelTimestamp):
    cattle = models.ForeignKey(Cattle)
    va = models.FloatField(_("Vitamin A (IU/dl)"), null=True)
    beta_carotene = models.FloatField(_("Beta carotene (ug/dl)"), null=True)
    ve = models.FloatField(_("Vitamin E (ug/dl)"), null=True)
    date_taken = models.DateField(_("Date taken"), null=True)

    class Meta:
        unique_together = ("cattle", "date_taken")

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.cattle, self.date_taken)


class BloodData2(ModelTimestamp):
    cattle = models.ForeignKey(Cattle)
    vc = models.FloatField(_("Vitamin C (IU/dl)"), null=True)
    date_taken = models.DateField(_("Date taken"), null=True)

    class Meta:
        unique_together = ("cattle", "date_taken")

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.cattle, self.date_taken)


class BodyData1(ModelTimestamp):
    cattle = models.ForeignKey(Cattle)

    weight = models.FloatField(_("Weight (kg)"), null=True)
    withers_height = models.FloatField(_("Withers height (cm)"), null=True)
    chest_circumference = models.FloatField(_("Chest circumference (cm)"), null=True)
    date_taken = models.DateField(_("Date taken"), null=True)

    class Meta:
        unique_together = ("cattle", "date_taken")

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.cattle, self.date_taken)


class BodyData2(ModelTimestamp):
    cattle = models.ForeignKey(Cattle)
    hip_height = models.FloatField(_("Hip height (cm)"), null=True)
    body_length = models.FloatField(_("Body length (cm)"), null=True)
    chest_depth = models.FloatField(_("Chest weight (cm)"), null=True)
    chest_width = models.FloatField(_("Chest width (cm)"), null=True)
    buttocks_length = models.FloatField(_("Buttocks length (cm)"), null=True)
    hip_width = models.FloatField(_("Hip width (cm)"), null=True)
    thurl_width = models.FloatField(_("Thurl width (cm)"), null=True)
    pin_bone_width = models.FloatField(_("Pin bone width (cm)"), null=True)
    date_taken = models.DateField(_("Date taken"), null=True)

    class Meta:
        unique_together = ("cattle", "date_taken")

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.cattle, self.date_taken)


class BodyTemp(ModelTimestamp):
    cattle = models.ForeignKey(Cattle)
    temp = models.FloatField(_("Temp (C)"), null=True)
    time_taken = models.DateTimeField(_("Time taken"), null=True)

    class Meta:
        unique_together = ("cattle", "time_taken")

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.cattle, self.time_taken)


class CoarseFeedComponent(ModelTimestamp):
    """
    dc = digestion coefficient
    mv = measurement value
    """
    identifier = models.CharField(_("Coarse feed identifier"), max_length=30, unique=True)
    crude_protein_mv = models.FloatField(_("Crude protein"), null=True)
    crude_protein_dc = models.FloatField(_("Crude protein digestion coefficient"), null=True)
    crude_fat_mv = models.FloatField(_("Crude fat"), null=True)
    crude_fat_dc = models.FloatField(_("Crude fat digestion coefficient"), null=True)
    nitrogen_free_extract_mv = models.FloatField(_("Nitrogen free extract"), null=True)
    nitrogen_free_extract_dc = models.FloatField(_("Nitrogen free extract digestion coefficient"), null=True)
    crude_fiber_mv = models.FloatField(_("Crude fiber"), null=True)
    crude_fiber_dc = models.FloatField(_("Crude fiber digestion coefficient"), null=True)
    total_digestible_nutrient = models.FloatField(_("Total digestible nutrient"), null=True)
    beta_carotene_content = models.FloatField(_("Beta carotene content"), null=True)

    def __str__(self):
        return "{}: {}".format(self.id, self.identifier)


class FeedData(ModelTimestamp):
    cattle = models.ForeignKey(Cattle)
    coarse_feed_component = models.ForeignKey(CoarseFeedComponent)

    coarse_feed_dosage = models.FloatField(_("Coarse feed dosage"), null=True)
    coarse_feed_residue = models.FloatField(_("Coarse feed residue"), null=True)
    concentrate_feed_dosage = models.FloatField(_("Concentrate feed dosage"), null=True)
    concentrate_feed_residue = models.FloatField(_("Concentrate feed residue"), null=True)
    vit_prep_concentrate_feed = models.FloatField(_("Concentrate feed vitamin preparation"), null=True)
    vit_prep_kyoto = models.FloatField(_("Vitamin preparation direct administration Kyoto"), null=True)
    vit_prep_hyogo = models.FloatField(_("Vitamin preparation direct administration Hyogo"), null=True)
    date_taken = models.DateField(_("Date taken"), null=True)

    class Meta:
        unique_together = ("cattle", "date_taken")

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.cattle, self.date_taken)


class RemarksData(ModelTimestamp):
    cattle = models.ForeignKey(Cattle)

    remarks = models.TextField(_("Remarks"))
    date_taken = models.DateField(_("Date taken"), null=True)

    class Meta:
        unique_together = ("cattle", "date_taken")

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.cattle, self.date_taken)


class QualityYieldData(ModelTimestamp):
    cattle = models.OneToOneField(Cattle, primary_key=True)

    rib_eye_area = models.FloatField(_("Rib eye area"), null=True)
    beef_flank_thickness = models.FloatField(_("Beef flank thickness"), null=True)
    # fat under the skin
    subcutaneous_fat_thickness = models.FloatField(_("Subcutaneous (under the skin) fat"), null=True)
    yield_ratio_std_val = models.FloatField(_("Yield ratio standard value"), null=True)
    bms = models.FloatField(_("Beef marbling standard"), null=True)
    carcass_weight = models.FloatField(_("Carcass weight"), null=True)

    def __str__(self):
        return "{}: {}".format(self.id, self.cattle)