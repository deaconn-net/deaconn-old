from distutils.log import info
from django.shortcuts import render
from . import models
from django.conf import settings

from django.template.defaultfilters import slugify

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

def article_view(request, article_id = None, slug = None):
    info = {}

    # Retrieve article
    try:
        info["article"] = models.Article.objects.get(id = article_id)
    except Exception:
        info["article"] = False

    # Common information.
    info["template_name"] = 'blog/view_article.html'
    info["title"] = 'Blog - Deaconn'

    if not info["article"].slug:
        info["article"].slug = slugify(info["article"].title)
        info["article"].save()

    if info["article"] != False:
        info["title"] = info["article"].title + ' - Blog'
        info["tags"] = info["article"].tags
        info["description"] = info["article"].description
        info["author"] = info["article"].author.first_name + " " + info["article"].author.last_name

    return render(request, 'home/page.html', info)