from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from myapp.form import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from myapp.models import Author, Blog, Comment
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.shortcuts import get_object_or_404  
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# home page view
class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html")


# register user
class RegisterView(View):
    template_name = "register.html"

    def get(self, request):
        form = UserRegisterForm()
        context = {"register_form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:home")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
        context = {"register_form": form}
        return render(request, self.template_name, context)


# login user
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse('main:home')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.info(self.request, f'You are now logged in as {form.cleaned_data.get("username")}.')
        return super().form_valid(form)


# logout user
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect("main:home")


# blog uploading
@method_decorator(login_required, name='dispatch')
class BlogPost(CreateView):
    model = Blog
    fields = ['author', 'title', 'content']


# list of all blog
class BlogList(ListView):
    paginate_by = 5
    queryset = Blog.objects.order_by('-created_at')


#List of all author
class AuthorList(ListView):
    queryset = Author.objects.all()


@method_decorator(login_required, name='dispatch')
class Comment(CreateView):
    model = Comment
    fields =['comment']
    
    def form_valid(self, form):
        blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        form.instance.blog = blog
        return super().form_valid(form)
class AuthorDetail(DetailView):
    model= Author
#Blog details
class BlogDetail(DetailView):
    model= Blog
