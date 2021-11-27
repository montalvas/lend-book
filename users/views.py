from django.shortcuts import render

def login(request):
    """Faz o login do usuário"""
    return render(request, 'users/login.html')

def cadastro(request):
    """Cdastra um usuário"""
    return render(request, 'users/cadastro.html')
