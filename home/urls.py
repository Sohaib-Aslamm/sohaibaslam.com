from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.sohaib_Home, name="Home"),
    path('Home', views.sohaib_Home, name="Home"),
    path('portfolio', views.Portfolio, name="portfolio"),
    path('blog', views.blog_list, name="blog"),
    path('search_blog', views.search_blog, name="search_blog"),
    path('sayhello', views.sayhello, name="sayhello"),
    path('piaic', views.PIAIC_Attachs, name="piaic"),
    path('PIAIC_QUERY', views.PIAIC_QUERY, name="PIAIC_QUERY"),
    path('notification', views.PIAIC_NOTIFI, name="notification"),
    path('PIAIC_NOTIFI_QUERY', views.PIAIC_NOTIFI_QUERY, name="PIAIC_NOTIFI_QUERY"),
    path('thank_you', views.thank_you, name="thank_you"),
    path('thank_you_notif', views.thank_you_notif, name="thank_you_notif"),
    path('<str:type>/<str:slug>', views.Detail_Record, name="Detail_Record"),
    path('blogReview', views.blogReview, name="blogReview"),
    ]
