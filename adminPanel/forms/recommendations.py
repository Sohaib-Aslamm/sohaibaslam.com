from django import forms
from adminPanel.models import Recommendations


class RecommendationsForm(forms.ModelForm):
    class Meta:
        model = Recommendations
        fields = '__all__'

        widgets = {
            'person': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your name'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter designation'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter brief description'}),
        }
