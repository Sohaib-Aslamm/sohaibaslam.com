from django.shortcuts import render
from adminPanel.models import SocialMedia, seoTags


def sohaib_Home(request):
    social_media = SocialMedia.objects.all()
    SEOTAGS = seoTags.objects.filter(page='home_page')
    context = {'social_media': social_media, 'SEOTAGS': SEOTAGS}
    return render(request, 'main_Home.html', context)