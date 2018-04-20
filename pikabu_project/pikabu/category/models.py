from django.db import models

# Create your models here.

class Category(models.Model):

    title = models.CharField(max_length=255, verbose_name='Category Name')

    class Meta:
        verbose_name_plural = u'Категории'

    def __str__(self):
        return self.title
