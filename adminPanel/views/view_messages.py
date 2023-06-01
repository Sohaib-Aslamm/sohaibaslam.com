from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from adminPanel.models import hello


@login_required(login_url='/user_login')
def viewMessage(request, id):
    messages_detail = hello.objects.get(id=id)
    return render(request, 'viewMessages.html', {'messages_detail': messages_detail})
