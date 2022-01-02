import datetime
from django.shortcuts import render, redirect
from users.models import User
from .models import Book, Category, Loan
from .forms import BookForm, CategoryForm
from django.urls import reverse

def index(request):
    user_id = request.session.get('user')
    
    if user_id:
        return redirect('/home/')
        
    return render(request, '/index.html')

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
        status = request.GET.get('status')
        
        try:
            book = Book.objects.get(id=id)
        except:
            return redirect('/home/?status=1')
        
        # Verifica se o livro está registrado no usuário que está acessando
        if book.user.id == user_id:
            categories = Category.objects.filter(user_id=user_id)
            loans = book.loan_set.all()
            context = {
                'book': book,
                'categories': categories,
                'loans': loans,
                'auth_user': user_id,
                'status': status
                }
            return render(request, 'books/details.html', context)
        else:
            return redirect('/home/?status=2')
    else:
        return redirect('/auth/login/?status=2')
    
def edit_book(request):
    user_id = request.session.get('user')
    
    if user_id:
        user = User.objects.get(id=user_id)
        book_id = request.POST.get('id')
        
        try:
            book = user.book_set.get(id=book_id)
        except:
            return redirect('/home/?status=1')
        
        book.name = request.POST.get('name')
        book.author = request.POST.get('author')
        book.co_author = request.POST.get('co_author')
        category = user.category_set.get(name=request.POST.get('category'))
        book.category = category
        book.save()
        
        return redirect(f'/details/{book_id}/?status=0')
        
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
            return redirect('/home/?status=0')
        else:
            return redirect('/home/?status=2')
    else:
        return redirect('/auth/login/?status=2')

def delete_book(request, id):
    user_id = request.session.get('user')
    
    if user_id:
        user = User.objects.get(id=user_id)
        book = user.book_set.all().filter(id=id)
        book.delete()
        return redirect('/home/?status=3')
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
            return redirect('/home/?status=4')
        else:
            return redirect('/home/?status=2')
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
            return redirect('/home/?status=5')
        else:
            return redirect('/home/?status=2')
    else:
        return redirect('/auth/login/?status=2')

def return_book(request):
    user_id = request.session.get('user')
    
    if user_id:
        if request.method == 'POST':
            user = User.objects.get(id=user_id)
            id_book = request.POST.get('book_id')
            if id_book:
                book = user.book_set.get(id=request.POST.get('book_id'))
                book.lent = False
                book.save()
                
                loan = book.loan_set.get(return_date__isnull=True)
                today = datetime.datetime.now().date()
                loan.return_date = today
                
                loan.save()
                return redirect('/home/?status=6')
            else:
                return redirect('/home/?status=2')
        else:
            return redirect('/home/?status=2')
    else:
        return redirect('/auth/login/?status=2')
    
    