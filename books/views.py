from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from users.models import User
from .models import Book, Category, Loan
from .forms import BookForm, CategoryForm


def home(request):
    """Mostra os livros"""
    user_id = request.session.get('user')
    
    if user_id:
        # Verificando erros de acesso
        status = request.GET.get('status')
        
        # Acessando todos os livros do usuário
        user = User.objects.get(id=user_id)
        books = user.book_set.all()
        form = BookForm()
        form_category = CategoryForm()
        # Modifica o campo categoria para receber a categoria registrada no usuario
        categories = Category.objects.filter(user_id=user_id)
        
        if not categories:
            category = Category(name='Geral', description='Livros em geral', user=user)
            category.save()
            
        form.fields['category'].queryset = categories
        
        context = {
            'books': books,
            'status': status,
            'auth_user': user_id,
            'form': form,
            'form_category': form_category,
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
            form = BookForm()
            # Modifica o campo categoria para receber a categoria registrada no usuario
            form.fields['category'].queryset = Category.objects.filter(user_id=user_id)
            context = {
                'book': book,
                'categories': categories,
                'loans': loans,
                'auth_user': user_id,
                'form': form
                }
            return render(request, 'books/details.html', context)
        else:
            return redirect('/book/home/?status=2')
    else:
        return redirect('/auth/login/?status=2')
    
def register_book(request):
    user_id = request.session.get('user')
    
    if user_id:
        if request.method == 'POST':
            form = BookForm(request.POST)
            if form.is_valid():
                new_book = form.save(commit=False)
                new_book.user = User.objects.get(id=user_id)
                new_book.save()
            return redirect('/book/home/')
        else:
            return redirect('/book/home/?status=2')
    else:
        return redirect('/auth/login/?status=2')

def delete_book(request, id):
    user_id = request.session.get('user')
    
    if user_id:
        user = User.objects.get(id=user_id)
        book = user.book_set.all().filter(id=id)
        book.delete()
        return redirect('/book/home/')
    else:
        return redirect('/auth/login/?status=2')

def register_category(request):
    user_id = request.session.get('user')
    
    if user_id:
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                new_category = form.save(commit=False)
                new_category.user = User.objects.get(id=user_id)
                new_category.save()
            return redirect('/book/home/?status=0')
        else:
            return redirect('/book/home/?status=2')
    else:
        return redirect('/auth/login/?status=2')

def loan(request):
    user_id = request.session.get('user')
    
    if user_id:
        if request.method == 'POST':
            borrower = request.POST.get('borrower')
            
            user = User.objects.get(id=user_id)
            book = user.book_set.get(id=request.POST.get('book_id'))
            book.lent = True
            book.save()
            
            loan = Loan(borrower=borrower, book=book)
            
            loan.save()
            return redirect('/book/home/')
        else:
            return redirect('/book/home/?status=2')
    else:
        return redirect('/auth/login/?status=2')
    
    