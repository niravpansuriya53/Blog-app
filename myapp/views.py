from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from myapp.form import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from myapp.models import Author, Blog


# home page view
class index(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html")


# register user
def register_request(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:home")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = UserRegisterForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


# login ser
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form": form})


# logout user
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect("main:home")


# blod uploding
class BlogPost(CreateView):
    model = Blog
    fields = ['author', 'title', 'content']


# list od all blog
class BlogList(ListView):
    paginate_by = 5
    queryset = Blog.objects.order_by('-created_at')


#L  ist of all Authoer detils 
class AuthorList(ListView):
    queryset = Author.objects.all()
