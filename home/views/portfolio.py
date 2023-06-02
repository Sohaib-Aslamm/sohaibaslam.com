from django.shortcuts import render
from adminPanel.models import About, Experience, Education, LangSkill, Portfolios, Recommendations, SocialMedia, \
    userBlog, seoTags, MainPage


def Portfolio(request):
    main_page_data = MainPage.objects.all()
    about = About.objects.all()
    experience = Experience.objects.all().order_by('-id')
    education = Education.objects.all()
    languages_skills = LangSkill.objects.all()
    Recommendation = Recommendations.objects.all()
    portfolio = Portfolios.objects.all()
    social_media = SocialMedia.objects.all()
    blog = userBlog.objects.order_by('-sNo')[:2]
    SEOTAGS = seoTags.objects.filter(page='portfolio_page')
    data = {'about': about, 'experience': experience, 'education': education, 'lang_skill': languages_skills,
            'portfolio': portfolio, 'Recommendation': Recommendation, 'social_media': social_media, 'blog': blog,
            'SEOTAGS': SEOTAGS, 'main_page_data': main_page_data}
    return render(request, 'portfolio.html', data)
