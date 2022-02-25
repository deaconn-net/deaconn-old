from django import template
from django.utils.safestring import mark_safe
from django.urls import reverse

register = template.Library()

from blog.views import blog_view

def do_tags(tags):
    ret = ''
    tags = tags.split(',')

    for tag in tags:
        ret = ret + '<a href="' + reverse('blog:index') + '?s=' + tag + '"><span class="tag">' + tag + '</span></a> '

    return mark_safe(ret)

register.filter('do_tags', do_tags)

