from django.contrib import admin
from myapp.models import Author, Blog, Comments

admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Comments)
