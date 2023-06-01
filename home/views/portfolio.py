from django.shortcuts import render
from adminPanel.models import About, Experience, Education, LangSkill, Portfolios, Recommendations, SocialMedia, \
    userBlog


def Portfolio(request):
    about = About.objects.all()
    experience = Experience.objects.all().order_by('-id')
    education = Education.objects.all()
    languages_skills = LangSkill.objects.all()
    Recommendation = Recommendations.objects.all()
    portfolio = Portfolios.objects.all()
    social_media = SocialMedia.objects.all()
    blog = userBlog.objects.all.order_by('-sNo')[:2]
    data = {'about': about, 'experience': experience, 'education': education, 'lang_skill': languages_skills,
            'portfolio': portfolio, 'Recommendation': Recommendation, 'social_media': social_media, 'blog': blog}
    return render(request, 'portfolio.html', data)