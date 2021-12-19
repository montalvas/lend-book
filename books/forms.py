from django import forms
from django.db.models import fields
from .models import Book, Category, Loan

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'co_author', 'category', 'lent']
        labels = {
            'name': 'Nome do livro',
            'author': 'Nome do autor',
            'co_author': 'Nome do co-autor',
            'category': 'Categoria',
            'lent': 'Emprestado',
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = {'name', 'description'}
        labels = {
            'name': 'Nome da categoria',
            'description': 'Descrição'
        }

    