from django.shortcuts import render
from adminPanel.models import SocialMedia


def sohaib_Home(request):
    social_media = SocialMedia.objects.all()
    context = {'social_media': social_media}
    return render(request, 'main_Home.html', context)