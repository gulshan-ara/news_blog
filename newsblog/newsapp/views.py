from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from .models import *

# Index function promised in urls
def index(request):
  blogs_list = BlogData.objects.all().order_by('-blog_creation_date')
  # Number of blogs to display per page
  blogs_per_page = 2
  # Get the current page from the request's GET parameters
  page = request.GET.get('page', 1)
  paginator = Paginator(blogs_list, blogs_per_page)

  try:
    blogs = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    blogs = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    blogs = paginator.page(paginator.num_pages)
  return render(request, 'newsapp/index.html', {'blogs' : blogs})

def blog(request, pk):
  # fetching values from blog table
  blog = BlogData.objects.get(pk=pk)
  return render(request, 'newsapp/blog.html', {'blog' : blog})