# -*- coding: utf-8 -*-
"""
Main views module
"""
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """
    Main page
    """
    template_name = 'index.html'
