from django.urls import path
from books import views


app_name = 'books'

urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
]
