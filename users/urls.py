from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    # Página de login
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro')
]