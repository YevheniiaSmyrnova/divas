"""
Main urls module
"""
from django.conf.urls import include, url
from django.contrib import admin
from divas.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
]
