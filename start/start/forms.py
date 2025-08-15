from django import forms

class sampleloginform(forms.Form):
    username = forms.CharField(min_length=8)
    password = forms.CharField(widget=forms.PasswordInput)
