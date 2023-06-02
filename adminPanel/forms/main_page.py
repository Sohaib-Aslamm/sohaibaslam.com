from django import forms
from adminPanel.models import MainPage


class MainPageForm(forms.ModelForm):
    class Meta:
        model = MainPage
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your name'}),
            'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'current skills'}),
            'tag_line': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter tag line'}),
            'description_1': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter paragraph 1'}),
            'description_2': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter paragraph 2'}),

        }