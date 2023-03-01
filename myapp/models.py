from django.db import models
import django.utils.timezone
from django.urls import reverse



#base model
class BaseModel(models.Model):
    created_at = models.DateTimeField(default=django.utils.timezone.now())
    updated_at = models.DateTimeField(default=django.utils.timezone.now())
    
    class Meta:
        abstract = True 
        
#Author details model
class Author(models.Model):
    name = models.CharField(max_length=30, null=False)
    brithdate = models.DateField()
    about_author = models.TextField()

    def __str__(self):
        return self.name

# blog uploding model
class Blog(BaseModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="blogs")
    title = models.CharField(max_length=70)
    content = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/blog/blogs/" 