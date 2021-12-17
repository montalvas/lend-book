from django.urls import path
from books import views


app_name = 'books'

urlpatterns = [
    # Página inicial
    path('home/', views.home, name='home'),
    # Informações do livro
    path('details/<int:id>', views.details, name='details'),
    # Cadastro de livro
    path('new_book/', views.register_book, name='register_book'),
    # Exclusão de livro
    path('delete/<int:id>', views.delete_book, name='delete_book'),
    # Cadastro de categoria
    path('new_category/', views.register_category, name='register_category'),
]
