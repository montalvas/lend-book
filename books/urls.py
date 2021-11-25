from django.urls import path
from .views import *


app_name = 'books'

urlpatterns = [
    # Página inicial
    path('/', IndexTemplateView.as_view(), name='index'),
    path('/cadastrar', CadastrarCreateView.as_view(), name='cadastrar')
]
