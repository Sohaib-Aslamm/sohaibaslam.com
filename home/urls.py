from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.sohaib_Home, name="Home"),
    path('Home', views.sohaib_Home, name="Home"),
    path('Portfolio', views.Portfolio, name="Portfolio"),
    path('blog', views.blogHome, name="blog"),
    path('postDetail/<int:sNo>', views.postDetail, name="postDetail"),
    path('addReview', views.blogReview, name="addReview"),
    # path('Read_Post/<int:sNo>', views.readPost, name="Read_Post"),
    ]
