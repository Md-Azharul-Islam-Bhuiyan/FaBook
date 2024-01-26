from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import News, NewsCategory
from .forms import NewsForm, NewsCategoryForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages



class NewsCategoryView(CreateView):
    model = NewsCategory
    form_class = NewsCategoryForm
    template_name = 'newsCategory.html'
    success_url = reverse_lazy("newsCategory")

    def form_valid(self, form):
        messages.success(self.request, 'News Category Successfully Included.')
        return super().form_valid(form)


class NewsViews(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'newsfeed.html'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.posted_user = self.request.user
        messages.success(self.request, 'News Successfully Posted.')
        return super().form_valid(form)
    

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['type'] = "Add News"
        return context


class EditNewsView(UpdateView):
    model = News 
    form_class = NewsForm
    pk_url_kwarg = 'id'
    template_name = 'newsfeed.html'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, 'News Successfully Updated.')
        return super().form_valid(form)
    

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['type'] = "Edit News"
        return context


class DeleteNewsView(DeleteView):
    model = News
    pk_url_kwarg = 'id'
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
