# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 03:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('post', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comments', to='post.Post', verbose_name='Название комментируемого поста'),
        ),
    ]
