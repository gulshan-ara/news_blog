from django.db import models
  
# Create your models here.
class BlogData(models.Model):
  categories = [
    ('Education', 'Education'),
    ('Finance', 'Finance'),
    ('Technology', 'Technology'),
    ('Automobile', 'Automobile'),
    ('Bollywood', 'Bollywood'),
    ('Politics', 'Politics'),
  ]
  
  blog_title = models.CharField(max_length=256, null=False, blank=False)
  blog_author = models.CharField(max_length=256, null=False, blank=False)
  blog_creation_date = models.DateField()
  blog_image_primary = models.ImageField(upload_to="img/%y")
  image_caption = models.CharField(max_length=256, null=False, blank=False, default='')
  blog_category = models.CharField(max_length=20, choices=categories, default='Education')
  related_link_one = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='related_links_one')
  related_link_two = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='related_links_two')
  related_link_three = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='related_links_three')
  related_link_four = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='related_links_four')
  inline_link_one = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='inline_links_one')
  inline_link_two = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='inline_links_two')
  blog_content_para_one = models.TextField(null=False, blank=False, default='')
  blog_content_para_two = models.TextField(null=False, blank=False, default='')
  blog_content_para_three = models.TextField(null=False, blank=False, default='')
  blog_content_para_four = models.TextField(null=True, blank=True)
  blog_content_para_five = models.TextField(null=True, blank=True)
  
  def __str__(self):
    return self.blog_title
  
