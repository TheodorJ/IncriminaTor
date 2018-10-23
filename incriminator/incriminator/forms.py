from django import forms

class IndexForm(forms.Form):
    ip = forms.CharField(label="Enter an IP:")
    date = forms.DateField(label="Enter a date:")
