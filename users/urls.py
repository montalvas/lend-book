from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    # Página de login
    path('login/', views.login, name='login'),
    
    # Página de cadastro
    path('cadastro/', views.cadastro, name='cadastro'),
    
    # Página de validar cadastro
    path('valida_cadastro/', views.valida_cadastro, name='valida_cadastro'),
    
    # Página de validar login
    path('valida_login/', views.valida_login, name='valida_login'),
    
    # Página de logout
    path('logout/', views.logout, name='logout')
]