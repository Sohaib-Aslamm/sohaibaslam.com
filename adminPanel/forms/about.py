from django import forms
from adminPanel.models import About


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

        widgets = {
            'fullName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your name'}),
            'Designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'current designation'}),
            'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'F-5 Islamabad, Pak'}),
            'areaofResearch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Python engineer'}),
            'previousJob': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter previous job'}),
            'School': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: engineering school'}),
            'Nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'your country'}),
            'meritalStatus': forms.Select(attrs={'class': 'form-control'}),
            'Birthday': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD-MM-YYYY'}),
            'Skype': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter skype id'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'enter email'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(+92) 344 4276747'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter brief description'}),
        }