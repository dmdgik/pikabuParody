from django.db import models
from django.conf import settings
import post.models

# Create your models here.


class Comment(models.Model):

    post_name = models.ForeignKey(post.models.Post, related_name='Comments', verbose_name=u'Название комментируемого поста')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Comments', verbose_name=u'Автор комментария')
    content_text = models.TextField(default='')
    date_of_create = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = u'Комментарии'

    def __str__(self):
        return u'{} ({})'.format(self.id, self.post_name.title)