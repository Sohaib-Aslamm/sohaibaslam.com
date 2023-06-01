from adminPanel.forms import AboutForm
from adminPanel.models import About


from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required(login_url='/user_login')
def adminAbout(request):
    if request.method == 'POST':
        ABFM = AboutForm(request.POST, request.FILES)
        if ABFM.is_valid():
            FN = ABFM.cleaned_data['fullName']
            DSG = ABFM.cleaned_data['Designation']
            STR = ABFM.cleaned_data['street']
            AOR = ABFM.cleaned_data['areaofResearch']
            PJ = ABFM.cleaned_data['previousJob']
            SCH = ABFM.cleaned_data['School']
            NAT = ABFM.cleaned_data['Nationality']
            MS = ABFM.cleaned_data['meritalStatus']
            BD = ABFM.cleaned_data['Birthday']
            SK = ABFM.cleaned_data['Skype']
            EM = ABFM.cleaned_data['Email']
            PH = ABFM.cleaned_data['Phone']
            DSC = ABFM.cleaned_data['description']
            RSM = ABFM.cleaned_data['resume']
            PR = ABFM.cleaned_data['profile']
            reg = About(fullName=FN, Designation=DSG, street=STR, areaofResearch=AOR, previousJob=PJ,
                        School=SCH, Nationality=NAT, meritalStatus=MS, Birthday=BD, Skype=SK,
                        Email=EM, Phone=PH, description=DSC, resume=RSM, profile=PR)
            reg.save()
            ABFM = AboutForm()
    else:
        ABFM = AboutForm()
    ABTMD = About.objects.all()
    return render(request, 'adminAbout.html', {'form': ABFM, 'ABTMD': ABTMD})
