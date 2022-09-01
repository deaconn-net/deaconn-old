import markdown
import deaconn.video_markdown as vid
from django.utils.safestring import mark_safe

text = "https://youtube.com/watch?v=0sULNZVdTnk&list=RD0sULNZVdTnk"

xd = mark_safe(markdown.markdown(text, extensions=[vid.VideoExtension(), 'fenced_code', 'codehilite']))

print(xd)