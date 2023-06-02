from django.shortcuts import render
from adminPanel.models import SocialMedia, seoTags, MainPage


def sohaib_Home(request):
    social_media = SocialMedia.objects.all()
    SEOTAGS = seoTags.objects.filter(page='home_page')
    main_page_data = MainPage.objects.all()
    context = {'social_media': social_media, 'SEOTAGS': SEOTAGS, 'main_page_data': main_page_data}
    return render(request, 'main_Home.html', context)