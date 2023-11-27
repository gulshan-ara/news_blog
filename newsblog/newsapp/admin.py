from django.contrib import admin
from .models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
  list_display = ('blog_title',
                  'blog_author',
                  'blog_creation_date',
                  'blog_image_primary',
                  'image_caption',
                  'blog_category',
                  'related_link_one',
                  'related_link_two',
                  'related_link_three',
                  'related_link_four',
                  'inline_link_one',
                  'inline_link_two',
                  'blog_content_para_one',
                  'blog_content_para_two',
                  'blog_content_para_three',
                  'blog_content_para_four',
                  'blog_content_para_five',
                  )
  
admin.site.register(BlogData, BlogAdmin)