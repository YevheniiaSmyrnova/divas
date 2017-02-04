# -*- coding: utf-8 -*-
"""
Blog admin module
"""
from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    """
    Post admin
    """
    fieldsets = [
        (u'Основная информация',
         {'fields': ['author', 'title', 'text']}),
        (u'Время',
         {'fields': ['created_date', 'published_date']}),
    ]
    list_display = ('author', 'title', 'created_date')
    list_filter = ['author']


admin.site.register(Post, PostAdmin)
