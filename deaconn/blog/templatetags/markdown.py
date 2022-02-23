import markdown

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

def do_markdown(contents):
    return mark_safe(markdown.markdown(contents))

register.filter('do_markdown', do_markdown)