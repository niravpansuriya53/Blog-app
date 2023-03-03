from django.db import models
import django.utils.timezone
from django.urls import reverse


# base model
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True


# Author details model
class Author(BaseModel):
    name = models.CharField(max_length=30, null=False)
    birthdate = models.DateField()
    about_author = models.TextField()

    def __str__(self):
        return self.name


# blog uploading model
class Blog(BaseModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="blogs")
    title = models.CharField(max_length=70)
    content = models.TextField()

    def __str__(self):
        return  f"{self.author} - {self.title}"

    def get_absolute_url(self):
        return reverse('main:bloglist')


# comment upload
class Comment(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog")
    comment = models.TextField()

    def __str__(self):
        return f"{self.blog.author} - {self.blog.title}  "
    
    def get_absolute_url(self):
        return reverse('main:bloglist')
    
    class Meta:
        ordering = ['-created_at']

