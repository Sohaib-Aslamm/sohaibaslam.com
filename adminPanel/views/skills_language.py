from adminPanel.forms import LangSkillForm

from adminPanel.models import LangSkill

from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required(login_url='/user_login')
def SkillsLang(request):
    if request.method == 'POST':
        SLFM = LangSkillForm(request.POST, request.FILES)
        if SLFM.is_valid():
            SK1 = SLFM.cleaned_data['skill1']
            EXPRT1 = SLFM.cleaned_data['expert1']
            SK2 = SLFM.cleaned_data['skill2']
            EXPRT2 = SLFM.cleaned_data['expert2']
            SK3 = SLFM.cleaned_data['skill3']
            EXPRT3 = SLFM.cleaned_data['expert3']
            SK4 = SLFM.cleaned_data['skill4']
            EXPRT4 = SLFM.cleaned_data['expert4']
            SK5 = SLFM.cleaned_data['skill5']
            EXPRT5 = SLFM.cleaned_data['expert5']
            SK6 = SLFM.cleaned_data['skill6']
            EXPRT6 = SLFM.cleaned_data['expert6']
            SK7 = SLFM.cleaned_data['skill7']
            EXPRT7 = SLFM.cleaned_data['expert7']
            SK8 = SLFM.cleaned_data['skill8']
            EXPRT8 = SLFM.cleaned_data['expert8']
            LANG1 = SLFM.cleaned_data['lang1']
            STR1 = SLFM.cleaned_data['str1']
            LANG2 = SLFM.cleaned_data['lang2']
            STR2 = SLFM.cleaned_data['str2']
            LANG3 = SLFM.cleaned_data['lang3']
            STR3 = SLFM.cleaned_data['str3']
            icon1 = SLFM.cleaned_data['Icon1']
            icon2 = SLFM.cleaned_data['Icon2']
            icon3 = SLFM.cleaned_data['Icon3']
            reg = LangSkill(skill1=SK1, skill2=SK2, skill3=SK3, skill4=SK4, skill5=SK5, skill6=SK6, skill7=SK7,
                            skill8=SK8, lang1=LANG1, lang2=LANG2, lang3=LANG3, Icon1=icon1, Icon2=icon2, Icon3=icon3,
                            expert1=EXPRT1, expert2=EXPRT2, expert3=EXPRT3, expert4=EXPRT4, expert5=EXPRT5,
                            expert6=EXPRT6, expert7=EXPRT7, expert8=EXPRT8, str1=STR1, str2=STR2, str3=STR3)
            reg.save()
            SLFM = LangSkillForm()
    else:
        SLFM = LangSkillForm()
    SLdata = LangSkill.objects.all()
    return render(request, 'adminLanguageSkills.html', {'form': SLFM, 'SLdata': SLdata})