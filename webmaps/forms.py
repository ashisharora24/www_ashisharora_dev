from django import forms

from .models import WebMaps

class WebMapsModelForms(forms.ModelForm):

    class Meta:
        model = WebMaps
        fields = ['latitude', 'longtitude', 'zoom']
