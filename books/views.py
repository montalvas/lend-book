from django.shortcuts import render, redirect 
from users.models import User
from .models import Book, Category, Loan


def home(request):
    """Mostra os livros"""
    user_id = request.session.get('user')
    
    if user_id:
        # Verificando erros de acesso
        status = request.GET.get('status')
        
        # Acessando todos os livros do usuário
        user = User.objects.get(id=user_id)
        books = user.book_set.all()
        context = {
            'books': books,
            'status': status,
            }
        
        return render(request, 'books/home.html', context)
    else:
        return redirect('/auth/login/?status=2')
    

def details(request, id):
    """Página de detalhes do livro"""
    user_id = request.session.get('user')
    
    if user_id:
        try:
            book = Book.objects.get(id=id)
        except:
            return redirect('/book/home/?status=1')
        
        # Verifica se o livro está registrado no usuário que está acessando
        if book.user.id == user_id:
            categories = Category.objects.filter(user_id=user_id)
            loans = book.loan_set.all()
            context = {
                'book': book,
                'categories': categories,
                'loans': loans
                }
            return render(request, 'books/details.html', context)
        else:
            return redirect('/book/home/?status=2')
    else:
        return redirect('/auth/login/?status=2')
    
