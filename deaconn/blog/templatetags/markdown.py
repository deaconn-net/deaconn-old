import markdown

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

from video_markdown import VideoExtension

def do_markdown(contents):
    return mark_safe(markdown.markdown(contents, extensions=[VideoExtension()]))

register.filter('do_markdown', do_markdown)