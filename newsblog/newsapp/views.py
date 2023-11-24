from django.shortcuts import render

# Create your views here.
from .models import *

# Index function promised in urls
def index(request):
  # fetching values from Gene table
  blogs = BlogData.objects.all()
  return render(request, 'newsapp/index.html', {'blogs' : blogs})