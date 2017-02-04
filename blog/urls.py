"""
Blog urls module
"""
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from blog.views import PostCreateView, PostListView, PostDetailView, PostUpdateView

urlpatterns = patterns(
    '',
    url(r'^$', login_required(PostListView.as_view()), name='list'),
    url(r'^post/(?P<pk>\w+)/$', login_required(PostDetailView.as_view()),
        name='detail'),
    url(r'^create/$', login_required(PostCreateView.as_view()), name='create'),
    url(r'^edit/(?P<pk>\w+)/$',
        login_required(PostUpdateView.as_view()), name='edit'),
)
