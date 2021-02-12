from django import forms
from django.utils import timezone


class AddTextForm(forms.Form):
    text = forms.CharField(max_length=350)
    # time_posted = forms.DateTimeField(default=timezone)
