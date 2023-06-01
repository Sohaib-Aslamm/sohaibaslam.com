from django.shortcuts import render, redirect
from adminPanel.forms import UserForm
from django.contrib import messages
from adminPanel.decorators import unauthenticated_user
from django.contrib.auth import authenticate,  login as auth_login, logout


@unauthenticated_user
def UserRegister(request):
    if request.method == 'POST':
        URFM = UserForm(request.POST, request.FILES)
        if URFM.is_valid():
            URFM.save()
            user = URFM.cleaned_data.get('username')
            messages.success(request, f'Hey !  {user} your account created successfully')
            return redirect('/user_login')
    else:
        URFM = UserForm()
    return render(request, 'User_Register.html', {'form': URFM})


@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.info(request, f'Welcome to your portfolio {user}')
            return redirect('/admin')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    messages.info(request, 'You are logged out !')
    return redirect('/user_login')