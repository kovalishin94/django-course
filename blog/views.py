from django.shortcuts import render
from django.views.generic import TemplateView


class StartPage(TemplateView):
    template_name = 'blog/index.html'
