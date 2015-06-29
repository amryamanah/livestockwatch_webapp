# -- coding: utf-8 --

__author__ = 'amryfitra'

from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import Place, Stall, Cattle, NeckbandPattern

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'


class StallForm(forms.ModelForm):
    class Meta:
        model = Stall
        fields = '__all__'


class CattleForm(forms.ModelForm):
    class Meta:
        model = Cattle
        exclude = ["stall"]
        widgets = {
            'birthday': SelectDateWidget(),
            'fat_start_date': SelectDateWidget(),
            'fat_finish_date': SelectDateWidget()
        }


class NeckbandPatternForm(forms.ModelForm):
    class Meta:
        model = NeckbandPattern
        exclude = ["cattle"]
        widgets = {
            "start_date": SelectDateWidget(),
            "end_date": SelectDateWidget()
        }

