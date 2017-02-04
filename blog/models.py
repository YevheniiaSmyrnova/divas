# -*- coding: utf-8 -*-
"""
Blog models module
"""
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
    Post model
    """
    author = models.ForeignKey('auth.User', verbose_name=u'Пользователь')
    title = models.CharField(u'Название', max_length=200)
    text = models.TextField(u'Текст')
    created_date = models.DateTimeField(u'Дата создания',
                                        default=timezone.now)
    published_date = models.DateTimeField(u'Дата публикации',
                                          blank=True, null=True)

    def publish(self):
        """
        Published date
        """
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Posts title
        """
        return self.title
