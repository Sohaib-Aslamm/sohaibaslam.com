from adminPanel.forms import PortfoliosForm

from adminPanel.models import Portfolios

from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required(login_url='/user_login')
def portfolios(request):
    if request.method == 'POST':
        PFFM = PortfoliosForm(request.POST, request.FILES)
        if PFFM.is_valid():
            LNK = PFFM.cleaned_data['link']
            THMBNL = PFFM.cleaned_data['thumbnail']
            reg = Portfolios(link=LNK, thumbnail=THMBNL)
            reg.save()
            PFFM = PortfoliosForm()
    else:
        PFFM = PortfoliosForm()
    PFdata = Portfolios.objects.all()
    return render(request, 'adminPortfolios.html', {'form': PFFM, 'PFdata': PFdata})