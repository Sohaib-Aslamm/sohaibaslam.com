from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.sohaib_Home, name="Home"),
    path('Home', views.sohaib_Home, name="Home"),
    path('Portfolio', views.Portfolio, name="Portfolio"),
    path('blog', views.blog_list, name="blog"),
    path('search_blog', views.search_blog, name="search_blog"),
    path('sayhello', views.sayhello, name="sayhello"),
    path('PIAIC', views.PIAIC_Attachs, name="PIAIC"),
    path('PIAIC_QUERY', views.PIAIC_QUERY, name="PIAIC_QUERY"),
    path('Notification', views.PIAIC_NOTIFI, name="Notification"),
    path('PIAIC_NOTIFI_QUERY', views.PIAIC_NOTIFI_QUERY, name="PIAIC_NOTIFI_QUERY"),
    path('thank_you', views.thank_you, name="thank_you"),
    path('thank_you_notif', views.thank_you_notif, name="thank_you_notif"),
    path('ViewDetail/<int:sNo>/<str:type>', views.Detail_Record, name="ViewDetail"),
    path('blogReview', views.blogReview, name="blogReview"),
    ]
