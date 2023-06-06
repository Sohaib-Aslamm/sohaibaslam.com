from django.shortcuts import render
from adminPanel.models import SocialMedia, \
    userBlog, blog_Review, PIAIC, PIAIC_Attachments, PIAIC_Review, PIAIC_Notifications, PIAIC_NOTIFI_Review, \
    PIAIC_ICONS


def Detail_Record(request, type, slug):
    if type == 'blog':
        rdPost = userBlog.objects.filter(slug=slug)
        coments = blog_Review.objects.filter(post__in=rdPost).order_by('-sNo')
        SMDT = SocialMedia.objects.all()
        RCPST = userBlog.objects.order_by('-sNo')[10:16]
        footer_recent = userBlog.objects.order_by('-sNo')[:2]
        context = {'rdPost': rdPost, 'RCPST': RCPST, 'SMDT': SMDT, 'coments': coments, 'footer_recent': footer_recent}
        return render(request, 'read_post.html', context)

    if type == 'piaic':
        readAttachment = PIAIC.objects.filter(slug=slug)
        Attachments = PIAIC_Attachments.objects.filter(Attachment_ID_id__in=readAttachment)
        ICONS = PIAIC_ICONS.objects.filter(Icon_ID_id__in=readAttachment)
        piaic_query = PIAIC_Review.objects.filter(post__in=readAttachment).order_by('-sNo')
        SMDT = SocialMedia.objects.all()
        RCPST = userBlog.objects.order_by('-sNo')[:2]
        context = {'readAttachment': readAttachment, 'Attachments': Attachments, 'piaic_query': piaic_query,
                   'ICONS': ICONS, 'RCPST': RCPST, 'SMDT': SMDT}
        return render(request, 'Read_Attachment.html', context)

    if type == 'notification':
        readAttachment = PIAIC_Notifications.objects.filter(slug=slug)
        piaic_query = PIAIC_NOTIFI_Review.objects.filter(post__in=readAttachment).order_by('-sNo')
        SMDT = SocialMedia.objects.all()
        RCPST = userBlog.objects.order_by('-sNo')[:2]
        context = {'readAttachment': readAttachment, 'piaic_query': piaic_query,
                   'RCPST': RCPST, 'SMDT': SMDT}
        return render(request, 'Read_PIAIC_Notifications.html', context)