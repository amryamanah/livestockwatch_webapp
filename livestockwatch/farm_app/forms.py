# -- coding: utf-8 --

__author__ = 'amryfitra'

from django import forms
from .models import Place, Stall

class NewStallFormWoPlace(forms.ModelForm):
    device_name = forms.CharField(max_length=20)

    class Meta:
        model = Stall
        exclude = ["place"]

class NewStallForm(forms.ModelForm):
    device_name = forms.CharField(max_length=20)

    class Meta:
        model = Stall
        fields = '__all__'
