from django.shortcuts import render, redirect, HttpResponseRedirect
from adminPanel.models import About, Experience, Education, LangSkill, Portfolios, Recommendations, SocialMedia, \
    userBlog, blog_Review

from django.core.paginator import Paginator



# Create your views here.



def sohaib_Home(request):
    social_media = SocialMedia.objects.all()
    context = {'social_media': social_media}
    return render(request, 'main_Home.html', context)


def Portfolio(request):
    about = About.objects.all()
    experience = Experience.objects.all()
    education = Education.objects.all()
    languages_skills = LangSkill.objects.all()
    Recommendation = Recommendations.objects.all()
    portfolio = Portfolios.objects.all()
    social_media = SocialMedia.objects.all()
    blog = userBlog.objects.all().order_by('-sNo')[:2]
    data = {'about': about, 'experience': experience, 'education': education, 'lang_skill': languages_skills,
            'portfolio': portfolio, 'Recommendation': Recommendation, 'social_media': social_media, 'blog': blog}
    return render(request, 'portfolio.html', data)


def blogHome(request):
    BLOGDATA = userBlog.objects.all().order_by('-sNo')
    paginator = Paginator(BLOGDATA, 9)
    pageNo = request.GET.get('page')
    BLOGDATAFINAL = paginator.get_page(pageNo)
    totalPages = BLOGDATAFINAL.paginator.num_pages
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    context = {'BLOGDATA': BLOGDATAFINAL, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)],
               'RCPST': RCPST, 'SMDT': SMDT}
    return render(request, 'blog.html', context)


def postDetail(request, sNo):
    rdPost = userBlog.objects.filter(sNo=sNo)
    coments = blog_Review.objects.filter(post__in=rdPost)
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    context = {'rdPost': rdPost, 'RCPST': RCPST, 'SMDT': SMDT, 'coments': coments}
    return render(request, 'read_post.html', context)


def blogReview(request):
    if request.method == 'POST':
        postSno = request.POST.get('postSno')
        author = request.POST.get('author')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        post_id = userBlog.objects.get(sNo=postSno)
        sv = blog_Review(author=author, email=email, comment=comment, post=post_id)
        sv.save()

        return redirect('/blog')
