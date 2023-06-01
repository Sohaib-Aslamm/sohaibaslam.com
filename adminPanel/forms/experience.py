from django import forms
from adminPanel.models import Experience


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'

        widgets = {
            'Designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter designation'}),
            'From': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD-MM-YYYY'}),
            'To': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD-MM-YYYY / Present'}),
            'Company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Google Corporation'}),
            'Street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'F-6 Islamabad, Pakistan'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter brief description'}),
        }