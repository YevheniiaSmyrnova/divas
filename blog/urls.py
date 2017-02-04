"""
CBlog urls module
"""
from django.conf.urls import patterns, url
from blog.views import post_list

urlpatterns = patterns(
    '',
    url(r'^$', post_list, name='post_list'),
)
