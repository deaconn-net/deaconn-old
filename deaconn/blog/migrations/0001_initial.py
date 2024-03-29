# Generated by Django 4.0.1 on 2022-02-23 01:22

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='The title of the article.', max_length=128, verbose_name='Title')),
                ('tags', models.CharField(help_text='Tags for this article.', max_length=255, verbose_name='Tags')),
                ('description', models.TextField(help_text='Text shown on the main blog page for article.', max_length=255, verbose_name='Description')),
                ('contents', models.TextField(help_text='The article content.', max_length=1000000, verbose_name='Contents')),
                ('image', models.ImageField(upload_to=blog.models.file_path)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
