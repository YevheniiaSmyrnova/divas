"""
Main urls module
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from divas.views import IndexView, RegisterCreateView

urlpatterns = [
    url(r'^register/$', RegisterCreateView.as_view(), name='register'),
    url(r'^login/$', login, {"template_name": "login.html"}, name='login'),
    url(r'^logout/$', logout, {"template_name": "logout.html"}, name='logout'),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^admin/', include(admin.site.urls)),
]
