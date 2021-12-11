from django.shortcuts import render
from django.shortcuts import redirect
from users.models import User
from .models import Book


def home(request):
    """Mostra os livros"""
    if request.session.get('user'):
        user = User.objects.get(id=request.session['user'])
        books = user.book_set.all()
        context = {'books': books}
        return render(request, 'books/home.html', context)
    else:
        return redirect('/auth/login/?status=2')
    

def details(request, id):
    """Página de detalhes do livro"""
    book = Book.objects.get(id=id)
    context = {'book': book}
    return render(request, 'books/details.html', context)
    
