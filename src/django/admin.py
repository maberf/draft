from django.contrib import admin
from .models import Fiisiteapp

@admin.register(Fiisiteapp)
class FiisiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'status')
    list_filter = ('status', 'created', 'published', 'author')  #  filters
    raw_id_fields = ('author',)
    date_hierarchy = 'published'  # filter by date
    search_fields = ('title','content')  # Pesquisar
    prepopulated_fields = {'slug':('title',)}   # fill slug with title value
"""
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250) #https://www.site.com.br/
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
"""

# Register your models here.
