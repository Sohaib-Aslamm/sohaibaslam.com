from django.shortcuts import render, redirect
from adminPanel.models import SocialMedia, userBlog, blog_Review
from django.db.models import Q
from django.core.paginator import Paginator


def blog_list(request):
    paginator = Paginator(userBlog.objects.values('sNo', 'title', 'heading', 'Icon', 'created_at').order_by('-sNo'), 5)
    page_number = request.GET.get('page')
    blog_data = paginator.get_page(page_number)
    total_pages = blog_data.paginator.num_pages

    recent_posts = userBlog.objects.values('sNo', 'title', 'heading', 'Icon', 'created_at').order_by('-sNo')[10:16]
    footer_recent = userBlog.objects.values('sNo', 'title', 'heading', 'Icon', 'created_at').order_by('-sNo')[:2]

    SMDT = SocialMedia.objects.all()

    context = {
        'BLOGDATA': blog_data,
        'lastPage': total_pages,
        'pageList': range(1, total_pages + 1),
        'RCPST': recent_posts,
        'footer_recent': footer_recent,
        'SMDT': SMDT,
    }

    return render(request, 'blog_list.html', context)


def search_blog(request):
    if request.method == 'POST':
        search_keyword = request.POST.get('search_keyword')
        blog_data = userBlog.objects.filter(
            Q(title__icontains=search_keyword) |
            Q(heading__icontains=search_keyword) |
            Q(description__icontains=search_keyword)
        ).values('sNo', 'title', 'heading', 'Icon', 'created_at').order_by('-sNo')

        paginator = Paginator(blog_data, 5)
        page_number = request.GET.get('page')
        blog_data_final = paginator.get_page(page_number)
        total_pages = blog_data_final.paginator.num_pages

        recent_posts = userBlog.objects.values('sNo', 'title', 'heading', 'Icon', 'created_at').order_by('-sNo')[10:16]
        footer_recent = userBlog.objects.values('sNo', 'title', 'heading', 'Icon', 'created_at').order_by('-sNo')[:2]

        SMDT = SocialMedia.objects.all()

        context = {
            'BLOGDATA': blog_data_final,
            'lastPage': total_pages,
            'pageList': range(1, total_pages + 1),
            'RCPST': recent_posts,
            'footer_recent': footer_recent,
            'SMDT': SMDT,
        }
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