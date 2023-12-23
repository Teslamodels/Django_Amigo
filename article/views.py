from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article

class ArticleHome(ListView):
    model = Article
    template_name = 'a_home.html'

class ArticleDetail(DetailView):
    model = Article
    template_name = 'a_detail.html'

class ArticleUpdate(UpdateView):
    model = Article
    fields = ['Title', 'Summary', 'Body', 'Photo']
    template_name = 'a_update.html'

class ArticleDelete(DeleteView):
    model = Article
    template_name = 'a_delete.html'
    success_url = reverse_lazy('article')

class ArticleCreate(CreateView):
    model = Article
    fields = ['Title', 'Summary', 'Body', 'Photo', 'Auhtor']
    template_name = 'a_create.html'


