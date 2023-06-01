from adminPanel.forms import EducationForm

from adminPanel.models import Education

from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required(login_url='/user_login')
def adminEducation(request):
    if request.method == 'POST':
        EDUFM = EducationForm(request.POST, request.FILES)
        if EDUFM.is_valid():
            SC = EDUFM.cleaned_data['School']
            SA = EDUFM.cleaned_data['StudyArea']
            FRM = EDUFM.cleaned_data['From']
            TO = EDUFM.cleaned_data['To']
            EI = EDUFM.cleaned_data['Icon']
            reg = Education(School=SC, From=FRM, To=TO, StudyArea=SA, Icon=EI)
            reg.save()
            EDUFM = EducationForm()
    else:
        EDUFM = EducationForm()
    data = Education.objects.all()
    return render(request, 'adminEducation.html', {'form': EDUFM, 'EDUdata': data})