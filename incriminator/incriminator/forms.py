from django import forms

import datetime

class IndexForm(forms.Form):
    ip = forms.CharField(label="Enter an IP:", widget=forms.TextInput(attrs={'placeholder': '86.59.21.38'}))
    date = forms.DateField(label="Enter a date:", widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))
