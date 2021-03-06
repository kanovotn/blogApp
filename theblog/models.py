from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    slug = models.SlugField(max_length=(255), unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body= RichTextField(blank=True, null=True)
    post_date = models.DateField(default=datetime.now)
    snippet = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, default='uncategorized')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)) )
        return reverse('home')


