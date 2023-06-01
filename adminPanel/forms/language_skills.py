from django import forms
from adminPanel.models import LangSkill


class LangSkillForm(forms.ModelForm):
    class Meta:
        model = LangSkill
        fields = '__all__'

        widgets = {
            'skill1': forms.TextInput(attrs={'class': 'form-control'}),
            'expert1': forms.Select(attrs={'class': 'form-control'}),
            'skill2': forms.TextInput(attrs={'class': 'form-control'}),
            'expert2': forms.Select(attrs={'class': 'form-control'}),
            'skill3': forms.TextInput(attrs={'class': 'form-control'}),
            'expert3': forms.Select(attrs={'class': 'form-control'}),
            'skill4': forms.TextInput(attrs={'class': 'form-control'}),
            'expert4': forms.Select(attrs={'class': 'form-control'}),
            'skill5': forms.TextInput(attrs={'class': 'form-control'}),
            'expert5': forms.Select(attrs={'class': 'form-control'}),
            'skill6': forms.TextInput(attrs={'class': 'form-control'}),
            'expert6': forms.Select(attrs={'class': 'form-control'}),
            'skill7': forms.TextInput(attrs={'class': 'form-control'}),
            'expert7': forms.Select(attrs={'class': 'form-control'}),
            'skill8': forms.TextInput(attrs={'class': 'form-control'}),
            'expert8': forms.Select(attrs={'class': 'form-control'}),
            'lang1': forms.TextInput(attrs={'class': 'form-control'}),
            'str1': forms.Select(attrs={'class': 'form-control'}),
            'lang2': forms.TextInput(attrs={'class': 'form-control'}),
            'str2': forms.Select(attrs={'class': 'form-control'}),
            'lang3': forms.TextInput(attrs={'class': 'form-control'}),
            'str3': forms.Select(attrs={'class': 'form-control'}),
        }
