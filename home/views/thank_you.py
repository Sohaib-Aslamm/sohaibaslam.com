from django.shortcuts import render, redirect


def thank_you(request):
    return render(request, 'thankyou.html')


def thank_you_notif(request):
    return render(request, 'thank_you_notification.html')