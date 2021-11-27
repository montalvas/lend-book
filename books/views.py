from django.shortcuts import render


def index(request):
    """Mostra os livros"""
    return render(request, 'books/index.html')

def cadastro(request):
    """Página de cadastro de livro"""
    return render(request, 'books/cadastro.html')
