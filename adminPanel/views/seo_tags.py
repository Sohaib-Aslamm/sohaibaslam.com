from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from adminPanel.models import seoTags
from adminPanel.forms import SEOTagsForm


@login_required(login_url='/user_login')
def SEOTags(request):
    if request.method == 'POST':
        SEOFM = SEOTagsForm(request.POST, request.FILES)
        if SEOFM.is_valid():
            title = SEOFM.cleaned_data['title']
            page = SEOFM.cleaned_data['page']
            canonical_link = SEOFM.cleaned_data['canonical_link']
            description = SEOFM.cleaned_data['description']
            tags = SEOFM.cleaned_data['tags']
            reg = seoTags(title=title, page=page, canonical_link=canonical_link, description=description, tags=tags)
            reg.save()
            SEOFM = SEOTagsForm()
    else:
        SEOFM = SEOTagsForm()
    SEODATA = seoTags.objects.all()
    return render(request, 'seoTags.html', {'form': SEOFM, 'SEODATA': SEODATA})
