from django.urls import path
from myapp import views
urlpatterns = [
    path('blog/',views.index.as_view(), name='home')
]
