from django.shortcuts import render, redirect
from adminPanel.models import SocialMedia, userBlog, blog_Review, seoTags
from django.db.models import Q
from django.core.paginator import Paginator
from django.urls import reverse


def blog_list(request):
    paginator = Paginator(userBlog.objects.values('sNo', 'title', 'heading', 'slug',  'Icon', 'created_at').order_by('-sNo'), 5)
    page_number = request.GET.get('page')
    blog_data = paginator.get_page(page_number)
    total_pages = blog_data.paginator.num_pages

    recent_posts = userBlog.objects.values('sNo', 'title', 'heading', 'slug', 'Icon', 'created_at').order_by('-sNo')[10:16]
    footer_recent = userBlog.objects.values('sNo', 'title', 'heading', 'slug',  'Icon', 'created_at').order_by('-sNo')[:2]

    SMDT = SocialMedia.objects.all()

    current_page = request.GET.get('page')
    canonical_link = reverse('blog')  # Assuming 'blog' is the name of your URL pattern

    if current_page:
        canonical_link += f'?page={current_page}'

    SEOTAGS = [{
        'title': "Sohaib Aslam's Blog - Data Science, Python, Computer Vision, and New Technologies",
        'description': "Discover a comprehensive blog sharing the latest technical news, computer science insights, programming tips, and technology updates. Stay informed and gain valuable knowledge in the ever-evolving world of technology.",
        'tags': "technical news, computer science, programming, technology updates, blog, insights, knowledge",
        'canonical_link': request.build_absolute_uri(canonical_link)
    }]

    context = {
        'BLOGDATA': blog_data,
        'lastPage': total_pages,
        'pageList': range(1, total_pages + 1),
        'RCPST': recent_posts,
        'footer_recent': footer_recent,
        'SMDT': SMDT,
        'SEOTAGS': SEOTAGS
    }

    return render(request, 'blog_list.html', context)


def search_blog(request):
    if request.method == 'POST':
        search_keyword = request.POST.get('search_keyword')
        blog_data = userBlog.objects.filter(
            Q(title__icontains=search_keyword) |
            Q(heading__icontains=search_keyword) |
            Q(description__icontains=search_keyword)
        ).values('sNo', 'title', 'heading', 'slug', 'Icon', 'created_at').order_by('-sNo')

        paginator = Paginator(blog_data, 5)
        page_number = request.GET.get('page')
        blog_data_final = paginator.get_page(page_number)
        total_pages = blog_data_final.paginator.num_pages

        recent_posts = userBlog.objects.values('sNo', 'title', 'heading',  'slug', 'Icon', 'created_at').order_by('-sNo')[10:16]
        footer_recent = userBlog.objects.values('sNo', 'title', 'heading',  'slug', 'Icon', 'created_at').order_by('-sNo')[:2]

        SMDT = SocialMedia.objects.all()
        SEOTAGS = seoTags.objects.filter(page='search_blog')

        context = {
            'BLOGDATA': blog_data_final,
            'lastPage': total_pages,
            'pageList': range(1, total_pages + 1),
            'RCPST': recent_posts,
            'footer_recent': footer_recent,
            'SMDT': SMDT,
            'SEOTAGS': SEOTAGS
        }
        return render(request, 'blog_list.html', context)


def blogReview(request):
    if request.method == 'POST':
        slug = request.POST.get('slug')
        author = request.POST.get('author')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        post = userBlog.objects.get(slug=slug)
        sv = blog_Review(author=author, email=email, comment=comment, post=post)
        sv.save()
        return redirect(f'/blog/{slug}')
