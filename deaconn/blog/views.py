from distutils.log import info
from django.shortcuts import render

def blog_view(request):
    info = {}
    return render(request, 'blog/blog.html', info)