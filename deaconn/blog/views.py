from distutils.log import info
from django.shortcuts import render
from . import models
from django.conf import settings

def blog_view(request):
    info = {}

    page = request.GET.get('p', 1)
    search = request.GET.get('s', None)

    # Common information.
    info["template_name"] = 'blog/blog.html'
    info["title"] = 'Blog - Deaconn'

    # Retrieve articles list.
    articles = models.Article.objects.all()

    if search is not None:
        articles = articles.filter(tags__icontains = search)

    info["articles_count"] = articles.count()

    start_idx = (int(page) * settings.BLOG_MAX_PER_PAGE) - settings.BLOG_MAX_PER_PAGE
    end_idx = (int(page) * settings.BLOG_MAX_PER_PAGE)

    info["page_num"] = page

    info["pages"] = []

    if info["articles_count"] > settings.BLOG_MAX_PER_PAGE:
        page_cnt = int(info["articles_count"] / settings.BLOG_MAX_PER_PAGE)
        for i in range(page_cnt):
            info["pages"].append(i + 1)

    info["articles"] = articles.order_by('-date_added')[start_idx:end_idx]

    return render(request, 'home/page.html', info)

def article_view(request, article_id):
    info = {}

    # Common information.
    info["template_name"] = 'blog/view_article.html'
    info["title"] = 'Blog - Deaconn'

    # Retrieve article
    try:
        info["article"] = models.Article.objects.get(id = article_id)
    except Exception:
        info["article"] = False

    return render(request, 'home/page.html', info)