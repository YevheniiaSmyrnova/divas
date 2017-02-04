# -*- coding: utf-8 -*-
"""
Main views module
"""
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """
    Main page
    """
    template_name = 'index.html'
