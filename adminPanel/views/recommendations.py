from adminPanel.forms import RecommendationsForm

from adminPanel.models import Recommendations
from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required(login_url='/user_login')
def recommendation(request):
    if request.method == 'POST':
        RECFM = RecommendationsForm(request.POST, request.FILES)
        if RECFM.is_valid():
            PER = RECFM.cleaned_data['person']
            DESG = RECFM.cleaned_data['designation']
            DESC = RECFM.cleaned_data['description']
            reg = Recommendations(person=PER, designation=DESG, description=DESC)
            reg.save()
            RECFM = RecommendationsForm()
    else:
        RECFM = RecommendationsForm()
    RECdata = Recommendations.objects.all()
    return render(request, 'adminRecommendations.html', {'form': RECFM, 'RECdata': RECdata})