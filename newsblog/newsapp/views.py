from django.shortcuts import render

# Create your views here.
from .models import *

# Index function promised in urls
def index(request):
  # fetching values from blog table
  blogs = BlogData.objects.all()
  return render(request, 'newsapp/index.html', {'blogs' : blogs})

def blog(request, pk):
  # fetching values from blog table
  blog = BlogData.objects.get(pk=pk)
  return render(request, 'newsapp/blog.html', {'blog' : blog})