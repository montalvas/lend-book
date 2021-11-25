from django.shortcuts import render
from django.views.generic import TemplateView, CreateView


class IndexTemplateView(TemplateView):
    # Mostra a página inicial
    template_name = 'books/index.html'

class CadastrarCreateView(CreateView):
    pass
