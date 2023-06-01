from adminPanel.forms import ExperienceForm

from adminPanel.models import Experience

from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required(login_url='/user_login')
def adminExperience(request):
    if request.method == 'POST':
        EXPFM = ExperienceForm(request.POST, request.FILES)
        if EXPFM.is_valid():
            DSG = EXPFM.cleaned_data['Designation']
            FRM = EXPFM.cleaned_data['From']
            TO = EXPFM.cleaned_data['To']
            CMP = EXPFM.cleaned_data['Company']
            STR = EXPFM.cleaned_data['Street']
            DESC = EXPFM.cleaned_data['Description']
            reg = Experience(Designation=DSG, From=FRM, To=TO, Company=CMP, Street=STR,
                             Description=DESC)
            reg.save()
            EXPFM = ExperienceForm()
    else:
        EXPFM = ExperienceForm()
    data = Experience.objects.all()
    return render(request, 'adminExperience.html', {'form': EXPFM, 'EXPdata': data})