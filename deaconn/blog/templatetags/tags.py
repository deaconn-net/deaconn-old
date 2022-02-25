from django import template
from django.utils.safestring import mark_safe
from django.urls import reverse

register = template.Library()

from blog.models import Article_Tags

def do_tags(article):
    ret = ''
    tags = Article_Tags.objects.filter(article = article)

    for tag in tags:
        add = ''

        if tag.category:
            add = ' category'
        ret = ret + '<a href="' + reverse('blog:index') + '?s=' + tag.tag.name + '"><span class="tag' + add + '">' + tag.tag.name + '</span></a> '

    return mark_safe(ret)

register.filter('do_tags', do_tags)

