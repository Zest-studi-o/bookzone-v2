from django.db import models
# to import the custom user
from django.conf import settings

# Choices for the 'status' field
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):

    SECTIONS = [
        ('Club', 'Club'),
        ('Bestseller', 'Bestseller'),
        ('Indie', 'Indie'),
    ]

    title = models.CharField(max_length=200, unique=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    section = models.CharField(max_length=25, choices=SECTIONS, default='Club')
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(max_length=200, unique=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
