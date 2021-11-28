from django.shortcuts import render
from django.shortcuts import redirect
from users.models import User


def home(request):
    """Mostra os livros"""
    if request.session.get('user'):
        user = User.objects.get(id=request.session['user'])
        return render(request, 'books/home.html')
    else:
        return redirect('/auth/login/?status=2')
    

def cadastro(request):
    """Página de cadastro de livro"""
    return render(request, 'books/cadastro.html')
