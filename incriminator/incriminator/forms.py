from django import forms

import datetime

class IndexForm(forms.Form):
    ip = forms.CharField(label="Enter an IP:")
    date = forms.DateField(label="Enter a date:", widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))
