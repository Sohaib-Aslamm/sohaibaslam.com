from django.shortcuts import redirect
from adminPanel.models import hello

from django.contrib import messages


def sayhello(request):
    if request.method == 'POST':
        yourName = request.POST.get('yourName')
        email = request.POST.get('email')
        description = request.POST.get('description')
        sv = hello(yourName=yourName, email=email, description=description)
        sv.save()
        messages.success(request, 'your message has been sent...')
        return redirect('/Home')