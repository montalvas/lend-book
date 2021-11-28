from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from hashlib import sha256
from .models import *


def login(request):
    """Faz o login do usuário"""
    status = request.GET.get('status')
    context = {'status': status}
    return render(request, 'users/login.html', context)

def cadastro(request):
    """Cdastra um usuário"""
    status = request.GET.get('status')
    context = {'status': status}
    return render(request, 'users/cadastro.html', context)

def valida_cadastro(request):
    """Faz a validação do cadastro do usuário"""
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    user = User.objects.filter(email = email)
    
    if len(name.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')
    
    if len(password) < 8:
        return redirect('/auth/cadastro/?status=2')
    
    if len(user) > 0:
        return redirect('/auth/cadastro/?status=3')

    try:
        password = sha256(password.encode()).hexdigest()
        user = User(name = name, email = email, password = password)
        user.save()
        
        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')

def valida_login(request):
    """Faz validação do login do usuário"""
    email = request.POST.get('email')
    password = request.POST.get('password')
    password = sha256(password.encode()).hexdigest()
    
    user = User.objects.filter(email=email).filter(password=password)
    
    if len(user) == 0:
        return redirect('/auth/login/?status=1')
    elif len(user) == 1:
        request.session['user'] = user[0].id
        return redirect('/book/home')
    
    return HttpResponse(f"email: {email} | senha: {password}")

def logout(request):
    """Encerra a sessão do usuário"""
    request.session.flush()
    return redirect('/auth/login/')