from django.contrib import admin
from .models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
  list_display = ('blog_title', 'blog_content', 'blog_author', 'blog_creation_date')
  
admin.site.register(BlogData, BlogAdmin)