from django.urls import path
from myapp import views


app_name = "main"
urlpatterns = [
    path('blog/', views.IndexView.as_view(), name='home'),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('blog/blogs/', views.BlogList.as_view(), name="bloglist"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("blog/blogger/", views.AuthorList.as_view(), name="authorlist"),
    path("blog/post/", views.BlogPost.as_view(), name="postblog"),
    path("blog/<int:pk>/", views.BlogDetail.as_view(), name="blogdetails"),
    path("blogs/<int:pk>/", views.AuthorDetail.as_view(), name="authordetails"),
    path("blogs/<int:pk>/create/", views.Comment.as_view(), name="comment"),
]  
