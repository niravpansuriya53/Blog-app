from django.shortcuts import render
from django.views.generic.base import View

class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html")