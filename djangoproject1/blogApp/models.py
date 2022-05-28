import imp
from django.db import models
from django.utils.text import slugify
from django.utils import timezone 
class Sample(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, primary_key=True)
    content = models.TextField()
    publishedAt = models.DateTimeField(default=timezone.now)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
# Create your models here.
