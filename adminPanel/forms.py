from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from adminPanel.models import About, Experience, Education, LangSkill, Portfolios, Recommendations, SocialMedia


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter user name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter your email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'choose password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'confirm password'}),
        }


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


class PortfoliosForm(forms.ModelForm):
    class Meta:
        model = Portfolios
        fields = '__all__'

        widgets = {
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paste your link here'}),
        }


class RecommendationsForm(forms.ModelForm):
    class Meta:
        model = Recommendations
        fields = '__all__'

        widgets = {
            'person': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your name'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter designation'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter brief description'}),
        }


class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        fields = '__all__'

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'enter email'}),
            'skype': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter skype'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(+92) 344 4276747'}),
            'github': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paste github link'}),
            'linkedin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paste linkedin link'}),
            'google_plus': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paste google+ link'}),
            'youtube': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paste youtube link'}),
            'website': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'website link'}),
        }


