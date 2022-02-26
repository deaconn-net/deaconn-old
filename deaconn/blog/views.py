from distutils.log import info
from django.shortcuts import render
from . import models
from django.conf import settings

from django.template.defaultfilters import slugify
from django.db.models import Q

from django.contrib.auth.models import User

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
        articles = articles.filter(Q(tags__icontains = search) | Q(description__icontains = search) | Q(title__icontains = search) | Q(contents__icontains = search))

    info["articles_count"] = articles.count()

    category_tags = models.Article_Tags.objects.filter(category = True)
    info["ctags"] = {}

    for ct in category_tags:
        if ct.tag.name not in info["ctags"]:
            info["ctags"][ct.tag.name] = 1
        else:
            info["ctags"][ct.tag.name] = info["ctags"][ct.tag.name] + 1

    info["ctags"] = {k: v for k, v in sorted(info["ctags"].items(), reverse = True, key = lambda item: item[1])}

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
    # Check if incoming comment.
    info = {}

    # Retrieve article
    try:
        info["article"] = models.Article.objects.get(id = article_id)
    except Exception:
        info["article"] = False

    if request.method == "POST" and request.user.is_authenticated:
        # Check to make comment.
        if 'add_comment_contents' in request.POST and len(request.POST['add_comment_contents']) > 15:
            models.Comment.objects.create(article = info["article"], author = request.user, contents = request.POST['add_comment_contents'])
            info["comment_successful"] = True
        
        # Check for article or comment edits.
        if 'article_edit' in request.POST:
            if info["article"] and (info["article"].author.id == request.user.id or request.user.is_staff):
                info["article_edit"] = True

        # Next check for edited fields.
        if 'article_title' in request.POST:
            if info["article"] and (info["article"].author.id == request.user.id or request.user.is_staff):
                info["article"].title = request.POST['article_title']
                info["article"].description = request.POST['article_description']
                info["article"].tags = request.POST['article_tags']
                info["article"].contents = request.POST['article_contents']

                if 'article_image' in request.FILES:
                    info["article"].image = request.FILES['article_image']
                elif 'article_image_del' in request.POST:
                    info["article"].image = None

                info["article"].save()
                info["article_edited"] = True

        # Check for comment edit.
        if 'comment_edit' in request.POST:
            id = request.POST['comment_id']
            
            try:
                comment = models.Comment.objects.get(id = id)
            except Exception:
                comment = False

            if comment and (comment.author.id == request.user.id or request.user.is_staff):
                info["comment_edit"] = True

        # Next check for edited fields.
        if 'comment_contents' in request.POST:
            id = request.POST['comment_id']
            
            try:
                comment = models.Comment.objects.get(id = id)
            except Exception:
                comment = False

            if comment and (comment.author.id == request.user.id or request.user.is_staff):
                comment.contents = request.POST['comment_contents']
                comment.save()
                info["comment_edited"] = True

        # Check for article delete.
        if 'article_delete' in request.POST:
            if info["article"] and (info["article"].author.id == request.user.id or request.user.is_staff):
                models.Article.objects.filter(id = info["article"].id).delete()
                info["article_deleted"] = True

        # Check for comment delete.
        if 'comment_delete' in request.POST:
            id = request.POST['comment_id']
            
            try:
                comment = models.Comment.objects.get(id = id)
            except Exception:
                comment = False

            if comment and (comment.author.id == request.user.id or request.user.is_staff):
                models.Comment.objects.get(id = id).delete()
                info["comment_deleted"] = True

    info["user"] = request.user

    # Common information.
    info["template_name"] = 'blog/view_article.html'
    info["title"] = 'Blog - Deaconn'

    if not info["article"].slug:
        info["article"].slug = slugify(info["article"].title)
        info["article"].save()

    if info["article"] != False:
        # Retrieve comments.
        info["comments"] = models.Comment.objects.filter(article = info["article"])

        # Fill out other information.
        info["title"] = info["article"].title
        info["tags"] = info["article"].tags
        info["description"] = info["article"].description
        info["author"] = info["article"].author.first_name + " " + info["article"].author.last_name

    return render(request, 'home/page.html', info)

def create_article(request):
    info = {}

    if 'article_title' in request.POST:
        if request.user and request.user.is_authenticated:
            item = models.Article.objects.create(author = request.user, title = request.POST['article_title'], tags = request.POST['article_tags'], description = request.POST['article_description'], contents = request.POST['article_contents'])

            if 'article_image' in request.FILES:
                item.image = request.FILES['article_image']
                item.save()
            
            info["article_added"] = True

    info["title"] = "Create Article"
    info["template_name"] = 'blog/create_article.html'
    info["user"] = request.user

    return render(request, 'home/page.html', info)