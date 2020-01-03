from django import forms

from .models import WebMaps

class WebMapsModelForms(forms.ModelForm):

    class Meta:
        model = WebMaps
        # this form generation on the basis of modelform
        fields = ['latitude', 'longtitude', 'zoom']

    # this is form validation
    def clean_latitude(self, *agrs, **kwargs):
        latitude = int(self.cleaned_data.get('latitude'))
        if latitude>90 or latitude<-90:
            raise forms.ValidationError("The latitude should be in the range of -90 to 90")
        return latitude

    # this is form validation
    def clean_longtitude(self, *agrs, **kwargs):
        longtitude = int(self.cleaned_data.get('longtitude'))
        if longtitude<-180 or longtitude>180:
            raise forms.ValidationError("The longtitude should be in the range of -180 to 180")
        return longtitude

    # this is form validation
    def clean_zoom(self, *agrs, **kwargs):
        zoom = int(self.cleaned_data.get('zoom'))
        if zoom<0 or zoom>10:
            raise forms.ValidationError("The zoom should be in the range of 0 to 10")
        return zoom
