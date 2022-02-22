from distutils.log import info
from django.shortcuts import render

def blog_view(request):
    info = {}
    info["template_name"] = 'blog/blog.html'
    info["title"] = 'Blog - Deaconn'
    return render(request, 'home/page.html', info)