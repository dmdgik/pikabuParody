from django.db import models
from django.conf import settings
import category.models

# Create your models here.


class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Автор поста')
    category = models.ManyToManyField(category.models.Category, related_name='Posts', verbose_name=u'Категории поста')
    title = models.CharField(max_length=255, verbose_name=u'Заголовок поста')
    content_text = models.TextField(default='', verbose_name=u'Текст поста')
    date_of_create = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = u'Посты'

    def __str__(self):

        return self.title
