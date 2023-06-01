from django import forms
from adminPanel.models import Portfolios


class PortfoliosForm(forms.ModelForm):
    class Meta:
        model = Portfolios
        fields = '__all__'

        widgets = {
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paste your link here'}),
        }
