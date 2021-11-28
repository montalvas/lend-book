from django.urls import path
from books import views


app_name = 'books'

urlpatterns = [
    # Página inicial
    path('home/', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
]
