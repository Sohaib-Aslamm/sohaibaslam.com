from adminPanel.models import PIAIC, PIAIC_Attachments, PIAIC_Notifications, PIAIC_ICONS


from django.shortcuts import render, redirect


def adminPIAIC(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        heading = request.POST.get('heading')
        tags = request.POST.get('tags')
        instructions = request.POST.get('instructions')
        instructions_By = request.POST.get('instructions_By')
        description = request.POST.get('editor1')
        files = request.FILES.getlist('files')
        icons = request.FILES.getlist('icons')
        sv = PIAIC(title=title, heading=heading, tags=tags, instructions=instructions, instructions_By=instructions_By,
                   description=description)
        sv.save()
        latest_id = PIAIC.objects.latest('sNo').sNo

        for f in files:
            Attachments = PIAIC_Attachments(files=f, Attachment_ID_id=latest_id)
            Attachments.save()

        for f in icons:
            ICONS = PIAIC_ICONS(icons=f, Icon_ID_id=latest_id)
            ICONS.save()

        return redirect('/adminPIAIC')

    all_data = PIAIC.objects.all().order_by('-sNo')
    return render(request, 'adminPIAIC.html', {'all_data': all_data})


def PIAIC_Notifi(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        heading = request.POST.get('heading')
        tags = request.POST.get('tags')
        instructions = request.POST.get('instructions')
        instructions_By = request.POST.get('instructions_By')
        description = request.POST.get('editor1')
        file = request.FILES.get('file')
        sv = PIAIC_Notifications(title=title, heading=heading, tags=tags, instructions=instructions, instructions_By=instructions_By,
                                 description=description, image=file)
        sv.save()
        return redirect('/adminPIAIC_Notifications')

    all_data = PIAIC_Notifications.objects.all().order_by('-sNo')
    return render(request, 'adminPIAIC_Notifications.html', {'all_data': all_data})