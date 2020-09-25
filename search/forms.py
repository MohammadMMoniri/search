from django import forms

class searchfeild(forms.Form):
    search = forms.CharField(label='search', max_length=200)