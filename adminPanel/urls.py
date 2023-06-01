from django.urls import path, include
from adminPanel import views

urlpatterns = [
    path('admin', views.adminHome, name="admin"),
    path('about', views.adminAbout, name="about"),
    path('experience', views.adminExperience, name="experience"),
    path('education', views.adminEducation, name="education"),
    path('languageskills', views.SkillsLang, name="languageskills"),
    path('portfolios', views.portfolios, name="portfolios"),
    path('recommendation', views.recommendation, name="recommendation"),
    path('socialMedia', views.social_media, name="socialMedia"),
    path('adminblog', views.adminblog, name="adminblog"),
    path('user_comments', views.user_comments, name="user_comments"),
    path('adminPIAIC', views.adminPIAIC, name="adminPIAIC"),
    path('adminPIAIC_Notifications', views.PIAIC_Notifi, name="adminPIAIC_Notifications"),
    path('seotags', views.SEOTags, name="seotags"),
    path('user_login', views.user_login, name="user_login"),
    path('user_logout', views.user_logout, name="user_logout"),

    path('view_Message/<int:id>', views.viewMessage, name="view_Message"),
    path('Delete/<int:id>/<str:type>', views.Delete, name="Delete"),
    path('Update/<int:id>/<str:type>', views.Update, name="Update"),
]
