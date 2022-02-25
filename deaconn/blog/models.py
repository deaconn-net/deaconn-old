from django.db import models
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify

from django.core.files.storage import default_storage

import string
import random

def file_path(instance, filename):
    str = ''

    while True:
        str = ''.join(random.choices(string.ascii_letters + string.digits, k = 8))

        if not default_storage.exists(str):
            break

    return str + '.' + filename.rsplit('.', 1)[1]

class Article(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    date_added = models.DateTimeField(editable = False, auto_now_add = True)
    date_updated = models.DateTimeField(editable = False, auto_now = True)

    title = models.CharField(verbose_name = "Title", help_text = "The title of the article.", max_length = 128)
    tags = models.CharField(verbose_name = "Tags", help_text = "Tags for this article.", max_length = 255)
    description = models.TextField(verbose_name = "Description", help_text = "Text shown on the main blog page for article.", max_length = 255)

    contents = models.TextField(verbose_name = "Contents", help_text = "The article content.", max_length = 1000000)

    image = models.ImageField(verbose_name = "Header Image", upload_to = file_path, blank = True)

    slug = models.SlugField(slugify('slug'), max_length = 60, blank = True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

        if self.id:
            # Delete current tags associated with this article.
            Article_Tags.objects.filter(article = self).delete()

            # Loop through each tag.
            tags = self.tags.split(',')

            for tag in tags:
                category = False

                tag = tag.strip()

                if tag.startswith('|'):
                    category = True
                    tag = tag[1:]

                new_tag = Tags.objects.get_or_create(name = tag)

                # Insert tag for article.
                Article_Tags.objects.create(article = self, tag = new_tag[0], category = category)
                    
class Tags(models.Model):
    name = models.CharField(unique = True, verbose_name = "Name", help_text = "Name of tag.", max_length = 64)
    description = models.TextField(verbose_name = "Description", help_text = "The tag description.", max_length = 255)

class Article_Tags(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete = models.CASCADE)
    category = models.BooleanField(default = False)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)

    author = models.ForeignKey(User, on_delete = models.CASCADE)
    date_added = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    contents = models.TextField(max_length = 10096)