from django import forms
from adminPanel.models import Education


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

        widgets = {
            'School': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter school'}),
            'StudyArea': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MS computer science'}),
            'From': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD-MM-YYYY'}),
            'To': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD-MM-YYYY/Present'}),
        }
