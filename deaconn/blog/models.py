from django.db import models
from django.contrib.auth.models import User

def file_path(instance, filename):    
    return "{0}/{1}".format(instance.id, filename)

class Article(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    date_added = models.DateTimeField(editable = False, auto_now_add = True)
    date_updated = models.DateTimeField(editable = False, auto_now = True)

    title = models.CharField(verbose_name = "Title", help_text = "The title of the article.", max_length = 128)
    tags = models.CharField(verbose_name = "Tags", help_text = "Tags for this article.", max_length = 255)
    description = models.TextField(verbose_name = "Description", help_text = "Text shown on the main blog page for article.", max_length = 255)

    contents = models.TextField(verbose_name = "Contents", help_text = "The article content.", max_length = 1000000)

    image = models.ImageField(verbose_name = "Header Image", upload_to = file_path)

    def __str__(self):
        return self.title