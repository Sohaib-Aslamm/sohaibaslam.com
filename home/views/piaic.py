from django.shortcuts import render, redirect
from adminPanel.models import SocialMedia, userBlog, PIAIC, PIAIC_Review, PIAIC_Notifications, PIAIC_NOTIFI_Review, \
    seoTags
from django.core.paginator import Paginator


def PIAIC_Attachs(request):
    All_Attachments = PIAIC.objects.all().order_by('-sNo')
    paginator = Paginator(All_Attachments, 9)
    pageNo = request.GET.get('page')
    Final_Attachments = paginator.get_page(pageNo)
    totalPages = Final_Attachments.paginator.num_pages
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SEOTAGS = seoTags.objects.filter(page='piaic_page')
    context = {'Final_Attachments': Final_Attachments, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)],
               'RCPST': RCPST, 'SMDT': SMDT, 'SEOTAGS': SEOTAGS}
    return render(request, 'PIAIC.html', context)


def PIAIC_QUERY(request):
    if request.method == 'POST':
        attSno = request.POST.get('attachsNo')
        author = request.POST.get('author')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        post_id = PIAIC.objects.get(sNo=attSno)
        sv = PIAIC_Review(author=author, email=email, comment=comment, post=post_id)
        sv.save()
        return redirect('/thank_you')


def PIAIC_NOTIFI(request):
    All_Attachments = PIAIC_Notifications.objects.all().order_by('-sNo')
    paginator = Paginator(All_Attachments, 9)
    pageNo = request.GET.get('page')
    Final_Attachments = paginator.get_page(pageNo)
    totalPages = Final_Attachments.paginator.num_pages
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SEOTAGS = seoTags.objects.filter(page='piaic_notification_page')
    context = {'Final_Attachments': Final_Attachments, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)],
               'RCPST': RCPST, 'SMDT': SMDT, 'SEOTAGS': SEOTAGS}
    return render(request, 'piaic_notifications.html', context)


def PIAIC_NOTIFI_QUERY(request):
    if request.method == 'POST':
        attSno = request.POST.get('attachsNo')
        author = request.POST.get('author')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        post_id = PIAIC_Notifications.objects.get(sNo=attSno)
        sv = PIAIC_NOTIFI_Review(author=author, email=email, comment=comment, post=post_id)
        sv.save()
        return redirect('/thank_you_notif')
