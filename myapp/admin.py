from django.contrib import admin
from myapp.models import Author, Blog, Comment

<<<<<<< HEAD
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Comment)
=======

class CommentInline(admin.TabularInline):
    model = Comment
    fields = ('comment',)
    extra = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    inlines = (CommentInline,)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('short_comment', 'blog', 'created_at')
    list_display_links = ('short_comment', 'blog')
    fields = ('comment', 'blog')
    
    def short_comment(self, obj):
        return obj.comment[:75]

admin.site.register(Author)
>>>>>>> main
