from django.urls import path
from myapp import views
from django.contrib.auth.decorators import login_required


app_name = "main"
urlpatterns = [
    path('blog/',views.index.as_view(), name='home'),
    path('register/', views.register_request, name="register"),
    path('blog/blogs/', views.BlogList.as_view(), name="bloglist"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("blog/blogger/", views.AuthorList.as_view(), name="authorlist"),
    path("blog/post/", login_required(views.BlogPost.as_view()), name="postblog"),
]
    