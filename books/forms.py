from django import forms
from .models import Book

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