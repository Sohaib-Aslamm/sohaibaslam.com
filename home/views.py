from django.shortcuts import render, redirect, HttpResponseRedirect
from adminPanel.models import About, Experience, Education, LangSkill, Portfolios, Recommendations, SocialMedia, \
    userBlog, blog_Review, hello, PIAIC, PIAIC_Attachments, PIAIC_Review, PIAIC_Notifications, PIAIC_NOTIFI_Review, \
    PIAIC_ICONS
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages


# Create your views here.


def sohaib_Home(request):
    social_media = SocialMedia.objects.all()
    context = {'social_media': social_media}
    return render(request, 'main_Home.html', context)


def Portfolio(request):
    about = About.objects.all()
    experience = Experience.objects.all().order_by('-id')
    education = Education.objects.all()
    languages_skills = LangSkill.objects.all()
    Recommendation = Recommendations.objects.all()
    portfolio = Portfolios.objects.all()
    social_media = SocialMedia.objects.all()
    blog = userBlog.objects.all().order_by('-sNo')[:2]
    data = {'about': about, 'experience': experience, 'education': education, 'lang_skill': languages_skills,
            'portfolio': portfolio, 'Recommendation': Recommendation, 'social_media': social_media, 'blog': blog}
    return render(request, 'portfolio.html', data)


def blog_list(request):
    BLOGDATA = userBlog.objects.all().order_by('-sNo')
    paginator = Paginator(BLOGDATA, 5)
    pageNo = request.GET.get('page')
    BLOGDATAFINAL = paginator.get_page(pageNo)
    totalPages = BLOGDATAFINAL.paginator.num_pages
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.all().order_by('-sNo')[10:16]
    footer_recent = userBlog.objects.all().order_by('-sNo')[:2]
    context = {'BLOGDATA': BLOGDATAFINAL, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)],
               'RCPST': RCPST, 'SMDT': SMDT, 'footer_recent': footer_recent}
    return render(request, 'blog_list.html', context)


def search_blog(request):
    if request.method == 'POST':
        search_keyword = request.POST.get('search_keyword')
        BLOGDATA = userBlog.objects.filter(Q(title__icontains=search_keyword) | Q(heading__icontains=search_keyword) | Q(description__icontains=search_keyword)).order_by('-sNo')
        paginator = Paginator(BLOGDATA, 5)
        pageNo = request.GET.get('page')
        BLOGDATAFINAL = paginator.get_page(pageNo)
        totalPages = BLOGDATAFINAL.paginator.num_pages
        SMDT = SocialMedia.objects.all()
        RCPST = userBlog.objects.all().order_by('-sNo')[10:16]
        footer_recent = userBlog.objects.all().order_by('-sNo')[:2]
        context = {'BLOGDATA': BLOGDATAFINAL, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)],
                   'RCPST': RCPST, 'SMDT': SMDT, 'footer_recent': footer_recent}
        return render(request, 'blog_list.html', context)


def blogReview(request):
    if request.method == 'POST':
        postSno = request.POST.get('postSno')
        author = request.POST.get('author')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        post_id = userBlog.objects.get(sNo=postSno)
        sv = blog_Review(author=author, email=email, comment=comment, post=post_id)
        sv.save()
        return redirect(f'/ViewDetail/{postSno}/blogDetail')


def sayhello(request):
    if request.method == 'POST':
        yourName = request.POST.get('yourName')
        email = request.POST.get('email')
        description = request.POST.get('description')
        sv = hello(yourName=yourName, email=email, description=description)
        sv.save()
        messages.success(request, 'your message has been sent...')
        return redirect('/Home')


def PIAIC_Attachs(request):
    All_Attachments = PIAIC.objects.all().order_by('-sNo')
    paginator = Paginator(All_Attachments, 9)
    pageNo = request.GET.get('page')
    Final_Attachments = paginator.get_page(pageNo)
    totalPages = Final_Attachments.paginator.num_pages
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    context = {'Final_Attachments': Final_Attachments, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)],
               'RCPST': RCPST, 'SMDT': SMDT}
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
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    context = {'Final_Attachments': Final_Attachments, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)],
               'RCPST': RCPST, 'SMDT': SMDT}
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


def thank_you(request):
    return render(request, 'thankyou.html')


def thank_you_notif(request):
    return render(request, 'thank_you_notification.html')


def Detail_Record(request, sNo, type):
    if type == 'blogDetail':
        rdPost = userBlog.objects.filter(sNo=sNo)
        coments = blog_Review.objects.filter(post__in=rdPost).order_by('-sNo')
        SMDT = SocialMedia.objects.all()
        RCPST = userBlog.objects.all().order_by('-sNo')[10:16]
        footer_recent = userBlog.objects.all().order_by('-sNo')[:2]
        context = {'rdPost': rdPost, 'RCPST': RCPST, 'SMDT': SMDT, 'coments': coments, 'footer_recent': footer_recent}
        return render(request, 'read_post.html', context)

    if type == 'Attachment_Detail':
        readAttachment = PIAIC.objects.filter(sNo=sNo)
        Attachments = PIAIC_Attachments.objects.filter(Attachment_ID_id=sNo)
        ICONS = PIAIC_ICONS.objects.filter(Icon_ID_id=sNo)
        piaic_query = PIAIC_Review.objects.filter(post__in=readAttachment).order_by('-sNo')
        SMDT = SocialMedia.objects.all()
        RCPST = userBlog.objects.all().order_by('-sNo')[:2]
        context = {'readAttachment': readAttachment, 'Attachments': Attachments, 'piaic_query': piaic_query,
                   'ICONS': ICONS, 'RCPST': RCPST, 'SMDT': SMDT}
        return render(request, 'Read_Attachment.html', context)

    if type == 'Notification_Detail':
        readAttachment = PIAIC_Notifications.objects.filter(sNo=sNo)
        piaic_query = PIAIC_NOTIFI_Review.objects.filter(post__in=readAttachment).order_by('-sNo')
        SMDT = SocialMedia.objects.all()
        RCPST = userBlog.objects.all().order_by('-sNo')[:2]
        context = {'readAttachment': readAttachment, 'piaic_query': piaic_query,
                   'RCPST': RCPST, 'SMDT': SMDT}
        return render(request, 'Read_PIAIC_Notifications.html', context)
