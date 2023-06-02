from adminPanel.forms import MainPageForm

from adminPanel.models import MainPage
from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required(login_url='/user_login')
def Main_Page(request):
    if request.method == 'POST':
        MNPFM = MainPageForm(request.POST, request.FILES)
        if MNPFM.is_valid():
            name = MNPFM.cleaned_data['name']
            skills = MNPFM.cleaned_data['skills']
            tag_line = MNPFM.cleaned_data['tag_line']
            desc_1 = MNPFM.cleaned_data['description_1']
            desc_2 = MNPFM.cleaned_data['description_2']
            reg = MainPage(name=name, skills=skills, tag_line=tag_line, description_1=desc_1, description_2=desc_2)
            reg.save()
            MNPFM = MainPageForm()
    else:
        MNPFM = MainPageForm()
    main_page_data = MainPage.objects.all()
    return render(request, 'adminMainPage.html', {'form': MNPFM, 'main_page_data': main_page_data})
