# -- coding: utf-8 --

__author__ = 'amryfitra'


from django import forms
from multiupload.fields import MultiFileField
from cattle_app.models import Cattle
from .models import ImageAnalysisSession, ImageAnalysisParameter, CaptureSession


class ImageAnalysisSessionForm(forms.ModelForm):
    class Meta:
        model = ImageAnalysisSession
        exclude = ["analysis_state"]


class ImageAnalysisParameterForm(forms.ModelForm):
    class Meta:
        model = ImageAnalysisParameter
        exclude = ["analysis_session"]


class RawImageUploadForm(forms.Form):
    period_of_the_day = forms.CharField(max_length=3,
                                        widget=forms.Select(choices=CaptureSession.PERIOD_TYPE))
    image_files = MultiFileField(min_num=1, max_num=100)


class RawImageUploadFormWithCattle(forms.Form):
    cattle = forms.ModelChoiceField(queryset=Cattle.objects.all())
    period_of_the_day = forms.CharField(max_length=3,
                                        widget=forms.Select(choices=CaptureSession.PERIOD_TYPE))
    image_files = MultiFileField(min_num=1, max_num=100)