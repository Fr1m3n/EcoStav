from django import forms
from Upload import models


class UploadForm(forms.ModelForm):
    class Meta:
        model = models.Image
        exclude = [""]

