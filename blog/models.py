from django.conf import settings
from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL


IMAGE_CATEGORY = (
    ('Primary', 'Primary'),
    ('Thumbnail', 'Thumbnail'),
    ('Secondary', 'Secondary'),
)


class PostPicture(models.Model):
    Picture = models.ImageField(upload_to='photos/blog/%Y/%m/', max_length=500, blank=True)
    PostId = models.ForeignKey('Post', on_delete=models.CASCADE)
    ImageTitle = models.CharField(max_length=150)
    Category = models.CharField(choices=IMAGE_CATEGORY, max_length=200)


class Post(models.Model):
    Slug = models.SlugField()
    Title = models.CharField(max_length=200)
    Content = models.TextField()
    PostPicture = None
    CoverPhoto = models.ImageField(upload_to='photos/blog/%Y/%m/', max_length=500, blank=True)
    Featured = models.BooleanField(default=False)
    Published = models.BooleanField(default=True)
    PublishDate = models.DateTimeField(default=datetime.now, blank=True)
    Modified = models.DateTimeField(auto_now=True)
    Author = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Title)
        super(Post, self).save()

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('blog:blog_post', args=[str(self.slug)])

    class Meta():
        # ordering = ('created',)
        get_latest_by = ('created',)
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
