from django import forms

class UploadImgForm(forms.Form):
    img = forms.FileField()
    fileName = forms.CharField(max_length=120)

class RatingForm(forms.Form):
	rating   = forms.IntegerField(required=True, max_value=5, min_value=1)
	username = forms.CharField(max_length=120)
	description = forms.CharField(required=False,max_length=5000)
