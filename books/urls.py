from django.urls import path
from books import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'books'

urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
    # Home
    path('home/', views.home, name='home'),
    # Informações do livro
    path('details/<int:id>/', views.details, name='details'),
    # Editar livro
    path('edit_book/', views.edit_book, name='edit_book'),
    # Cadastro de livro
    path('new_book/', views.register_book, name='register_book'),
    # Exclusão de livro
    path('delete/<int:id>/', views.delete_book, name='delete_book'),
    # Cadastro de categoria
    path('new_category/', views.register_category, name='register_category'),
    # Emprestar livro
    path('loan/', views.loan, name='loan'),
    # Devolver livro
    path('return_book/', views.return_book, name='return_book')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
