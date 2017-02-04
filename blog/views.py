# -*- coding: utf-8 -*-
"""
Blog views module
"""
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView


from blog.models import Post


class PostListView(ListView):
    """
    List of posts
    """
    model = Post
    context_object_name = 'posts'
    paginate_by = 20


class PostDetailView(DetailView):
    """
    Detail about post
    """
    model = Post


class PostCreateView(CreateView):
    """
    Add new post
    """
    model = Post
    fields = ['author', 'title', 'text']
    success_url = reverse_lazy('blog:list')

    def get_context_data(self, **kwargs):
        """
        Extends context data
        :param kwargs:
        :return: context
        """
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['page_title'] = u'Создание нового поста'
        return context

    def form_valid(self, form):
        """
        The successful addition of new post
        :param form:
        :return: message
        """
        message = super(PostCreateView, self).form_valid(form)
        mes = u'Пост успешно добавлен.'
        messages.success(self.request, mes)
        return message


class PostUpdateView(UpdateView):
    """
    Edit information about post
    """
    model = Post
    fields = ['title', 'text']

    def get_success_url(self):
        """
        Get success url
        :return: get success url
        """
        return reverse_lazy('blog:detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        """
        Extends context data
        :param kwargs:
        :return: context
        """
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = u'Редактирование данных'
        return context

    def form_valid(self, form):
        """
        The successful edition
        :param form:
        :return: message
        """
        message = super(PostUpdateView, self).form_valid(form)
        mes = u'Данные изменены.'
        messages.success(self.request, mes)
        return message
