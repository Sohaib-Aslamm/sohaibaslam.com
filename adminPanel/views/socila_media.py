from adminPanel.forms import SocialMediaForm

from adminPanel.models import SocialMedia
from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required(login_url='/user_login')
def social_media(request):
    if request.method == 'POST':
        SMFM = SocialMediaForm(request.POST, request.FILES)
        if SMFM.is_valid():
            EM = SMFM.cleaned_data['email']
            SK = SMFM.cleaned_data['skype']
            PH = SMFM.cleaned_data['phone']
            GIT = SMFM.cleaned_data['github']
            LIK = SMFM.cleaned_data['linkedin']
            GP = SMFM.cleaned_data['google_plus']
            YTB = SMFM.cleaned_data['youtube']
            WEB = SMFM.cleaned_data['website']
            reg = SocialMedia(email=EM, skype=SK, phone=PH, github=GIT, linkedin=LIK, google_plus=GP, youtube=YTB,
                              website=WEB)
            reg.save()
            SMFM = SocialMediaForm()
    else:
        SMFM = SocialMediaForm()
    SMdata = SocialMedia.objects.all()
    return render(request, 'adminSocialmedia.html', {'form': SMFM, 'SMdata': SMdata})