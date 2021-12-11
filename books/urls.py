from django.urls import path
from books import views


app_name = 'books'

urlpatterns = [
    # Página inicial
    path('home/', views.home, name='home'),
    # Página de informações do livro
    path('details/<int:id>', views.details, name='details'),
]
