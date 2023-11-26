from django.db import models
  
# Create your models here.
class BlogData(models.Model):
  blog_title = models.CharField(max_length=256, null=False, blank=False)
  blog_content = models.TextField(null=False, blank=False)
  blog_author = models.CharField(max_length=256, null=False, blank=False)
  blog_creation_date = models.DateField()
  blog_image_primary = models.ImageField(upload_to="img/%y")
  
  def __str__(self):
    return self.blog_title