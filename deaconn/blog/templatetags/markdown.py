import markdown

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

import markdown_strikethrough
from video_markdown import VideoExtension

def do_markdown(contents):
    return mark_safe(markdown.markdown(contents, extensions=['fenced_code', 'codehilite', 'markdown_strikethrough:StrikethroughExtension', VideoExtension()]))

register.filter('do_markdown', do_markdown)