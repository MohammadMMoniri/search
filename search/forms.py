from django import forms
from .models import links



class searchfeild(forms.ModelForm):
    class Meta:
        model = links
        fields = ['searched_word']