from django import forms
from . import models


class DescriptionForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ('description',)

