import markdown

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

def do_markdown(contents):
    return mark_safe(markdown.markdown(contents, extensions=['fenced_code', 'codehilite']))

register.filter('do_markdown', do_markdown)