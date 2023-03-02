from django.urls import path
from myapp import views
from django.contrib.auth.decorators import login_required


app_name = "main"
urlpatterns = [
    path('blog/',views.IndexView.as_view(), name='home'),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('blog/blogs/', views.BlogList.as_view(), name="bloglist"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("blog/blogger/", views.AuthorList.as_view(), name="authorlist"),
    path("blog/post/", login_required(views.BlogPost.as_view()), name="postblog"),
    path("blog/<int:pk>/create/", login_required(views.Comment.as_view()), name="comments"),    
]
    