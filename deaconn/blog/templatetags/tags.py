from django import template
from django.utils.safestring import mark_safe
from django.urls import reverse

register = template.Library()

from blog.views import blog_view

def do_tags(tags):
    ret = ''
    tags = tags.split(',')

    for tag in tags:
        ret = ret + '<span class="tag"><a href="' + reverse('blog:index') + '?s=' + tag + '">' + tag + '</a></span> '

    return mark_safe(ret)

register.filter('do_tags', do_tags)

