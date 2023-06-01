from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from adminPanel.models import hello


@login_required(login_url='/user_login')
def adminHome(request):
    my_messages = hello.objects.all()
    return render(request, 'HomeAdmin.html', {'my_messages': my_messages})
