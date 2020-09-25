from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):  # filter to published status
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
            .filter(status='published')

class Fiisiteapp(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published' ) #draft status to each publishing
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250) #https://www.site.com.br/
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
    published2 = PublishedManager()

    class Meta:
        ordering = ('published',) #key for presentation order "-" signal changes

    def __str__(self):
        return f' {self.title} - {self.slug}'

    # Create your models here.