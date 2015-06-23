# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name='Slug', blank=True)),
                ('summary', models.TextField(null=True, verbose_name='Summary', blank=True)),
                ('image', models.ImageField(upload_to=b'articles/%Y/%m/%d', null=True, verbose_name='Image', blank=True)),
                ('modified', models.DateTimeField(default=datetime.datetime.now, verbose_name='Modified')),
                ('published', models.BooleanField(default=False)),
                ('body', tinymce.models.HTMLField(verbose_name='Body')),
            ],
            options={
                'ordering': ['-modified'],
                'verbose_name': 'Article',
            },
        ),
    ]
